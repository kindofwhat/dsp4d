# DSP4D Paper Revision - Quick PRD

The DSP4D research paper on optimal LLM size for medical document classification has received comprehensive supervisor feedback (Vorabpruefung) identifying structural issues, missing citations, verbose AI-sounding prose, and a weak narrative thread. The goal is to implement all feedback by 2026-03-25 (5 days) to produce a submission-ready BFH CAS thesis. The paper must become shorter and more academically rigorous. Key structural changes: rename Ch 2 to "Related Work" and trim aggressively, move metrics from Ch 2.1 to Ch 3.6 with use-case justifications, make Ch 3 coherent about what was built, sharply separate Results/Discussion, and derive custom metrics properly.

Content improvements include adding missing citations throughout (especially Ch 2.4), overhauling the Golden/Silver Answer definitions in Ch 3.3, introducing all terms at first mention (llm-validator, G-Eval), better embedding figures/tables, and trimming Ch 1. Formal fixes cover BFH template compliance, broken references ("??"), appendix links, and GitLab repository link placement.

Out of scope: no new experiments, no new diagrams, no fundamental rewrite, no build pipeline changes. Work proceeds in small topic-based batches with atomic commits. Christian is the primary implementer; Benjamin may review. The authoritative feedback source is `paper/DSP4D-Feedback-Zusammenfassung.md`.

---

*Generated with Clavix Planning Mode*
*Generated: 2026-03-20T10:00:00Z*
