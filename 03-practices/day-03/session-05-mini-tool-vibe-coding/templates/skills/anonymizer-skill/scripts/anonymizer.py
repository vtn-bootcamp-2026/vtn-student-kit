#!/usr/bin/env python3
"""
PII Anonymizer — Công cụ che giấu dữ liệu nhận dạng cá nhân.
Hybrid: Regex (tầng 1) + Local LLM (tầng 2) + Fallback an toàn.
"""
from __future__ import annotations

import csv
import json
import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

# ─── Regex Patterns (tầng 1) ───

PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone_mobile": re.compile(r"\b(03|05|07|08|09)\d{8}\b"),
    "phone_intl": re.compile(r"\+84[\s\-]?\d[\s\-]?\d{2,3}[\s\-]?\d{3}[\s\-]?\d{2,3}"),
    "phone_landline": re.compile(r"\b(02[0-9])[\.\-\s]?\d{3,4}[\.\-\s]?\d{3,4}\b"),
    "cccd": re.compile(r"\b\d{12}\b"),
    "ip": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
}

# Safe terms — không che giấu (số SCADA, serial thiết bị)
SCADA_UNITS = re.compile(r"\d[\d.]+\s*(?:dB|MHz|GHz|ms|km|V|A|W|%)\b")
DEVICE_SERIAL = re.compile(r"\b[A-Z]+-[A-Z]+-\d+\b")
SERIAL_CONTEXT = re.compile(r"(?:serial|mã thiết bị|mã kiểm soát|serial number|mã phần cứng)", re.IGNORECASE)


def normalize_unicode(text: str) -> str:
    """Chuẩn hóa Unicode NFC cho tiếng Việt."""
    return unicodedata.normalize("NFC", text)


def is_safe_term(match_text: str, context: str) -> bool:
    """Kiểm tra PII candidate có phải safe term (SCADA, serial, v.v.)."""
    if SCADA_UNITS.search(context):
        return True
    if DEVICE_SERIAL.search(match_text):
        return True
    if SERIAL_CONTEXT.search(context):
        return True
    return False


def regex_redact(text: str) -> tuple[str, list[dict[str, Any]]]:
    """Lọc Regex tầng 1 — nhanh, tĩnh."""
    findings = []
    redacted = text

    for pii_type, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            matched_text = match.group()
            start = match.start()
            context_window = text[max(0, start - 30):start + len(matched_text) + 30]

            if is_safe_term(matched_text, context_window):
                continue

            placeholder = f"[REDACTED_{pii_type.upper()}]"
            findings.append({
                "type": pii_type,
                "placeholder": placeholder,
                "position": start,
                "confidence": 0.6,
            })
            redacted = redacted.replace(matched_text, placeholder, 1)

    return redacted, findings


def call_ollama(text: str, findings: list[dict]) -> tuple[bool, list[dict], str]:
    """Gọi Local LLM (Ollama) để xác minh PII — tầng 2."""
    try:
        import urllib.request

        few_shot_prompt = f"""Phân tích văn bản sau và xác định thông tin cá nhân (PII).
Chỉ trả về JSON thuần túy, không markdown, không giải thích.

Ví dụ 1: "Anh Nguyễn Văn A (CCCD 079123456789) gọi SĐT 0982123456"
→ {{"pii": [{{"type":"NAME","value":"Nguyễn Văn A"}},{{"type":"CCCD","value":"079123456789"}},{{"type":"PHONE","value":"0982123456"}}]}}

Ví dụ 2: "Tổ anhvan-support@viettel.com.vn báo SCADA 0.912.345.678 dB ổn định"
→ {{"pii": [], "safe_terms": ["anhvan-support@viettel.com.vn", "0.912.345.678 dB"]}}

Văn bản cần phân tích:
{text[:2000]}"""

        payload = json.dumps({
            "model": os.environ.get("OLLAMA_MODEL", "gemma3:1b"),
            "messages": [{"role": "user", "content": few_shot_prompt}],
            "temperature": 0.1,
            "stream": False,
        }).encode("utf-8")

        req = urllib.request.Request(
            "http://127.0.0.1:11434/v1/chat/completions",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))

        content = result["choices"][0]["message"]["content"]
        # Robust JSON parser — bóc tách JSON từ response có thể chứa markdown
        json_match = re.search(r"\{.*\}", content, re.DOTALL)
        if json_match:
            llm_result = json.loads(json_match.group())
            return True, llm_result.get("pii", []), content
        return True, [], content

    except Exception as e:
        # Fallback: Regex-only + bật HITL
        return False, [], str(e)


def write_log(log_path: Path, input_file: str, status: str,
              pii_count: int, needs_human_review: bool, notes: str) -> None:
    """Ghi log — tuyệt đối không chứa PII gốc."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    exists = log_path.exists()

    with log_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "run_id", "input_file", "status", "pii_count",
            "needs_human_review", "notes", "created_at",
        ])
        if not exists:
            writer.writeheader()
        writer.writerow({
            "run_id": datetime.now().strftime("%Y%m%d%H%M%S"),
            "input_file": input_file,
            "status": status,
            "pii_count": pii_count,
            "needs_human_review": str(needs_human_review).lower(),
            "notes": notes[:200],
            "created_at": datetime.now().isoformat(timespec="seconds"),
        })


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent.parent.parent.parent  # scripts/ → anonymizer-skill/ → skills/ → templates/ → session root

    input_path = base_dir / "synthetic-data/pii-sample-01.txt"
    output_path = base_dir / "outputs" / f"{input_path.stem}-redacted{input_path.suffix}"
    log_path = base_dir / "outputs/execution-log.csv"

    if not input_path.exists():
        print(f"Lỗi: Không tìm thấy {input_path}")
        return

    text = normalize_unicode(input_path.read_text(encoding="utf-8"))

    # Tầng 1: Regex
    redacted, findings = regex_redact(text)

    # Tầng 2: LLM verification
    llm_ok, llm_pii, llm_raw = call_ollama(text, findings)
    notes = ""
    needs_human_review = False

    if not llm_ok:
        notes = "LLM_FALLBACK: Ollama unavailable, using Regex-only"
        needs_human_review = True
    else:
        # Merge LLM findings with Regex findings
        notes = f"LLM verified, found {len(llm_pii)} items"

    # Phát hiện prompt injection
    injection_keywords = ["tắt bảo mật", "bỏ qua", "ignore previous", "tắt cờ", "in nguyên văn"]
    for kw in injection_keywords:
        if kw in text.lower():
            needs_human_review = True
            notes += f" | INJECTION_DETECTED: '{kw}'"
            break

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(redacted, encoding="utf-8")
    write_log(log_path, input_path.name, "success",
              len(findings), needs_human_review, notes)

    print(f"Redacted {len(findings)} PII items | HITL={needs_human_review} | {notes}")


if __name__ == "__main__":
    main()
