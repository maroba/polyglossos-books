---
name: build
description: Baut ein Kapitel oder das ganze Buch als PDF/EPUB via Make und Pandoc. Aufruf - /build <buch> [kapitelnummer]
---

# /build <buch> [N]

Reines Tooling, keine Agenten.

- Mit Kapitelnummer: `make chapter/<buch>/<N>` → einzelnes Kapitel-PDF.
- Ohne: `make book/<buch>` → Gesamt-PDF + EPUB.

Bei Pandoc-/LaTeX-Fehlern: Fehlermeldung lesen, Ursache beheben (häufig:
kaputtes Markdown im Kapitel, fehlende Schrift, Sonderzeichen in Tabellen)
und erneut bauen. Wenn die Ursache eine inhaltliche Änderung erfordert, nicht
selbst umschreiben — an den Nutzer melden oder /review-chapter vorschlagen.

Nach Erfolg: Pfad(e) der Artefakte nennen und die PDF-Datei mit SendUserFile
an den Nutzer senden.
