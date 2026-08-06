#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().with_name("complete_cdts_corpus.py")
text = path.read_text(encoding="utf-8")
old = '    "что пять принятых артефактов автоматически канонизируют ARB и CDTS;",'
new = '    "- что пять принятых артефактов автоматически канонизируют ARB и CDTS;",'
if old not in text:
    raise SystemExit("warning marker line not found")
path.write_text(text.replace(old, new), encoding="utf-8")
print("warning marker aligned")
