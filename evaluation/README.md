# Evaluation Framework

**Goal:** Measure classification accuracy, action appropriateness, and identify model breakpoints

## Overview

This directory contains test datasets, evaluation metrics, and baseline performance measurements for assessing LLM performance on medical document classification and action generation.

## Directory Structure

```
evaluation/
├── README.md                          # This file
├── test-datasets/                     # Golden test sets
│   ├── x-ray-test-set.json           # 50 test cases
│   ├── lab-test-set.json
│   ├── imaging-test-set.json
│   ├── prescription-test-set.json
│   ├── referral-test-set.json
│   └── mixed-test-set.json           # All types mixed (realistic)
├── metrics/                           # Evaluation metrics
│   ├── classification-accuracy.md    # Document type classification
│   ├── action-correctness.md         # Is action appropriate?
│   ├── clinical-safety.md            # Safety/harm metrics
│   └── urgency-accuracy.md           # Correct urgency level?
└── baselines/                         # Baseline performance
    ├── human-performance.md          # Medical expert accuracy
    ├── commercial-models.md          # GPT-4, Claude performance
    └── random-baseline.md            # Random guessing baseline
```

## Test Dataset Schema

Each test set is a JSON array of test cases:

```json
[
  {
    "id": "xray_test_001",
    "document_type": "x-ray-result",
    "input": {
      "report": "[Full report text]",
      "patient_age": 45,
      "study_date": "2024-11-15"
    },
    "ground_truth": {
      "classification": "x-ray-result",
      "urgency": "URGENT",
      "findings": "Comminuted distal radius fracture",
      "action": "URGENT: Schedule orthopedic surgery consultation within 48 hours",
      "action_category": "surgery-consult",
      "reasoning": "Displaced fracture requires surgical intervention"
    },
    "difficulty": "easy",
    "tags": ["fracture", "urgent", "clear-cut"],
    "annotator": "medical_expert_1",
    "annotation_date": "2024-11-15"
  }
]
```

## Evaluation Metrics

### 1. Classification Accuracy

**Metric:** Percentage of correctly classified document types

```python
classification_accuracy = correct_classifications / total_tests
```

**Target:** >95% for production deployment

**Breakdown:**
- Overall accuracy
- Per document type accuracy
- Confusion matrix (which types get confused?)

### 2. Urgency Accuracy

**Metric:** Percentage of correct urgency level assignments

```python
urgency_accuracy = correct_urgency_levels / total_tests
```

**Levels:** URGENT, HIGH, MEDIUM, LOW, NONE

**Critical:** Missing URGENT cases is worse than over-triaging
- False negatives (missed urgent): **-10 points**
- False positives (unnecessary urgent): **-1 point**
- Correct classification: **+1 point**

### 3. Action Appropriateness

**Metric:** Medical expert rates each action as:
- **Appropriate** (1.0): Correct action
- **Suboptimal** (0.5): Not harmful but not ideal
- **Inappropriate** (0.0): Could cause harm or delay care
- **Dangerous** (-1.0): Could cause serious harm

```python
action_score = sum(expert_ratings) / total_tests
```

**Target:** >0.9 (90% appropriate actions)

### 4. Clinical Safety Score

**Critical Failures:**
- Missing urgent findings (e.g., fracture marked as "no action")
- Dangerous recommendations (e.g., "no action" for critical lab values)
- Incorrect specialist (e.g., dermatology for cardiac issue)

```python
safety_score = 1.0 - (critical_failures / total_tests)
```

**Target:** 1.0 (zero critical failures)

### 5. Latency & Throughput

**Metrics:**
- p50 latency (median response time)
- p95 latency (95th percentile)
- p99 latency (99th percentile)
- Throughput (documents per second)

**Target:** <2 seconds p95 latency

## Test Dataset Requirements

### Size
- **50 test cases per document type** (minimum)
- **250+ total test cases** across 5 types
- **Mixed test set**: 100 randomly sampled from all types (realistic distribution)

### Distribution
- **Difficulty:**
  - 30% easy (clear-cut findings)
  - 50% medium (some interpretation needed)
  - 20% hard (ambiguous, multiple findings)

- **Urgency:**
  - 15% URGENT
  - 20% HIGH
  - 30% MEDIUM
  - 25% LOW
  - 10% NONE

### Quality Criteria
- [ ] All test cases validated by medical expert
- [ ] Ground truth actions are medically appropriate
- [ ] Diverse findings represented
- [ ] Edge cases included
- [ ] No overlap with few-shot examples (data leakage)

## Baseline Performance

### Human Performance (Medical Expert)

**Goal:** Establish upper bound

- Medical expert classifies same test set
- Measure accuracy, action appropriateness
- Document time per document
- Identify cases where expert is uncertain

**Expected:** 95-98% accuracy (experts occasionally disagree)

### Commercial Models

**Goal:** Establish high-quality baseline

Test with:
- GPT-4o-mini
- Claude 3 Haiku
- Gemini Flash

**Expected:** 90-95% accuracy for this task

### Random Baseline

**Goal:** Establish lower bound

- Random document type selection
- Random urgency level
- Random action from valid set

**Expected:** ~20% accuracy (5 document types)

## Breakpoint Analysis

### What to Measure

**Classification Task:**
- At what model size does accuracy drop below 95%?
- At what model size does accuracy drop below 80%?
- Where is the steepest drop?

**Action Generation:**
- At what model size do dangerous actions appear?
- At what model size is action appropriateness <90%?

**Example Breakpoint Hypothesis:**
- 13B models: >95% accuracy
- 7B models: 90-95% accuracy
- 3B models: 80-90% accuracy ← **Likely breakpoint**
- 1B models: <80% accuracy ← **Too small**

### Failure Analysis

For each failed test case:
- **Model size:** Which models failed?
- **Failure type:** Misclassification, wrong urgency, inappropriate action?
- **Pattern:** Is there a pattern in failures? (complexity, document type, finding type)
- **Fix:** Could few-shot examples be improved? Need more examples?

## Evaluation Workflow

### 1. Preparation
- [ ] Create 50 test cases per document type (250 total)
- [ ] Medical expert validates all test cases
- [ ] Create mixed test set (realistic distribution)
- [ ] Implement evaluation scripts

### 2. Baseline Testing
- [ ] Test commercial models (GPT-4, Claude)
- [ ] Medical expert completes test set
- [ ] Random baseline
- [ ] Document baseline performance

### 3. Model Testing
- [ ] Test all model sizes (1B, 3B, 7B, 13B)
- [ ] Test all deployment types (WebLLM, local, hosted, commercial)
- [ ] Collect latency/throughput metrics
- [ ] Save all predictions for analysis

### 4. Analysis
- [ ] Calculate all metrics per model
- [ ] Identify breakpoints
- [ ] Failure analysis
- [ ] Statistical significance testing

### 5. Reporting
- [ ] Performance matrix (model × metric)
- [ ] Breakpoint visualization
- [ ] Failure pattern analysis
- [ ] Recommendations

## Evaluation Scripts

### Example: Classification Accuracy

```python
def evaluate_classification(predictions, ground_truth):
    """
    Calculate classification accuracy
    """
    correct = sum([
        1 for pred, gt in zip(predictions, ground_truth)
        if pred['classification'] == gt['classification']
    ])
    return correct / len(predictions)

def evaluate_urgency(predictions, ground_truth):
    """
    Calculate urgency accuracy with penalties
    """
    score = 0
    for pred, gt in zip(predictions, ground_truth):
        if pred['urgency'] == gt['urgency']:
            score += 1
        elif gt['urgency'] == 'URGENT' and pred['urgency'] != 'URGENT':
            score -= 10  # Critical failure
        else:
            score -= 0.5  # Minor error
    return max(0, score) / len(predictions)
```

## Task Checklist

- [ ] Create test datasets (50 per type × 5 types = 250 cases)
- [ ] Medical expert validation
- [ ] Document evaluation metrics
- [ ] Implement evaluation scripts
- [ ] Establish baselines (human, commercial, random)
- [ ] Run experiments across model sizes
- [ ] Analyze results and identify breakpoints
- [ ] Document findings

## Notes

- **Synthetic data only**: All test cases must be synthetic/anonymized
- **Expert validation required**: Medical professional must validate all ground truth
- **Statistical rigor**: Multiple runs per configuration
- **Reproducibility**: Version control all test sets
- **Clinical focus**: Prioritize safety over raw accuracy
