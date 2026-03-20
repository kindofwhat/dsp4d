# Product Requirements Document: DSP4D Paper Revision

## Problem & Goal

The DSP4D research paper ("Optimal LLM Size for Medical Document Classification Using Context Engineering") has undergone pre-review (Vorabpruefung) by the BFH supervisor. Extensive feedback was received via handwritten PDF annotations and email, identifying structural weaknesses, missing citations, overly verbose AI-generated-sounding text, and unclear narrative flow ("roter Faden"). The paper cannot be submitted in its current state.

**Goal:** Implement all supervisor feedback to produce a submission-ready academic paper that meets BFH CAS thesis standards by **2026-03-25** (5 days). The paper must become shorter, more precise, and more academically rigorous — not longer.

## Requirements

### Must-Have Changes (Priority 1 — Structural)

1. **Rename Chapter 2** from "Theory / State of Research" to "Related Work" and rigorously trim content to only what is relevant to the research questions
2. **Move metrics from Ch 2.1 to Ch 3.6** — remove broad theoretical treatment from Related Work; introduce each metric in Methodology with a use-case example and justification
3. **Make Chapter 3 coherent** — clearly explain what was built (Eval Pipeline, Silver Answers App, llm-validator), which models were used, and why
4. **Sharply separate Results (Ch 4) and Discussion (Ch 5)** — move Silver Answer Validity (4.1) to Discussion, move Correlation Analysis (5.5) to Results
5. **Derive and justify custom metrics** (JSON Structural Similarity, DAG metric) — explain what they measure and their significance for the use case

### Must-Have Changes (Priority 2 — Content)

6. **Add missing citations throughout** — especially Ch 2.4 ("Why Prompt Engineering Matters"), SLM definition, and all unsupported claims
7. **Overhaul Ch 3.3 (Golden Answer Generation)** — clearly define Golden/Silver Answers, justify en/de language switch in prompts, show example dataset
8. **Introduce terms where first used** — llm-validator, G-Eval, Silver Answers must be explained at first mention, not pages later
9. **Better embed figures and tables** — declare AI-generated images, reference tables in text with interpretation, fix "??" references
10. **Trim Chapter 1** — reconsider "A Note on the Craft" (decision point), motivate use case concisely

### Must-Have Changes (Priority 3 — Formal)

11. **Check BFH template compliance** — logo, headers, footers per BFH Thesisvorlage
12. **Fix appendix references** — all in-text references to appendix must work correctly
13. **Fix broken table references** — resolve "??" references (Table 4, Table 7, etc.)
14. **Insert GitLab link** at an appropriate place (not in Abstract)

### Technical Requirements

- **Build system:** Pandoc Markdown -> pdflatex via Task runner
- **Chapter structure:** Controlled by `paper/defaults.yaml` input-files list
- **Citations:** BibTeX in `references.bib`, referenced as `[@key]`
- **Language:** `lang: de-CH` (Swiss German), paper content in English
- **Template:** `templates/bfh-thesis.tex` (BFH Thesisvorlage)

### Workflow Requirements

- **Small, topic-based work batches** with atomic git commits per logical change
- **Primary author:** Christian (solo implementation, Benjamin may review)
- **AI assistance:** Claude helps with restructuring and trimming; human reviews all changes for academic integrity
- **Direction:** Paper must get SHORTER, not longer. Every edit should reduce verbosity.

## Out of Scope

- **No new experiments** — research methodology and results are final
- **No new diagrams or figures** — work with existing visuals only
- **No fundamental rewrite** — restructure, trim, and sharpen existing content
- **No changes to the build pipeline** — Pandoc/LaTeX/Task setup stays as-is
- **No content fabrication** — all additions must be traceable to existing research or proper citations

## Additional Context

- **Supervisor concern about AI-generated text:** Chapter 2 especially flagged as too verbose and AI-sounding. Trimming must prioritize making text concise and precise, not just shorter.
- **"A Note on the Craft" (Ch 1):** Supervisor questioned its appropriateness. This is a decision point — may keep, modify, or remove based on author preference.
- **Deadline pressure:** 5 days means prioritization is critical. Priority 1 (structural) changes have the highest impact and should be tackled first.
- **The feedback document** (`paper/DSP4D-Feedback-Zusammenfassung.md`) contains the complete, structured feedback with page references and is the authoritative source for all required changes.

---

*Generated with Clavix Planning Mode*
*Generated: 2026-03-20T10:00:00Z*
