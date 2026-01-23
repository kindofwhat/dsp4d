# GEMINI.md - DSP4D Project Guide

## Project Overview

**DSP4D (Data Sovereignty Procedures for Doctors)** is a research project investigating the optimal LLM size for medical document classification using context engineering strategies.

- **Objective:** Find the smallest LLM for reliable clinical intent classification.
- **Institution:** Bern University of Applied Sciences (BFH).
- **Dataset:** GraSCCo (German clinical texts).

## Development Commands

All paper-related tasks must be executed from the `paper/` directory.

### Build Tasks
- **Full Build (PDF):** `task build`
- **Fast Build (Draft):** `task build-draft`
- **Word Export:** `task build-word`
- **HTML Export:** `task build-html`
- **Watch Mode:** `task watch` (Auto-rebuilds on file changes)

### Setup & Maintenance
- **Initial Setup:** `task setup` (Installs Pandoc and BasicTeX)
- **LaTeX Setup:** `task setup-latex` (Installs required LaTeX packages)
- **Open Output:** `task open`
- **Clean Project:** `task clean`

## Project Structure (Paper Directory)

```
paper/
├── GEMINI.md             # This file
├── README.md             # Paper-specific overview
├── Taskfile.yml          # Build automation
├── defaults.yaml         # Pandoc configuration
├── references.bib        # BibTeX bibliography
├── chapters/             # Content sections
│   ├── 00-frontmatter/   # Title, Abstract, Metadata
│   ├── 01-introduction/  # Introduction
│   ├── 02-theory/        # Theoretical background
│   ├── 03-methodology/   # Research design
│   ├── 04-results/       # Findings
│   ├── 05-discussion/    # Analysis
│   └── 99-backmatter/    # Appendices, etc.
├── assets/               # Images and figures
├── templates/            # LaTeX templates
└── output/               # Generated documents (gitignored)
```

## Writing & Style Guidelines

### Content Standards
- **Language:** Academic German (consistent with GraSCCo context).
- **Format:** Pandoc-flavored Markdown.
- **Citations:** Use BibTeX keys from `references.bib` with `[@key]` syntax.
- **Figures:** Place in `assets/` and use relative paths.

### Academic Rigor
- Maintain consistency in technical terms: *LLM*, *GraSCCo*, *Context Engineering*, *Data Sovereignty*.
- Focus on the core research question: "What is the smallest LLM that can reliably classify clinical findings?"
- Ensure all claims are supported by the research plan in `project.md`.

## Metadata & Configuration
- **Frontmatter:** Managed in `chapters/00-frontmatter/metadata.yaml`.
- **Pandoc Settings:** Defined in `defaults.yaml`.
- **Reference Styles:** Controlled via `Thesisvorlage.docx` or `reference-styles.docx` (if present).

## Operational Guidelines for Gemini
- **Context Awareness:** Always check `project.md` for the latest research goals.
- **Atomic Commits:** Prefer small, focused commits (e.g., `feat(paper): update methodology`, `fix(refs): correct bib entry`).
- **Data Privacy:** Never include real patient data; use only the synthetic GraSCCo corpus.
- **Cross-Platform:** The `Taskfile.yml` handles OS differences; rely on it for builds.