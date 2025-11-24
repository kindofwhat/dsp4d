# Testing Directory (Migrated)

**Status:** This directory has been migrated to the phase-based structure.

## New Location

All testing and experimentation materials are now organized under:

**`../phase4-experimentation/`**

### What This Directory Was For

Original purpose (from old README):
> "Describe how to test LLMs for performance vs size and RAG. Have test results here."

This has been expanded into a comprehensive experimentation framework.

## Migration Guide

If you're looking for testing materials, see:

### Phase 4 Structure

```
phase4-experimentation/
├── README.md                          # Complete experimentation guide
├── baseline/                          # Non-RAG baseline tests
│   ├── experiment-config.yaml
│   ├── run-baseline.py
│   └── results/
├── rag-enhanced/                      # RAG-enabled tests
│   ├── experiment-config.yaml
│   ├── run-rag-experiments.py
│   └── results/
│       ├── llama-3.2-1b/
│       │   ├── k3/
│       │   ├── k5/
│       │   └── k10/
│       └── ...
├── security/                          # Security-focused tests
│   ├── data-leakage-tests.py
│   ├── prompt-injection-tests.py
│   └── pii-exposure-tests.py
└── results/                           # Consolidated results
    └── performance-matrix.csv
```

### What to Test

Phase 4 covers comprehensive testing:

1. **Baseline Testing** (Week 9)
   - All models without RAG
   - Accuracy metrics (Exact Match, F1, BLEU)
   - Performance metrics (Latency, Memory, Throughput)

2. **RAG-Enhanced Testing** (Week 10)
   - All models with RAG enabled
   - Multiple k-values (3, 5, 10 documents)
   - RAG-specific metrics (Context relevance, Answer faithfulness)
   - Comparison to baseline

3. **Security Testing** (Week 11)
   - Data leakage detection
   - Prompt injection resistance
   - PII exposure testing
   - Deployment scenario comparison (on-device vs cloud)

### Test Datasets

Test datasets are created in Phase 2 and stored at:
- `../phase2-test-design/datasets/medical/`
- `../phase2-test-design/datasets/financial/`
- `../phase2-test-design/datasets/legal/`

Each contains:
- `questions.json` - Test questions
- `verified-answers.json` - Ground truth
- `documents/` - RAG corpus

## How to Run Tests

See comprehensive guides:
1. **Phase 2 README**: Dataset preparation and metrics definition
2. **Phase 3 README**: Model setup and RAG implementation
3. **Phase 4 README**: Running experiments and collecting results
4. **Phase 5 README**: Analyzing results and creating reports

## Notes

This directory is kept for backward compatibility. All new testing work should go in the appropriate phase directory:
- **Test design** → `phase2-test-design/`
- **Test setup** → `phase3-setup/`
- **Test execution** → `phase4-experimentation/`
- **Test analysis** → `phase5-analysis/`

This directory may be removed after confirming migration is complete.
