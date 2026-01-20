# Related Work / Prior Work

This directory contains the literature review and analysis for the "Related Work" chapter of the paper.

## Structure

### 1. Clinical NLP & Datasets (`clinical-nlp/`)
**Focus:** Existing approaches to medical document classification and action generation.
- **GraSCCo Corpus:** Literature using this specific dataset (Modersohn et al.).
- **De-identification:** Methods for handling PII in medical text.
- **German Clinical NLP:** Specific challenges of German medical terminology.

### 2. Model Scaling & Efficiency (`model-scaling/`)
**Focus:** The trade-off between model size and performance.
- **Scaling Laws:** Chinchilla, Kaplan, and "Densing Law".
- **Small Language Models (SLMs):** Capabilities of Phi-3, Llama 3.2 (1B/3B).
- **Quantization:** Impact of 4-bit/8-bit quantization on clinical accuracy.

### 3. Context Engineering Strategies (`context-engineering/`)
**Focus:** Techniques to enhance small model performance.
- **Few-Shot Learning:** In-context learning papers (Brown et al., Min et al.).
- **RAG:** Retrieval-Augmented Generation for domain adaptation.
- **Prompt Engineering:** Chain-of-Thought, System Instructions.

## Workflow
1.  Add PDF papers or notes to the respective subdirectories.
2.  Summarize key findings in markdown files.
3.  Synthesize into the `paper.md` "Related Work" section.
