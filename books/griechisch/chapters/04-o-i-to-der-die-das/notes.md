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
  - [x] R1 [major] chapter.md:121-127 — Genus-Endungsregeln umgebaut: keine lateinische Umschrift mehr, Regel knüpft an die GESCHRIEBENE Endung an, gezeigt an ganzen deklarierten Beispielwörtern (ο δρόμος/φούρνος/σκύλος; η πλατεία/αγορά/εκκλησία; το σχολείο/μαγαζί/σπίτι). Keine isolierten Endungsfragmente.
  - [x] R2 [major] chapter.md (Übung 2 Aufgabenstellung) — erledigt (exercise-designer, 2026-06-07): Faustregel jetzt vollständig in griechischer Schrift an ganzen deklarierten Beispielwörtern (Wörter, die wie **ο δρόμος** aufhören → männlich; wie **η αγορά** → weiblich; wie **το σχολείο**/**το σπίτι** → sächlich). Keine Transliteration, keine isolierten Endungsfragmente; konsistent mit dem überarbeiteten Grammatikteil (Anknüpfung an die GESCHRIEBENE Endung am ganzen Wort).
  - [x] R3 [minor] chapter.md:110-113 — Aussprache-Hinweis als echte Aussprachehilfe belassen, aber rein verbal umformuliert (keine quotierten Latein-Laute mehr außer den vollen deutschen Vergleichswörtern Sonne/Biene).
  - [x] R4 [minor] chapter.md (Übung 5) — erledigt (exercise-designer, 2026-06-07): Titel jetzt „(Wortschatz festigen)", Untertext „So festigst du den neuen Wortschatz des Kapitels". Kein irreführendes „Wiederholung" mehr.
- reader: **COMPREHENSION-FAILURE** → an Nutzer eskaliert; Entscheidung: „Fixen & weiterlaufen" (Box-Failure ist design-bedingtes Falsch-Positiv, Build füllt aus meta.yaml). Befunde:
  - [ ] L1/L4/L5 leere Wortschatz-Box & Übungswörter nur in Grammatik → BY DESIGN (Build generiert Box aus meta.yaml; alle Wörter deklariert — von continuity+reviewer bestätigt). Keine inhaltliche Aktion.
  - [x] L2/L3 [gap, ECHT] Genus-Abschnitt komplett auf das GESCHRIEBENE Wortende umgestellt; keine Eta/Jota-Namen, keine Buchstabenform-Beschreibung mehr. Regel knüpft ausdrücklich ans Wortbild („das Auge entscheidet, nicht das Ohr"), gezeigt an ganzen deklarierten Beispielwörtern. Klang nur noch in der separaten Aussprachehilfe (R3).
  - [x] L6 [pacing] Genus-Erkennungs-Abschnitt entzerrt: Faustregel (3 Wortgruppen) → Ausnahme (ο άντρας) → zentraler Rat (jedes Nomen mit Artikel lernen), nacheinander statt 4 Konzepte auf einmal.
  - [x] L7 [gap] erledigt (exercise-designer, 2026-06-07): Lösung (a) gewählt — das Eigennamen-Item entfernt; Übung 6 verlangt jetzt durchgehend nur Artikel-vor-Ding mit gewöhnlichen, eingeführten Nomen (η εκκλησία, το μαγαζί, η πλατεία, το σχολείο). Artikel-vor-Name bleibt der freien Produktion (Ü7, mit ο Κώστας als optionalem, im Dialog modelliertem Angebot) vorbehalten; keine ungedeckte aktive Produktion mehr.
- ai-guard: **überwiegend menschlich**, KI-Schablone v. a. im Genus-Mittelteil:
  - [x] G1/G2/G4 chapter.md — Meta-Floskel „Jetzt kommt der Punkt …" gestrichen; Genus-Abschnitt steigt direkt mit der Sachaussage ein. Bullet-Block bleibt als Faustregel-Liste, aber rhythmisch eingebettet (Faustregel → Ausnahme im Fließtext → Rat).
  - [x] G3 chapter.md — „Faustregeln, keine Gesetze. Verlass dich nicht blind darauf." direkt, mit konkretem Ausnahmebeispiel **ο άντρας** (endet wie ein weibliches Wort, ist männlich).
  - [x] G5 chapter.md — Kurzschlag eingebaut: „Deshalb hilft am Ende nur eins." als kurzer Satz vor dem Rat, jedes Nomen mit Artikel zu lernen.
  - [x] G6 chapter.md — Übereinstimmungs-Absatz gestrafft; Mittelsatz weg, Pointe (**η γυναίκα**/**το σπίτι** = Zufall, keine Regel) trägt allein.
  - [x] G7 chapter.md — Meta-Ankündigung gestrafft: „Vor jedem Ding im Dialog steht ein kurzes Wörtchen:" statt der ausgewalzten Aufforderung.
  - [x] G8 chapter.md — Abschnitt „Auch Personen haben ein grammatisches Genus" umgebaut: kein Zeig-Block + Tabelle mehr, sondern durchlaufende Prosa (Mann/Frau/Rollenwörter in einem Satz, Kind-Ausnahme als eigener Gedanke) — bricht den Dreischritt-Rhythmus.
- cultural-reviewer: **Befunde** (Landeskunde atmosphärisch gut, aber γειτονιά leicht verklärt):
  - [x] K1 chapter.md — Untertitel neutral: „η γειτονιά — Viertel, Nachbarschaft, soziales Netz". Gegenwartsbezug abgesichert: „Am spürbarsten … in kleineren Städten, auf den Inseln und in gewachsenen Wohnstraßen, aber auch mitten in Athen oder Thessaloniki …" — keine Allgemeingültigkeit mehr.
  - [x] K3 chapter.md — präzisiert: „Eine Kirche hat jede γειτονιά — mindestens eine, und oft gibt sie dem ganzen Viertel den Namen". Kirchen-Eigennamen lateinisch umschrieben (Agios Pandeleïmonas, Agia Paraskevi) → Continuity-neutral, keine griechischen Tokens nötig.
  - [x] K4 chapter.md — „deutsche Distanz" ersatzlos gestrichen. Einbindung differenziert: „Wer neu zuzieht, dem begegnet oft viel Neugier und Offenheit … Wirklich dazuzugehören braucht trotzdem seine Zeit — die ersten Fragen sind ein freundlicher Anfang, nicht schon die ganze Aufnahme."
  - [x] K5 chapter.md — Satz zum φαρμακείο ergänzt: erste Anlaufstelle bei kleinen Beschwerden, bevor man an einen Arzt denkt. Überlädt die Sektion nicht.
  - [x] K7 chapter.md — regionale/soziale Differenzierung im selben Satz wie K1: lebendiger in Kleinstädten/auf Inseln/in gewachsenen Wohnstraßen, aber auch in alten Vierteln Athens/Thessalonikis.

## Phase 4 — Re-Review Runde 1 (nach teacher+exercise-designer)
- continuity: 0 Verstöße; reviewer: **FREIGABE** (Transliteration weg, Genusregel ans Schriftbild geknüpft, Genus/Akzente/Lösungen korrekt); cultural: **FREIGABE** (K1/K3/K4/K5/K7 sachlich gelöst, nicht überkorrigiert)
- reader: **kein COMPREHENSION-FAILURE** (Genusregel jetzt durcharbeitbar). Restliche gaps:
  - [x] L2 [gap] chapter.md:117-120 — erledigt (teacher, Runde 2): abstrakte Falle „hören gleich auf, klingen aber verschieden geschrieben" gestrichen (kein sauberes Beispiel ohne neue Nomen mit gleichem Klang/verschiedener Schrift verfügbar — ω/ο bzw. η/ι/ει-Paare nicht im deklarierten Wortschatz). Aussage trägt jetzt allein über „das Auge entscheidet hier, nicht das Ohr".
  - [x] L3 [gap] chapter.md:125-131 — erledigt (teacher, Runde 2): Endungen jetzt benannt und am ganzen Wort fett hervorgehoben (Wörter auf **-ος** wie ο δρόμ**ος**; auf **-α**/**-εία** wie η αγορ**ά**, η πλατ**εία**; auf **-ι**/**-ο** wie το μαγαζ**ί**, το σχολεί**ο**). Damit greifbar und auf Übung 2 anwendbar. Tokenizer-Check: `**` werden vor Tokenisierung entfernt → δρόμ**ος** wird zum ganzen Token δρόμος (deklariert); freistehende **-ος** etc. mit führendem Bindestrich fallen unter den Lookbehind-Guard der GREEK_TOKEN_RE (kein Match nach „-") → kein isoliertes Fragment, continuity-neutral.
  - [x] L4 [confusing] ο άντρας — erledigt (teacher, Runde 2): Ausnahme steht jetzt direkt nach der Faustregel mit benannter Endung („Das Wort hört auf **-ας**, sieht damit beinahe weiblich aus, und ist trotzdem männlich"), Schlusssatz „deshalb steht die Ausnahme hier gleich neben der Regel" macht die Reihenfolge explizit. Harte Reihenfolge entschärft.
  - [ ] L5 φούρνος/φαρμακείο/γυναίκα nur in Grammatik/Tabelle → BY DESIGN (in meta.yaml deklariert, Build-Box deckt sie); keine Aktion
  - [x] L6 [confusing] Übung 6 — erledigt (exercise-designer, 2026-06-07): Option (b) gewählt — in Lenas Frage steht der Artikel jetzt fest (η εκκλησία / το μαγαζί / η πλατεία / το σχολείο, Beispiel: ο δρόμος), nur Marías Antwort hat eine Lücke. Aufgabenstellung sagt das explizit („In Lenas Frage steht der Artikel schon da — füll nur Marías Antwort aus"). Lösungsschlüssel füllte ohnehin nur die Antwort → jetzt konsistent. Begründung für (b): Artikel-Einsetzen im Satz ist Ü3; Ü6 ist gelenkte Antwort-Produktion, da soll die Frage als sauberes Input-Modell stehen. Nur eingeführtes Material (Nom. Sg., ο/η/το, deklarierte Nomen).
  - [ ] L1 η-Aussprache/Alphabet-Metafrage → CURRICULUM-EBENE (kein Alphabet-Vorkapitel), kein Kapitel-Defekt; keine Aktion
- ai-guard: **überwiegend menschlich**, Reste:
  - [x] G1 [doppelung] chapter.md:84-95 — erledigt (teacher, Runde 2): Prosa-Nachsatz entwiederholt; statt „Vor jedem Hauptwort steht ein kurzes Wörtchen …" jetzt „Mal **η**, mal **ο**, mal **το** — das ist der bestimmte Artikel." Keine wortgleiche Doppelung zur Blockquote-Einleitung mehr.
  - [x] G2 [liste] chapter.md:125-131 — erledigt (teacher, Runde 2): Dreier-Bullet-Block in Fließtext umgeformt (drei Endungen in lebendigem Absatz, Endungen benannt) → löst zugleich L3. Letzte Schablonenstelle aufgelöst.
  - [x] G3 [floskel] chapter.md:316 — erledigt (teacher, Runde 2): „Und ganz nebenbei" im Landeskunde-Schluss gestrichen, Absatz steigt direkt mit der Sachaussage ein; Pointe (echtes Griechisch beim Grüßen) trägt allein. Zusätzlich Runde 2 (Re-Review): Die Floskel stand noch wortgleich im Dialog-Nachsatz (Z.65 „und ganz nebenbei taucht vor jedem Ding …") → dort entfernt: „und vor jedem Ding taucht ein kleines Wort auf …". Keine Floskel-Doppelung mehr zwischen Dialog-Schluss und Landeskunde.
  - [x] G4 [rhythmus] chapter.md:77-80 — erledigt (teacher, Runde 2): vier gleichlange Sätze aufgebrochen, Kurzsatz „Sie zeigen das **Genus** des Hauptworts an: …" + „Das Griechische macht es genauso, nur mit anderen Wörtern." → variierender Rhythmus, Lehrerstimme.

### Fokussierte Re-Review Runde 2 (teacher, 2026-06-07) — Verifikation + Restfix
- Kern L3/G2: Genusregel ist benennbar — drei Endungen im Fließtext benannt und am ganzen Wort fett hervorgehoben (**-ος** an ο δρόμ**ος**/φούρν**ος**/σκύλ**ος**; **-α**/**-εία** an η αγορ**ά**/πλατ**εία**/εκκλησ**ία**; **-ι**/**-ο** an το μαγαζ**ί**/σπίτ**ι**/σχολεί**ο**). Auf Übung 2 anwendbar. Kein Bullet-Block mehr.
- Tokenizer-Verifikation gegen lib/greek.py: (1) tokenize() entfernt `**` vor dem Matchen → δρόμ**ος** = ganzes Token δρόμος (deklariert). (2) GREEK_TOKEN_RE-Lookbehind `(?<![…-])` blockiert jedes Match nach Bindestrich → freistehende **-ος**/**-α**/**-εία**/**-ι**/**-ο**/**-ας** erzeugen KEINE Tokens. Continuity-neutral, kein isoliertes Fragment.
- L2: bereits gelöst (abstrakte Falle gestrichen, „das Auge entscheidet, nicht das Ohr" trägt allein) — bestätigt.
- L4: ο άντρας steht direkt nach der Faustregel mit benannter Endung **-ας** („sieht beinahe weiblich aus, ist trotzdem männlich"); Reihenfolge explizit gemacht — bestätigt.
- G1: Dialog-Blockquote-Einleitung und Prosa-Nachsatz nicht mehr wortgleich („Mal **η**, mal **ο**, mal **το** — das ist der bestimmte Artikel.") — bestätigt.
- G3: Restfix im Dialog-Schluss (s. o.) durchgeführt.
- G4: Rhythmus im Grammatik-Einstieg variiert — bestätigt.
