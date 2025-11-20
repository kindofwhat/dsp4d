# Phase 2: Test Design & Dataset Preparation

**Duration:** Weeks 4-6
**Effort:** ~25 hours
**Status:** Not Started

## Objectives

1. Create 3-4 domain-specific test scenarios
2. Define "sensitivity levels" for data classification
3. Establish success criteria for each scenario
4. Develop golden datasets (50-100 test questions per scenario)
5. Create relevance-graded document sets for RAG testing
6. Define comprehensive evaluation metrics

## Directory Structure

```
phase2-test-design/
├── README.md                          # This file
├── scenarios/                         # Test scenario definitions
│   ├── medical-diagnosis.md          # Medical diagnosis assistance scenario
│   ├── financial-advisory.md         # Financial advisory scenario
│   ├── legal-document-analysis.md    # Legal document analysis scenario
│   └── scenario-template.md          # Template for new scenarios
├── datasets/                          # Golden datasets
│   ├── medical/                      # Medical domain dataset
│   │   ├── questions.json            # 50-100 test questions
│   │   ├── verified-answers.json     # Ground truth answers
│   │   └── documents/                # RAG document corpus
│   ├── financial/                    # Financial domain dataset
│   │   ├── questions.json
│   │   ├── verified-answers.json
│   │   └── documents/
│   ├── legal/                        # Legal domain dataset
│   │   ├── questions.json
│   │   ├── verified-answers.json
│   │   └── documents/
│   └── dataset-schema.md             # JSON schema documentation
└── metrics/                           # Metrics definitions
    ├── accuracy-metrics.md           # Exact match, F1, BLEU
    ├── rag-specific-metrics.md       # Context relevance, faithfulness, relevancy
    ├── security-metrics.md           # Data leakage, prompt injection
    ├── performance-metrics.md        # Latency, memory, throughput
    └── evaluation-plan.md            # Complete evaluation strategy
```

## Key Deliverables

### Week 4: Define Test Scenarios (10 hours)

- [ ] **Medical Diagnosis Assistance Scenario** (`scenarios/medical-diagnosis.md`)
  - Use case: Doctor needs quick digest of large medical reports
  - Sensitivity level: HIGH (patient data, HIPAA/GDPR compliance)
  - Success criteria: >85% accuracy, <2s latency, zero data leakage
  - Input types: Lab reports, imaging results, patient history
  - Output types: Classification, abstract/summary, action items

- [ ] **Financial Advisory Scenario** (`scenarios/financial-advisory.md`)
  - Use case: Financial document analysis and recommendation
  - Sensitivity level: HIGH (financial data, regulatory compliance)
  - Success criteria: >90% accuracy, secure on-premise deployment
  - Input types: Financial statements, market reports, regulations
  - Output types: Risk assessment, compliance checks, summaries

- [ ] **Legal Document Analysis Scenario** (`scenarios/legal-document-analysis.md`)
  - Use case: Contract review and legal research
  - Sensitivity level: HIGH (attorney-client privilege)
  - Success criteria: >90% accuracy, complete privacy
  - Input types: Contracts, case law, legal opinions
  - Output types: Key clause extraction, risk identification, precedent analysis

- [ ] **Sensitivity Level Framework** (`scenarios/sensitivity-levels.md`)
  - Define LOW, MEDIUM, HIGH, CRITICAL levels
  - Map to deployment requirements (cloud, on-premise, air-gapped)
  - Define data handling procedures per level

### Week 5-6: Golden Dataset Creation (15 hours)

- [ ] **Medical Dataset** (`datasets/medical/`)
  - 50-100 test questions with verified answers
  - Document corpus: Medical guidelines, research papers, case studies
  - Relevance grades: Highly relevant, relevant, marginally relevant, not relevant
  - Include edge cases: Ambiguous symptoms, multiple conditions, rare diseases

- [ ] **Financial Dataset** (`datasets/financial/`)
  - 50-100 test questions covering analysis, compliance, risk assessment
  - Document corpus: Regulations, market data, financial statements
  - Synthetic data for privacy (use public financial data as base)

- [ ] **Legal Dataset** (`datasets/legal/`)
  - 50-100 test questions on contract analysis, legal research
  - Document corpus: Sample contracts, legal summaries, regulations
  - Synthetic/anonymized data only

- [ ] **Evaluation Metrics Definition** (`metrics/`)
  - **Accuracy Metrics**: Exact match, F1 score, BLEU, ROUGE
  - **RAG-Specific**: Context relevance, answer faithfulness, answer relevancy (RAGAS)
  - **Security**: Data leakage detection, prompt injection resistance, PII exposure tests
  - **Performance**: Latency (p50, p95, p99), memory usage, tokens/second

## Dataset Format Specifications

### Question-Answer JSON Schema
```json
{
  "id": "unique_identifier",
  "scenario": "medical|financial|legal",
  "question": "The test question",
  "ground_truth_answer": "Verified correct answer",
  "context_documents": ["doc_id_1", "doc_id_2"],
  "difficulty": "easy|medium|hard",
  "sensitivity_level": "low|medium|high|critical",
  "evaluation_criteria": {
    "exact_match": true,
    "semantic_similarity_threshold": 0.85,
    "required_concepts": ["concept1", "concept2"]
  }
}
```

### Document Relevance Schema
```json
{
  "doc_id": "unique_identifier",
  "content": "Full document text",
  "metadata": {
    "source": "guideline|research|case_study",
    "date": "2024-01-15",
    "sensitivity": "high"
  },
  "relevance_grades": {
    "question_id": "highly_relevant|relevant|marginal|not_relevant"
  }
}
```

## Success Criteria

### Dataset Quality
- ✅ 50-100 questions per scenario with verified answers
- ✅ Diverse difficulty levels (easy, medium, hard)
- ✅ Edge cases and challenging scenarios included
- ✅ Relevance-graded document sets for RAG evaluation
- ✅ Synthetic/anonymized data only (no real PII)

### Metric Coverage
- ✅ Accuracy metrics defined and measurable
- ✅ RAG-specific metrics aligned with RAGAS framework
- ✅ Security tests for data leakage and prompt injection
- ✅ Performance benchmarks established

## Handoff to Phase 3

**Prerequisites for Phase 3:**
- Golden datasets ready in JSON format
- Document corpora prepared and indexed
- Evaluation metrics clearly defined
- Security test scenarios documented

**Artifacts to Deliver:**
1. Complete test scenarios with success criteria
2. Golden datasets (150-300 total questions across scenarios)
3. Document corpora with relevance grades
4. Comprehensive evaluation plan
5. Baseline performance expectations

## Resources

### Dataset Sources (Use Synthetic/Public Data Only)
- **Medical**: PubMedQA, MedQA (use as templates, create synthetic versions)
- **Financial**: Public SEC filings, financial literacy datasets
- **Legal**: Public domain contracts, legal summaries

### Tools for Dataset Creation
- **Synthetic Data Generation**: Using LLMs to create realistic scenarios
- **Annotation Tools**: Label Studio, Prodigy for relevance grading
- **Validation**: Cross-validation with domain experts (if available)

### Evaluation Frameworks
- RAGAS metrics: https://docs.ragas.io/en/latest/concepts/metrics/
- BLEU/ROUGE calculators: https://huggingface.co/spaces/evaluate-metric
- Security testing frameworks: OWASP LLM Top 10

## Notes

- **Data Privacy**: Use only synthetic or public domain data
- **Reproducibility**: Document data generation process
- **Version Control**: Git track all datasets with clear versioning
- **Quality Assurance**: Peer review of questions and answers
- **Edge Cases**: Deliberately include challenging scenarios
