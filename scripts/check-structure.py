#!/usr/bin/env python3
"""Check that every notebook folder matches a chapter in the book.

Each language folder must contain only `chapters/<slug>/<slug>.ipynb`, where
<slug> is a chapter file name from that edition's _quarto.yml in the book
repository. The book's chapter list is read from GitHub, so a renamed or
renumbered chapter shows up here as a failure instead of a silently stale link.

    python3 scripts/check-structure.py
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = "https://raw.githubusercontent.com/bbardakk/uygulamali-dogal-dil-isleme/main/{lang}/_quarto.yml"


def book_slugs(lang):
    text = urllib.request.urlopen(BOOK.format(lang=lang), timeout=30).read().decode("utf-8")
    return set(re.findall(r"chapters/([0-9]{2}-[a-z0-9-]+)\.qmd", text))


def main():
    problems = []
    count = 0
    for lang in ("en", "tr"):
        slugs = book_slugs(lang)
        base = ROOT / lang / "chapters"
        for folder in sorted(p for p in base.iterdir() if p.is_dir()):
            if folder.name not in slugs:
                problems.append(f"{lang}/chapters/{folder.name}: no chapter with this slug in the book")
                continue
            notebook = folder / f"{folder.name}.ipynb"
            if not notebook.exists():
                problems.append(f"{lang}/chapters/{folder.name}: missing {notebook.name}")
            else:
                count += 1
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"check-structure: {count} notebook(s), every folder matches a book chapter")


if __name__ == "__main__":
    main()
