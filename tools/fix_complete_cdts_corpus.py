#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().with_name("complete_cdts_corpus.py")
text = path.read_text(encoding="utf-8")
old = 'text = replace_exact(text, "пять принятых артефакта", "шесть принятых артефактов", "AGENTS reading order")'
new = 'text = replace_exact(text, "пять принятых артефактов", "шесть принятых артефактов", "AGENTS reading order")'
if old not in text:
    raise SystemExit("House migration reading-order marker line not found")
path.write_text(text.replace(old, new), encoding="utf-8")
print("House migration reading-order marker aligned")
