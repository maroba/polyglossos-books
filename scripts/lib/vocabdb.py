"""Kumulatives Vokabular aus den Kapitel-Sidecars berechnen.

Es gibt keine separate Vokabel-Gesamtdatei: Die Wahrheit liegt in den
meta.yaml-Sidecars; hier wird sie on-the-fly aggregiert.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .chapters import load_chapters
from .greek import normalize


@dataclass
class VocabDB:
    known_lemmas: set[str] = field(default_factory=set)   # normalisierte Lemmata
    known_forms: set[str] = field(default_factory=set)    # normalisierte Einzelformen
    lemma_chapter: dict[str, int] = field(default_factory=dict)  # Lemma -> Einführungskapitel

    def add_entry(self, entry: dict, chapter: int) -> None:
        lemma = entry["lemma"].strip()
        norm = normalize(lemma)
        self.known_lemmas.add(norm)
        self.lemma_chapter.setdefault(norm, chapter)
        # Mehrwort-Lemmata (Phrasen wie "γεια σου"): Einzelwörter als Formen aufnehmen
        for word in lemma.split():
            self.known_forms.add(normalize(word))
        for form in entry.get("inflected_forms") or []:
            self.known_forms.add(normalize(form))

    def knows_form(self, token: str) -> bool:
        return normalize(token) in self.known_forms

    def knows_lemma(self, lemma: str) -> bool:
        return normalize(lemma) in self.known_lemmas


def cumulative_vocab(book: str, upto_chapter: int, include_own: bool = True) -> VocabDB:
    """Vokabular der Kapitel 1..upto_chapter-1; mit include_own auch die
    Neueinführungen von Kapitel upto_chapter selbst."""
    db = VocabDB()
    limit = upto_chapter if include_own else upto_chapter - 1
    for c in load_chapters(book):
        if c.number > limit:
            continue
        for entry in c.meta.get("vocab_introduced") or []:
            db.add_entry(entry, c.number)
    return db
