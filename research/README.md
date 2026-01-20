# Research

This directory contains literature reviews, background research, and theoretical foundations for the project.

## Research Areas

### 1. Context Engineering & In-Context Learning
**Focus:** Understanding how different context strategies affect model performance.
- **RAG (Retrieval-Augmented Generation):** Retrieval of guidelines vs. similar cases.
- **Few-Shot Learning:** Optimal number of examples, static vs. dynamic selection.
- **Long-Context:** Trade-offs of processing full documents vs. retrieval.
- **Prompt Engineering:** Chain-of-Thought, System Instructions.

*Location:* `few-shot-learning/` (to be renamed/expanded) and new notes.

### 2. Model Size & Performance (Scaling Laws)
**Focus:** How performance degrades as model size decreases.
- Breakpoint analysis for classification tasks.
- "Densing Law" and quantization effects.
- Capabilities of Small Language Models (SLMs) like Phi-3, Llama-3.2-1B.

*Location:* `model-size-studies/`

### 3. Existing Work
**Focus:** Prior art in medical document processing and SLMs.
- Literature review on LLM size vs. performance.
- Benchmarks for medical NLP.

*Location:* `existing-work/`

## Key Research Questions for Phase 1

1.  **Context vs. Size:** Can a rich context (RAG/Few-Shot) compensate for a smaller model size (1B/3B)?
2.  **Retrieval Strategy:** Is it better to retrieve *rules* (guidelines) or *instances* (similar past cases) for medical classification?
3.  **Efficiency:** What is the latency cost of RAG vs. Long-Context on edge devices (Raspberry Pi)?

## Directory Structure

```
research/
├── README.md                          # This file
├── existing-work/                     # General literature review
│   └── existing-work.md
├── context-engineering/               # Strategies (RAG, Few-Shot, etc.)
│   ├── few-shot-learning/            # (Legacy folder, merging here)
│   ├── rag-methods.md                # NEW: Research on RAG
│   └── context-window-studies.md     # NEW: Research on context length
└── model-size-studies/                # Scaling laws and quantization
    ├── classification-tasks.md
    └── small-model-capabilities.md
```