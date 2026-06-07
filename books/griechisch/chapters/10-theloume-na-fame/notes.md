# Pipeline-Protokoll — Kapitel 10: theloume-na-fame

- Lauf: /new-chapter griechisch 10, gestartet 2026-06-07
- Curriculum: praesens-omega-pl (Präsens -ω Plural; θέλω να + Verb als Chunk),
  CEFR A1 (+ recycle praesens-omega-sg, fragewoerter-demonstrativa)
- vocab_target 16, vocab_recycle_min 8; Themen Essen/Taverne/Wünsche/Bestellen
- cultural_topic: gemeinsam essen — μεζέδες teilen statt Einzelportionen
- can_do: sagen, was man möchte (θέλω…) und einen Wunsch mit να äußern
  (θέλω να φάω); das Präsens auf -ω im Plural gebrauchen (θέλουμε, μένουν);
  zu zweit eine Bestellung formulieren

## Befunde

### Phase 1 (Schreiben — teacher, 2026-06-07)

- chapter.md, meta.yaml und notes.md neu erstellt. Alle Sektions-Marker gesetzt:
  lernziele, dialog lang=el, vokabeln [leer, nur Überschrift], grammatik,
  uebungen [Platzhalter], landeskunde, loesungen [Platzhalter]. Übungen +
  Lösungen bewusst leer für den exercise-designer (exercises: count 0, types []).
  status: entwurf.

- **Grammatik-Aufbau** (Beispiele → Muster → Regel, wie Kap. 3–9): erst der
  Vergleich θέλω/θέλουμε aus dem Dialog (ich → wir), dann die vollständige
  Paradigma-Tabelle (Singular Kap. 3 als obere Hälfte, Plural neu als untere),
  Endungen am ganzen Wort hervorgehoben (κάν**ουμε**, μέν**ουν**), kein
  Dreier-Bullet-Block. Aussprache-Falle -ουμε (voller u-Laut) auf Deutsch.
  Dann der Aha-Moment Τι κάνετε;, dann θέλω voll konjugiert, dann der να-Wunsch
  als Chunks, zuletzt die -ομε-Falle (deutsch benannt, keine ausgeschriebene
  Falschform).

- **Aha-Moment Τι κάνετε; ausdrücklich genutzt (Vorgabe):** eigener Abschnitt.
  Das in Kap. 3 rezeptiv als Höflichkeits-Block gelernte Τι κάνετε; wird als
  κάν-ετε = die -ετε-Pluralform identifiziert und ins System eingeordnet; der
  Kellner sagt parallel Τι θέλετε;. Doppelrolle -ετε = höfliches Sie / ihr
  explizit gemacht.

- **θέλω να als Chunks (Vorgabe):** θέλω να φάω / θέλουμε να φάμε / θέλω να πιω
  als feste Blöcke behandelt; offen gesagt, dass φάω/φάμε/πιω eine eigene
  Verbform (Aorist-/Konjunktivstamm) sind, die nach να verlangt wird und erst
  später systematisch kommt (wie das Block-Vorgehen bei Τι κάνετε;). Ausdrückliche
  Warnung: Chunks nicht aus Teilen bauen, φάω nicht in andere Personen setzen.
  να als „Scharnier" erklärt (deutsch „zu" / unsichtbar).

- **Plural NUR bei Verben (Vorgabe):** Alle Nomen im Dialog/Grammatik/Landeskunde
  stehen im Nominativ Singular (το ψάρι, μία σαλάτα, το κρασί, η κάρτα …). Plural
  tritt ausschließlich an den Verbformen auf (θέλουμε, θέλετε; κάνουμε/κάνετε/
  κάνουν, μένουμε/μένετε/μένουν in der Tabelle). Nomen-Plural erst Kap. 15 —
  bewusst gemieden.

- **μεζέδες NICHT in griechischer Schrift (Vorgabe):** In der Landeskunde nur
  das Konzept auf Deutsch beschrieben (kleine geteilte Gerichte in der Tischmitte,
  „haben einen eigenen Namen, den du später noch lernst"). Kein griechisches
  Plural-Wort μεζέδες im Text.

- **Landeskunde** (gemeinsam essen, Teilen): konkret und differenziert (Vorgabe).
  Kontrast deutsches Restaurant (Einzelteller) vs. ταβέρνα (gemeinsame Bestellung,
  Schüsseln in der Tischmitte, jeder kostet von allem). Sprachlicher Bezug: deshalb
  am Tisch so oft das wir (θέλουμε να φάμε). Klischeefrei: ausdrücklich KEIN
  tägliches Festgelage — werktags mittags schnell/schlicht und jeder für sich;
  das geteilte Essen gehört eher Abend/Wochenende/Familie. Es geht ums Miteinander,
  nicht um die Menge — keine „üppig feiernde Griechen"-Folklore.

### Vokabel-Bilanz

- **NEU eingeführt (12 Einträge in vocab_introduced; Lernpensum im Zielband 16):**
  - **θέλω** (verb) — neues Verb, volles Paradigma; Pluralformen θέλεις/θέλει/
    θέλουμε/θέλετε/θέλουν als inflected_forms.
  - **θέλω-να-Chunks** (3 × phrase): θέλω να φάω, θέλουμε να φάμε, θέλω να πιω;
    je mit den να-Verbformen (να φάω/φάω, να φάμε/φάμε, να πιω/πιω) als
    inflected_forms-Backstop für den Tokenizer.
  - **Plural-Backstop für bekannte -ω-Verben (Grammatik-Kern):** κάνω und μένω
    (Lemmata aus Kap. 3) hier ERNEUT in vocab_introduced, aber ausschließlich mit
    den NEUEN Pluralformen als inflected_forms (κάνουμε/κάνουν/κάνουνε;
    μένουμε/μένετε/μένουν/μένουνε), damit continuity_check/Tokenizer diese Formen
    als bekannt erkennt. Kein neues Lemma — Recycling mit erweitertem Paradigma;
    deshalb κάνω/μένω zusätzlich in vocab_recycled mit Hinweis.
  - **Taverne/Bestellen:** ταβέρνα (f), κάρτα (f, Speisekarte — Alternative zum
    bekannten μενού Kap. 5), σερβιτόρος (m, Kellner).
  - **Speisen/Getränke (alle Nom Sg):** σαλάτα (f), κοτόπουλο (n), κρασί (n).
  - **Belegdichte ≥ 2× in verschiedenen Kontexten:** θέλω/θέλουμε/θέλετε
    durchgehend (Dialog + beide Grammatik-Tabellen + Landeskunde); θέλω να φάω/
    θέλουμε να φάμε/θέλω να πιω je im Dialog + Grammatik + (φάμε) Landeskunde;
    κοτόπουλο 3×, κρασί 3×, σαλάτα 2×, ταβέρνα 2× (Dialog-Vorspann + Landeskunde),
    κάρτα 2× (κάρτα ansehen + Ορίστε η κάρτα). Pluralformen κάνουμε/μένουν etc. in
    der Paradigma-Tabelle (Lehrmaterial). Kein Einmal-Wort ohne Wiederaufnahme.

- **RECYCELT (Vorgabe min. 8; deklariert 28):** Verben κάνω/μένω (Kap. 3, jetzt
  Plural-System); Fragewort τι (Kap. 3/9); είναι (Kap. 6, Τι είναι φρέσκο εδώ;);
  εγώ (Kap. 6) / εσύ (Kap. 1) als betonte Subjekte am Tisch; εδώ (Kap. 3);
  ναι/και/πολύ/ωραία/ευχαριστώ/παρακαλώ/ορίστε (Kap. 1/2); μία (Kap. 5);
  καλησπέρα (Kap. 1); Getränke νερό (Kap. 2)/μπίρα (Kap. 5); Speisen ψάρι/ψωμί/
  πατάτα/φέτα (Kap. 9); Adjektiv φρέσκος (Kap. 9, sächl. φρέσκο); Artikel ο/η/το
  (Kap. 4). Grammatik-Recycling: praesens-omega-sg (Singular als obere Tabellen-
  hälfte, Brücke zum Plural) und fragewoerter-demonstrativa (τι in Τι θέλετε;).

### Eiserne-Regel-Selbstprüfung

- **Nur Bekanntes + Neudeklariertes + Eigennamen.** Alle griechischen Tokens
  (Lernziele, Dialog, Grammatik-Beispiele/Tabellen, Landeskunde) manuell gegen
  das kumulative Vokabular Kap. 1–9 + die Neudeklarationen abgeglichen.
  Eigennamen: Λένα, Νίκος, Μαρία — erlaubt, sparsam.
  - In der Entwurfsphase ENTFERNT, weil außerhalb des erlaubten Materials:
    - **έχει / έχω** (haben, erst Kap. 16): „Τι έχει η ταβέρνα;" → „Τι είναι
      φρέσκο εδώ;" (είναι Kap. 6, φρέσκο Kap. 9, εδώ Kap. 3).
    - **λίγο** (ein bisschen, nicht eingeführt): „λίγο ψωμί" → „Φρέσκο ψωμί";
      „Λίγο κρασί" → „Ναι, κρασί!".
    - **πιείτε** (να-Verbform 2. Pl., nicht als Chunk deklariert): Kellnerfrage
      „Και να πιείτε;" → „Και τι θέλετε;" (θέλετε regulär). Es bleiben nur die
      drei deklarierten να-Chunks φάω/φάμε/πιω.

- **Plural NUR bei Verbformen; Nomen im Nominativ Singular.** Geprüft: kein
  Nomen-Plural im ganzen griechischen Text. το ψάρι, το κοτόπουλο, η σαλάτα/μία
  σαλάτα, το κρασί, το ψωμί, η ταβέρνα, η κάρτα, ο σερβιτόρος — alle Nom Sg.
  Plural ausschließlich an Verben (θέλουμε/θέλετε im Dialog; volle Paradigma-
  Tabellen für κάνω/μένω/θέλω).

- **Keine σε+Artikel-Fusion außer στη/στην.** Im Kapitel kommt überhaupt keine
  σε-Fusion vor (Tavernen-Szene ohne Ortsangabe-Bedarf). στον/στο/στους nicht
  verwendet. Kein Genitiv, kein anderer Kasus als Nominativ.

- **Keine ausgeschriebenen Falschformen.** Die -ουμε-Falle wird über die
  Endungs-Notation behandelt: Überschrift „nicht auf -ομε", im Text „auf -ομε
  statt auf -ουμε" — Endungsnotation mit Bindestrich (wie die Curriculum-Vorgabe
  selbst „nicht auf -ομε" formuliert), KEIN ausgeschriebenes Falschwort *θέλομε.

- **Keine isolierten Einzelbuchstaben/Fragmente in deutscher Prosa.** Endungen
  durchgehend als Bindestrich-Notation (-ω/-εις/-ει/-ουμε/-ετε/-ουν, -ομε) —
  konsistent mit Kap. 3/9. Volle Formen am ganzen Wort hervorgehoben
  (κάν**ουμε**, μέν**ουν**, θέλ**ουμε**). Das anfangs eingebaute nackte Digraph-
  Fragment „**ου**" (ohne Bindestrich) ENTFERNT und durch „voller u-Laut" /
  Endung „-ουμε" ersetzt. Aussprache nur auf Deutsch kommentiert, keine
  Transliteration im Lauftext (nur *-ume* als Aussprachehinweis kursiv, wie
  „la-i-kí" in der Kap.-9-meta).

- **μεζέδες nicht in griechischer Schrift.** Bestätigt — Konzept nur deutsch
  beschrieben.

- **Akzente Monotoniko korrekt.** θέλω/θέλεις/θέλει/θέλουμε/θέλετε/θέλουν;
  φάω/φάμε/πιω; κοτόπουλο, κρασί (Endbetonung), σαλάτα, ταβέρνα, κάρτα,
  σερβιτόρος; να unbetont; να φάω/να φάμε/να πιω.

- **Stil.** Keine Meta-Ankündigungsfloskeln, kein „gute Nachricht"/„Keine Sorge"/
  „Das ist dein Anker"/„Schauen wir uns … an". Die drei Pluralendungen NICHT als
  schematischer Dreier-Bullet-Block, sondern in einem Fließtext-Satz + Tabelle
  mit am ganzen Wort hervorgehobenen Endungen. Konkrete Tavernen-Szene als Rahmen,
  variierter Satzrhythmus. Metasprache Deutsch.

- Hinweis für die Prüfphase: continuity_check.py / validate_schema.py mangels
  Ausführungsrecht nicht selbst gelaufen; Abgleich manuell. Besonders prüfen:
  Tokenisierung der inflected_forms (θέλουμε/θέλετε/θέλουν; κάνουμε/κάνουν;
  μένουμε/μένετε/μένουν; να φάω/φάω, να φάμε/φάμε, να πιω/πιω); dass κάνω/μένω-
  Doppel-Deklaration (nur Plural-Backstop) nicht als Lemma-Konflikt mit Kap. 3
  gewertet wird; dass die να-Chunks als phrase-Lemmata greifen.

### Phase 2 (Übungen — exercise-designer, 2026-06-07)

- 8 Übungen + vollständiger Lösungsschlüssel in @section: uebungen/loesungen
  geschrieben; meta.yaml exercises: count 8, types (Liste von Strings, kein
  items): matching, form-recognition, conjugation-gap-fill ×2, chunk-gap-fill,
  multiple-choice, dialogue-gap-fill, free-production. Progression rezeptiv
  (Ü1/2: Endung↔Person, Form zuordnen) → gelenkt (Ü3/4: Plural-Endung bzw. θέλω
  einsetzen; Ü5: θέλω-να-Chunk wählen; Ü6: MC; Ü7: Tavernen-Mini-Dialog) → frei
  (Ü8: eigener Bestelldialog zu zweit). Figuren/Schauplatz des Dialogs
  weiterverwendet (Lena/Níkos/María, ταβέρνα, Bestellen). Ü3 (κάνω/μένω-Plural,
  Singular-Brücke) deckt das Recycling praesens-omega-sg/-pl ab.

- **Befund + Korrektur — uneingeführte Subjektpronomen entfernt (eiserne Regel):**
  Der Erstentwurf der Übungen benutzte durchgängig **Εμείς** (wir) und einmal
  **Αυτοί** (sie) als explizite Subjekte. Beide sind NICHT eingeführt: vor Kap. 10
  existieren nur εγώ (Kap. 6) und εσύ (Kap. 1); εμείς/εσείς/αυτοί/αυτές fehlen
  völlig, αυτός (Kap. 9) ist nur Nom Sg ohne Plural. Der Kapitel-Dialog selbst
  drückt das wir korrekt nur über die Verbendung aus (Θέλουμε φρέσκο ψάρι, ohne
  Pronomen) — was ja das Lernziel ist. Daher alle Εμείς getilgt (Person nur über
  deutsche Klammer + Endung), Αυτοί μένουν → Η Λένα και η Μαρία μένουν (Eigennamen-
  Subjekt). Lösungen + Begründungen angeglichen; Großschreibung am Satzanfang
  korrigiert (Θέλουμε). In Ü3/Ü6 ausdrücklich didaktisiert: kein eigenes Wort für
  wir/sie nötig, die Endung trägt die Person.

- **Befund + Korrektur — άλλο (Ü7):** „Και τι άλλο θέλετε;" → „Και τι θέλετε;"
  (άλλο nicht eingeführt; ersetzt durch die Dialog-Formulierung Και τι θέλετε;).

- **Eiserne-Regel-Selbstprüfung Übungen:** Plural NUR an Verben (θέλουμε/θέλετε/
  θέλουν, κάνουμε/κάνετε, μένουν); alle Nomen Nom Sg (μία σαλάτα, το ψάρι, κρασί,
  ψωμί, κοτόπουλο, νερό, μπίρα …). θέλω να φάω/φάμε/πιω nur als ganze Chunks
  abgefragt (Ü5/Ü7/Ü8), φάω nie flektiert/zerlegt. Distraktoren in Ü6 = falsche
  Personalendung derselben Verbform (typischer Fehler), keine Unsinns-/
  Längenoptionen. Keine ausgeschriebenen Falschformen — -ομε nur als Endungs-
  notation benannt. στην Αθήνα nur als bekannter Block μένω στην Αθήνα (Kap. 6,
  στη/στην erlaubt). Eigennamen Λένα/Νίκος/Μαρία. Akzente Monotoniko geprüft.
  Aufgabenstellungen Deutsch, Beispiel-Item bei jedem neuen Übungstyp.

- Hinweis: continuity_check.py erneut über das ganze Kapitel laufen lassen —
  bestätigen, dass nach Tilgung von εμείς/αυτοί/άλλο keine uneingeführten Tokens
  mehr in den Übungen/Lösungen stehen.

### Phase 3 (Übungs-Korrektur — exercise-designer, 2026-06-07)

- [x] **Continuity — Übung 3: nackte Verbstämme + Lücke entfernt.** Der
  continuity_check flaggte die isolierten Stammfragmente (Θέλ/Κάν/μέν/κάν/θέλ aus
  „Θέλ______ νερό", „Κάν______ μία σαλάτα", „μέν______ εδώ", „Τι θέλ______;",
  „Τι κάν______;") als undeklarierte Tokens — es sind keine vollständigen Wörter.
  Übung 3 (Aufgabe, Beispiel UND Lösungen) auf das Format von Übung 4 umgestellt:
  Cue ist jetzt das vollständige, deklarierte Verb in der Grundform (1. Sg.
  θέλω/κάνω/μένω, in der Klammer „— von …" genannt), die GANZE Zielform kommt in
  die Lücke. Beispiel: „Κάν______ μία σαλάτα. *(wir)*" → „______ μία σαλάτα.
  *(wir — von κάνω)*", Lösung „**Κάνουμε** μία σαλάτα. — wir → -ουμε."
  Didaktischer Fokus bleibt die Plural-Endung (-ουμε/-ετε/-ουν): Lösungen zeigen
  die ganze korrekte Form mit hervorgehobener Endung + deutscher Endungsnamen
  („wir → -ουμε"). Aufgabenstellung/Überschrift angepasst („Plural-Form" statt
  „Plural-Endung", „schreib die ganze Form in die Lücke"). Kein nackter Stamm +
  Lücke mehr (per Grep bestätigt: keine weiteren Stamm+Lücke-Stellen in Ü1–Ü8).
  Weiterhin nur eingeführtes Material, Nomen Nom Sg, keine ausgeschriebenen
  Falschformen; θέλω-να-Chunks unberührt (nur in Ü5/Ü7/Ü8, ganz).

## /new-chapter griechisch 10 — Phase 2 (parallele Prüfung) — 2026-06-07
Baseline: validate_schema 0 Fehler, continuity_check 0 Verstöße. Orchestrator-/Designer-Fixes: εμείς/αυτοί/άλλο getilgt; Übung-3-Stamm+Lücke → ganze Verbform.

### Befunde Runde 1
- reviewer: **FREIGABE** (Plural-Paradigmen/θέλω/Chunks/Genus korrekt; κάνω/μένω-Doppeldeklaration technisch+didaktisch unbedenklich):
  - [ ] R1 [minor] chapter.md:237 + :287 — „der bekannte Gruß aus Kapitel 3" identisch bei Ü3.5 (κάνετε) und Ü6.5 (κάνεις), löst sich gegensätzlich → einen Hinweis variieren → exercise-designer
  - [ ] R2 [minor] Aussprachehinweis „-ume" OK (keine Aktion)
- reader: **kein COMPREHENSION-FAILURE**:
  - [ ] L1 [gap] chapter.md:169 „φάω … in derselben Form, die du bisher kanntest" — φάω ist NEU (nie vorher gesehen), „bisher kanntest" sachlich falsch → teacher
  - [ ] L2 [gap] θέλω να φάω vs. θέλουμε να φάμε — φάμε statt erwartetem *φάουμε erzeugt aktive Verwirrung; kurz erklären, dass φάω/φάμε/πιω Sonderformen eines unregelmäßigen Verbs sind (als Block, NICHT die -ουμε-Regel anwenden) → teacher
  - [ ] L4 [continuity/Bedeutung] Ü3.1 „Κάνουμε μία σαλάτα" — κάνω in „bestellen/zubereiten"-Bedeutung; in Kap. 3 nur „machen/tun (wie geht's)" → klären/entschärfen (κάνω eindeutig im bekannten „machen"-Sinn ODER Verb tauschen) → exercise-designer
  - [ ] L3 [gap] να nicht als Wörtchen/Partikel benannt → teacher: knapp einordnen
  - [ ] L5 [pacing] Ü3.5-Aha-Moment vor Grammatik-Auflösung — Klammerhinweis rettet; minor
  - [ ] L6 [pacing] großer Schritt (6 Formen + θέλω + να-Konstruktion + 3 Blöcke) → optionale Wegmarke
- ai-guard: **überwiegend menschlich** (Positiv: Landeskunde „kein tägliches Festgelage"):
  - [ ] G1/G2 [meta/floskel] chapter.md:77-79 „Dieses Kapitel hat zwei Teile … Hand in Hand" → streichen
  - [ ] G3 [floskel] Überschrift „Erst schauen: …" → Vorderteil streichen
  - [ ] G4 [floskel] chapter.md:83 „Sieh dir … an" → direkt
  - [ ] G5 [floskel] Überschrift „Der Aha-Moment" → Inhalt selbst sprechen lassen
  - [ ] G6 [hedging] chapter.md:168 „ehrliche Vorwarnung" → einfach sachlich (deckt sich mit L1)
  - [ ] G7 [rhythmus] chapter.md:109-118 zwei gleichgebaute Absätze → einen straffen
  - [ ] G8 [liste] Lernziel-Parallelismus (optional)
  - [ ] G10 [floskel/redundanz] „Achtung deutsche Falle" 3× (Z.109/183/229); eigener -ομε-Abschnitt wiederholt Z.109-113 → zusammenführen
