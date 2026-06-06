---
name: status
description: Fortschrittsübersicht über ein Buch oder alle Bücher - Kapitelstatus, offene Befunde, Vokabelzahlen. Aufruf - /status [buch]
---

# /status [buch]

Reines Tooling, keine Agenten.

1. `.venv/bin/python scripts/progress_report.py [buch]`
2. Gib die Tabelle wieder und ergänze eine kurze Einordnung:
   - Wo steht das Buch (Kapitel fertig/geprüft/entwurf, aktuelles GER-Niveau)?
   - Gibt es Kapitel mit offenen Befunden? → /review-chapter vorschlagen.
   - Wann war der letzte /audit-vocab-Lauf sinnvollerweise (Faustregel: alle
     ~5 Kapitel)?
3. Nichts verändern.
