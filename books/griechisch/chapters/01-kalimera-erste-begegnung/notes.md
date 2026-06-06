# Pipeline-Protokoll — Kapitel 1: kalimera-erste-begegnung

- Lauf: /new-chapter griechisch 1, gestartet 2026-06-06
- Curriculum: anrede-su-sas; vocab_target 12; Themen Begrüßung/Verabschiedung/Höflichkeit/Vorstellung

## Befunde

### Phase 1 (Schreiben)
- [x] Schema-Fehler: YAML-Quoting in meta.yaml Z. 41 (Anführungszeichen in gloss_de) — mechanisch vom Orchestrator korrigiert (Single-Quotes), kein Inhalt geändert

### Phase 2/3 — Review-Runde 1 (alle 5 Prüfer)

**continuity-checker (KONTINUITÄT: OK, aber Sidecar-Lücken):**
- [x] C4 — Dialog-Überschrift auf Deutsch geändert: „Dialog — Lenas erster Tag in Athen" (griechischer Titel entfernt)
- [x] C5 — Sprecher-Label „Νεαρός" durch Eigennamen „Νίκος" ersetzt (löst sich über R2-Fix)
- [x] C6 — κύριος (gender m, inflected_forms: [κύριε]) in meta.yaml deklariert

**reviewer (Urteil: überarbeitung nötig):**
- [x] R1 — „Αντίο σας!" am Schalter → „Γεια σας!"; αντίο jetzt am endgültigen Abschied am Ende der Abendszene (zweimal: Lena + Nikos)
- [x] R2 — „Εσύ;" wird beantwortet: Nikos nennt seinen Namen („Νίκος.") und grüßt zurück; zusätzlich neuer Grammatik-Unterabschnitt „Εσύ; — die Frage zurückgeben"
- [x] R3 — Betonungspassage korrigiert: σου/σας als tonlose, ans Vorwort angelehnte Klitika ohne eigenen Akzent dargestellt (γειά-σου als ein Klangwort), statt „leichte Betonung"
- [x] R4 — gelöst über K2-Fix (zweite Szene auf den Abend verlegt, καλησπέρα dort idiomatisch)
- [x] R5 [minor] Glosse σου/σας als bewusste A0-Vereinfachung akzeptiert (keine Aktion)
- [x] R6 [minor] 11 statt 12 Vokabeln: im Toleranzband (keine Aktion; ggf. löst K2-Fix das)
- [x] R7 [minor] Wortschatz-Abschnitt leer: by design (Build generiert aus meta.yaml)
- [x] R8 [major] Folgeänderung zu R1 in Übungen/Lösungen abgearbeitet: Übung 3 an neuen Dialog angeglichen (Item „Αντίο σας!" am Schalter raus; jetzt Γεια σας! zum Abschied + Frau→Lena „Γεια σας, κυρία Λένα", Aufgabenstellung neutralisiert, Lösung 3 nachgezogen); Übung 5 Dialog-Rekonstruktion korrigiert (Schalter endet mit „Ευχαριστώ. Γεια σας!", falsches „Καλησπέρα!" in Morgen-Szene entfernt, Lösungsreihenfolge angepasst); Musterlösung 6b „Αντίο σας!" → „Γεια σας!" (αντίο als Alternative im Hinweis). Übung 1 (ναι→d) bleibt korrekt, ναι via Wortschatz-Box gedeckt. Übungen 2 und 4 ohne Dialog-Widerspruch. Nur deklariertes Vokabular + Eigennamen (Λένα, Νίκος, Μαρία).

**reader (kein COMPREHENSION-FAILURE):**
- [x] L1–L3 — Hinweis vor dem Dialog ergänzt („Alle neuen Wörter … findest du gleich darunter in der Wortschatz-Box"). ναι aus dem Dialog entfernt (Antwort umgebaut), κυρία/ευχαριστώ bleiben, stehen in der Box; Dialogfluss trägt auch ohne Box (Begrüßung/Vorstellung/Abschied sind aus Kontext lesbar)
- [x] L4 — „Εσύ;" jetzt in eigenem Grammatik-Unterabschnitt erklärt (Funktion als Rückfrage „und du?")
- [x] L5 — Satz nach der Tabelle ergänzt: „(selten)"-Formen nicht aktiv lernen, nur wiedererkennen

**ai-guard (Gesamturteil: überwiegend menschlich):**
- [x] G1+G2 — „trägt eine große Entscheidung" durch konkrete Aussage ersetzt (du/Sie-Entscheidung am Satzende, Parallele zum Deutschen)
- [x] G3 — Doppel-Hedging aufgelöst: klare Aussage (σας üblich; oft hängt man gar nichts an und sagt nur καλημέρα)
- [x] G5 — „ungewohnt, aber praktisch" umformuliert zu klarer Nutzen-Aussage ohne Symmetrie-Hedging
- [x] G6 — Zwei-Punkt-Liste der με-λένε-Beispiele in Fließsatz aufgelöst
- [x] G7 — Meta-Ankündigung „Eine zweite Beobachtung lohnt sich" gestrichen, direkter Einstieg mit der Frage
- [x] G4: nur Beobachtung, keine Aktion nötig

**cultural-reviewer:**
- [x] K2 (= R4) — zweite Szene (Taxistand) auf den Abend verlegt; καλησπέρα hat dort jetzt ehrlichen Platz, Tageszeit-Kontrast didaktisch genutzt (Lena seit dem Morgen unterwegs). καλησπέρα bleibt deklariert und für Übung 1 erhalten
- [x] K1 — Grußzeiten korrigiert: Grenze fließend, viele wechseln schon gegen Mittag (ab eins, zwei) zu καλησπέρα, andere bleiben länger bei καλημέρα
- [x] K3 — κυρία + Vorname nuanciert: üblich v. a. wenn Nachname (noch) unbekannt; Alltag, Lehrerin, Arzt
- [x] K7 — „ist sehr griechisch" entschärft zu „überrascht uns am Anfang"

### Orchestrator-Befund nach Runde 1
- [x] O1 [dramaturgie] Taxistand-Mann von „Νίκος" zu „Κώστας" umbenannt, um die Kollision mit dem Kafenío-Besitzer Níkos (Kap. 2) zu vermeiden. Namenswahl: Κώστας statt Γιώργος, weil Γιώργος im Vokativ zu „Γιώργο" wird und Lena ihn im Dialog direkt anspricht — diese unerklärte Vokativ-Veränderung wollte ich Lernenden auf A0 ersparen. Bei Κώστας umgehe ich den Vokativ ganz: Lenas Schluss-Replik „Καλησπέρα, Νίκο!" wurde zu „Καλησπέρα!" vereinfacht (kein direkter namentlicher Anspruch mehr), und der Mann nennt sich nur im Nominativ „Κώστας." als Antwort auf „Εσύ;". Alle Vorkommen konsistent angepasst: Sprecher-Labels (3×), Grammatik-Erklärung zu „Εσύ;" (Fließtext „Kostas"), und die beiden generischen με-λένε-Beispielnamen „Με λένε Νίκο" → „Με λένε Κώστα" (Dialog-Konsistenz, damit im selben Kapitel kein Νίκος-Echo bleibt) — inkl. Musterlösung 6a. Per Grep verifiziert: kein Νίκ-Vorkommen mehr in chapter.md. Übungen 3/Lösung 3 nennen den Mann ohnehin nur als „junger Mann am Taxistand" (kein Name), keine Änderung nötig. meta.yaml unberührt (Eigennamen werden nicht deklariert).

### Phase 2/3 — Review-Runde 2

**continuity-checker: KONTINUITÄT OK**
- [x] C2.1 [LEMMATIZER-MISS] „γειά" Z. 118 — KEINE inflected_forms-Ergänzung: Die Schreibung selbst ist der Befund (siehe R2.1), Textfix löst beides

**reviewer (überarbeitung nötig):**
- [x] R2.1 [blocker] Aussprache-Notiz neu gefasst (eigener Block „Wie es klingt"): Akzent-Variante „γειά-σου" komplett entfernt; jetzt „γεια σου in einem Zug ineinander laufen lassen", durchgehend akzentlose Schreibung γεια σου / σου / σας. Aussage „tragen keinen Akzent" bleibt.
- [x] R2.2 [major] με-λένε-Beispiele auf indeklinable Namen umgestellt: „Με λένε Μαρία" / „Με λένε Λένα" (kein stiller Κώστας→Κώστα-Wechsel mehr). Κώστας bleibt Dialogfigur, nennt sich nur im Nominativ „Κώστας." auf „Εσύ;".
- [x] R2.3 [minor] Folgekonsistenz Musterlösung 6a: „Με λένε Κώστα" (Akkusativ-Form) → indeklinabler Name „Με λένε Μαρία", konsistent mit dem Grammatikteil (με-λένε-Beispiele „Μαρία"/„Λένα"). Da 6b bisher „Μαρία" nutzte, dort auf „Λένα" umgestellt, damit die beiden Musterlösungen unterschiedliche, im Kapitel etablierte indeklinable Namen zeigen.
- [x] R2.4 [minor] κύριος in meta.yaml: notes-Feld "nur rezeptiv (Landeskunde)" ergänzt (Double-Quotes).

**reader (kein COMPREHENSION-FAILURE):**
- [x] L2.1/L2.2 ευχαριστώ/καλησπέρα im Dialog vor Erklärung — durch generierte Wortschatz-Box direkt nach dem Dialog gelöst (by design); Hinweis vor Dialog existiert bereits
- [x] L2.3 [comprehension-gap] ναι natürlich im Dialog untergebracht: Κώστας' Abschiedsreplik ist jetzt „Ναι, αντίο!" (bestätigendes ναι vor dem Abschiedsgruß) → deklariertes Vokabular kommt nun auch im Dialog vor.
- [x] L2.4 [confusing] „tonlos" ersetzt durch „haben keine eigene Betonung" / „hängen sich leise an".
- [x] L2.5 [pacing] Aussprache-Notiz aus „Stolperstelle" gelöst → eigene ###-Überschrift „Wie es klingt".

**ai-guard (klingt menschlich; Detailbefunde):**
- [x] G2.1 [redundanz] σας-Regel-Bullet gestrafft (kein „distanziert", kürzer) und Folgeprosa von 3 auf 2 Zeilen gekürzt — die Doppelung „Sie oder ihr / höfliches Sie und schlichtes ihr" steht jetzt nur noch einmal.
- [x] G2.2 [struktur] = L2.5: eigener Block „Wie es klingt".
- [x] G2.3 [hedging] „Wenn du dich vertust, ist das kein Drama" gestrichen.

**cultural-reviewer:**
- [x] K2.1 [fakt] Uhrzeiten („ab eins, zwei") entfernt: jetzt „irgendwann im Laufe des Nachmittags wechseln die meisten … mit γεια σας liegst du zu jeder Stunde richtig". Keine konkreten Zeiten mehr.
- [x] K2.2 [pragmatik] Κώστας eröffnet jetzt neutral nur mit „Καλησπέρα!" (ein Gruß); Lena duzt mit „Γεια σου!", Κώστας schwenkt um („Γεια σου, Λένα!"). Registerwechsel sichtbar gemacht, auch im Vorspann beschrieben. Ein Gruß pro Replik.
- [x] K2.3 [pragmatik] καλησπέρα fällt jetzt ausschließlich als BEGRÜSSUNG (Κώστας' Eröffnung). Lenas Abschied ist „Αντίο!", Κώστας erwidert „Ναι, αντίο!" — kein καλησπέρα mehr beim Abschied.
- [ ] K2.4 [hinweis, vertagt] Taxistand-Szene abends sozial ambig (Anmach-Lesart) → für spätere Überarbeitung notiert, kein Blocker

### Folgekonsistenz-Runde (Übungen + Lösungen gegen neuen Dialog) — 2026-06-06
- [x] R2.3 erledigt (siehe oben).
- [x] Vollständige Gegenprüfung aller 6 Übungen + Lösungen gegen den überarbeiteten Dialog (Abendszene neu: Κώστας „Καλησπέρα!", Lena „Γεια σου!", Abschied „Αντίο!"/„Ναι, αντίο!"; με-λένε indeklinabel; keine γειά-Akzentvariante):
  - Übung 5 (Dialog ordnen): vorgegebene Repliken + Lösungsreihenfolge 1–5 stimmen exakt mit Szene 1 (Schalter) überein — keine Änderung nötig.
  - Übung 1 (Zuordnung): ναι, καλημέρα, αντίο, ευχαριστώ, καλησπέρα alle im neuen Dialog vorhanden; Lösungstext rein neutral (keine „kommt nicht im Dialog vor"-Behauptung) — keine Änderung nötig.
  - Übung 3 + Lösung: alle vier σου/σας-Items decken sich mit den Dialogrepliken (Frau→Lena σας, Lena-Abschied σας, Lena→Κώστας σου, Κώστας→Lena σου); Begründungen korrekt — keine Änderung nötig.
  - Übungen 2, 4: dialogunabhängig, σου/σας-Logik konsistent; keine Tageszeit-Kollision — keine Änderung nötig.
  - Materialdisziplin geprüft: nur deklariertes Vokabular (meta.yaml) + Kapitel-Eigennamen (Λένα, Κώστας, Μαρία).

### Review-Runde 3 (final) — ALLE PRÜFER GRÜN
- continuity-checker: KONTINUITÄT OK, 0 Verstöße (nur Eigennamen)
- reviewer: FREIGABE (R3.1 minor kosmetisch: Zeitangabe καλημέρα meta.yaml ↔ chapter.md leicht abweichend — unkritisch, notiert)
- reader: durcharbeitbar, keine comprehension-gaps; 3 Kleinst-Beobachtungen (warum „selten", „umschwenken"-Erzählung, κύριε nur Landeskunde) — notiert für spätere Politur
- ai-guard: FREIGABE
- cultural-reviewer: FREIGABE
- [x] Mini-Defekt Übung 1: Beispiel-Item „0. ναι → **d**" verriet wörtlich Test-Item 5 (ναι → d). Fix (Variante a): Beispiel auf γεia umgestellt — γεια ist in meta.yaml deklariert, kommt aber nicht in der a–e-Liste vor; es demonstriert nur das Eintrage-Format (griech. Wort → dt. Bedeutung) mit eigener Beispielzeile außerhalb der Optionen. Alle fünf Test-Items (καλημέρα, αντίο, ευχαριστώ, καλησπέρα, ναι) bleiben erhalten, Lösungsschlüssel Übung 1 (1→e, 2→c, 3→a, 4→b, 5→d) unverändert. meta.yaml exercises.count/types unverändert (6). Kein neues Vokabular eingeführt.

### Offen für spätere Überarbeitung (nicht blockierend)
- [ ] K2.4 Taxistand-Szene sozial ambig (vertagt aus Runde 2)
- [ ] R3.1 Zeitangaben-Feinabstimmung meta.yaml:8 ↔ chapter.md
- [ ] Reader-Kleinigkeiten: „(selten)"-Begründung, Erzähl-Kommentar „schwenkt um", κύριε-Stolperer
