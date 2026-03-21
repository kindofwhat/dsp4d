# Implementation Plan: DSP4D Paper Revision

**Project**: dsp4d-paper-revision
**Generated**: 2026-03-20
**Deadline**: 2026-03-25
**Feedback source**: `paper/DSP4D-Feedback-Zusammenfassung.md`

## Technical Context
- **Build**: `cd paper && task build` (Pandoc Markdown -> pdflatex)
- **Chapters**: `paper/chapters/XX-name/index.md`
- **Citations**: `paper/references.bib` (62 entries), `[@key]` syntax
- **Principle**: Every edit makes the paper SHORTER or more precise.

---

## Phase 1: Structural Moves

Content moves between chapters. Do these first — they change the paper's skeleton.

- [x] **Rename Ch 2 to "Related Work"**
  Task ID: p1-01
  > **File**: `02-theory/index.md` line 1
  > **Action**: Change `# Theory / State of Research` to `# Related Work`
  > **Feedback**: *"Kapitelüberschrift umbenennen: Theory / State of Research → Related Work (handschriftlich durchgestrichen und korrigiert im Inhaltsverzeichnis)"* [Kap 2, Strukturelle Änderung]
  > **Commit**: _pending_

- [x] **Delete metrics section from Ch 2, keep only what Ch 3.6 needs**
  Task ID: p1-02
  > **File**: `02-theory/index.md` lines 5–63 (entire "Evaluations in Classical Text Analysis")
  > **Action**: Remove the full section (String Similarity, Classification Metrics, Generation Metrics, Semantic Metrics, LLM-as-a-Judge, Evaluation Challenges). These ~60 lines go away entirely — the relevant metrics are reintroduced in the next task.
  > **Feedback**: *"Die Unterkapitel 2.1.1–2.1.6: In Kap 3 darstellen, und die verwendeten Metriken / die Metrik im Use Case sinnvoll begründen"* [Kap 2.1, Handschriftlich Inhaltsverzeichnis]
  > **Commit**: _pending_

- [x] **Rewrite Ch 3.6 (Evaluation Metrics) with use-case justification per metric**
  Task ID: p1-03
  > **File**: `03-methodology/index.md` lines 423–444
  > **Action**: For each metric actually used (BLEU, ROUGE, Token F1, Levenshtein, Semantic Sim, JSON Sim, DAG, LLM-Judge), write 2–3 sentences: (1) what it measures, (2) why it's relevant for clinical extraction (with concrete example, e.g. "Levenshtein catches date format mismatches like '2025-03-14' vs '14.03.2025'"), (3) known limitation. Remove metrics not used. Reference moved content from old Ch 2.1 where applicable.
  > **Feedback**: *"Für jede Metrik begründen (mit Beispiel!), warum sie in dieser Arbeit sinnvoll ist. Nur relevante Metriken vorstellen."* [Kap 3.6, Handschriftlich S. 36]
  > **Also addresses**: *"Unklar bleibt die Wahl der Metriken und was sie in Bezug auf den Use-Case aussagen sollen"* [Kap 4, E-Mail]
  > **Commit**: _pending_

- [x] **Move Section 4.1 (Silver Answer Validity) to Discussion**
  Task ID: p1-04
  > **File**: `04-results/index.md` lines 7–17 → `05-discussion/index.md` (new section before Limitations)
  > **Action**: Cut "Validity of Silver Answers as Evaluation Benchmark" from Ch 4. Insert in Ch 5 as "Validity of the Evaluation Benchmark" before Limitations. Fix Ch 4 intro to flow directly into "Overview of Models".
  > **Feedback**: *"Gehört das tatsächlich hierher? Discussion?"* [S. 43, Handschriftlich bei 4.1]
  > **Also addresses**: *"Die Kapitel Results und Discussion sollten schärfer getrennt werden"* [Kap 4, E-Mail]
  > **Commit**: _pending_

- [x] **Move Section 5.5 (Metric Correlation Analysis) to Results**
  Task ID: p1-05
  > **File**: `05-discussion/index.md` lines 82–97 → `04-results/index.md` (new section after JSON Structural Similarity)
  > **Action**: Move entire "Metric Correlation Analysis" section including the figure reference (`04-metric-correlation.png`) to Ch 4 as a new section. Add 1-sentence interpretation summary in Ch 5 that references the moved section.
  > **Feedback**: *"Gehört ins Result-Kapitel" / "Results?"* [S. 53, Handschriftlich bei 5.5]
  > **Commit**: _pending_

- [x] ~~**Move Logprobs fallback discussion to Discussion or shorten**~~ *(superseded by p3-10: G-Eval to Appendix)*
  Task ID: p1-06
  > **File**: `03-methodology/index.md` lines 498–502
  > **Action**: The paragraph starting "Practically this turned out to be problematic..." and "Consequence for judge model selection" (lines 498–502) is discussion/reflection, not methodology description. Either move to Ch 5 Discussion or reduce to 1 sentence in Ch 3.
  > **Feedback**: *"Gehört das tatsächlich hierher? Discussion?"* [S. 43, Handschriftlich]
  > **Commit**: _pending_

---

## Phase 2: Ch 2 (Related Work) — Trim & Sharpen

After Phase 1, Ch 2 has lost ~60 lines of metrics. Now trim remaining sections.

- [x] **Ch 2.2: Remove Privacy/Security if unused in methodology**
  Task ID: p2-01
  > **File**: `02-theory/index.md` lines 70–81 (Privacy, Security, and Data Sovereignty)
  > **Action**: Review whether Data Leakage, Adversarial Vulnerabilities, and Ethical Gaps are referenced anywhere in Ch 3–5. If not used → cut the subsection. If used → keep but add 1-sentence bridge: "These risks directly motivate the local deployment constraint in our methodology (Chapter 3)."
  > **Feedback**: *"Werden diese Aspekte in der Arbeit verwendet?"* [S. 13, Handschriftlich]
  > **Commit**: _pending_

- [x] **Ch 2.2: Add relevance bridge for Specialized Medical Applications**
  Task ID: p2-02
  > **File**: `02-theory/index.md` lines 83–92
  > **Action**: Add 1 opening sentence before each subsection (Wu dual-stage, ELMTEX, GraSCCo) connecting it to OUR research question. E.g. before ELMTEX: "This finding directly supports our hypothesis that smaller models can perform clinical extraction tasks."
  > **Feedback**: *"Kurze Intro mit Begründung, warum das für die Fragestellung relevant ist"* [S. 13, Handschriftlich bei 2.2.2]
  > **Commit**: _pending_

- [x] **Ch 2.3: Move "Implications" to the BEGINNING of the section**
  Task ID: p2-03
  > **File**: `02-theory/index.md` — move lines 119–121 to right after line 97
  > **Action**: The relevance of 2.3 is only clear at the end ("Implications for This Study"). Move this paragraph to the section opening so the reader knows upfront WHY they're reading about scaling laws. Reword slightly for introduction position.
  > **Feedback**: *"Erst hier erfahren wir, warum wir 2.3 lesen mussten..."* [S. 15, Handschriftlich bei 2.3.6]
  > **Commit**: _pending_

- [x] **Ch 2.3: Cut "Historical Context" subsection**
  Task ID: p2-04
  > **File**: `02-theory/index.md` lines 99–101
  > **Action**: The Kaplan/Hoffmann paragraph is 3 lines. It's already referenced in the opening. Either merge into one sentence in the section intro or delete entirely — the citations can stay as parentheticals.
  > **Feedback**: *"Das Kapitel könnte auf das Wesentliche gekürzt werden"* [S. 14, Handschriftlich]
  > **Commit**: _pending_

- [x] **Ch 2.3: Add source for SLM definition (<100B parameters)**
  Task ID: p2-05
  > **File**: `02-theory/index.md` line 109 ("the term SLM refers to language models with fewer than 100 billion parameters")
  > **Action**: Add a citation. Check if `lu2024slmsurvey` defines this threshold. If not, find/add an appropriate source.
  > **Feedback**: *"Gibt es dann auch eine Quelle?"* [S. 14, Handschriftlich bei SLM-Definition]
  > **Commit**: _pending_

- [x] **Ch 2.4: Add citations to "Why Prompt Engineering Matters" (5 claims)**
  Task ID: p2-06
  > **File**: `02-theory/index.md` lines 131–141
  > **Action**: Five numbered claims currently have ZERO citations. Map to existing refs:
  > 1. "Bridging the Capability Gap" → `[@brown2020language]` or `[@wei2022chain]`
  > 2. "Reducing Hallucinations" → needs a hallucination source
  > 3. "Ensuring Consistency" → `[@bsharat2023principled]`
  > 4. "Maximizing Limited Resources" → `[@lu2024slmsurvey]`
  > 5. "Enabling Transparent Reasoning" → `[@wei2022chain]`, `[@kojima2022large]`
  > Add `[@key]` to each. Add new BibTeX entries only if truly needed.
  > **Feedback**: *Mehrfach "Quelle" als Randbemerkung bei den 5 Punkten* [S. 16–17, Handschriftlich]
  > **Commit**: _pending_

- [x] **Ch 2.4: Remove duplicate prompting techniques table (already in Appendix)**
  Task ID: p2-07
  > **File**: `02-theory/index.md` lines 145–170
  > **Action**: The 4-technique comparison table is already in Appendix 6.1 with 20 techniques. Replace lines 145–170 with a single sentence: "A comprehensive comparison of 20 prompting techniques is provided in [Appendix: Comprehensive Comparison of Prompting Techniques](#appendix-promp-techs). Based on this analysis, CoT was selected for the following reasons:"
  > **Feedback**: *"Quelle" — Tabelle sollte in den Anhang verschoben werden* [S. 17, Handschriftlich]
  > **Commit**: _pending_

- [x] **Ch 2.4: Qualify "optimal technique" claim for CoT**
  Task ID: p2-08
  > **File**: `02-theory/index.md` line 172 ("Chain-of-Thought: The Optimal Technique")
  > **Action**: The heading claims CoT is "optimal" — this must be supported or softened. Options: (a) change heading to "Chain-of-Thought: The Selected Technique for..." (b) add empirical evidence supporting "optimal". Also trim the 4 pages of CoT justification (lines 172–235) — the core argument can be made in ~1 page.
  > **Feedback**: *"Das muss doch bewiesen werden"* [S. 18, Handschriftlich]
  > **Commit**: _pending_

---

## Phase 3: Ch 3 (Methodology) — Coherence & Clarity

Address the core email feedback: "Kapitel 3 wirkt wenig zusammenhängend."

- [x] **Describe the evaluation pipeline as a coherent system**
  Task ID: p3-01
  > **File**: `03-methodology/index.md` — section opening (lines 3–7) and section 3.5 (lines 396–420)
  > **Action**: The supervisor says Ch 3 doesn't make clear what was built. Add a clear paragraph early in Ch 3 (after the 4-phase overview) that names all three self-built components: (1) Silver Answers App (Node.js/React, cloud-based, for generating reference answers via Gemini), (2) llm-validator (Java 21/Quarkus, local, for running the evaluation pipeline), (3) the evaluation metrics (custom JSON Similarity + DAG). State what each does and how they connect.
  > **Feedback**: *"Kapitel 3 wirkt wenig zusammenhängend. Wurde die Eval Pipeline selbst gebaut? Welche Modelle wurden verwendet und warum?"* [Kap 3, E-Mail]
  > **Also addresses**: *"Eigenbau oder Framework wie RAGAS?"* [S. 26, Handschriftlich]
  > **Commit**: _pending_

- [x] **Explain procedure phases narratively (not just list)**
  Task ID: p3-02
  > **File**: `03-methodology/index.md` lines 15–25
  > **Action**: Each of the 4 phases is currently a heading + 1 dense paragraph. Rewrite each to 2–3 clear sentences: WHAT happens, WHO does it, WHAT tool is used, WHAT output is produced. Currently reads "deklarativ, erklärt nicht".
  > **Feedback**: *"Ist deklarativ, erklärt nicht"* [S. 21, Handschriftlich]
  > **Commit**: _pending_

- [x] **Declare source of methodology overview figure**
  Task ID: p3-03
  > **File**: `03-methodology/index.md` line 11
  > **Action**: Add source to figure caption for `03-Methodology-Overview.png`. If AI-generated: "Source: Authors, generated using [tool]." If hand-made: "Source: Authors."
  > **Feedback**: *"Quelle Bild (generiert??)"* [S. 21, Handschriftlich bei Abbildung 1]
  > **Commit**: _pending_

- [x] **Add GraSCCo example or cross-reference to Appendix**
  Task ID: p3-04
  > **File**: `03-methodology/index.md` lines 28–39 (Data Source: GraSCCo)
  > **Action**: Add a short example or reference: "Appendix [Gold Standard Example](#appendix-gold-standard) shows a representative GraSCCo clinical report alongside its CoT-extracted structured output." The example already exists in Appendix §3.
  > **Feedback**: *"Einen Beispieldatensatz zeigen"* [S. 22, Handschriftlich]
  > **Commit**: _pending_

- [x] **Define Golden Answer vs Silver Answer clearly at first use**
  Task ID: p3-05
  > **File**: `03-methodology/index.md` lines 40–42
  > **Action**: Current text is vague ("Silver Answers... preliminary structured outputs"). Rewrite to a crisp definition box:
  > - **Silver Answer**: LLM-generated structured output (by Gemini 2.5 Pro with CoT), used as evaluation benchmark
  > - **Golden Answer**: Silver Answer that has been validated/corrected by a medical expert (GP)
  > - Explain WHY we use Silver Answers (expert time constraint) and acknowledge limitation
  > **Feedback**: *"Was ist das? Warum?"* [S. 23, Handschriftlich bei Golden/Silver Answer]
  > **Commit**: _pending_

- [x] **Justify English prompts for German documents**
  Task ID: p3-06
  > **File**: `03-methodology/index.md` near line 107 (System Prompt section)
  > **Action**: Add 2 sentences before the prompt block: "The system prompt is formulated in English while input documents are German. This reflects standard LLM practice: instruction-tuned models typically achieve better instruction adherence with English-language system prompts, while the output constraint (German content values, line 115) ensures extracted medical content remains in the source language."
  > **Feedback**: *"Hat der Sprachwechsel (en/de) Gründe? Was wirkt besser?"* [S. 25, Handschriftlich bei 3.3.3]
  > **Commit**: _pending_

- [x] **Derive JSON Structural Similarity: why, what, significance**
  Task ID: p3-07
  > **File**: `03-methodology/index.md` lines 465–467
  > **Action**: Current text is 3 lines. Expand to ~8 lines covering:
  > 1. WHY: Standard metrics (BLEU, ROUGE) don't capture structural compliance — a model can produce semantically correct text in wrong JSON format, which is unusable in a clinical pipeline
  > 2. WHAT: Flattens JSON to leaf paths, computes normalized Levenshtein per leaf (ref Appendix)
  > 3. SIGNIFICANCE: Score of 1.0 = perfect schema match; 0.0 = unparseable; e.g. a model outputting free text instead of JSON scores 0.0 regardless of medical correctness
  > **Feedback**: *"Herleitung, Begründung, Aussagekraft"* [S. 40, Handschriftlich bei JSON Similarity]
  > **Also addresses**: *"Die 'custom metrics' sollten hergeleitet und begründet werden"* [Kap 3, E-Mail]
  > **Commit**: _pending_

- [x] **Derive DAG metric: why, what, significance**
  Task ID: p3-08
  > **File**: `03-methodology/index.md` lines 469–471
  > **Action**: Same structure as p3-07:
  > 1. WHY: Single-prompt LLM-as-a-Judge conflates multiple quality dimensions; DAG decomposes into format, accuracy, completeness, terminology
  > 2. WHAT: Directed Acyclic Graph with 4 parallel assessment nodes, each scored 0–1, averaged (ref Appendix)
  > 3. SIGNIFICANCE: Allows identifying WHERE a model fails — e.g. a model scoring high on completeness but low on format compliance tells a different story than one failing on factual accuracy
  > **Feedback**: *"Herleitung, Begründung, Aussagekraft"* [S. 40, Handschriftlich bei DAG-Metrik]
  > **Commit**: _pending_

- [x] **Introduce llm-validator at first conceptual mention**
  Task ID: p3-09
  > **File**: `03-methodology/index.md` — add a sentence around line 22 (Phase III description)
  > **Action**: llm-validator first appears at line 410 but Phase III already describes its function conceptually. Add one sentence: "This pipeline is implemented as *llm-validator*, a purpose-built evaluation framework described in Section 3.5." This creates an early anchor.
  > **Feedback**: *"Erstmalig. Wäre nur einen Satz, dann den Begriff dort eingeführt"* [S. 35, Handschriftlich]
  > **Commit**: _pending_

- [x] **Move G-Eval content to Appendix, note it was not used**
  Task ID: p3-10
  > **File**: `03-methodology/index.md` lines 473–502 (G-Eval figure + "The Logprobs Problem in G-Eval" + fallback strategy + judge model selection) → `06-appendix/index.md`
  > **Action**: Move the entire G-Eval section (~30 lines + figure `03-GEval-Algorithm.png`) to Appendix. In Ch 3, replace with 2–3 sentences: "G-Eval [@liu2023geval] was evaluated as a candidate for probability-weighted scoring but could not be used due to inconsistent logprobs support across providers (see Appendix [G-Eval Investigation](#appendix-geval)). The evaluation therefore relies on direct LLM-as-a-Judge scoring via the DAG metric and a one-shot field comparison." This also resolves p1-06 (Logprobs fallback → Discussion).
  > **Feedback**: *"Verständnisfrage" / G-Eval section confusing* [S. 41, Handschriftlich] + *"Gehört das tatsächlich hierher? Discussion?"* [S. 43, Handschriftlich bei Fallback]
  > **Note**: Supersedes task p1-06 (move Logprobs fallback). Both are resolved by moving the entire G-Eval block.
  > **Commit**: _pending_

- [x] **Clean up "Model Output Filtering" draft marker**
  Task ID: p3-11
  > **File**: `03-methodology/index.md` lines 196–198
  > **Action**: Remove the draft transition text: "Here is a draft for the new paragraph, written in the academic, structured, and technical tone of the DSP4D paper. It is designed to be placed directly below the Administrative Modules paragraph in section 3.3.4." and the `***` separator. This is clearly leftover editing text.
  > **Feedback**: General quality — draft artifacts in final text
  > **Commit**: _pending_

- [x] **Remove EULA boilerplate from Ch 3.4**
  Task ID: p3-12
  > **File**: `03-methodology/index.md` lines 350–393
  > **Action**: The 43-line EULA compliance template is not academic content — it's a legal boilerplate. Either move to Appendix or delete entirely. Replace with 1 sentence: "Models under restrictive licenses (Llama 3.1, Gemma) require attribution notices; the full compliance template is available in the project repository."
  > **Feedback**: Implicit — Ch 3 is too long and verbose, this is low-value content
  > **Commit**: _pending_

---

## Phase 4: Ch 1 (Introduction) — Trim

- [ ] [BLOCKED: Awaiting user decision] **Decision: "A Note on the Craft" — keep, footnote, or remove?**
  Task ID: p4-01
  > **File**: `01-introduction/index.md` lines 3–16
  > **Action**: HUMAN DECISION REQUIRED. The supervisor questioned this section: "Was hat die Fontwahl zu bedeuten?" Options:
  > (a) Remove entirely (safest for academic submission)
  > (b) Reduce to 1-sentence footnote
  > (c) Keep but reword in academic tone
  > **Feedback**: *"Was hat die Fontwahl zu bedeuten?"* [S. 7, Handschriftlich bei Introduction]
  > **Commit**: _pending_

- [x] **Tighten motivation — keep it concise**
  Task ID: p4-02
  > **File**: `01-introduction/index.md` lines 19–31
  > **Action**: Currently 3 paragraphs (~13 lines) for motivation. Reduce to 2 short paragraphs: (1) problem: GP administrative overload + data sovereignty constraint, (2) solution: local LLM deployment needs model size validation. Cut redundant phrasing like "This project addresses the critical imperative to identify a resource-efficient paradigm for GenAI".
  > **Feedback**: *"Nur kurz darüber reden, und begründen, warum der Use Case sinnvoll ist"* [S. 7, Handschriftlich]
  > **Commit**: _pending_

- [x] **Add transition from Research Questions to Ch 2**
  Task ID: p4-03
  > **File**: `01-introduction/index.md` after line 38
  > **Action**: Add 1–2 sentences bridging to Ch 2: "The following chapter reviews related work on LLM evaluation, medical NLP, and context engineering strategies that inform our methodology."
  > **Feedback**: *"Der Übergang zu Kapitel 2 muss besser motiviert sein"* [S. 8, Handschriftlich]
  > **Commit**: _pending_

---

## Phase 5: Ch 4 & 5 (Results / Discussion) — Sharpen

- [x] **Reduce repetitive model listing in Ch 4.2**
  Task ID: p5-01
  > **File**: `04-results/index.md` lines 19–27
  > **Action**: The "Overview of Models and Evaluation Metrics" section repeats what Ch 3 already established. Replace with 2 sentences: "Eleven models were evaluated in a Zero-Shot configuration using the metrics defined in Section 3.6. Table X–Y present the mean scores across all 62 test cases."
  > **Feedback**: *"Der Leser will das nicht in die Cloud — ist repetitiv"* [S. 45, Handschriftlich]
  > **Commit**: _pending_

- [x] **Add metric interpretation per results table**
  Task ID: p5-02
  > **File**: `04-results/index.md` — after each table
  > **Action**: After each of the 4 tables, add 2–3 sentences answering: "What does this metric category tell us about clinical deployment viability?" Also address: is averaging appropriate? What does mean score X actually mean for a GP using this model?
  > **Feedback**: *"Fehlende Erläuterung: Geeignete Metric, insbesondere was misst sie? Was wird da gemittelt? Darf man mitteln? Was sagt das Mittel aus?"* [S. 46, Handschriftlich]
  > **Commit**: _pending_

- [x] **Add explicit table references in Discussion interpretations**
  Task ID: p5-03
  > **File**: `05-discussion/index.md` lines 8–38
  > **Action**: Every numerical claim in 5.1 must reference its source table. E.g. "Granite 3.3 (composite: 0.344, Table \ref{tab:composite})" instead of just "(composite: 0.344)". Check all 5 subsections of 5.1.
  > **Feedback**: *"Auf die Tabellen Bezug nehmen, die Werte ablesen, warum"* [S. 48, Handschriftlich bei 5.1]
  > **Commit**: _pending_

- [x] **Define or justify 95% pass-rate threshold in RQ1 answer**
  Task ID: p5-04
  > **File**: `05-discussion/index.md` line 55 (RQ1 answer)
  > **Action**: The text says "No model achieves a 95% pass rate" but this threshold appears without prior definition. Either: (a) define it in Ch 3 Evaluation Metrics as a success criterion, or (b) justify the choice here with 1 sentence.
  > **Feedback**: *"Wurde die Schwelle früher vorgestellt?"* [S. 50, Handschriftlich bei 5.3 RQ1]
  > **Commit**: _pending_

- [x] **Add variability data for Limitation 3 (single evaluation run)**
  Task ID: p5-05
  > **File**: `05-discussion/index.md` line 74 (Limitation 3)
  > **Action**: Current text mentions single run but no numbers on variability. If data from multiple runs exists, add standard deviation. If not, state explicitly: "Variability analysis was not performed due to cost constraints; the token cost per full evaluation run (see Appendix) would require ~X million tokens for 10-run self-consistency."
  > **Feedback**: *"Gibt's da keine Statistiken?"* [S. 51, Handschriftlich bei Limitation 3]
  > **Commit**: _pending_

- [x] **Resolve stale comment references (#R-TAB-SEMANTIC, #R-TAB-PASS)**
  Task ID: p5-06
  > **File**: `05-discussion/index.md` lines 30, 50 (HTML comments)
  > **Action**: Line 30 references `#R-TAB-SEMANTIC` — no such table exists. Line 50 references `#R-TAB-PASS` — no such table exists. Determine if these tables should be created in Ch 4 (semantic similarity breakdown? pass-rate table?) or remove the stale comments.
  > **Feedback**: Discovered during analysis — broken internal references
  > **Commit**: _pending_

---

## Phase 6: Formal & Cross-Cutting

- [x] **Build PDF and fix all "??" broken references**
  Task ID: p6-01
  > **Action**: Run `task build`, search output for "??". Fix broken `\ref{}` in markdown source. Known issue: `Table \ref{tab:logprobs-compat}` in Ch 3 line 479 uses LaTeX syntax — verify pandoc renders it.
  > **Feedback**: *"Tabellen-Referenzen fixen — einige Tabellen haben ?? als Referenz"* [P3-13]
  > **Commit**: _pending_

- [x] **Verify all appendix cross-references work**
  Task ID: p6-02
  > **Action**: Grep all `#appendix-` anchors in chapter files. Verify each target exists in `06-appendix/index.md`. Known refs: `#appendix-promp-techs`, `#appendix-gold-standard`, `#appendix-json-sim`, `#appendix-dag`, `#appendix-metrics-reference`, `#appendix-token-cost`, `#appendix-pearson`, `#appendix-silver-answers`.
  > **Feedback**: *"Hinweise aus dem Text in den Anhang: Verweis muss funktionieren und korrekt sein"* [E-Mail]
  > **Commit**: _pending_

- [x] **Check BFH template compliance (logo, headers, footers)**
  Task ID: p6-03
  > **Action**: Build PDF, compare against BFH Thesisvorlage. Check `templates/bfh-thesis.tex` and `00-frontmatter/metadata.yaml`.
  > **Feedback**: *"Formatvorlage prüfen: Logo, Kopf- und Fusszeilen — stimmt die Vorlage?"* [E-Mail]
  > **Commit**: _pending_

- [x] **Insert GitLab repository link (not in Abstract)**
  Task ID: p6-04
  > **File**: `03-methodology/index.md` (in Experimental Setup section, ~line 400) or as footnote in Ch 1
  > **Action**: Add GitLab URL. Supervisor said NOT in abstract.
  > **Feedback**: *"An geeigneter Stelle Link auf GitLab"* [Abstract, Handschriftlich]
  > **Commit**: _pending_

- [x] **Declare all AI-generated figures**
  Task ID: p6-05
  > **Files**: All figure captions across chapters
  > **Action**: Check each figure: `03-Methodology-Overview.png`, `03-screen-silver-answers.png`, `03-test-setup.png`, `sceen_llm-validator.png`, `03-GEval-Algorithm.png`, `04-metric-correlation.png`. If AI-generated, add "Source: Generated using [tool]" to caption.
  > **Feedback**: *"Quelle Bild (generiert??)"* [S. 21, Handschriftlich]
  > **Commit**: _pending_

---

## Phase 7: Final Review

- [x] **Full PDF build — verify page count decreased**
  Task ID: p7-01
  > **Action**: Build final PDF. Count pages. Compare to current version. Verify: no "??", all figures render, ToC shows "Related Work", all tables labeled.
  > **Commit**: N/A — verification only

- [x] **Read-through: verify "roter Faden" (narrative flow)**
  Task ID: p7-02
  > **Action**: Sequential read of all chapters. Check: (1) every term is defined before use, (2) each chapter opens with bridge to previous, (3) no forward-references to undefined concepts, (4) Results = data, Discussion = interpretation. Flag remaining issues.
  > **Feedback**: *"Roter Faden fehlt: Konzepte zu spät eingeführt, Zusammenhang zwischen Kapiteln nicht klar"* [Handschriftlich, mehrere Stellen]
  > **Commit**: N/A — verification only

---

## Feedback Coverage Tracker

When a task is completed, mark it `[x]` and fill in the commit hash. This tracker maps feedback items to tasks:

| Feedback Item | Task(s) | Status |
|---|---|---|
| **E-Mail: Formatvorlage prüfen** | p6-03 | pending |
| **E-Mail: Quellenangaben für ALLE Behauptungen** | p2-06 | pending |
| **E-Mail: Hinweise in den Anhang** | p6-02 | pending |
| **E-Mail: Verdacht auf generierten Text, rigoros kürzen** | p2-07, p2-08, p3-11, p4-02 | pending |
| **E-Mail: Kap 3 wenig zusammenhängend, Eval Pipeline?** | p3-01, p3-02 | pending |
| **E-Mail: Custom Metrics herleiten** | p3-07, p3-08 | pending |
| **E-Mail: Results/Discussion schärfer trennen** | p1-04, p1-05 | pending |
| **Handschrift: Kap 2 → Related Work** | p1-01 | pending |
| **Handschrift: Metriken aus 2.1 nach 3.6** | p1-02, p1-03 | pending |
| **Handschrift: Roter Faden fehlt** | p2-03, p3-09, p4-03, p7-02 | pending |
| **Handschrift: Sprachwechsel en/de begründen** | p3-06 | pending |
| **Handschrift: GitLab Link** | p6-04 | pending |
| **Handschrift: Note on the Craft hinterfragen** | p4-01 | pending |
| **Handschrift: Beispieldatensatz zeigen** | p3-04 | pending |
| **Handschrift: Golden/Silver Answer definieren** | p3-05 | pending |
| **Handschrift: Annotation Platform Grafik/Erklärung** | p3-01 | pending |
| **Handschrift: Quelle für SLM-Definition** | p2-05 | pending |
| **Handschrift: CoT "optimal" beweisen** | p2-08 | pending |
| **Handschrift: Quellen bei Prompt Engineering** | p2-06 | pending |
| **Handschrift: Tabelle in Anhang** | p2-07 | pending |
| **Handschrift: JSON/DAG Herleitung** | p3-07, p3-08 | pending |
| **Handschrift: llm-validator zu spät eingeführt** | p3-09 | pending |
| **Handschrift: 4.1 → Discussion** | p1-04 | pending |
| **Handschrift: 5.5 → Results** | p1-05 | pending |
| **Handschrift: Tabellen besser erläutern (Kap 4)** | p5-02 | pending |
| **Handschrift: Auf Tabellen Bezug nehmen (Kap 5)** | p5-03 | pending |
| **Handschrift: 95%-Schwelle definiert?** | p5-04 | pending |
| **Handschrift: Statistiken für Limitation 3** | p5-05 | pending |
| **Handschrift: Quellen Logprobs-Tabelle** | p6-01 | pending |
| **Handschrift: G-Eval Verständnisfrage / zu spät** | p3-10 | pending |
| **Handschrift: Fallback-Strategie → Discussion?** | p3-10 (supersedes p1-06) | pending |
| **Handschrift: Bilder-Quelle deklarieren** | p3-03, p6-05 | pending |
| **Handschrift: Procedure erklärt nicht** | p3-02 | pending |
| **Handschrift: Privacy/Security verwendet?** | p2-01 | pending |
| **Handschrift: Kap 2 kürzen** | p2-03, p2-04, p2-07, p2-08 | pending |
| **Handschrift: Tabellen-Referenzen ??** | p6-01 | pending |

---

*Generated by Clavix /clavix:plan — 2026-03-20*
