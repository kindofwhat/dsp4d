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


<!-- CLAVIX:START -->
## Clavix Integration

This project uses Clavix for prompt improvement and PRD generation. The following slash commands are available:

> **Command Format:** Commands shown with colon (`:`) format. Some tools use hyphen (`-`): Claude Code uses `/clavix:improve`, Cursor uses `/clavix-improve`. Your tool autocompletes the correct format.

### Prompt Optimization

#### /clavix:improve [prompt]
Optimize prompts with smart depth auto-selection. Clavix analyzes your prompt quality and automatically selects the appropriate depth (standard or comprehensive). Use for all prompt optimization needs.

### PRD & Planning

#### /clavix:prd
Launch the PRD generation workflow. Clavix will guide you through strategic questions and generate both a comprehensive PRD and a quick-reference version optimized for AI consumption.

#### /clavix:plan
Generate an optimized implementation task breakdown from your PRD. Creates a phased task plan with dependencies and priorities.

#### /clavix:implement
Execute tasks or prompts with AI assistance. Auto-detects source: tasks.md (from PRD workflow) or prompts/ (from improve workflow). Supports automatic git commits and progress tracking.

Use `--latest` to implement most recent prompt, `--tasks` to force task mode.

### Session Management

#### /clavix:start
Enter conversational mode for iterative prompt development. Discuss your requirements naturally, and later use `/clavix:summarize` to extract an optimized prompt.

#### /clavix:summarize
Analyze the current conversation and extract key requirements into a structured prompt and mini-PRD.

### Refinement

#### /clavix:refine
Refine existing PRD or prompt through continued discussion. Detects available PRDs and saved prompts, then guides you through updating them with tracked changes.

### Agentic Utilities

These utilities provide structured workflows for common tasks. Invoke them using the slash commands below:

- **Verify** (`/clavix:verify`): Check implementation against PRD requirements. Runs automated validation and generates pass/fail reports.
- **Archive** (`/clavix:archive`): Archive completed work. Moves finished PRDs and outputs to archive for future reference.

**When to use which mode:**
- **Improve mode** (`/clavix:improve`): Smart prompt optimization with auto-depth selection
- **PRD mode** (`/clavix:prd`): Strategic planning with architecture and business impact

**Recommended Workflow:**
1. Start with `/clavix:prd` or `/clavix:start` for complex features
2. Refine requirements with `/clavix:refine` as needed
3. Generate tasks with `/clavix:plan`
4. Implement with `/clavix:implement`
5. Verify with `/clavix:verify`
6. Archive when complete with `/clavix:archive`

**Pro tip**: Start complex features with `/clavix:prd` or `/clavix:start` to ensure clear requirements before implementation.
<!-- CLAVIX:END -->
