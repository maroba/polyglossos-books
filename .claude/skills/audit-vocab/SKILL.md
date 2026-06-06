---
name: audit-vocab
description: Buchweite Konsistenzprüfung von Vokabular und Curriculum-Einhaltung über alle geschriebenen Kapitel, mit Agent-Triage der Auffälligkeiten. Aufruf - /audit-vocab <buch>
---

# /audit-vocab <buch>

Periodische Gesamtprüfung (z. B. nach jeder Handvoll Kapitel) — findet
Drift, den die Einzelkapitel-Pipeline nicht sieht.

## Ablauf

1. `.venv/bin/python scripts/validate_schema.py <buch>`
2. `.venv/bin/python scripts/coverage_stats.py <buch>` — liefert:
   Soll/Ist neuer Vokabeln, Recycling-Quoten, Grammatik-Abgleich mit dem
   Curriculum, nie wiederverwendete Wörter.
3. `.venv/bin/python scripts/continuity_check.py <buch> --all --json`
4. **continuity-checker**-Agent triagiert die Treffer aus Schritt 3 über alle
   Kapitel (VERSTOSS / LEMMATIZER-MISS / FEHLENDE-DEKLARATION / EIGENNAME).
5. Auswertung an den Nutzer:
   - Verstöße je Kapitel (mit Triage-Verdikt)
   - vorgeschlagene `inflected_forms`-Ergänzungen als fertige YAML-Schnipsel
     — erst nach Bestätigung des Nutzers in die Sidecars übernehmen
   - Curriculum-Drift (vocab_target verfehlt, Recycling unter Minimum,
     Grammatik-IDs ohne Deckung)
   - „tote" Wörter (eingeführt, nie wiederverwendet) — als Hinweis an
     künftige Kapitel/Curriculum, nicht als Fehler
6. Echte Verstöße in die notes.md der betroffenen Kapitel eintragen
   (Checkboxen), mit Hinweis auf /review-chapter.

Keine automatischen Edits an Kapitelinhalten — dieser Skill diagnostiziert.
