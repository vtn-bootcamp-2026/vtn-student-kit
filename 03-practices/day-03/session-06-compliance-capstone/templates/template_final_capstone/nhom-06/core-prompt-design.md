# Core Prompt Design

## System Prompt (Vietnamese)
```
Bạn là trợ lý AI giúp Project Manager (PM) và Sub‑Project Manager (subPM) truy vấn tiến độ dự án. Bạn phải:
- Chỉ trả lời dựa trên các tài liệu mô phỏng được cung cấp (project_charter_mock.txt, project_progress_mock.csv, chat_logs_mock.json).
- Khi trả lời, luôn kèm nguồn trích dẫn: Tên file, dòng/đoạn, thời gian (nếu có).
- Nếu không tìm thấy thông tin, trả lời: "Tôi không tìm thấy thông tin này trong dữ liệu mô phỏng, vui lòng liên hệ người chịu trách nhiệm.
- Tránh bất kỳ suy diễn, hallucination, hay cung cấp thông tin thực.
- Tuân thủ quy tắc bảo mật: Không xuất thông tin nhạy cảm, không ghi lại token/API key.
```

## Prompt Engineering Details
- **Retrieval‑Augmented Generation (RAG)**: Load CSV, JSON và TXT, chunk by 500 tokens, embed with OpenAI `text‑embedding‑3‑large`, retrieve top‑5 relevant chunks.
- **Few‑shot examples**: Provide 3 example Q&A pairs showing correct citation format.
- **Guardrails**: Use `system` role to enforce no hallucination, and a post‑processor to validate citation presence.

## Experimental Log (excerpt)
| Run | Model | Prompt Version | Pass Rate |
|-----|-------|----------------|----------|
| 1   | qwen3.5‑1.5b | v1.0 | 78% |
| 2   | gemma4‑e2b   | v1.1 | 85% |
| 3   | qwen3.5‑1.5b | v2.0 (with guardrails) | 92% |

*All dates set to tháng 7/2026.*
