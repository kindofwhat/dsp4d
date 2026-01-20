# Testing & Experimentation

**Status:** This directory serves as a guide to the project's testing methodology.

**Actual testing resources are located in:**
- **`../evaluation/`**: Test datasets, metrics, and ground truth.
- **`../experiments/`**: Execution scripts, logs, and raw results.

## Testing Scope

We evaluate models across three dimensions:
1.  **Model Size:** 1B, 3B, 7B, 13B.
2.  **Context Strategy:** Zero-Shot, One-Shot, Few-Shot, RAG.
3.  **Deployment:** WebLLM, Local (Edge), API.

## Methodology

### 1. Baseline (Zero-Shot)
Establish the native capability of each model size without assistance.
*Location:* `../experiments/classification/`

### 2. Context Engineering Tests
Compare how different strategies improve performance:
- **Few-Shot:** Provide 3-5 examples.
- **RAG:** Retrieve relevant context (guidelines or similar cases).
*Location:* `../experiments/generation/` and `../experiments/classification/`

### 3. Breakpoint Analysis
Identify the "sweet spot" where performance is acceptable (>95% accuracy) but resource usage is minimized.
*Location:* `../experiments/breakpoint-analysis/`

## Quick Links

- [Test Datasets](../evaluation/test-datasets/)
- [Evaluation Metrics](../evaluation/metrics/)
- [Experiment Results](../experiments/results/)