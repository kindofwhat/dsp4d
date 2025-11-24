# Research Directory (Migrated)

**Status:** This directory has been migrated to the phase-based structure.

## New Location

All research materials are now organized under:

**`../phase1-research/`**

### What Was Here

1. **existing-work.md** → Now at `../phase1-research/literature/existing-work.md`
   - Comprehensive literature review on LLM size vs performance
   - RAG impact analysis
   - Leaderboard research

2. **Research questions** (from old README.md):
   - What existing work exists on LLM performance vs. size? ✅ Answered in existing-work.md
   - What existing work exists on RAG impact on LLM performance? ✅ Answered
   - What existing work exists on Prompt Engineering impact? ⏳ To be explored in Phase 1
   - What existing work exists on open source models in leaderboards? ✅ Answered

## Migration Guide

If you're looking for research materials, see:

### Phase 1 Structure

```
phase1-research/
├── README.md                          # Phase 1 objectives and progress
├── literature/
│   ├── existing-work.md              # ← YOUR COMPREHENSIVE RESEARCH IS HERE
│   ├── papers/                       # Academic papers (PDFs)
│   └── summaries/                    # Paper summaries
├── frameworks/
│   ├── ragas-evaluation.md           # Framework evaluations
│   ├── langchain-evaluators.md
│   ├── haystack-evaluation.md
│   └── framework-comparison.md       # Final selection
└── benchmarks/
    ├── medical-benchmarks.md         # Domain-specific benchmarks
    ├── financial-benchmarks.md
    ├── legal-benchmarks.md
    └── security-benchmarks.md
```

## Outstanding Research Questions

From the original README, still to be addressed in Phase 1:

- [ ] **Prompt Engineering Impact**: How does prompt engineering affect LLM performance?
  - Investigate few-shot prompting, chain-of-thought, etc.
  - Impact on smaller models specifically
  - To be documented in `phase1-research/literature/prompt-engineering.md`

## Notes

This directory is kept for backward compatibility. All new research work should go in `phase1-research/`.

To avoid confusion, this directory may be removed after confirming all content has been successfully migrated and no external references point here.
