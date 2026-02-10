# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DSP4D (Data Sovereignty Procedures for Doctors)** — BFH research project investigating the optimal LLM size for medical document classification using context engineering strategies (Zero-Shot, Few-Shot, RAG, Long-Context). Dataset: GraSCCo (German clinical texts).

## Build Commands

All paper builds require [Task](https://taskfile.dev/) and run from the `paper/` directory:

```bash
cd paper
task setup            # First-time: install pandoc + LaTeX
task setup-latex      # First-time: install LaTeX packages (new terminal after setup)
task build            # Full PDF build with citations
task build-draft      # Fast PDF without citations
task build-word       # Word document (uses reference-styles.docx template)
task build-html       # HTML version
task watch            # Auto-rebuild on .md/.yaml/.bib changes
task open             # Open generated PDF
task clean            # Remove output/
```

Output goes to `paper/output/dsp4d-paper.pdf` (gitignored).

## CI/CD

GitHub Actions (`.github/workflows/publish.yml`) builds the PDF on push to `main`/`master`/`doc/paper` and deploys to GitHub Pages. Published at: https://kindofwhat.github.io/dsp4d/dsp4d-paper.pdf

## Paper Architecture

The paper uses **Pandoc Markdown** compiled to PDF via pdflatex with a custom BFH thesis template.

**Build pipeline:** `defaults.yaml` defines input files, template, and citation config. Chapters are concatenated in order:

```
paper/
├── defaults.yaml                    # Pandoc config (input file order, template, bibliography)
├── templates/bfh-thesis.tex         # Custom LaTeX template (BFH Thesisvorlage)
├── references.bib                   # BibTeX bibliography
├── references/                      # Downloaded PDFs of cited papers
├── download_refs.py                 # Script to bulk-download reference PDFs from arXiv/URLs
├── chapters/
│   ├── 00-frontmatter/metadata.yaml # Title, authors, abstract, thesis metadata
│   ├── 01-introduction/index.md
│   ├── 02-theory/index.md
│   ├── 03-methodology/index.md
│   ├── 04-results/index.md
│   ├── 05-discussion/index.md
│   ├── 98-critical-evaluation/      # Exists but not in defaults.yaml input list
│   └── 99-backmatter/index.md
└── assets/                          # Images (bfh-logo.jpg, diagrams)
```

**Key detail:** Chapter order is controlled by `defaults.yaml` `input-files` list, NOT by directory naming. To add a chapter, both the file and the `defaults.yaml` entry are needed. Note that `98-critical-evaluation/` exists on disk but is not currently included in the build.

**Citations:** BibTeX format in `references.bib`, referenced as `[@citation_key]` in markdown. Processed by pandoc-citeproc.

**Language:** Paper metadata sets `lang: de-CH` (Swiss German).

## Reference Management

`paper/download_refs.py` downloads PDFs for all references in `references.bib`:
- Resolves arXiv IDs, explicit URLs, and manual mappings
- Saves to `paper/references/` directory
- Run: `cd paper && python download_refs.py`

## File Conventions

- Markdown files: lowercase with hyphens (`few-shot-learning.md`)
- Chapters: numbered directories with `index.md` entry point
- Commit format: `<type>(<scope>): <subject>` (e.g., `feat(paper): add methodology section`)
