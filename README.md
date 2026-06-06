# polyglossos-books

Agent-gestütztes Autorensystem für Sprachlehrbücher (A0 → C1).
Erstes Buch: **Neugriechisch für Deutschsprachige**.

## Aufbau

```
.claude/agents/     8 Custom Agents (teacher, reviewer, reader, ai-guard, ...)
.claude/skills/     Workflows: /plan-curriculum, /new-chapter, /review-chapter,
                    /audit-vocab, /build, /status
scripts/            Python-Tools (Continuity-Check, Statistiken, Build)
schemas/            JSON-Schemas für curriculum.yaml und meta.yaml
shared/             Pandoc-Templates und Didaktik-Leitfaden
books/<sprache>/    Ein Verzeichnis pro Buch
```

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m spacy download el_core_news_sm
```

Für den PDF-Build werden `pandoc` und eine TeX-Distribution mit `xelatex` benötigt.

## Bauen

```sh
make chapter/griechisch/01    # einzelnes Kapitel (Smoke-Test)
make book/griechisch          # ganzes Buch: PDF + EPUB
```

## Arbeitsweise

1. `/plan-curriculum griechisch` — Master-Curriculum erstellen (einmalig, dann iterieren)
2. `/new-chapter griechisch N` — Kapitel-Pipeline: schreiben → prüfen → überarbeiten
3. `/audit-vocab griechisch` — buchweite Konsistenzprüfung
4. `/status griechisch` — Fortschrittsübersicht

Die Pipeline läuft hybrid-autonom: Sie stoppt bei Agenten-Konflikten, bei
`comprehension-failure` des reader-Agenten und bei verbleibenden
Continuity-Verstößen.
