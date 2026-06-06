"""Griechisch-spezifische Sprachverarbeitung: Tokenisierung, Normalisierung,
Lemmatisierung (spaCy el_core_news_sm, lazy geladen).

Griechische Schrift ist selbst-identifizierend: Wir extrahieren einfach alle
Tokens in griechischer Schrift aus dem gesamten Kapitel — damit werden auch
griechische Beispiele in Grammatik- und Übungsabschnitten erfasst, und
Transliterationen (Lateinschrift) fallen automatisch heraus.
"""
from __future__ import annotations

import re
import unicodedata

# Griechisch + Griechisch-Erweitert (Polytonisch), inkl. Apostroph-Elision (θ' αγαπώ).
# Guards gegen metalinguistische Zitate: kein Match nach/vor Bindestrich
# (Endungs- und Stamm-Zitate wie „-εις", „μέν-") und keine Teil-Matches
# mitten im Wort (sonst matcht „-εις" ab dem ι als „ις").
GREEK_TOKEN_RE = re.compile(
    r"(?<![Ͱ-Ͽἀ-῿-])[Ͱ-Ͽἀ-῿]+(?:['’][Ͱ-Ͽἀ-῿]+)*(?![Ͱ-Ͽἀ-῿-])"
)

_nlp = None


def normalize(s: str) -> str:
    """NFC + lowercase. Akzente bleiben erhalten (bedeutungsunterscheidend!),
    aber Groß-/Kleinschreibung und finales Sigma werden vereinheitlicht."""
    s = unicodedata.normalize("NFC", s).lower().strip()
    return s.replace("ς", "σ")


def strip_accents(s: str) -> str:
    """Nur für Fuzzy-Vergleiche — niemals zum Schreiben verwenden."""
    decomposed = unicodedata.normalize("NFD", s)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if not unicodedata.combining(c)))


def tokenize(text: str) -> list[str]:
    """Alle griechisch-schriftlichen Tokens im Text (Reihenfolge erhalten).

    Markdown-Hervorhebungen werden vorher entfernt, damit κάν**ω** als ein
    Token gelesen wird und Endungs-Zitate wie **-εις** dem Lookbehind nicht
    entwischen."""
    cleaned = text.replace("**", "").replace("__", "")
    return GREEK_TOKEN_RE.findall(cleaned)


def get_nlp():
    global _nlp
    if _nlp is None:
        import spacy
        _nlp = spacy.load("el_core_news_sm", disable=["parser", "ner"])
    return _nlp


def lemmatize(tokens: list[str]) -> dict[str, tuple[str, str]]:
    """token -> (lemma, pos) via spaCy. Tokens werden dedupliziert."""
    unique = list(dict.fromkeys(tokens))
    if not unique:
        return {}
    nlp = get_nlp()
    result = {}
    # Als Einzeldokument verarbeiten, damit der Tagger Kontext hat, wäre besser —
    # aber wir bekommen Tokens ohne Kontext. Pragmatisch: ein Token pro "Satz".
    for token, doc in zip(unique, nlp.pipe(unique)):
        if len(doc) > 0:
            result[token] = (doc[0].lemma_, doc[0].pos_)
        else:
            result[token] = (token, "X")
    return result
