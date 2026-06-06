---
name: plan-curriculum
description: Erstellt oder überarbeitet das Master-Curriculum eines Buches (A0→C1) mit dem curriculum-architect-Agenten, validiert Schema und Struktur. Aufruf - /plan-curriculum <buch>
---

# /plan-curriculum <buch>

Erzeugt bzw. überarbeitet `books/<buch>/curriculum.yaml` — das Fundament des
Buches. Hier wird NICHT geschrieben, nur geplant.

## Ablauf

1. **Bestandsaufnahme:** Existiert schon ein Curriculum? Gibt es Kapitel mit
   Status über `geplant`? (Dann dürfen nur künftige Kapitel geändert werden —
   dem Agenten mitgeben.)
2. **Neuentwurf in zwei Stufen** (bei bestehendem Curriculum: nur Stufe 2 für
   die betroffenen Teile):
   - Stufe A: **curriculum-architect** entwirft die Grobgliederung — Units je
     GER-Stufe, Kapitelanzahl, Themenbögen, Figuren/Schauplätze als roter
     Faden. Diese Grobgliederung dem Nutzer zur Bestätigung vorlegen
     (AskUserQuestion), BEVOR die Detailarbeit beginnt — sie zu revidieren
     ist später teuer.
   - Stufe B: **curriculum-architect** arbeitet die Kapitel aus und schreibt
     curriculum.yaml. Bei sehr vielen Kapiteln in Tranchen je GER-Stufe
     (eigener Agent-Aufruf pro Unit, jeweils mit der fertigen YAML der
     vorigen Units als Kontext), damit die Progression nahtlos bleibt.
3. **Validierung (mechanisch):**
   - `.venv/bin/python scripts/validate_schema.py <buch>`
   - `.venv/bin/python scripts/coverage_stats.py <buch> --dry`
   Fehler gehen zur Korrektur an den curriculum-architect zurück (max. 2
   Runden, dann Stopp und Nutzer fragen).
4. **Abnahme:** Zusammenfassung an den Nutzer — Kapitelzahl je Stufe,
   Grammatik-Meilensteine, geschätzter Gesamtwortschatz. Kein Auto-Start des
   Schreibens: Das Curriculum soll der Nutzer in Ruhe ansehen.

## Grundsätze

- Strukturfehler im Curriculum werden nie „hingebogen" — sie gehen immer
  zurück an den Agenten oder den Nutzer.
- Einmal vergebene grammar-IDs und slugs sind Verträge (Sidecars verweisen
  darauf) — bei Überarbeitungen niemals umbenennen.
