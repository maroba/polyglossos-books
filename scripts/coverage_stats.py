#!/usr/bin/env python3
"""Buchweite Curriculum- und Vokabular-Statistiken.

  .venv/bin/python scripts/coverage_stats.py <buch>          # Ist-Stand
  .venv/bin/python scripts/coverage_stats.py <buch> --dry    # nur Curriculum-Struktur prüfen

--dry prüft (vor dem Schreiben des ersten Kapitels):
  - Kapitel-IDs lückenlos und aufsteigend
  - depends_on verweist nur auf frühere Kapitel (azyklisch)
  - grammar_recycle-IDs wurden in einem früheren Kapitel als grammar_new eingeführt

Ohne --dry zusätzlich (gegen die vorhandenen meta.yaml):
  - Soll/Ist neuer Vokabeln pro Kapitel (vocab_target)
  - Recycling-Quote (vocab_recycle_min)
  - grammar_introduced ↔ Curriculum grammar_new
  - eingeführte Wörter, die in späteren Kapiteln nie wieder vorkommen
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


import argparse
import sys

from lib.chapters import load_chapters, load_curriculum
from lib.greek import normalize, tokenize


def check_structure(curriculum: dict) -> list[str]:
    problems = []
    chapters = curriculum["chapters"]
    ids = [c["id"] for c in chapters]
    if ids != sorted(set(ids)):
        problems.append("Kapitel-IDs sind nicht eindeutig aufsteigend.")
    if ids and ids != list(range(1, len(ids) + 1)):
        problems.append(f"Kapitel-IDs sind nicht lückenlos 1..{len(ids)}.")
    grammar_intro: dict[str, int] = {}
    for c in chapters:
        for g in c.get("grammar_new") or []:
            if g["id"] in grammar_intro:
                problems.append(f"Kapitel {c['id']}: Grammatik-ID '{g['id']}' bereits in Kapitel {grammar_intro[g['id']]} eingeführt.")
            grammar_intro.setdefault(g["id"], c["id"])
    for c in chapters:
        for dep in c.get("depends_on") or []:
            if dep >= c["id"]:
                problems.append(f"Kapitel {c['id']}: depends_on {dep} ist nicht früher (Zyklus!).")
        for gid in c.get("grammar_recycle") or []:
            intro = grammar_intro.get(gid)
            if intro is None:
                problems.append(f"Kapitel {c['id']}: grammar_recycle '{gid}' wird nirgends eingeführt.")
            elif intro >= c["id"]:
                problems.append(f"Kapitel {c['id']}: grammar_recycle '{gid}' wird erst in Kapitel {intro} eingeführt.")
    return problems


def report_progress(book: str, curriculum: dict) -> None:
    written = {c.number: c for c in load_chapters(book)}
    cur_by_id = {c["id"]: c for c in curriculum["chapters"]}

    # Wo taucht jedes Lemma nach seiner Einführung wieder auf?
    later_use: dict[str, bool] = {}
    all_tokens_by_chapter = {n: {normalize(t) for t in tokenize(ch.markdown())} for n, ch in written.items()}
    for n, ch in written.items():
        for entry in ch.meta.get("vocab_introduced") or []:
            lemma = normalize(entry["lemma"])
            words = {normalize(w) for w in entry["lemma"].split()}
            used = any(words & all_tokens_by_chapter[m] for m in all_tokens_by_chapter if m > n)
            later_use[lemma] = used

    print(f"{'Kap':>4} {'CEFR':<5} {'Status':<15} {'neu (Soll)':>11} {'recycelt (Min)':>15}  Grammatik ok?")
    for cid, cur in cur_by_id.items():
        ch = written.get(cid)
        if ch is None:
            print(f"{cid:>4} {cur['cefr']:<5} {'geplant':<15} {'- (' + str(cur.get('vocab_target', '?')) + ')':>11}")
            continue
        n_new = len(ch.meta.get("vocab_introduced") or [])
        n_rec = len(ch.meta.get("vocab_recycled") or [])
        want_gr = {g["id"] for g in cur.get("grammar_new") or []}
        have_gr = {g["id"] for g in ch.meta.get("grammar_introduced") or []}
        gr_ok = "ja" if want_gr == have_gr else f"NEIN (fehlt: {want_gr - have_gr or '-'}, extra: {have_gr - want_gr or '-'})"
        new_col = f"{n_new} ({cur.get('vocab_target', '?')})"
        rec_col = f"{n_rec} ({cur.get('vocab_recycle_min', 0)})"
        status = ch.meta.get("status", "?")
        print(f"{cid:>4} {cur['cefr']:<5} {status:<15} {new_col:>11} {rec_col:>15}  {gr_ok}")

    never_again = [l for l, used in later_use.items() if not used]
    total = sum(len(ch.meta.get("vocab_introduced") or []) for ch in written.values())
    print(f"\nKumulativ eingeführt: {total} Lemmata in {len(written)} geschriebenen Kapiteln.")
    if len(written) > 1 and never_again:
        print(f"Nie wiederverwendet ({len(never_again)}): {', '.join(sorted(never_again)[:30])}"
              + (" …" if len(never_again) > 30 else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--dry", action="store_true", help="nur Curriculum-Struktur prüfen")
    args = ap.parse_args()

    curriculum = load_curriculum(args.book)
    problems = check_structure(curriculum)
    for p in problems:
        print(f"STRUKTUR  {p}")
    if not problems:
        print(f"Curriculum-Struktur ok ({len(curriculum['chapters'])} Kapitel, Ziel {curriculum['target_cefr']}).")
    if not args.dry:
        print()
        report_progress(args.book, curriculum)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
