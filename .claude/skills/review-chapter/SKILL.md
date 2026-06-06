---
name: review-chapter
description: Re-Review eines bestehenden Kapitels ohne Neuschreiben — parallele Prüfung durch alle Prüfagenten, Überarbeitungsrunden, gleiche Stop-Bedingungen wie /new-chapter. Aufruf - /review-chapter <buch> <kapitelnummer>
---

# /review-chapter <buch> <N>

Wie /new-chapter, aber ohne die Schreibphase — für nachträgliche Iteration,
nach Nutzer-Edits oder zum Wiederaufsetzen nach einem Pipeline-Stopp.

## Ablauf

1. Kapitel N muss existieren (chapter.md + meta.yaml), sonst Abbruch mit
   Hinweis auf /new-chapter.
2. `.venv/bin/python scripts/validate_schema.py <buch>` — Schemafehler zuerst
   beheben lassen (teacher).
3. Offene Befunde in `notes.md`? Dann zuerst teacher/exercise-designer zur
   Abarbeitung schicken, danach prüfen. Sonst direkt prüfen.
4. **Parallele Prüfung** — identisch zu /new-chapter Phase 2 (reader bekommt
   ausschließlich die chapter.md von Kapitel 1..N!).
5. **Konsolidierung, Überarbeitungsrunden (max. 3), Stop-Bedingungen,
   Abschluss** — identisch zu /new-chapter Phasen 3–5. Bei Erfolg Status auf
   `geprueft` heben (war er `draft-complete`) bzw. bestätigen.
