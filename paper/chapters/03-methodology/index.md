# Methodology

## Procedure

Siehe nice Graphik von Beni

 
## Data Source: GraSCCo

Instead of generic document types, this research utilizes the **Graz Synthetic Clinical text Corpus (GraSCCo)** [@GraSCCo_PII_V2_2025; @modersohn2022grascco]. 

GraSCCo is the first publicly shareable, multiply-alienated German clinical text corpus, designed specifically for clinical NLP tasks without compromising 
patient privacy.

The corpus provides a diverse set of clinical scenarios, which we use to evaluate the models' ability to classify document intent and generate appropriate 
clinical actions based on German-language clinical reports.

The task we give the models is to update a patients health record (HBA) based on supplied clinical report. 

## Golden Answer Generation

Due to lack of access to expert medical knowledge, we generate golden answers as ground truth for the models by asking a state of the art LLM to create those.
We then validated at least a subset of those answers with a medical expert.

## Experimental Setup

### Architecture
Maschine von Beni, Chrigels notebook, Google cloud für Gemini, Evaluationsframeworks



### Models Evaluated

TBD!!

| Model | Parameters | Deployment |
|-------|------------|------------|
| Llama 3.2 | 1B | Edge/WebLLM |
| Llama 3.2 | 3B | Edge |
| Phi-3 Mini | 3.8B | Edge/WebLLM |
| Llama 3.1 | 7B | Hosted |


### Context Engineering Strategies

1. **Zero-Shot** - Instructions only (baseline)
2. **One/Few-Shot** - Multiple examples with Golden Answers
3. **Prompt Chaining**  

TBD by Beni

## Evaluation Metrics

- **Classification Accuracy** — Correct document type identification
- **Action Appropriateness** — Clinical validity of suggested actions
- **Latency** — Inference time on target hardware
