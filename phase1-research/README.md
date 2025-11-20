# Phase 1: Literature Review & Framework Selection

**Duration:** Weeks 1-3
**Effort:** ~20 hours
**Status:** In Progress

## Objectives

1. Survey existing research on LLM size vs. performance trade-offs
2. Review papers on RAG impact on model performance (focus on smaller models)
3. Document security/privacy implications of different model sizes
4. Identify relevant benchmarks for sensitive data scenarios
5. Evaluate and select evaluation frameworks

## Directory Structure

```
phase1-research/
├── README.md                          # This file
├── literature/                        # Literature review materials
│   ├── existing-work.md              # Comprehensive research summary (COMPLETED)
│   ├── papers/                       # Downloaded academic papers
│   └── summaries/                    # Paper summaries and notes
├── frameworks/                        # Evaluation framework comparisons
│   ├── ragas-evaluation.md           # RAGAS framework analysis
│   ├── langchain-evaluators.md       # LangChain evaluation tools
│   ├── haystack-evaluation.md        # Haystack evaluation analysis
│   └── framework-comparison.md       # Final comparison and selection
└── benchmarks/                        # Benchmark research
    ├── medical-benchmarks.md         # Medical domain benchmarks
    ├── financial-benchmarks.md       # Financial domain benchmarks
    ├── legal-benchmarks.md           # Legal domain benchmarks
    └── security-benchmarks.md        # Security/privacy benchmarks
```

## Key Deliverables

- [x] **Literature Review** (`literature/existing-work.md`)
  - LLM size vs performance research
  - RAG impact on smaller models
  - Open-source model leaderboards
  - Densing law findings (capability density doubles every 3.5 months)

- [ ] **Framework Selection** (`frameworks/framework-comparison.md`)
  - RAGAS evaluation (recommended for RAG-specific metrics)
  - Alternative frameworks (LangChain, Haystack, MLflow)
  - Comparison matrix with pros/cons
  - Final recommendation with justification

- [ ] **Benchmark Identification** (`benchmarks/`)
  - Domain-specific benchmarks for medical, financial, legal use cases
  - Security and privacy evaluation criteria
  - Data sovereignty compliance metrics

## Current Progress

### Completed
- ✅ Comprehensive literature review on LLM size vs performance
- ✅ RAG impact analysis (10-30% performance improvements documented)
- ✅ Open-source leaderboard analysis (Hugging Face, Vellum, Artificial Analysis)
- ✅ Identified optimal range: 7B-13B parameters with RAG

### In Progress
- 🔄 Framework evaluation (RAGAS, LangChain, Haystack)
- 🔄 Security benchmark identification

### Not Started
- ⬜ Medical domain benchmark research
- ⬜ Financial domain benchmark research
- ⬜ Legal domain benchmark research

## Key Findings from Literature Review

### LLM Size Trends
- **Densing Law**: Model parameters for equivalent performance halve every 3.5 months
- **Sweet Spot**: 7B-13B parameters with RAG can match 70B+ models for specific tasks
- **Test-Time Compute**: OpenAI's o1 approach emphasizes reasoning steps over pure size

### RAG Impact
- **Performance Gains**: 10-30% accuracy improvements over standard approaches
- **Cost-Effectiveness**: More economical than massive models for domain-specific tasks
- **Innovations**: Speculative RAG, RAFT, Adaptive Retrieval, GraphRAG

### Security Considerations
- On-premise deployment feasible with 7B-13B models
- Air-gapped environments possible
- Data sovereignty procedures critical for medical use case

## Next Steps

1. **Week 3 Tasks**:
   - Complete framework evaluation matrix
   - Test RAGAS with sample medical scenario
   - Document framework selection rationale
   - Set up development environment with chosen tools

2. **Handoff to Phase 2**:
   - Recommended framework and tools
   - Identified benchmarks for test scenarios
   - Security/privacy evaluation criteria

## Resources

### Academic Papers
Store PDFs in `literature/papers/` and create summaries in `literature/summaries/`

### Framework Documentation
- RAGAS: https://docs.ragas.io/
- LangChain Evaluators: https://python.langchain.com/docs/guides/evaluation
- Haystack: https://docs.haystack.deepset.ai/docs/evaluation
- MLflow LLM Evaluation: https://mlflow.org/docs/latest/llm-tracking.html

### Benchmarks
- Hugging Face Open LLM Leaderboard: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- RAGAS Benchmarks: https://docs.ragas.io/en/latest/concepts/metrics/
- Medical QA Datasets: PubMedQA, MedQA, USMLE

## Notes

- Keep all research findings version-controlled
- Document methodology for reproducibility
- Note hardware requirements for framework testing
- Consider data sovereignty requirements from the start
