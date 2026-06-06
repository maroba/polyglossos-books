#!/usr/bin/env python3
"""Continuity-Check: Verwendet Kapitel N nur bekanntes Vokabular?

Hybrid-Pipeline:
  1. Griechisch-schriftliche Tokens aus chapter.md extrahieren
  2. Exakt-Match gegen bekannte Formen (Lemmata-Wörter + inflected_forms)
  3. Rest: spaCy-Lemmatisierung, Lemma gegen bekannte Lemmata
  4. Verbleibende Unbekannte ausgeben — Triage übernimmt der
     continuity-checker-Agent (echter Verstoß / Lemmatizer-Miss / fehlende
     Deklaration im Sidecar)

Aufruf:
  .venv/bin/python scripts/continuity_check.py <buch> <kapitel>
  .venv/bin/python scripts/continuity_check.py <buch> --all
  Optionen: --json

Exit-Code 1, wenn unbekannte Nicht-Eigennamen-Tokens gefunden wurden.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


import argparse
import json
import sys
from collections import Counter

from lib.chapters import load_chapter, load_chapters
from lib.greek import lemmatize, normalize, strip_accents, tokenize
from lib.vocabdb import cumulative_vocab


def check_chapter(book: str, number: int) -> dict:
    chapter = load_chapter(book, number)
    db = cumulative_vocab(book, number, include_own=True)
    tokens = tokenize(chapter.markdown())
    counts = Counter(normalize(t) for t in tokens)

    # Stufe 1: exakte Formen
    unknown = [t for t in dict.fromkeys(tokens) if not db.knows_form(t)]

    # Stufe 2: Lemmatisierung
    findings = []
    if unknown:
        lemmas = lemmatize(unknown)
        for token in unknown:
            lemma, pos = lemmas.get(token, (token, "X"))
            if db.knows_lemma(lemma):
                continue
            # Fuzzy-Hinweis: bekannt bis auf Akzente? (häufiger Tippfehler)
            accent_hint = any(
                strip_accents(normalize(token)) == strip_accents(f) for f in db.known_forms
            )
            findings.append({
                "token": token,
                "lemma": lemma,
                "pos": pos,
                "count": counts[normalize(token)],
                "proper_noun": pos == "PROPN" or (token[:1].isupper() and lemma[:1].isupper()),
                "accent_mismatch_hint": accent_hint,
            })

    violations = [f for f in findings if not f["proper_noun"]]
    return {
        "book": book,
        "chapter": number,
        "tokens_total": len(tokens),
        "tokens_unique": len(set(normalize(t) for t in tokens)),
        "known_lemmas": len(db.known_lemmas),
        "findings": findings,
        "violation_count": len(violations),
    }


def print_report(result: dict) -> None:
    print(f"\n== Kapitel {result['chapter']} ({result['book']}) ==")
    print(f"Tokens: {result['tokens_total']} ({result['tokens_unique']} unique), "
          f"bekannte Lemmata bis hierher: {result['known_lemmas']}")
    if not result["findings"]:
        print("OK — alle griechischen Tokens bekannt.")
        return
    print(f"{'Token':<20} {'Lemma':<20} {'POS':<7} {'n':>3}  Hinweis")
    for f in result["findings"]:
        hints = []
        if f["proper_noun"]:
            hints.append("Eigenname?")
        if f["accent_mismatch_hint"]:
            hints.append("Akzent-Abweichung zu bekannter Form!")
        print(f"{f['token']:<20} {f['lemma']:<20} {f['pos']:<7} {f['count']:>3}  {', '.join(hints)}")
    print(f"→ {result['violation_count']} potenzielle Verstöße (Eigennamen ausgenommen). "
          f"Triage durch continuity-checker-Agent erforderlich.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("chapter", nargs="?", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.all:
        numbers = [c.number for c in load_chapters(args.book)]
    elif args.chapter:
        numbers = [args.chapter]
    else:
        ap.error("Kapitelnummer oder --all angeben.")

    results = [check_chapter(args.book, n) for n in numbers]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print_report(r)
    return 1 if any(r["violation_count"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
