# DSP4D: LLM Size Optimization for Sensitive Data Processing

**Data Sovereignty Procedures for Doctors (DSP4D)**

A 3-month research project investigating the optimal LLM size for handling sensitive data with RAG (Retrieval Augmented Generation).

## Project Overview

**Duration:** 3 months (13 weeks)
**Total Effort:** 100 hours
**Institution:** Bern University of Applied Sciences (BFH)

### Core Research Question

> **"How small can an LLM be while still effectively processing sensitive data (medical, financial, legal) with RAG support?"**

### Objectives

1. Identify size thresholds for different sensitivity levels
2. Quantify RAG impact on model size requirements
3. Create reproducible evaluation framework for LLM testing
4. Provide actionable recommendations for production deployments

### Key Use Case: Medical Document Summarization

Doctors need quick digests of lengthy medical reports, especially after hours when digital information floods in. This requires:
- **High data sensitivity** (HIPAA/GDPR compliance)
- **On-device/local deployment** (data sovereignty)
- **Fast inference** (real-time assistance)
- **High accuracy** (medical correctness critical)

## Project Structure

This project is organized into **5 phases** following the detailed project plan in `project.md`:

```
dsp4d/
├── README.md                          # This file
├── project.md                         # Detailed 13-week project plan
├── Themenantrag Gen KI 1.0...docx    # Thesis proposal document
│
├── initial/                           # Early brainstorming (historical reference)
│   └── README.md                      # Meeting notes and initial ideas
│
├── phase1-research/                   # WEEKS 1-3: Literature Review (20h)
│   ├── README.md                      # Phase objectives and progress
│   ├── literature/                    # Research papers and summaries
│   │   ├── existing-work.md          # ✅ Comprehensive literature review
│   │   ├── papers/                   # Academic PDFs
│   │   └── summaries/                # Paper summaries
│   ├── frameworks/                    # Evaluation framework comparison
│   │   ├── ragas-evaluation.md
│   │   ├── langchain-evaluators.md
│   │   ├── haystack-evaluation.md
│   │   └── framework-comparison.md   # Final selection
│   └── benchmarks/                    # Domain-specific benchmarks
│       ├── medical-benchmarks.md
│       ├── financial-benchmarks.md
│       ├── legal-benchmarks.md
│       └── security-benchmarks.md
│
├── phase2-test-design/                # WEEKS 4-6: Dataset Preparation (25h)
│   ├── README.md                      # Test design objectives
│   ├── scenarios/                     # Test scenario definitions
│   │   ├── medical-diagnosis.md
│   │   ├── financial-advisory.md
│   │   ├── legal-document-analysis.md
│   │   └── scenario-template.md
│   ├── datasets/                      # Golden datasets
│   │   ├── medical/
│   │   │   ├── questions.json
│   │   │   ├── verified-answers.json
│   │   │   └── documents/
│   │   ├── financial/
│   │   └── legal/
│   └── metrics/                       # Metrics definitions
│       ├── accuracy-metrics.md       # Exact match, F1, BLEU
│       ├── rag-specific-metrics.md   # Context relevance, faithfulness
│       ├── security-metrics.md       # Data leakage, prompt injection
│       └── performance-metrics.md    # Latency, memory, throughput
│
├── phase3-setup/                      # WEEKS 7-8: Experimental Setup (15h)
│   ├── README.md                      # Setup objectives
│   ├── models/                        # Model selection and configs
│   │   ├── model-selection.md
│   │   ├── model-configs/
│   │   ├── quantization/
│   │   └── download-scripts/
│   └── rag-implementation/            # RAG pipeline
│       ├── rag-architecture.md
│       ├── vector-db/
│       ├── embeddings/
│       ├── chunking/
│       ├── retrieval/
│       └── pipeline-code/
│           ├── requirements.txt
│           ├── rag_pipeline.py
│           ├── indexing.py
│           └── retrieval.py
│
├── phase4-experimentation/            # WEEKS 9-11: Experiments (30h)
│   ├── README.md                      # Experimentation guide
│   ├── baseline/                      # Non-RAG baseline tests
│   │   ├── run-baseline.py
│   │   └── results/
│   ├── rag-enhanced/                  # RAG-enabled tests
│   │   ├── run-rag-experiments.py
│   │   └── results/
│   │       ├── llama-3.2-1b/
│   │       │   ├── k3/
│   │       │   ├── k5/
│   │       │   └── k10/
│   │       └── ...
│   ├── security/                      # Security testing
│   │   ├── data-leakage-tests.py
│   │   ├── prompt-injection-tests.py
│   │   └── pii-exposure-tests.py
│   └── results/                       # Consolidated results
│       └── performance-matrix.csv
│
├── phase5-analysis/                   # WEEKS 12-13: Analysis & Docs (10h)
│   ├── README.md                      # Analysis objectives
│   ├── data-analysis/                 # Statistical analysis
│   │   ├── statistical-tests.ipynb
│   │   ├── performance-curves.ipynb
│   │   ├── rag-impact-analysis.ipynb
│   │   └── cost-benefit.ipynb
│   ├── visualizations/                # Charts and plots
│   │   ├── plots/
│   │   └── tables/
│   └── final-report/                  # Deliverables
│       ├── report.md                 # 15-20 page report
│       ├── executive-summary.md
│       ├── methodology.md
│       ├── results.md
│       ├── recommendations.md
│       └── reproducibility-package/
│
├── research/                          # ⚠️ MIGRATED to phase1-research/
│   └── README.md                      # Migration notice
│
└── testing/                           # ⚠️ MIGRATED to phase4-experimentation/
    └── README.md                      # Migration notice
```

## Quick Start Guide

### Current Status: Phase 1 (Literature Review)

**Completed:**
- ✅ Comprehensive literature review on LLM size vs performance
- ✅ RAG impact analysis (10-30% improvements documented)
- ✅ Open-source model leaderboard research
- ✅ Key finding: 7B-13B parameters with RAG can match 70B+ baseline models

**In Progress:**
- 🔄 Evaluation framework selection (RAGAS recommended)
- 🔄 Domain-specific benchmark identification

**Next Steps:**
- Complete framework evaluation
- Set up development environment
- Prepare for Phase 2 (test design)

### How to Navigate

1. **Understand the project**: Read `project.md` for detailed timeline
2. **Check current phase**: See `phase1-research/README.md` for progress
3. **Review research findings**: See `phase1-research/literature/existing-work.md`
4. **Explore future phases**: Read README files in phase2-5 directories

### Development Setup (Phase 3)

```bash
# Virtual environment will be created in Phase 3
# For now, research is documentation-focused

# To view project structure
tree -L 2 dsp4d/

# To track progress
git status
git log --oneline
```

## Key Findings from Phase 1

### LLM Size Trends

**Densing Law Discovery:**
- Capability density (capability per parameter) doubles every 3.5 months
- Model parameters for equivalent performance halve every 3.5 months
- Example: MiniCPM-1 2.4B (Feb 2024) matches Mistral-7B (Sep 2023)

**Optimal Range for Sensitive Data:**
- 7B-13B parameters with RAG
- Can match 70B+ models for domain-specific tasks
- Feasible for on-premise, air-gapped deployment

### RAG Impact

**Performance Gains:**
- 10-30% accuracy improvements over baseline
- MRAG: 10% improvement on exact matches, 25% on category matches
- Fusion RAG: 10-30% accuracy gains
- RAFT: Outperforms traditional RAG in specialized domains

**Cost-Effectiveness:**
- More economical than massive models for domain tasks
- Enables on-device deployment (Raspberry Pi, edge devices)
- Supports data sovereignty requirements

### Innovations to Explore

- **Speculative RAG**: Parallel processing for reduced latency
- **Adaptive Retrieval**: Dynamic retrieval based on query complexity
- **GraphRAG**: Knowledge graph integration
- **RAFT**: RAG + fine-tuning with synthetic datasets

## Project Timeline

| Phase | Weeks | Effort | Focus |
|-------|-------|--------|-------|
| **Phase 1** | 1-3 | 20h | Literature review, framework selection |
| **Phase 2** | 4-6 | 25h | Test design, dataset preparation |
| **Phase 3** | 7-8 | 15h | Model setup, RAG implementation |
| **Phase 4** | 9-11 | 30h | Baseline, RAG, security testing |
| **Phase 5** | 12-13 | 10h | Analysis, visualization, final report |

**Total:** 13 weeks, 100 hours

## Expected Deliverables

1. **Evaluation Framework** - Documented testing methodology ✅ (Phase 1)
2. **Golden Test Sets** - 150-300 test questions across scenarios (Phase 2)
3. **Performance Matrix** - Model size vs accuracy with/without RAG (Phase 4)
4. **Sweet Spot Analysis** - Recommendations per sensitivity level (Phase 5)
5. **Final Report** - 15-20 page comprehensive analysis (Phase 5)

## Technology Stack (Planned)

### Models to Test
- **1B**: Llama 3.2 1B, Phi-3-mini
- **3B**: Llama 3.2 3B, Phi-3-small
- **7B**: Mistral 7B, Llama 3.1 7B
- **13B**: Llama 3.1 13B, Vicuna 13B

### RAG Components
- **Vector DB**: ChromaDB (prototyping) or Qdrant (production)
- **Embeddings**: all-MiniLM-L6-v2, bge-base-en-v1.5, or e5-large-v2
- **Framework**: LangChain for RAG orchestration

### Evaluation
- **RAG Metrics**: RAGAS (context relevance, answer faithfulness, relevancy)
- **Accuracy**: Exact Match, F1, BLEU, ROUGE
- **Security**: OWASP LLM Top 10, custom injection tests
- **Performance**: Latency, memory usage, tokens/second

### Development
- **Python**: 3.10+
- **ML**: PyTorch, HuggingFace Transformers
- **Tracking**: MLflow or Weights & Biases
- **Analysis**: Pandas, NumPy, SciPy, Matplotlib, Seaborn

## Critical Success Factors

- ✅ **Consistent Testing**: Identical prompts, settings, and metrics across all models
- ✅ **RAG Quality**: High-quality retrieval (poor retrieval skews results)
- ✅ **Real-world Relevance**: Practical scenarios mirroring actual use cases
- ✅ **Statistical Rigor**: Multiple runs per configuration for significance
- ✅ **Data Sovereignty**: Only synthetic/public data, no real PII

## Resources & Documentation

### Academic References
- **Densing Law**: Xiao et al. (2025), Nature Machine Intelligence
- **RAG Survey**: Yu et al. (2024), arXiv:2405.07437
- **RAGAS**: Es et al. (2023), arXiv:2309.15217
- **RAFT**: Zhang et al. (2024), arXiv preprint

### Tools & Frameworks
- **RAGAS**: https://docs.ragas.io/
- **LangChain**: https://python.langchain.com/
- **ChromaDB**: https://docs.trychroma.com/
- **HuggingFace**: https://huggingface.co/docs

### Leaderboards
- **Open LLM Leaderboard**: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- **Vellum**: https://www.vellum.ai/llm-leaderboard
- **Artificial Analysis**: https://artificialanalysis.ai/

## Git Workflow

This is an active Git repository. Commit guidelines:

```bash
# Atomic commits with descriptive messages
git commit -m "feat(phase1): add RAGAS framework evaluation"
git commit -m "docs(phase2): create medical scenario definition"
git commit -m "test(phase4): run baseline experiments for 7B models"

# Branch for experiments (if needed)
git checkout -b experiment/rag-k-values

# Tag milestones
git tag -a phase1-complete -m "Literature review and framework selection complete"
```

## Contact & Collaboration

**Project Members:**
- Research Lead: [Your Name]
- Advisor: Beni
- Stakeholders: 3 doctors (via hin.ch platform)

**Related Initiatives:**
- Electronic Patient Dossier (EPD) integration
- hin.ch communication platform
- Apertus data sovereignty project

## Notes for AI Assistants

When working in this project:
1. **Always check which phase you're in** - Each phase has specific objectives
2. **Follow the project plan** - See `project.md` for detailed timeline
3. **Document everything** - This is research, reproducibility is critical
4. **Use synthetic data only** - Never commit real PII or sensitive data
5. **Think about data sovereignty** - Security and privacy are core requirements
6. **Check phase README files** - Each has detailed guidance and checklists

## License & Usage

This is educational research for BFH. Results intended for:
- Academic publication
- Open-source reproducibility package
- Practical deployment guidelines for sensitive data scenarios

---

**Last Updated:** November 20, 2025
**Current Phase:** Phase 1 (Literature Review & Framework Selection)
**Status:** In Progress
