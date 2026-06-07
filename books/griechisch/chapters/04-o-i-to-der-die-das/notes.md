# Pipeline-Protokoll — Kapitel 4: o-i-to-der-die-das

- Lauf: /new-chapter griechisch 4, gestartet 2026-06-06
- Curriculum: artikel-genus-nom-sg (+ recycle praesens-omega-sg, hoeflichkeitsformeln)
- vocab_target 16, vocab_recycle_min 6; Themen Nachbarschaft/Stadtviertel/Orte/Personen
- cultural_topic: γειτονιά (Nachbarschaft), María als Nachbarin

## Befunde

### Phase 1 (Schreiben)

- meta.yaml angelegt; chapter.md (vorhandener Entwurf) gegen die eiserne Regel
  geprüft und an zwei Stellen korrigiert:
  - Dialog-Schluss „Όλα εδώ." entfernt — όλα ist eine Pluralform, Plural kommt
    erst Kap. 15. Schluss jetzt „Εδώ η γειτονιά, Λένα!" (nur Bekanntes).
  - Endungsregeln im Grammatikteil umformuliert: statt freistehender
    griechischer Endungsfragmente (-ος, -α, -η …; Verstoß gegen Regel 5,
    Tokenizer) jetzt lateinische Umschrift mit deutscher Erklärung, die
    Endung am ganzen, deklarierten Beispielwort sichtbar.
- 16 thematische Nomen neu eingeführt (Vokabel-Richtwert genau getroffen),
  je mit Genus/Artikel. Dazu deklariert: die Artikel ο und το (Grammatik-
  Neueinführung; η war Kap. 3 rezeptiv) sowie das Adverb εκεί (Pendant zu εδώ).
- 17 Vokabeln aus Kap. 1–3 recycelt (Vorgabe: min. 6); praesens-omega-sg
  (Τι κάνεις;, μένω implizit) und Höflichkeitsformeln natürlich wiederverwendet.
- Kein Akkusativ/Genitiv, kein Plural, kein unbestimmter Artikel — bewusst im
  Nominativ Singular geblieben.
- Selbstanmerkung für die Prüfphase: φούρνος, αγορά, φαρμακείο, γειτόνισσα
  erscheinen nur in der Grammatik-Prosa als Kontrast-/Endungsbeispiele
  (rezeptiv), nicht im Dialog. Falls der continuity-checker engere Dialog-
  Verankerung verlangt, ließen sie sich reduzieren; ich halte sie als
  Genus-Kontraste (deutsch ≠ griechisch) jedoch für didaktisch wertvoll.
- continuity_check.py konnte ich mangels Ausführungsrecht nicht selbst laufen
  lassen; alle Greek-Tokens manuell gegen kumulatives + neu deklariertes
  Vokabular abgeglichen — ohne Restbefund (Eigennamen Μαρία/Λένα/Κώστας
  ausgenommen).

### Phase 2 (Übungen)

- 7 Übungen + vollständiger Lösungsschlüssel ergänzt; meta.yaml exercises
  aktualisiert (count 7, types: article-recognition, genus-sorting, gap-fill,
  contrast-multiple-choice, matching, guided-production, free-production).
- Progression rezeptiv → frei: Ü1 Artikel erkennen → Ü2 nach Genus sortieren
  → Ü3 Lückentext (Artikel einsetzen) → Ü4 deutsche Genus-Falle (Kerntyp,
  Distraktoren = je das vom deutschen Wort verleitete falsche Genus) → Ü5
  Wortschatz-Wiederholung (matching) → Ü6 gelenkte Produktion (mit Artikel
  antworten) → Ü7 freie Produktion (eigenes Viertel zeigen).
- Übungen verwenden durchgehend Figuren/Schauplatz des Kapitels (María, Lena,
  Kώστας, die γειτονιά) und Dialogwendungen (εδώ/εκεί + Ort + Artikel).
- Eiserne Regel eingehalten: ausschließlich Nominativ Singular, kein Plural,
  kein Akkusativ/Genitiv, kein unbestimmter Artikel (ένας/μία/ένα erst Kap. 5).
  Distraktoren in Ü4 sind ausschließlich die drei bekannten Artikel ο/η/το.
  Recycling: Ü5 ist reine Wortschatz-Wiederholung; εδώ (Kap. 3), ναι, καλά u. a.
  in den Aufgabenstellungen wiederverwendet.

## /new-chapter griechisch 4 — Phase 2 (parallele Prüfung) — 2026-06-07

Baseline nach exercise-designer: validate_schema 0 Fehler, continuity_check 0 Verstöße (nur Eigennamen).

### Befunde Runde 1
- continuity-checker: **KONTINUITÄT OK** (0 Verstöße; durchgehend Nominativ Singular, kein Plural/Kasus/unbestimmter Artikel; alle Tokens deklariert/recycelt)
- reviewer: **überarbeitung nötig** (Genus aller 16 Nomen, Akzente, Übungslogik korrekt):
  - [ ] R1 [major] chapter.md:121-127 — Genus-Endungsregeln in lateinischer Umschrift („-os/-a/-i/-ma") statt griechischer Schrift → Transliterationsverbot (didaktik.md) verletzt. Auf griechische Endungen umstellen (-ος/-α/-η/-ο/-ι/-μα).
  - [ ] R2 [major] chapter.md:207-208 (Übung 2 Aufgabenstellung) — gleiche Transliteration, zusätzlich INKONSISTENT (-ος/-α griechisch, „-i" lateinisch in einem Satz). → exercise-designer.
  - [ ] R3 [minor] chapter.md:110-113 — Aussprache-Lautannäherungen („o"/„to"/„i") Grenzfall; als echte Aussprachehilfe vertretbar, teacher-Urteil.
  - [ ] R4 [minor] chapter.md:247 (Übung 5) — Titel „Wiederholung" irreführend (prüft NEU eingeführtes Vokabular) → „Wortschatz festigen". → exercise-designer.
- reader: **COMPREHENSION-FAILURE** → an Nutzer eskaliert; Entscheidung: „Fixen & weiterlaufen" (Box-Failure ist design-bedingtes Falsch-Positiv, Build füllt aus meta.yaml). Befunde:
  - [ ] L1/L4/L5 leere Wortschatz-Box & Übungswörter nur in Grammatik → BY DESIGN (Build generiert Box aus meta.yaml; alle Wörter deklariert — von continuity+reviewer bestätigt). Keine inhaltliche Aktion.
  - [ ] L2/L3 [gap, ECHT] Eta(η)/Jota(ι)-Unterscheidung am Schriftbild/Klang, bevor Alphabet eingeführt — η und ι klingen beide „i", am Klang nicht trennbar; Schriftbild-Beschreibung („n mit Bein") setzt Alphabetkenntnis voraus. → Genusregel auf die GESCHRIEBENE Endung in griechischer Schrift umstellen (deckt R1/R2 mit ab), nicht auf Hören/Buchstabenform.
  - [ ] L6 [pacing] Genus-Erkennungs-Abschnitt zu dicht (4 Konzepte/10 Zeilen) → beim Umbau entzerren.
  - [ ] L7 [gap] Übung 6 verlangt aktiv Artikel vor Eigennamen (___ Κώστας;), im Kapitel nicht aktiv vorbereitet → exercise-designer: Item anpassen oder im Text die Artikel-vor-Namen-Produktion knapp decken.
- ai-guard: **überwiegend menschlich**, KI-Schablone v. a. im Genus-Mittelteil:
  - [ ] G1/G2/G4 chapter.md:117-127 — leere Meta-Ankündigung „Jetzt kommt der Punkt, an dem das Griechische dir tatsächlich hilft" + schematischer Dreier-Bullet-Block → in Fließtext/variieren (deckt sich mit L6/R1-Umbau)
  - [ ] G3 [hedging] chapter.md:129-130 „verlässliche Faustregeln, keine eisernen Gesetze" → direkter, mit konkretem Ausnahmebeispiel (ο άντρας)
  - [ ] G5 [rhythmus] chapter.md:138-141 drei mittellange Sätze → Kurzschlag einbauen
  - [ ] G6 [hedging] chapter.md:160-163 „Das ist angenehm" Mittelsatz streichen
  - [ ] G7 [floskel] chapter.md:82-84 „Sieh dir an, was María vor jedem Ding sagt" Meta-Ankündigung straffen
  - [ ] G8 [symmetrie] Dreischritt zeigen→erklären→tabellieren wiederholt sich (Z.82-103/117-134/165-178) → einen Abschnitt anders bauen
