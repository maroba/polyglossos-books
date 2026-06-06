---
name: build
description: Baut ein Kapitel oder Buch als PDF/EPUB, die Release-Artefakte für die Website oder die komplette GitHub-Pages-Site. Aufruf - /build <buch> [kapitelnummer] | /build <buch> release | /build site
---

# /build — Build-Varianten

Reines Tooling, keine Agenten.

- `/build <buch> <N>` → `make chapter/<buch>/<N>` — einzelnes Kapitel-PDF (Smoke-Test).
- `/build <buch>` → `make book/<buch>` — Gesamt-PDF + EPUB nach `books/<buch>/build/`.
- `/build <buch> release` → `make release/<buch>` — wie book, kopiert die
  Artefakte zusätzlich nach `books/<buch>/dist/`. **dist/ wird committet** —
  das sind die Download-Dateien der Website. Nach dem Kopieren committen
  (nur nach Rückfrage beim Nutzer, falls nicht ohnehin Teil eines
  größeren Commits).
- `/build site` → `make site` — baut die komplette GitHub-Pages-Site nach
  `_site/` (Landing-Page + chunkedhtml pro Buch + Downloads aus dist/).
  Lokale Vorschau; das Deployment macht GitHub Actions
  (`.github/workflows/pages.yml`) bei jedem Push auf main automatisch.

Bei Pandoc-/LaTeX-Fehlern: Fehlermeldung lesen, Ursache beheben (häufig:
kaputtes Markdown im Kapitel, fehlende Schrift, Sonderzeichen in Tabellen)
und erneut bauen. Wenn die Ursache eine inhaltliche Änderung erfordert, nicht
selbst umschreiben — an den Nutzer melden oder /review-chapter vorschlagen.

Nach Erfolg: Pfad(e) der Artefakte nennen; einzelne PDFs mit SendUserFile an
den Nutzer senden.
