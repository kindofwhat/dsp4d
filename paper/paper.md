---
# =============================================================================
# BFH Thesis Metadata
# =============================================================================
title: "Optimal LLM Size for Medical Document Classification Using Context Engineering"
subtitle: "Data Sovereignty Procedures for Doctors (DSP4D)"

# Author information
author:
  - Christian Haegler

# BFH-specific metadata
thesis-type: "Semesterarbeit"
studiengang: "CAS Generative KI"
betreuer: "[Betreuer einfügen]"
auftraggeber: "[Auftraggeber einfügen]"
experte: "[Experte einfügen]"
date: "2025"

# Department shown in footer
department: "Departement Technik und Informatik"

# Assets
logo: "assets/bfh-logo.jpg"
# cover-image: "assets/cover.jpg"  # Optional cover image

# Document options
toc: true
declaration: true

# Abstract / Management Summary
abstract: |
  This paper investigates the minimum viable Large Language Model (LLM) size
  required for reliable medical document classification and clinical action
  generation. We evaluate multiple context engineering strategies—including
  few-shot learning, retrieval-augmented generation (RAG), and long-context
  approaches—to determine optimal trade-offs between model size, inference
  cost, and clinical accuracy. Our experiments focus on edge deployment
  scenarios where data sovereignty requirements mandate local processing.

  **Keywords:** Large Language Models, Few-Shot Learning, Medical Document
  Classification, Edge Deployment, Data Sovereignty
---

# Introduction

Doctors face an increasing volume of medical documents requiring timely review
and action. After office hours, the challenge of efficiently processing X-ray
results, lab reports, and specialist referrals becomes critical for patient care.

This research addresses a fundamental question: *What is the smallest LLM that
can reliably classify medical documents and generate appropriate clinical
actions?*

## Motivation

<!-- Describe the problem and why it matters -->

## Research Questions

1. What is the minimum model size for reliable document classification (>95% accuracy)?
2. How do different context engineering strategies affect the size-accuracy trade-off?
3. Can sub-3B parameter models achieve clinical safety standards with appropriate context?

# Theory / State of Research

## Large Language Models and Scaling Laws

<!-- Background on LLM capabilities and how they scale with size -->

## Context Engineering Strategies

### Few-Shot Learning

In-context learning enables models to perform tasks by conditioning on
examples provided in the prompt [@brown2020language].

### Retrieval-Augmented Generation

<!-- RAG background -->

### Long-Context Approaches

<!-- Long context windows background -->

## Medical Document Processing and German Clinical NLP

<!-- Prior work on medical NLP, specifically referencing GraSCCo -->

# Methodology

## Data Source: GraSCCo

Instead of generic document types, this research utilizes the **Graz Synthetic Clinical text Corpus (GraSCCo)** [@GraSCCo_PII_V2_2025; @modersohn2022grascco]. GraSCCo is the first publicly shareable, multiply-alienated German clinical text corpus, designed specifically for clinical NLP tasks without compromising patient privacy.

The corpus provides a diverse set of clinical scenarios, which we use to evaluate the models' ability to classify document intent and generate appropriate clinical actions based on German-language clinical narratives.

## Experimental Setup

### Models Evaluated

| Model | Parameters | Deployment |
|-------|------------|------------|
| Llama 3.2 | 1B | Edge/WebLLM |
| Llama 3.2 | 3B | Edge |
| Phi-3 Mini | 3.8B | Edge/WebLLM |
| Llama 3.1 | 7B | Hosted |

### Context Strategies

1. **Zero-Shot** — Instructions only (baseline)
2. **One-Shot** — Single example
3. **Few-Shot** — 3-5 curated examples
4. **RAG** — Retrieved guidelines/similar cases

## Evaluation Metrics

- **Classification Accuracy** — Correct document type identification
- **Action Appropriateness** — Clinical validity of suggested actions
- **Latency** — Inference time on target hardware

# Results

## Classification Task

<!-- Results of document classification experiments -->

## Action Generation Task

<!-- Results of clinical action generation experiments -->

### Breakpoint Analysis

<!-- Where do models fail? At what complexity? -->

### Size vs. Accuracy Trade-offs

<!-- Main findings with tables and figures -->

## Impact of Context Engineering

<!-- How much does few-shot/RAG help smaller models? -->

## Deployment Viability

<!-- Can these models run on Raspberry Pi, in browser? -->

# Discussion / Conclusion

## Implications for Clinical Practice

<!-- What does this mean for doctors? -->

## Limitations

<!-- Study limitations -->

## Future Work

<!-- Next steps -->

# List of Figures {.unnumbered}

<!-- Will be auto-generated if using proper figure captions -->

# List of Tables {.unnumbered}

<!-- Will be auto-generated if using proper table captions -->

# Glossary {.unnumbered}

**Context Engineering**
: The practice of designing prompts and providing relevant information to improve LLM performance on specific tasks.

**Edge Deployment**
: Running machine learning models locally on devices rather than in the cloud.

**Few-Shot Learning**
: Providing a small number of examples in the prompt to guide model behavior.

**GraSCCo**
: Graz Synthetic Clinical text Corpus — a German clinical text corpus for NLP research.

**RAG (Retrieval-Augmented Generation)**
: A technique that combines information retrieval with text generation to improve accuracy.

# References {.unnumbered}

::: {#refs}
:::

# Appendix {.unnumbered}

<!-- Additional materials, detailed results, code snippets -->

## A. Prompt Templates {.unnumbered}

<!-- Example prompts used in experiments -->

## B. Detailed Results {.unnumbered}

<!-- Extended result tables -->
