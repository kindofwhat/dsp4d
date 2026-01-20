# Context Examples & RAG Corpus

**Goal:** Create high-quality input-output pairs per document type to serve as context for various engineering strategies.

## Overview

This directory contains curated examples that serve multiple purposes in our context engineering experiments:
1.  **Few-Shot / One-Shot:** Examples provided directly in the prompt.
2.  **RAG Knowledge Base:** A corpus of "past cases" that can be retrieved dynamically based on similarity.
3.  **Fine-Tuning Data:** (Optional) Potential dataset for future fine-tuning experiments.

**Approach:**
- **High Quality:** Each example validated by a medical expert.
- **Diverse:** Cover common cases, edge cases, and urgency levels.
- **Structured:** Stored in JSON for programmatic access by any strategy.

## Directory Structure

```
few-shot-examples/
├── README.md                          # This file
├── x-ray-results/
│   ├── examples.json                 # 10-20 input-output pairs
│   ├── selection-strategy.md         # How to pick 3-5 examples
│   └── prompt-template.md            # Prompt format with examples
├── lab-reports/
│   ├── examples.json
│   ├── selection-strategy.md
│   └── prompt-template.md
├── imaging-reports/
│   ├── examples.json
│   ├── selection-strategy.md
│   └── prompt-template.md
├── prescriptions/
│   ├── examples.json
│   ├── selection-strategy.md
│   └── prompt-template.md
└── referrals/
    ├── examples.json
    ├── selection-strategy.md
    └── prompt-template.md
```

## Example JSON Schema

Each `examples.json` file contains an array of input-output pairs:

```json
[
  {
    "id": "xray_001",
    "document_type": "x-ray-result",
    "input": {
      "report": "FINDINGS: Comminuted fracture of the distal radius with dorsal angulation. No evidence of carpal bone injury. Soft tissues unremarkable.",
      "patient_age": 45,
      "study_date": "2024-11-15"
    },
    "output": {
      "classification": "x-ray-result",
      "urgency": "URGENT",
      "findings": "Comminuted distal radius fracture",
      "action": "URGENT: Schedule orthopedic surgery consultation within 48 hours. Patient requires surgical evaluation for fracture stabilization.",
      "reasoning": "Displaced fracture requires surgical intervention to prevent complications and restore function."
    },
    "difficulty": "easy",
    "tags": ["fracture", "urgent", "surgery-required"]
  },
  {
    "id": "xray_002",
    "document_type": "x-ray-result",
    "input": {
      "report": "FINDINGS: No acute fracture or dislocation. Mild degenerative changes of the AC joint. Rotator cuff muscles grossly intact.",
      "patient_age": 58,
      "study_date": "2024-11-15"
    },
    "output": {
      "classification": "x-ray-result",
      "urgency": "LOW",
      "findings": "Mild degenerative AC joint changes",
      "action": "Schedule routine orthopedic consultation within 4-6 weeks if symptoms persist. Consider physical therapy referral.",
      "reasoning": "Degenerative changes are chronic and do not require urgent intervention. Symptomatic management is appropriate."
    },
    "difficulty": "easy",
    "tags": ["normal-variant", "routine", "degenerative"]
  }
]
```

## Example Selection Strategy

### Static vs Dynamic Selection

**Static (simpler):**
- Always use the same 3-5 examples per document type
- Pros: Consistent, reproducible, faster
- Cons: May not be optimal for edge cases

**Dynamic (better performance):**
- Select 3-5 most similar examples based on input document
- Similarity metrics: TF-IDF, sentence embeddings, keyword matching
- Pros: Better context for edge cases, higher accuracy
- Cons: Requires embedding model, more complex

### Recommended Approach

**Hybrid:**
1. Start with static examples (baseline performance)
2. Implement dynamic selection
3. Compare performance (static vs dynamic)
4. Document improvement (or lack thereof)

### Selection Criteria

When selecting examples dynamically:
- **Similarity**: Most similar to input document (cosine similarity)
- **Diversity**: Cover different urgency levels (URGENT, HIGH, LOW, NONE)
- **Difficulty**: Include both clear-cut and ambiguous cases
- **Coverage**: Ensure all major finding types represented

## Prompt Template Structure

Each `prompt-template.md` documents the prompt format:

```markdown
# Prompt Template for [Document Type]

## System Prompt

You are a medical document classification assistant. Your task is to:
1. Classify the document type
2. Identify key findings
3. Determine urgency level
4. Recommend appropriate clinical action

You must be accurate and err on the side of caution - when in doubt, escalate urgency.

## Few-Shot Examples Format

Here are some examples of [document type] classification and action generation:

**Example 1:**
Input: [Document text]
Output:
- Classification: [Type]
- Urgency: [Level]
- Findings: [Key findings]
- Action: [Recommended action]
- Reasoning: [Clinical justification]

**Example 2:**
[...]

**Example 3:**
[...]

## User Prompt

Now classify this document and recommend appropriate action:

[Input document]

Output format:
- Classification:
- Urgency:
- Findings:
- Action:
- Reasoning:
```

## Quality Guidelines

### Input Documents
- **Realistic**: Based on actual medical report formats (anonymized)
- **Complete**: Include all relevant information
- **Varied**: Different findings, urgency levels, complexity
- **Unambiguous**: Clear enough for consistent annotation

### Output Actions
- **Specific**: "Schedule orthopedic surgery consult within 48h" not "See doctor"
- **Actionable**: Clear next step that can be executed
- **Safe**: Medically appropriate and conservative when uncertain
- **Justified**: Reasoning explains why this action is recommended

### Difficulty Levels

- **Easy**: Clear-cut findings, obvious action
  - Example: "Acute fracture" → "Urgent surgery consult"
- **Medium**: Some interpretation needed
  - Example: "Suspicious nodule" → "Follow-up imaging vs specialist"
- **Hard**: Ambiguous findings, multiple factors
  - Example: "Incidental finding in asymptomatic patient" → Action depends on age, history, risk factors

## Task Checklist

### Per Document Type

- [ ] Create 10-20 high-quality examples
  - [ ] 5 easy examples
  - [ ] 10 medium examples
  - [ ] 5 hard examples
- [ ] Validate with medical expert
- [ ] Document selection strategy
- [ ] Create prompt template
- [ ] Test prompt with sample LLM

### Example Distribution

Each document type should include:
- [ ] URGENT cases (20%)
- [ ] HIGH priority cases (20%)
- [ ] MEDIUM priority cases (30%)
- [ ] LOW priority cases (20%)
- [ ] NO ACTION cases (10%)

### Quality Validation

- [ ] Medical expert reviews all examples
- [ ] Actions are clinically appropriate
- [ ] Reasoning is medically sound
- [ ] Examples cover common scenarios
- [ ] Edge cases are included

## Notes

- **Synthetic only**: Use only synthetic/anonymized data
- **Expert validation required**: All examples must be reviewed by medical professional
- **Consistent format**: All examples follow same JSON schema
- **Versioning**: Track example sets with version numbers (v1.0, v1.1, etc.)
- **Iterative improvement**: Update examples based on model performance

## Resources

- Few-shot learning best practices
- Medical report formatting guidelines
- Clinical decision support systems
- Prompt engineering techniques
