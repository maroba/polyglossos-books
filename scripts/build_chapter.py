#!/usr/bin/env python3
"""Rendert Kapitel für den Build: generiert die Wortschatz-Box aus meta.yaml
(Single Source of Truth) in den @section:vokabeln-Abschnitt.

  .venv/bin/python scripts/build_chapter.py <buch> <kapitel> [--out DIR]
  .venv/bin/python scripts/build_chapter.py <buch> --all [--out DIR]

Schreibt gerenderte Markdown-Dateien nach books/<buch>/build/rendered/.
Den Pandoc-Aufruf übernimmt das Makefile.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


import argparse
import re
import sys
from pathlib import Path

from lib.chapters import Chapter, SECTION_RE, book_dir, load_chapter, load_chapters


def vocab_table(meta: dict) -> str:
    entries = meta.get("vocab_introduced") or []
    if not entries:
        return "_In diesem Kapitel wird kein neues Vokabular eingeführt._\n"
    with_translit = any(e.get("translit") for e in entries)
    if with_translit:
        lines = ["| Griechisch | Aussprache | Deutsch |", "|---|---|---|"]
    else:
        lines = ["| Griechisch | Deutsch |", "|---|---|"]
    for e in entries:
        lemma = e["lemma"]
        if e.get("gender"):
            article = {"m": "ο", "f": "η", "n": "το"}[e["gender"]]
            lemma = f"{article} {lemma}"
        gloss = e["gloss_de"]
        if e.get("notes"):
            gloss += f" _({e['notes']})_"
        if with_translit:
            lines.append(f"| **{lemma}** | {e.get('translit') or ''} | {gloss} |")
        else:
            lines.append(f"| **{lemma}** | {gloss} |")
    return "\n".join(lines) + "\n"


def render(chapter: Chapter) -> str:
    md = chapter.markdown()
    matches = list(SECTION_RE.finditer(md))
    for i, m in enumerate(matches):
        attrs_name = m.group("name")
        if attrs_name != "vokabeln":
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        body = md[m.end():end]
        # Überschrift des Abschnitts erhalten, Rest durch generierte Tabelle ersetzen
        heading = re.match(r"\s*(#{1,3}[^\n]*\n)", body)
        head = heading.group(1) if heading else "## Wortschatz\n"
        return md[: m.end()] + "\n" + head + "\n" + vocab_table(chapter.meta) + "\n" + md[end:]
    return md  # kein vokabeln-Abschnitt: unverändert


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("chapter", nargs="?", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    out_dir = args.out or book_dir(args.book) / "build" / "rendered"
    out_dir.mkdir(parents=True, exist_ok=True)

    chapters = load_chapters(args.book) if args.all else [load_chapter(args.book, args.chapter)]
    for ch in chapters:
        out = out_dir / f"{ch.number:02d}-{ch.slug}.md"
        out.write_text(render(ch), encoding="utf-8")
        print(f"gerendert: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
