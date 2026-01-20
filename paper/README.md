# DSP4D: Optimal LLM Size for Medical Document Classification

**Data Sovereignty Procedures for Doctors (DSP4D)**

Finding the minimum viable LLM size for classifying medical documents and generating clinical actions using context engineering strategies.

## Project Overview

**Duration:** 3 months (13 weeks)
**Total Effort:** 100 hours
**Institution:** Bern University of Applied Sciences (BFH)
**Dataset:** [Graz Synthetic Clinical text Corpus (GraSCCo) v2](https://doi.org/10.5281/zenodo.15747389)

### Core Research Question

> **"What is the smallest LLM that can reliably classify clinical findings and generate appropriate clinical actions using context engineering on the GraSCCo corpus?"**

### The Challenge

Doctors are overwhelmed with clinical documentation. We use the **GraSCCo** corpus—a publicly shareable, multiply-alienated German clinical text corpus—to simulate real-world scenarios where a system must:
1. **Identify clinical intent** and document classification.
2. **Extract key information** (diagnosis, findings, urgency).
3. **Generate appropriate action** (schedule surgery, order follow-up, refer to specialist).

**Critical Requirements:**
- **High accuracy** (medical correctness is critical)
- **Data sovereignty** (on-device/local deployment, no cloud)
- **German Language Support** (GraSCCo is in German)
- **Fast inference** (real-time assistance)
- **Small footprint** (edge devices, Raspberry Pi, WebLLM in browser)

### Approach: Context Engineering Strategies

## Quick Start

### Prerequisites

- [Homebrew](https://brew.sh/) (macOS)
- [Task](https://taskfile.dev/) — `brew install go-task/tap/go-task`

### Setup

```bash
# Install pandoc and LaTeX
task setup
task setup-latex
```

### Build Paper

```bash
task build          # Build PDF
task open           # Open PDF
task build:word     # Build Word document
task build:draft    # Fast build (no citations)
task watch          # Auto-rebuild on changes
```

### Available Tasks

```bash
task                # List all available tasks
task clean          # Remove generated files
```

## Project Structure

```
dsp4d/
├── paper/                  # Academic paper (Pandoc/Markdown)
│   ├── paper.md           # Main paper content
│   ├── defaults.yaml      # Pandoc configuration
│   └── references.bib     # Bibliography
├── output/                 # Generated PDFs (gitignored)
│
├── research/              # Literature review & background
├── document-types/        # Medical document definitions
├── few-shot-examples/     # Example sets per document type
├── evaluation/            # Test datasets & metrics
├── models/                # Model configurations
├── experiments/           # Experimental code & results
└── analysis/              # Final analysis & recommendations
```

## Key Documents

- **[project.md](project.md)** — Detailed project plan, timeline, research questions
- **[paper/paper.md](paper/paper.md)** — Academic paper draft
- **[research/README.md](research/README.md)** — Research overview

## Success Metrics

- Classification accuracy >95%
- Action appropriateness >90%
- Latency <2 seconds
- Runs on Raspberry Pi 5

## Resources

- [WebLLM](https://webllm.mlc.ai/) — Browser-based LLM
- [Ollama](https://ollama.ai/) — Local deployment
- [Groq](https://groq.com/) — Fast inference API

---

**Status:** Research & document type definition phase
