#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().with_name("complete_cdts_corpus.py")
text = path.read_text(encoding="utf-8")
replacements = {
    'text = replace_exact(text, "пять принятых артефакта", "шесть принятых артефактов", "AGENTS reading order")':
        'text = replace_exact(text, "пять принятых артефактов", "шесть принятых артефактов", "AGENTS reading order")',
    '    "что пять принятых артефактов автоматически канонизируют ARB и CDTS;",':
        '    "что пять принятых артефакта автоматически канонизируют ARB и CDTS;",',
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"House migration marker line not found: {old}")
    text = text.replace(old, new)
path.write_text(text, encoding="utf-8")
print("House migration markers aligned")
