import re
import json
from pathlib import Path

# Regex cho các loại PII chuẩn
PATTERNS = {
    'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    'phone': re.compile(r'\b(?:\+84\s?|0)\d{2,3}[\s.-]?\d{3}[\s.-]?\d{3,4}\b'),
    'cccd': re.compile(r'\b\d{12}\b'),
}

def anonymize_text(text: str) -> str:
    if not text:
        return ''
    result = text
    # Ẩn Email
    result = PATTERNS['email'].sub('[REDACTED_EMAIL]', result)
    # Ẩn Số điện thoại
    result = PATTERNS['phone'].sub('[REDACTED_PHONE]', result)
    # Ẩn CCCD
    result = PATTERNS['cccd'].sub('[REDACTED_CCCD]', result)
    return result
