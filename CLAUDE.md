# CLAUDE.md - DSP4D Project

## Project Overview

**DSP4D (Data Sovereignty Procedures for Doctors)** is a research project investigating the optimal LLM size for medical document classification using context engineering strategies.

- **Duration:** 3 months (13 weeks)
- **Institution:** Bern University of Applied Sciences (BFH)
- **Dataset:** GraSCCo (Graz Synthetic Clinical text Corpus) - German clinical texts

## Project Structure

```
dsp4d/
├── CLAUDE.md                              # This file
├── paper/                                 # Academic paper and research content
│   ├── Taskfile.yml                      # Build tasks (cross-platform)
│   ├── paper.md                          # Main paper (Pandoc Markdown)
│   ├── defaults.yaml                     # Pandoc configuration
│   ├── references.bib                    # Bibliography (BibTeX)
│   ├── output/                           # Generated PDFs (gitignored)
│   ├── README.md                         # Paper-specific documentation
│   ├── project.md                        # Detailed project plan
│   │
│   ├── research/                         # Literature review & background
│   ├── document-types/                   # Medical document definitions
│   ├── few-shot-examples/                # Example sets per document type
│   ├── evaluation/                       # Test datasets & metrics
│   ├── models/                           # Model configurations
│   ├── experiments/                      # Experimental code & results
│   └── analysis/                         # Final analysis & recommendations
│
├── Test_ai_bniweb_ch.ipynb              # Initial API test notebook
└── Themenantrag*.docx                    # Thesis proposal document
```

## Building the Paper

All paper-related tasks are run from the `paper/` directory:

```bash
cd paper

# First-time setup (install pandoc + LaTeX)
task setup
task setup-latex    # Run in new terminal after setup

# Build PDF
task build          # Full build with citations
task build-draft    # Fast build without citations
task build-word     # Word document
task build-html     # HTML version

# Development
task watch          # Auto-rebuild on file changes (recursive)
task open           # Open generated PDF
task clean          # Remove output directory
```

### Cross-Platform Support

The Taskfile auto-detects the OS and uses appropriate tools:

| Platform | Package Manager | Watch Tool | PDF Viewer |
|----------|----------------|------------|------------|
| macOS | brew | fswatch | open |
| Linux | apt-get | inotifywait | xdg-open |
| Windows | chocolatey | manual | start |

### Paper Format

The paper uses **Pandoc Markdown** with:
- YAML frontmatter for metadata (title, author, abstract)
- BibTeX citations: `[@citation_key]`
- Standard academic structure with numbered sections
- LaTeX PDF output via pdflatex

## Research Focus

### Core Research Question
> "What is the smallest LLM that can reliably classify clinical findings and generate appropriate clinical actions?"

### Context Engineering Strategies Evaluated
1. **Zero-Shot** — Instructions only (baseline)
2. **Few-Shot** — 1-5 curated examples in prompt
3. **RAG** — Retrieved guidelines/similar cases
4. **Long-Context** — Full context where window permits

### Key Requirements
- High accuracy (medical correctness critical)
- Data sovereignty (on-device/local deployment)
- German language support (GraSCCo corpus)
- Small footprint (edge devices, WebLLM)

## Development Guidelines

### When Working on This Project

1. **Paper content** is in `paper/paper.md` - edit there for academic content
2. **Build from paper/ directory** - `cd paper && task build`
3. **Use synthetic data only** - never commit real patient information
4. **Citations** go in `paper/references.bib` (BibTeX format)

### File Naming Conventions
- Markdown files: lowercase with hyphens (`few-shot-learning.md`)
- Data files: descriptive names (`x-ray-test-set.json`)
- Configuration: lowercase (`defaults.yaml`)

### Git Workflow
```bash
# Atomic commits with descriptive messages
git commit -m "feat(paper): add methodology section"
git commit -m "docs(research): literature review on scaling laws"
git commit -m "data(evaluation): add golden test set for lab reports"
```

## Key Documents

- **[paper/paper.md](paper/paper.md)** — Main academic paper
- **[paper/project.md](paper/project.md)** — Detailed project plan & timeline
- **[paper/README.md](paper/README.md)** — Paper-specific overview
- **[paper/research/](paper/research/)** — Literature review notes
