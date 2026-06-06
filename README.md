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
make book/griechisch          # ganzes Buch: PDF + EPUB (nach build/)
make release/griechisch       # PDF + EPUB nach dist/ (committet, Website-Downloads)
make site                     # GitHub-Pages-Site nach _site/ (lokale Vorschau)
```

## Veröffentlichung (GitHub Pages)

Alle Bücher werden über **eine** GitHub-Pages-Site veröffentlicht:
Landing-Page mit Buchliste, pro Buch eine HTML-Version (eine Seite pro
Kapitel) plus PDF/EPUB-Download.

- Die HTML-Site baut GitHub Actions bei jedem Push auf `main` automatisch
  (`.github/workflows/pages.yml`) — nur pandoc, kein LaTeX in CI.
- PDF/EPUB entstehen lokal mit `make release/<buch>` und werden in
  `books/<buch>/dist/` committet; die Site verlinkt sie.
- Einmalig im Repo aktivieren: Settings → Pages → Source: „GitHub Actions".

## Arbeitsweise

1. `/plan-curriculum griechisch` — Master-Curriculum erstellen (einmalig, dann iterieren)
2. `/new-chapter griechisch N` — Kapitel-Pipeline: schreiben → prüfen → überarbeiten
3. `/audit-vocab griechisch` — buchweite Konsistenzprüfung
4. `/status griechisch` — Fortschrittsübersicht

Die Pipeline läuft hybrid-autonom: Sie stoppt bei Agenten-Konflikten, bei
`comprehension-failure` des reader-Agenten und bei verbleibenden
Continuity-Verstößen.
