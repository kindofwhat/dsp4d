# DSP4D: Optimal LLM Size for Medical Document Classification

**Data Sovereignty Procedures for Doctors (DSP4D)**

[📄 **Read the latest PDF**](https://kindofwhat.github.io/dsp4d/dsp4d-paper.pdf)

Finding the minimum viable LLM size for classifying medical documents and generating clinical actions using context engineering strategies.

## Project Overview
...
### Available Tasks

```bash
task                # List all available tasks
task clean          # Remove generated files
```

## Continuous Integration

This project uses **GitHub Actions** to automatically build the paper.

- **Automatic Build:** Every push to `main` or `doc/paper` triggers a PDF build.
- **Artifacts:** The resulting PDF is stored as a build artifact in the "Actions" tab.
- **Deployment:** The latest version is automatically published to [GitHub Pages](https://kindofwhat.github.io/dsp4d/dsp4d-paper.pdf).

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
