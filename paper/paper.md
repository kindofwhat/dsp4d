---
title: "Optimal LLM Size for Medical Document Classification Using Context Engineering"
subtitle: "Data Sovereignty Procedures for Doctors (DSP4D)"
author:
  - name: Your Name
    affiliation: Bern University of Applied Sciences (BFH)
    email: your.email@bfh.ch
date: 2025
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

## Contributions

- A systematic evaluation framework for medical document classification with LLMs
- Comparative analysis of context engineering strategies (few-shot, RAG, long-context)
- Practical deployment recommendations for edge devices

# Background

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

## Medical Document Processing

<!-- Prior work on medical NLP -->

# Methodology

## Document Types

We evaluate five medical document categories:

1. **X-Ray Results** — Radiology reports with findings
2. **Lab Reports** — Blood work, urinalysis, cultures
3. **Medical Imaging** — CT, MRI, ultrasound reports
4. **Prescriptions** — Medication orders
5. **Referrals** — Specialist consultation requests

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

# Experiments

## Classification Task

<!-- Results of document classification experiments -->

## Action Generation Task

<!-- Results of clinical action generation experiments -->

## Breakpoint Analysis

<!-- Where do models fail? At what complexity? -->

# Results

## Size vs. Accuracy Trade-offs

<!-- Main findings with tables and figures -->

## Impact of Context Engineering

<!-- How much does few-shot/RAG help smaller models? -->

## Deployment Viability

<!-- Can these models run on Raspberry Pi, in browser? -->

# Discussion

## Implications for Clinical Practice

<!-- What does this mean for doctors? -->

## Limitations

<!-- Study limitations -->

## Future Work

<!-- Next steps -->

# Conclusion

<!-- Summary of findings and recommendations -->

# References

::: {#refs}
:::
