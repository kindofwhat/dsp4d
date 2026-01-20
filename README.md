# DSP4D: Optimal LLM Size for Medical Document Classification

**Data Sovereignty Procedures for Doctors (DSP4D)**

Finding the minimum viable LLM size for classifying medical documents and generating clinical actions using context engineering strategies.

## Project Overview

| | |
|---|---|
| **Duration** | 3 months (13 weeks) |
| **Effort** | 100 hours |
| **Institution** | Bern University of Applied Sciences (BFH) |

### Research Question

> *"What is the smallest LLM that can reliably classify medical documents and generate appropriate clinical actions?"*

### Approach

We evaluate multiple context engineering strategies:
- **Zero-Shot** — Instructions only (baseline)
- **Few-Shot** — 1-5 curated examples in prompt
- **RAG** — Retrieved guidelines/similar cases
- **Long-Context** — Full context where window permits

For detailed project plan, timeline, and methodology, see **[project.md](project.md)**.

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
