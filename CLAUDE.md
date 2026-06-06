# polyglossos-books — Konventionen

Agent-gestütztes Autorensystem für Sprachlehrbücher (A0 → C1).
Erstes Buch: Neugriechisch für Deutschsprachige (`books/griechisch/`).

## Wahrheitsquellen

- `books/<buch>/curriculum.yaml` — Master-Curriculum: was in welchem Kapitel
  eingeführt wird. Kapitel dürfen davon nicht abweichen.
- `books/<buch>/chapters/NN-slug/meta.yaml` — Sidecar pro Kapitel: deklariert
  eingeführtes Vokabular (`vocab_introduced`) und Grammatik (`grammar_introduced`).
  Jedes neue Wort im Kapiteltext MUSS hier deklariert sein.
- `shared/styles/didaktik.md` — Stil- und Didaktik-Leitfaden für alle
  schreibenden Agenten.

## Eiserne Regeln

1. **Nur Bekanntes verwenden:** Kapitel N darf im Zielsprachen-Text nur
   Vokabular und Grammatik aus Kapiteln 1..N-1 plus die eigenen
   Neueinführungen verwenden. Prüfbar via
   `.venv/bin/python scripts/continuity_check.py <buch> <N>`.
2. **Single Source of Truth:** Die Wortschatz-Box in `chapter.md` wird beim
   Build aus `meta.yaml` generiert — niemals von Hand in beiden Stellen pflegen.
3. **Sektions-Marker:** Kapitel verwenden HTML-Kommentar-Marker
   (`<!-- @section: dialog lang=el -->`); `lang=el` kennzeichnet
   Zielsprachen-Text für den Tokenizer. Marker nicht entfernen oder umbenennen.
4. **Griechisch immer mit korrekten Akzenten** (Monotoniko). Akzente sind
   bedeutungsunterscheidend (πότε/ποτέ).
5. Metasprache aller Erklärungen, Befunde und Commits: **Deutsch**.

## Tooling

- Python: `python3 -m venv .venv`, Abhängigkeiten in `requirements.txt`,
  Aufrufe immer via `.venv/bin/python`.
- Schema-Validierung: `.venv/bin/python scripts/validate_schema.py`
- Build: `make chapter/<buch>/<NN>` bzw. `make book/<buch>` (pandoc + xelatex).
- Pandoc-Profile getrennt nach Format: `shared/pandoc/{pdf,epub,html}.yaml` —
  niemals LaTeX-Spezifisches (header.tex) in epub/html-Profile mischen.

## Veröffentlichung

Alle Bücher teilen sich EINE GitHub-Pages-Site (`make site` → `_site/`,
deployt via `.github/workflows/pages.yml`). CI baut nur HTML (kein LaTeX!) —
`scripts/build_site.py` darf deshalb keine Abhängigkeit auf spacy oder
xelatex bekommen. PDF/EPUB werden lokal mit `make release/<buch>` gebaut und
in `books/<buch>/dist/` committet (einzige committeten Binärartefakte).

## Pipeline-Stop-Bedingungen (Hybrid-Modus)

`/new-chapter` läuft autonom, hält aber an und fragt den Nutzer bei:
- **(A)** ungelöstem Konflikt zwischen Agenten-Befunden
- **(B)** `comprehension-failure` des reader-Agenten
- **(C)** Continuity-Verstößen, die nach max. 3 Überarbeitungsrunden bestehen
