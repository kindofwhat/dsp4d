# DSP4D Paper – Gesammeltes Feedback (Vorabprüfung)

> **Dokument:** "Optimal LLM Size for Medical Document Classification Using Context Engineering"
> **Autoren:** Christian Sprecher, Benjamin Haegler
> **Studiengang:** CAS Generative KI, BFH
> **Feedback-Quellen:** (1) Handschriftliche Anmerkungen im PDF (rot), (2) E-Mail-Feedback der Betreuerin

---

## Übergreifende / Generelle Punkte

### Aus E-Mail:
- **Formatvorlage prüfen:** Logo, Kopf- und Fusszeilen - stimmt die Vorlage?
- **Quellenangaben für ALLE Behauptungen:** Durchgehend fehlen Belege. Jede Behauptung braucht eine Quelle oder einen Beweis.
- **Hinweise aus dem Text in den Anhang:** Wo im Text auf den Anhang verwiesen wird, muss der Verweis auch tatsächlich funktionieren und korrekt sein.
- **Verdacht auf zu viel generierten Text:** Insbesondere Kapitel 2 wirkt, als sei vieles KI-generiert - der Text ist zu ausschweifend und kommt nicht auf den Punkt. Rigoros kürzen!

### Aus handschriftlichen Anmerkungen:
- **Roter Faden fehlt:** An mehreren Stellen wird angemerkt, dass Konzepte zu spät eingeführt werden oder der Zusammenhang zwischen Kapiteln nicht klar ist. Begriffe müssen dort eingeführt werden, wo sie erstmals relevant sind - nicht erst Seiten später.
- **Sprache der Prompts:** Handschriftlicher Hinweis bei 3.3.3 fragt: "Hat der Sprachwechsel (en/de) Gründe?" - dies muss begründet werden, wenn Prompts auf Englisch sind, aber der Kontext Deutsch ist.

---

## Abstract (S. 1)

- **Handschriftlich:** "An geeigneter Stelle Link auf GitLab" - das GitLab-Repository soll verlinkt werden, aber an passender Stelle (nicht im Abstract selbst).

---

## Kapitel 1: Introduction (S. 7–8)

### Handschriftliche Anmerkungen (Inhaltsverzeichnis + S. 7):
- **"Nur kurz darüber reden, und begründen, warum der Use Case sinnvoll ist"** - Die Einleitung soll den Use Case knapp motivieren und begründen. Nicht zu ausschweifend.
- **"Was hat die Fontwahl zu bedeuten?"** - Der Abschnitt "A Note on the Craft" mit dem humorvollen Disclaimer über KI-Nutzung wird kritisch hinterfragt. Was soll das? Ist das angemessen für eine wissenschaftliche Arbeit?

### Handschriftliche Anmerkung (S. 8, Research Questions):
- Keine spezifische Kritik an den Forschungsfragen selbst, aber der Übergang zu Kapitel 2 muss besser motiviert sein.

---

## Kapitel 2: Theory / State of Research (S. 8–19)

### Strukturelle Änderung:
- **Kapitelüberschrift umbenennen:** "Theory / State of Research" → **"Related Work"** (handschriftlich durchgestrichen und korrigiert im Inhaltsverzeichnis)

### Aus E-Mail:
- **Text ist viel zu ausschweifend und kommt wenig auf den Punkt.** Es drängt sich die Frage auf, wie viel davon generiert wurde. **Rigoros kürzen**, nur in Bezug auf die Fragestellung Relevantes nennen.

### Kapitel 2.1: Evaluations in Classical Text Analysis (S. 9–11)
- **Handschriftlich (Inhaltsverzeichnis):** Die Unterkapitel 2.1.1–2.1.6 sind mit einer Klammer versehen und der Kommentar lautet: **"In Kap 3 darstellen, und die verwendeten Metriken / die Metrik im Use Case sinnvoll begründen"** - Die Metriken sollen NICHT hier breit theoretisch abgehandelt werden, sondern in Kapitel 3 vorgestellt werden, und zwar nur die tatsächlich verwendeten. Jede Metrik muss mit einem Beispiel begründet werden, warum sie für diese Arbeit sinnvoll ist.

### Kapitel 2.2: LLM in the Context of Medical Science (S. 12–13)
- **Handschriftlich (S. 13, Ende):** "Werden diese Aspekte in der Arbeit verwendet?" - Es ist unklar, ob die genannten Privacy/Security-Aspekte (Data Leakage, Adversarial Vulnerabilities) tatsächlich in der eigenen Methodik eine Rolle spielen. Wenn nicht, kürzen.
- **Handschriftlich (S. 13, bei 2.2.2):** "Kurze Intro mit Begründung, warum das für die Fragestellung relevant ist" - Jeder Unterabschnitt braucht eine Brücke zur eigenen Forschungsfrage.

### Kapitel 2.3: Scaling Laws and Model Efficiency (S. 14–15)
- **Handschriftlich (S. 14):** "Gibt es dann auch eine Quelle?" - Bei der Definition von SLM (<100B Parameter) fehlt eine Quelle.
- **Handschriftlich (S. 14):** "Das Kapitel könnte auf das Wesentliche gekürzt werden" - Zu viel Historical Context, der nicht direkt zur Fragestellung beiträgt.
- **Handschriftlich (S. 15, bei 2.3.6):** "Erst hier erfahren wir, warum wir 2.3 lesen mussten..." - Die Relevanz des Kapitels wird erst ganz am Ende klar. Besser: gleich am Anfang von 2.3 die Relevanz für die eigene Arbeit herstellen.

### Kapitel 2.4: Context Engineering Strategies (S. 15–19)
- **Handschriftlich (S. 16–17):** Mehrfach **"Quelle"** als Randbemerkung - Zu den 5 Punkten unter "Why Prompt Engineering Matters" fehlen durchgehend Quellenangaben. Jede Behauptung braucht einen Beleg.
- **Handschriftlich (S. 18):** "Das muss doch bewiesen werden" - Die Aussage, dass CoT die "optimale Technik" ist, wird behauptet aber nicht empirisch belegt. Es braucht Evidenz oder zumindest eine differenziertere Argumentation.
- **Handschriftlich (S. 17, bei der Prompting-Techniques-Tabelle):** "Quelle" - Die umfangreiche Vergleichstabelle sollte in den Anhang verschoben werden (was teilweise schon gemacht wurde), und im Haupttext nur die relevante Auswahl bleiben.

---

## Kapitel 3: Methodology (S. 20–42)

### Aus E-Mail:
- **Kapitel 3 wirkt wenig zusammenhängend.** Wurde die Eval Pipeline selbst gebaut? Welche Modelle wurden verwendet und warum?
- **Kapitel 3 soll erläutern, was ihr tatsächlich gebaut habt und wie** - das wird nicht klar.
- **3.3 scheint zentral zu sein, doch die Message kommt nicht rüber** - das Kapitel muss überarbeitet werden.
- **Die 'custom metrics' sollten hergeleitet und begründet werden** - ihre Aussagekraft muss klar werden.

### Kapitel 3.1: Procedure (S. 21)
- **Handschriftlich (S. 21, bei Abbildung 1):** "Quelle Bild (generiert??)" - Ist das Bild KI-generiert? Wenn ja, muss das deklariert werden.
- **Handschriftlich (S. 21):** "Ist deklarativ, erklärt nicht" - Die vier Phasen werden nur aufgezählt/deklariert, aber nicht erklärt. Es fehlt eine narrative Erklärung, WAS in jeder Phase konkret passiert und WARUM.

### Kapitel 3.2: Data Source GraSCCo (S. 22)
- **Handschriftlich (S. 22):** "Einen Beispieldatensatz zeigen" - Es fehlt ein konkretes Beispiel eines GraSCCo-Dokuments, damit der Leser versteht, womit gearbeitet wird.

### Kapitel 3.3: Golden Answer Generation (S. 23–30)
- **Handschriftlich (S. 23):** "Was ist das? Warum?" - Der Begriff "Golden Answer" / "Silver Answer" muss besser eingeführt und die Unterscheidung klarer gemacht werden.
- **Handschriftlich (S. 25, beim Prompt):** "Hat der Sprachwechsel Gründe? Was wirkt besser?" - Warum sind die Prompts auf Englisch, wenn die Dokumente auf Deutsch sind?
- **Handschriftlich (S. 25, bei den Kategorien):** Markierungen "a", "b", "c" neben den Constraints und Kategorien - scheinen Verbesserungsvorschläge zur Nummerierung/Struktur zu sein.
- **Handschriftlich (S. 26, bei 3.3.4):** "Mit Grafik erläutern" - Die Annotation Platform braucht eine visuelle Darstellung (Architekturdiagramm o.ä.).
- **Handschriftlich (S. 26):** "Eigenbau oder Framework wie RAGAS?" - Es muss klar werden, ob die Plattform ein Eigenbau ist oder auf einem bestehenden Framework basiert.

### Kapitel 3.4: Selecting SLMs (S. 30–33)
- **Handschriftlich (S. 31):** "Es müsste eher..." - Der Selektionsprozess wirkt nicht stringent genug. Die Kriterien müssen schärfer formuliert werden.

### Kapitel 3.5: Experimental Setup (S. 34–35)
- **Handschriftlich (S. 35, links):** "Golden/Silver Answers in 3.3 erklärt werden" - Der Begriff wird hier erneut verwendet, aber die Erklärung gehört nach vorne (3.3).
- **Handschriftlich (S. 35, bei Evaluation Framework):** "Erstmalig. Wäre nur einen Satz, dann den Begriff dort eingeführt" - Der llm-validator wird hier erstmals erwähnt, sollte aber früher eingeführt werden.
- **Handschriftlich (S. 35, bei 3.5.2 Silver Answer App):** "Stelle, stellen, klar, der Begriff eingeführt wurde" und "bis las wie ein blocker, was eben einen Good ist" - Klarere Einführung des Begriffs und der App nötig.

### Kapitel 3.6: Evaluation Metrics (S. 36–42)
- **Handschriftlich (S. 36):** **"Metriken aus Kap 2 streichen und hier einführen. Für jede Metrik begründen (mit Beispiel!), warum sie in dieser Arbeit sinnvoll ist. Nur relevante Metriken vorstellen."** - Das ist ein zentraler Punkt: Die Metriken gehören nicht in den Theorie-Teil, sondern hierher, und jede muss mit einem konkreten Beispiel aus dem Use Case begründet werden.
- **Handschriftlich (S. 36):** "Wo kommt das plötzlich her? Teil der Pipeline aus 3.3?" - Die Verbindung zwischen Metriken und der in 3.3 beschriebenen Pipeline ist unklar.
- **Handschriftlich (S. 37):** "dito" bei Statistical Metrics und Generative Metrics - Wiederholung des Feedbacks: Begründung fehlt.
- **Handschriftlich (S. 38, bei Abbildung 3):** "Das erfahren wir hier zu spät" - Das Test-Setup-Diagramm kommt zu spät im Kapitel. Es sollte früher stehen, um den Leser zu orientieren.
- **Handschriftlich (S. 39):** "Roter Faden: so etwas wird schon früher gesagt" - Redundanzen mit früheren Abschnitten.
- **Handschriftlich (S. 39, bei Abbildung 4):** "Hier wird es an dieser Stelle" - Die llm-validator-Oberfläche wird zu spät gezeigt.
- **Handschriftlich (S. 40):** **"Herleitung, Begründung, Aussagekraft"** - Bei JSON Structural Similarity und DAG-Metrik fehlt die Herleitung: Warum diese Metrik? Was misst sie genau? Was sagt sie über den Use Case aus?
- **Handschriftlich (S. 41, bei G-Eval):** "Verständnisfrage" und Notizen zu "vorhanden, Faden, Vorhersagen" - Der G-Eval-Abschnitt ist verwirrend. Der Zusammenhang mit dem Rest muss klarer werden.
- **Handschriftlich (S. 42, bei Logprobs-Tabelle):** "Ausserhalb der Tabelle, Rechtsfertigungen und Quellen" und "Tabelle real unterlegen" - Die Logprobs-Kompatibilitätstabelle braucht Quellenangaben. Die Informationen sollten mit realen Tests belegt werden.
- **Handschriftlich (S. 43):** "Welches ist da genau?" - Unklar, welches Modell als Fallback-Judge verwendet wird.
- **Handschriftlich (S. 43):** "Gehört das tatsächlich hierher? Discussion?" - Der Absatz über die Fallback-Strategie gehört möglicherweise eher in die Discussion.

---

## Kapitel 4: Results (S. 43–47)

### Aus E-Mail:
- **Die Kapitel Results und Discussion sollten schärfer getrennt werden.**
- **Einige der in Discussion genannten Fakten wurden früher im Text nicht wahrgenommen** → Sicherstellen, dass wichtige Fakten und Konzepte in Kapitel 3 eingeführt werden, z.B. G-Eval.
- **Unklar bleibt die Wahl der Metriken und was sie in Bezug auf den Use-Case aussagen sollen.**

### Handschriftliche Anmerkungen:
- **S. 43 (4.1 Validity of Silver Answers):** "Gehört das tatsächlich hierher? Discussion?" - Dieser Abschnitt ist eher Discussion-Material, nicht Results.
- **S. 45 (4.2):** "Der Leser will das nicht in die Cloud - ist repetitiv" - Die Beschreibung der Modelle und Metriken wiederholt sich. Gestraffter formulieren.
- **S. 45–46 (Tabellen):** "Resultate gerafft aufbereiten" - Die Tabellen brauchen eine bessere Erläuterung. Welche Metrik eignet sich am besten? Was wird gemittelt? Darf man mitteln? Was sagt das Mittel aus?
- **S. 46:** "Fehlende Erläuterung: Geeignete Metric, insbesondere was misst sie? Was wird da gemittelt? Darf man mitteln? Was sagt das Mittel aus?" - Kritische methodische Frage zur Aggregation der Scores.

---

## Kapitel 5: Discussion (S. 48–54)

### Aus E-Mail:
- **Results und Discussion schärfer trennen.** Fakten, die in der Discussion interpretiert werden, müssen vorher in Kapitel 3 oder 4 eingeführt worden sein.

### Handschriftliche Anmerkungen:
- **S. 48 (5.1):** "Auf die Tabellen Bezug nehmen, die Werte ablesen, warum" - Die Discussion referenziert Zahlen, ohne explizit auf die Tabellen zu verweisen. Jede Interpretation muss klar auf eine Tabelle/Abbildung verweisen.
- **S. 50 (5.3, RQ1):** "Wurde die Schwelle früher vorgestellt?" - Die 95%-Pass-Rate-Schwelle wird in der Beantwortung der Forschungsfrage verwendet, aber es ist unklar, ob sie vorher definiert wurde.
- **S. 51 (5.4, Limitations):** "Gibt's da keine Statistiken?" - Bei Limitation 3 (Single evaluation run) fehlen konkrete Zahlen zur Variabilität.
- **S. 53 (5.5, Metric Correlation):** "Gehört ins Result-Kapitel" / "Results?" - Die Korrelationsanalyse ist ein Ergebnis und gehört in Kapitel 4, nicht in die Discussion.

---

## Kapitel 6: Appendices

- **Handschriftlich (S. 27):** "Nur die? Und die Metriken aus Kap 2?" - Im Appendix zur Silver Answers App fehlt der Bezug zu den Evaluationsmetriken.
- Der umfangreiche Appendix 6.7 (Silver Answers App) ist sehr lang - prüfen, ob alles nötig ist oder gekürzt werden kann.

---

## Zusammenfassung der wichtigsten Aktionspunkte (priorisiert)

### Priorität 1 - Strukturelle Änderungen:
1. **Kap 2 umbenennen** in "Related Work" und rigoros kürzen - nur fragestellungsrelevante Inhalte behalten
2. **Metriken aus Kap 2.1 nach Kap 3.6 verschieben** - dort jede Metrik mit Beispiel und Begründung für den Use Case einführen
3. **Kap 3 zusammenhängender gestalten** - klar machen, was selbst gebaut wurde (Eval Pipeline, Silver Answers App, llm-validator), welche Modelle verwendet wurden und warum
4. **Results (Kap 4) und Discussion (Kap 5) scharf trennen** - 4.1 (Silver Answer Validity) und 5.5 (Correlation Analysis) gehören ins jeweils andere Kapitel
5. **Custom Metrics (JSON Similarity, DAG) herleiten und begründen** - Aussagekraft für den Use Case klarmachen

### Priorität 2 - Inhaltliche Verbesserungen:
6. **Quellenangaben ergänzen** - durchgehend, insbesondere in Kap 2.4 ("Why Prompt Engineering Matters") und bei der SLM-Definition
7. **Kap 3.3 überarbeiten** - "Golden/Silver Answers" klar definieren, Sprachwechsel en/de begründen, Beispiel-Datensatz zeigen
8. **Begriffe rechtzeitig einführen** - llm-validator, G-Eval, Silver Answers müssen dort erklärt werden, wo sie erstmals auftauchen
9. **Abbildungen und Tabellen besser einbetten** - Quellen für generierte Bilder angeben, Tabellen im Text referenzieren und interpretieren
10. **Kap 1 kürzen** - "A Note on the Craft" überdenken, Use Case knapp und überzeugend motivieren

### Priorität 3 - Formales:
11. **Formatvorlage prüfen** - Logo, Kopf-/Fusszeilen gemäss BFH-Vorgabe
12. **Anhang-Verweise prüfen** - alle Verweise im Text müssen korrekt auf den Anhang zeigen
13. **Tabellen-Referenzen fixen** - einige Tabellen haben "??" als Referenz (z.B. Table 4, Table 7)
14. **GitLab-Link an geeigneter Stelle einfügen**
