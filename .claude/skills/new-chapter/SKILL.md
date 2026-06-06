---
name: new-chapter
description: Schreibt ein neues Lehrbuchkapitel über die volle Agenten-Pipeline (teacher → exercise-designer → parallele Prüfung → Überarbeitung). Läuft hybrid-autonom mit definierten Stop-Bedingungen. Aufruf - /new-chapter <buch> <kapitelnummer>
---

# /new-chapter <buch> <N> — Kapitel-Pipeline

Orchestriert das Schreiben von Kapitel N. Du (der Hauptagent) bist der
Orchestrator: Du startest Subagenten via Agent-Tool, sammelst Befunde und
entscheidest nach den Regeln unten. Inhaltliche Eingriffe machst du nicht
selbst — schreiben tun teacher und exercise-designer.

## Phase 0 — Setup

1. Lies `books/<buch>/curriculum.yaml`; existiert der Eintrag für Kapitel N
   nicht → Abbruch mit Hinweis auf /plan-curriculum.
2. Prüfe, dass die Kapitel 1..N-1 existieren und mindestens Status
   `draft-complete` haben (meta.yaml). Lücken → Stopp, Nutzer fragen.
3. Lege `books/<buch>/chapters/NN-slug/` an (Nummer zweistellig, slug aus
   Curriculum). Existiert das Kapitel schon mit Status über `geplant` →
   Stopp, Nutzer fragen (Überschreiben ist destruktiv).
4. Leere `notes.md` anlegen mit Kopf: Kapitel, Datum, Pipeline-Lauf.

## Phase 1 — Schreiben

5. **teacher**-Agent: Kapitel N schreiben (chapter.md + meta.yaml). Gib ihm
   im Prompt: Buch, Kapitelnummer, den Curriculum-Eintrag wörtlich, und den
   Hinweis, das kumulative Vokabular aus den meta.yaml der Vorkapitel zu
   lesen.
6. Danach sofort mechanisch: `.venv/bin/python scripts/validate_schema.py <buch>`
   — Schema-Fehler gehen als Korrekturauftrag zurück an den teacher, bevor
   irgendein Review läuft.
7. **exercise-designer**-Agent: Übungen + Lösungsschlüssel ergänzen.

## Phase 2 — Parallele Prüfung

8. Starte parallel (ein Block, mehrere Agent-Aufrufe):
   - **continuity-checker**: Buch + Kapitelnummer nennen.
   - **reviewer**: Kapitelpfad nennen.
   - **reader**: WICHTIG — nenne ihm ausschließlich die Pfade der
     chapter.md von Kapitel 1..N. Weise ihn an, NICHTS anderes zu lesen
     (keine meta.yaml, kein Curriculum, keine späteren Kapitel — die
     enthalten Wissen, das der Lernende noch nicht hat).
   - **ai-guard**: Kapitelpfad nennen.
   - **cultural-reviewer**: nur falls das Kapitel laut Curriculum ein
     cultural_topic hat oder der Dialog landeskundliche Aussagen macht.

## Phase 3 — Befunde konsolidieren

9. Trage alle Befunde als Checkboxen in `notes.md` ein, gruppiert nach Agent,
   mit Original-Kennung (R1, L2, C3, G4, K5 …).
10. Klassifiziere:
    - **Sofort-Stopp (an Nutzer eskalieren, Pipeline-Ende):**
      a) reader meldet `COMPREHENSION-FAILURE`;
      b) Befunde widersprechen sich (z. B. reviewer fordert idiomatischere
         Wendung, die continuity-checker als nicht eingeführt blockt) und es
         gibt keine Lösung, die beide erfüllt;
      c) ein Befund stellt den Curriculum-Eintrag selbst in Frage (Sprung zu
         groß, vocab_target unrealistisch).
      Beim Stopp: Konflikt in 3–5 Sätzen zusammenfassen, konkrete Optionen
      nennen, Frage an den Nutzer.
    - **Überarbeitbar:** alles andere.

## Phase 4 — Überarbeitung (max. 3 Runden)

11. **teacher** (und bei Übungs-Befunden **exercise-designer**) mit den
    offenen Befunden aus notes.md beauftragen; sie haken ab.
    LEMMATIZER-MISS-Schnipsel des continuity-checkers darfst du direkt in die
    betreffenden meta.yaml übernehmen (mechanische Änderung).
12. Danach erneut prüfen — aber nur mit den Agenten, die Befunde hatten
    (grüne Prüfer nicht wiederholen), plus IMMER continuity-checker, wenn
    sich griechischer Text geändert hat.
13. Markiert ein Schreibagent einen Befund als `[verweigert]` und der
    Prüfagent besteht in der Folgerunde darauf → Sofort-Stopp (b).
14. Nach 3 Runden nicht grün → Stopp, Lage zusammenfassen, Nutzer fragen.

## Phase 5 — Abschluss

15. Alle Prüfer grün UND `continuity_check.py` ohne VERSTOSS:
    - meta.yaml: `status: draft-complete`
    - Smoke-Test: `make chapter/<buch>/<N>` (Build-Fehler → beheben lassen)
    - Kurzbericht an den Nutzer: was das Kapitel lehrt, wie viele Befunde es
      gab und wie sie gelöst wurden, was offen blieb, Pfad zum PDF.

## Grundsätze

- Du veränderst Kapitelinhalte nie selbst (Ausnahme: Schritt 11,
  inflected_forms). Urteile fällen die Spezialisten.
- Jeder Pipeline-Schritt hinterlässt seine Spur in notes.md — das ist das
  Protokoll für /status und für spätere Läufe.
- Bei jedem Stopp: Zustand ist gespeichert; /review-chapter kann nach der
  Nutzer-Entscheidung wiederaufsetzen.
