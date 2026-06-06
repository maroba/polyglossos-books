#!/usr/bin/env python3
"""Fortschrittsbericht für /status.

  .venv/bin/python scripts/progress_report.py [buch]

Offene Befunde werden als unerledigte Markdown-Checkboxen (`- [ ]`) in den
notes.md der Kapitel gezählt.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


import re
import sys

from lib.chapters import BOOKS_DIR, load_chapters, load_curriculum

OPEN_FINDING_RE = re.compile(r"^\s*- \[ \]", re.MULTILINE)


def report(book: str) -> None:
    try:
        curriculum = load_curriculum(book)
    except FileNotFoundError:
        print(f"{book}: noch kein Curriculum — mit /plan-curriculum {book} beginnen.")
        return
    written = {c.number: c for c in load_chapters(book)}
    total = len(curriculum["chapters"])
    done = sum(1 for c in written.values() if c.meta.get("status") in ("geprueft", "fertig"))
    cum_vocab = 0

    print(f"== {book} — Ziel {curriculum['target_cefr']}, {total} Kapitel geplant ==")
    print(f"{'Kap':>4} {'CEFR':<5} {'Titel':<42} {'Status':<15} {'Vok.':>5} {'kum.':>5} {'offen':>6}")
    for cur in curriculum["chapters"]:
        ch = written.get(cur["id"])
        status = ch.meta.get("status", "geplant") if ch else "geplant"
        n_vocab = len(ch.meta.get("vocab_introduced") or []) if ch else 0
        cum_vocab += n_vocab
        open_findings = ""
        if ch and ch.notes_path.exists():
            n_open = len(OPEN_FINDING_RE.findall(ch.notes_path.read_text(encoding="utf-8")))
            open_findings = str(n_open) if n_open else ""
        title = cur["title_de"][:40]
        print(f"{cur['id']:>4} {cur['cefr']:<5} {title:<42} {status:<15} {n_vocab:>5} {cum_vocab:>5} {open_findings:>6}")
    print(f"\n{done}/{total} Kapitel geprüft/fertig, {cum_vocab} Lemmata kumulativ eingeführt.")


def main() -> int:
    books = [sys.argv[1]] if len(sys.argv) > 1 else [d.name for d in sorted(BOOKS_DIR.iterdir()) if d.is_dir()]
    for book in books:
        report(book)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
