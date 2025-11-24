# DSP4D: Optimal LLM Size for Medical Document Classification & Action Generation

**Data Sovereignty Procedures for Doctors (DSP4D)**

Finding the minimum viable LLM size for classifying medical documents and generating appropriate clinical actions using few-shot prompting.

## Project Overview

**Duration:** 3 months (13 weeks)
**Total Effort:** 100 hours
**Institution:** Bern University of Applied Sciences (BFH)

### Core Research Question

> **"What is the smallest LLM that can reliably classify medical documents and generate appropriate clinical actions using few-shot prompting?"**

### The Challenge

Doctors are overwhelmed with medical documents after hours. They need a system that can:
1. **Identify document type** (X-ray result, lab report, imaging report, prescription, referral)
2. **Extract key information** (diagnosis, findings, urgency)
3. **Generate appropriate action** (schedule surgery, order follow-up, refer to specialist)

**Critical Requirements:**
- **High accuracy** (medical correctness is critical)
- **Data sovereignty** (on-device/local deployment, no cloud)
- **Fast inference** (real-time assistance)
- **Small footprint** (edge devices, Raspberry Pi, WebLLM in browser)

### Approach: Few-Shot Prompting

Instead of RAG, we use **few-shot learning**:
- Provide 3-5 examples per document type in the prompt
- Examples include: input document → expected output action
- **Dynamic selection**: Choose most relevant examples based on document similarity

**Example:**
```
You are a medical document assistant. Classify the document and suggest appropriate action.

Examples:
1. [X-ray result showing fracture] → "URGENT: Schedule orthopedic surgery consultation within 48 hours"
2. [X-ray result normal] → "No action required. File in patient record."
3. [X-ray result suspicious mass] → "Schedule CT scan and oncology referral within 1 week"

Now classify this document:
[New X-ray result]
```

## Project Structure

```
dsp4d/
├── README.md                          # This file
├── project.md                         # Detailed project plan
│
├── research/                          # Background research
│   ├── few-shot-learning/            # Few-shot learning techniques
│   │   ├── few-shot-classification.md
│   │   ├── prompt-engineering.md
│   │   └── example-selection.md      # Dynamic vs static examples
│   ├── model-size-studies/           # Model size vs performance
│   │   ├── classification-tasks.md
│   │   └── small-model-capabilities.md
│   └── existing-work/                # Prior research
│       └── existing-work.md          # LLM size research (from old structure)
│
├── document-types/                    # 5-10 medical document types
│   ├── definitions/                  # What each type is
│   │   ├── x-ray-results.md
│   │   ├── lab-reports.md
│   │   ├── imaging-reports.md        # CT, MRI, ultrasound
│   │   ├── prescriptions.md
│   │   └── referrals.md
│   └── workflows/                    # Type → Action mappings
│       ├── x-ray-workflow.md         # X-ray → surgery/follow-up/nothing
│       ├── lab-workflow.md           # Lab → medication/repeat/specialist
│       └── imaging-workflow.md       # Imaging → surgery/monitoring/specialist
│
├── few-shot-examples/                 # Example sets per document type
│   ├── x-ray-results/
│   │   ├── examples.json             # 10-20 input-output pairs
│   │   ├── selection-strategy.md     # How to pick 3-5 examples
│   │   └── prompt-template.md        # Prompt format with examples
│   ├── lab-reports/
│   ├── imaging-reports/
│   ├── prescriptions/
│   └── referrals/
│
├── evaluation/                        # Testing framework
│   ├── test-datasets/                # Golden test sets
│   │   ├── x-ray-test-set.json      # 50 test cases
│   │   ├── lab-test-set.json
│   │   └── mixed-test-set.json      # All types mixed
│   ├── metrics/                      # Evaluation metrics
│   │   ├── classification-accuracy.md
│   │   ├── action-correctness.md    # Is suggested action appropriate?
│   │   └── clinical-safety.md       # Safety/harm metrics
│   └── baselines/                    # Baseline performance
│       └── human-performance.md     # What accuracy do doctors achieve?
│
├── models/                            # Model configurations
│   ├── webllm/                       # Browser-based (WebLLM)
│   │   ├── phi-3-mini.yaml
│   │   └── llama-3.2-1b.yaml
│   ├── local-edge/                   # Raspberry Pi, edge devices
│   │   ├── llama-3.2-1b.yaml
│   │   ├── llama-3.2-3b.yaml
│   │   └── phi-3-small.yaml
│   ├── hosted-free/                  # Groq, Together, Fireworks
│   │   ├── llama-3.1-7b.yaml
│   │   └── mistral-7b.yaml
│   └── commercial/                   # OpenAI, Claude, Gemini
│       ├── gpt-4o-mini.yaml
│       └── claude-3-haiku.yaml
│
├── experiments/                       # Finding breakpoints
│   ├── classification/               # Document type classification
│   │   ├── run-classification.py
│   │   └── results/
│   ├── generation/                   # Action generation quality
│   │   ├── run-generation.py
│   │   └── results/
│   ├── breakpoint-analysis/          # Where do models fail?
│   │   ├── analyze-failures.ipynb
│   │   └── failure-patterns.md
│   └── results/                      # Consolidated results
│       └── performance-matrix.csv
│
└── analysis/                          # Final analysis
    ├── performance/                  # Accuracy vs model size
    │   ├── size-vs-accuracy.ipynb
    │   └── cost-benefit.md
    ├── deployment/                   # Deployment recommendations
    │   ├── webllm-guide.md
    │   ├── raspberry-pi-guide.md
    │   └── hosted-comparison.md
    └── recommendations/              # Final recommendations
        ├── final-report.md
        └── deployment-matrix.md
```

## Document Types (5-10 Types)

### 1. X-Ray Results
**Input:** Radiology report with findings
**Actions:**
- URGENT: Schedule surgery (fractures, acute findings)
- Schedule specialist consultation (suspicious findings)
- Order follow-up X-ray (monitoring needed)
- No action required (normal findings)

### 2. Lab Reports
**Input:** Blood work, urinalysis, cultures
**Actions:**
- URGENT: Hospitalize (critical values)
- Adjust medication (abnormal but manageable)
- Schedule follow-up labs (monitoring)
- No action required (normal values)

### 3. Medical Imaging Reports (CT/MRI/Ultrasound)
**Input:** Detailed imaging study
**Actions:**
- Schedule surgery (operable findings)
- Refer to specialist (oncology, neurology, etc.)
- Schedule follow-up imaging (monitoring)
- No action required

### 4. Prescriptions
**Input:** Medication prescription
**Actions:**
- Approve and send to pharmacy
- Request clarification (drug interactions, allergies)
- Deny and suggest alternative
- Forward to specialist

### 5. Referrals (to be expanded to 10 types)
**Input:** Specialist referral request
**Actions:**
- Approve referral
- Request additional tests first
- Deny and manage in primary care
- Redirect to different specialist

## Model Deployment Types

### 1. WebLLM (Browser-Based)
- **Models:** Phi-3-mini (3.8B), Llama 3.2 1B
- **Deployment:** Runs entirely in browser (privacy!)
- **Use Case:** Doctor's personal device, no server needed
- **Limitation:** Model size constrained by device memory

### 2. Local/Edge (Raspberry Pi, NUC)
- **Models:** Llama 3.2 1B-3B, Phi-3 series
- **Deployment:** Small device in clinic (air-gapped)
- **Use Case:** Practice-wide deployment, complete data sovereignty
- **Limitation:** 8-16GB RAM constraint

### 3. Hosted Free (Groq, Together, Fireworks)
- **Models:** Llama 3.1 7B-70B, Mistral 7B
- **Deployment:** Free API tier (rate limited)
- **Use Case:** Testing, low-volume practices
- **Limitation:** Data leaves premise (compliance issue)

### 4. Commercial (OpenAI, Anthropic, Google)
- **Models:** GPT-4o-mini, Claude 3 Haiku, Gemini Flash
- **Deployment:** Paid API
- **Use Case:** High accuracy baseline, comparison
- **Limitation:** Cost + data sovereignty concerns

## Research Questions

### Primary Question
**"What is the minimum viable model size for this task?"**

### Secondary Questions
1. **Classification accuracy**: At what size can models reliably classify document types? (>95% target)
2. **Action appropriateness**: At what size do suggested actions become clinically safe? (>90% target)
3. **Few-shot effectiveness**: Do 3-5 examples provide enough context? Or do we need more?
4. **Example selection**: Does dynamic selection improve performance vs. static examples?
5. **Deployment viability**: Can 1B-3B models run on Raspberry Pi with acceptable latency (<2s)?

## Expected Findings

Based on Phase 1 research (densing law, model capabilities):

**Hypothesis:**
- **1B models**: May struggle with nuanced classification (65-75% accuracy)
- **3B models**: Likely sufficient for classification (85-90% accuracy)
- **7B models**: Good action generation (90-95% accuracy)
- **13B+ models**: Diminishing returns for this specific task

**Breakpoint Prediction:**
- **Classification task**: 3B models should be sufficient
- **Action generation**: May require 7B for clinical safety
- **Overall**: Sweet spot likely at 3B-7B range

## Timeline (Simplified)

| Week | Focus | Deliverables |
|------|-------|-------------|
| 1-2 | Research & document type definition | 5-10 document types defined with workflows |
| 3-4 | Few-shot example creation | 10-20 examples per type, prompt templates |
| 5-6 | Test dataset preparation | 50 test cases per type, evaluation metrics |
| 7-8 | Model setup & deployment testing | All 4 deployment types working |
| 9-10 | Classification experiments | Accuracy per model size per type |
| 11 | Action generation experiments | Action appropriateness evaluation |
| 12 | Breakpoint analysis | Where do models fail? Why? |
| 13 | Final analysis & recommendations | Deployment guide, final report |

## Success Metrics

### Technical Metrics
- **Classification accuracy**: >95% for chosen model size
- **Action appropriateness**: >90% (validated by medical expert)
- **Latency**: <2 seconds per document
- **Deployment**: Successfully runs on target hardware (Raspberry Pi 5)

### Research Metrics
- **Breakpoint identified**: Clear threshold where models fail
- **Cost-benefit**: Optimal model size for accuracy/cost trade-off
- **Deployment guide**: Practical recommendations for 4 deployment scenarios
- **Reproducibility**: Complete code + datasets for replication

## Critical Success Factors

- ✅ **Clinical safety**: Actions must be medically appropriate
- ✅ **Data sovereignty**: Must work on-device/local
- ✅ **Practical viability**: Must run on affordable hardware
- ✅ **Real-world testing**: Test with actual (anonymized) medical documents
- ✅ **Expert validation**: Medical professional validates appropriateness

## Resources

### Few-Shot Learning
- Brown et al. (2020). "Language Models are Few-Shot Learners" (GPT-3 paper)
- Min et al. (2022). "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
- Zhao et al. (2021). "Calibrate Before Use: Improving Few-Shot Performance of Language Models"

### Medical NLP
- Medical document classification benchmarks
- Clinical decision support systems
- Medical information extraction datasets

### Model Deployment
- WebLLM: https://webllm.mlc.ai/
- Ollama (local deployment): https://ollama.ai/
- Groq (fast inference): https://groq.com/
- HuggingFace Inference: https://huggingface.co/inference-api

## Next Steps

1. **Define document types** (Week 1-2)
   - Research common medical document types
   - Define 5-10 types with clinical expert input
   - Create workflow diagrams (type → actions)

2. **Create few-shot examples** (Week 3-4)
   - 10-20 synthetic examples per type
   - Validate with medical expert
   - Design prompt templates

3. **Build test datasets** (Week 5-6)
   - 50 test cases per type
   - Mix of easy/medium/hard cases
   - Ground truth from medical expert

4. **Setup models** (Week 7-8)
   - Configure all 4 deployment types
   - Benchmark baseline latency/memory
   - Verify data sovereignty compliance

## Notes for AI Assistants

When working on this project:
1. **Medical accuracy is critical** - Always validate clinical appropriateness
2. **Use synthetic data only** - Never commit real patient information
3. **Data sovereignty is non-negotiable** - Prefer local/edge solutions
4. **Focus on breakpoint analysis** - Where exactly do models fail?
5. **Practical deployment matters** - Must work on real hardware constraints

---

**Last Updated:** November 20, 2025
**Status:** Structure created, ready for document type definition
**Current Focus:** Week 1-2 - Research & document type definition
