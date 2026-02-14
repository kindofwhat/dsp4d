# Methodology

**Development of an Algorithmic Framework for Resource-Efficient Local LLM Selection**

The primary objective of this study is the development of an algorithmic selection framework designed to identify the most resource-efficient Large Language Model (LLM) suitable for local execution. By validating output quality against a set of verified "Golden Answers", this research seeks to establish an optimal equilibrium between computational performance and data sovereignty. The proposed algorithm argues for a shift away from maximalist parameter counts towards targeted efficiency without compromising output fidelity.

## Procedure

![four-phase methodological approach](assets/03-Methodology-Overview.png)

The research design follows a rigorous four-phase methodological approach to ensure reproducibility and statistical significance:

### Phase I: Dataset Curation and Establishment of Ground Truth
The initial phase focuses on the identification and preprocessing of a stable text corpus. This corpus serves as the foundational bedrock for deriving "Golden Answers" (Ground Truth). Establishing this baseline is critical, as it functions not only for the initial assessment of the chosen State-of-the-Art (SOTA) LLM but also acts as the immutable comparative benchmark during the subsequent model evaluation phases.

### Phase II: Automated Generation and Supervised Validation of Reference Solutions
In this step, a selected high-performance LLM is utilised to generate high-fidelity "Golden Answers". To ensure domain-specific accuracy, these outputs undergo a supervised review and validation process by a qualified subject matter expert (General Practitioner). Concurrently, various prompt engineering techniques are evaluated, with sessions systematically logged. This data retention is essential to argue whether complex prompting strategies yield comparable performance enhancements when applied to significantly smaller models later in the process.

### Phase III: Technical Implementation of the Multi-Model Evaluation Pipeline
A robust evaluation framework is engineered to assess a diverse array of LLMs, varying in architecture, quantisation, and parameter size. The system is designed to task these models with reproducing the "Golden Answers" derived from the corpus in Phase I. Consistent with Phase II, the previously identified prompt engineering strategies are re-evaluated within this constrained environment. The pipeline captures comprehensive performance metrics, generating the necessary empirical data input for the final analysis.

### Phase IV: Statistical Analysis and Optimal Model Identification
The concluding phase involves a multi-dimensional assessment of the generated data to isolate the optimal model. This includes the application of context-aware content metrics as well as an "LLM-as-a-Judge" paradigm to comparatively evaluate the semantic quality of the outputs. By synthesising these qualitative and quantitative insights, the study identifies the specific LLM that strictly adheres to the pre-defined requirements, thereby validating the feasibility of high-quality, local, and resource-efficient generative AI.

 
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
TBD i suggest we discuss the coice of prompting technique for the LLM evaluation aswell

#### The 3 Most Potent Techniques for Golden Answers (for a state of the art LLM)

While Role Prompting and Skeleton-of-Thought are valuable, they are "modifiers" or "accelerators." The three techniques below are architectural necessities for ensuring the accuracy required for a scientific Gold Standard.

##### 1. Prompt Chaining (The Architecture)

**Source Evidence:** The Prompt Engineering Guide highlights that chaining is essential for "Document QA" where extraction and synthesis are separate logical steps.

**Why it wins**

Medical documentation in GraSCCo is unstructured and "messy." Trying to extract, clean, standardize, and format data in a single shot leads to cognitive overload for the model.

**Application**

You must split the generation of Golden Answers into a pipeline:

* **Step 1 (Extraction):** "Extract all medical entities." (Raw list).
* **Step 2 (Grounding):** "Match these entities to ICD-10/RxNorm codes." (Standardization).
* **Step 3 (Formatting):** "Convert this standardized list into the final JSON schema."

**Value**

If the JSON is broken, you only debug Step 3. If a drug is missed, you debug Step 1. This traceability is vital for a thesis.

---

##### 2. Self-Consistency (The Validator)

**Source Evidence:** The paper *Self-Consistency Improves Chain of Thought Reasoning* proves that replacing greedy decoding with "sample-and-marginalize" (majority voting) improves performance on complex reasoning tasks by significant margins (e.g., +17.9% on GSM8K).

**Why it wins**

You are creating a "Gold Standard" using AI, which is inherently risky. A single pass of GPT-4 might hallucinate a symptom.

**Application**

For every GraSCCo document, run your extraction prompt 5 to 10 times.

* **Mechanism:** If 8/10 runs extract "Hypertension," accept it as Truth. If only 2/10 extract "Diabetes," discard it as noise/hallucination.

**Value**

This statistically "purifies" your Golden Answers, making them a defensible ground truth for your scientific evaluation.

---

##### 3. Multi-Persona / Role Prompting (The Expert Layer)

**Source Evidence:** New sources from Reddit and K2View emphasize that telling the model who to be ("You are a skeptical expert") drastically changes the quality of output compared to generic prompts.

**Why it wins**

GraSCCo contains specific Swiss-German medical shorthand. A generic model might miss context.

**Application**

Instead of just "Summarize this," you combine Role Prompting with a Multi-Persona loop:

* **Pass 1 (Persona A - The Scribe):** "You are a medical scribe. Transcribe the key facts."
* **Pass 2 (Persona B - The Senior Consultant):** "You are a Senior Physician. Review the scribe's notes against the original text. Point out missing diagnoses or errors."

**Value**

This acts as an automated **"Four-Eyes Principle"** (*Vier-Augen-Prinzip*), mimicking the real-world medical workflow where a senior doctor signs off on a junior doctor's note.


## Evaluation Metrics

### Test Setup

Use DeepEval to evaluate the respective models responses

- **Classification Accuracy** — Correct document type identification
- **Action Appropriateness** — Clinical validity of suggested actions
- **Latency** — Inference time on target hardware
