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

Due to the lack of a specialized medical background, we use a State-of-the-Art (SOTA) Large Language Model (LLM) to generate initial "Silver Answers". These serve as preliminary structured outputs derived from the GraSCCo medical corpus. To ensure the high quality and clinical validity of these answers, a subset of the LLM-generated responses is undergo evaluation by one or more medical experts. This human-in-the-loop verification allows us to refine the outputs into a "Gold Standard" (Golden Ansers) additionally suitable for benchmarking smaller models.

### Preparation Work

To ensure a structured and scientifically sound prompt engineering process, the following preparatory steps were undertaken in collaboration with medical professionals.

#### Medical Context Stratification

The reports from the **GraSSCCO** corpus were categorized into specific medical fields. This stratification allows for a granular comparison of model performance across different clinical contexts and enables an evaluation of the models' ability to correctly assign documents to their respective domains.

The following categories were defined for this study:

* Oncology
* Neurology
* Psychiatry
* Cardiology
* Internal Medicine
* Surgery
* Orthopedics
* Ophthalmology
* Dermatology

#### Standardized Output Format

In collaboration with a **General Practitioner (GP)**, a simplified output format was developed. This structure serves as the template for the prompt's output, allowing for the isolated evaluation of partial results and specific data extraction capabilities.

The standardized format consists of the following six sections:

1. **Categories:** One or more precise categories from the predefined list above.
2. **Date and Source:** The date of the report and the issuing entity (e.g., institute, clinic, or specific physician).
3. **Diagnosis:** The specific diagnosis as documented by the author of the original report.
4. **Relevant Metrics:** Extraction of laboratory values, measurement data (e.g., blood pressure, BMI), and other clinical parameters.
5. **Current or Advised Medications:** A list of medications, specifically distinguishing between the patient’s **current** medication and **recommended/prescribed** new treatments.
6. **Follow-up:** Extraction of the next clinical steps or planned interventions mentioned in the report.

#### Prompt Constraints and Data Integrity

To minimize "hallucinations" and ensure clinical reliability, the prompt instructions include strict constraints:

* **Evidence-Based Extraction:** The model is instructed to only output values if there is a clear and unambiguous reference within the source text.
* **Linguistic Consistency:** The output must be generated in the **original language** of the document (German) to maintain technical accuracy and prevent translation errors during the extraction phase.

### Selection of Prompting Technique: Chain-of-Thought (CoT)

To generate these Silver Answers, we have selected Chain-of-Thought (CoT) prompting. Based on the Comprehensive Comparison of Prompting Techniques, CoT was chosen over other methods for the following strategic reasons:
* Clinical Reasoning Alignment: CoT instructs the model to generate intermediate reasoning steps. In a medical context, this is critical for connecting implied symptoms to explicit medical codes and prevents the model from "skipping" vital clinical details.
* Reduced Hallucinations: By breaking down the task—for example, listing medications first, then checking their historical status, and finally formatting the output—the model is less likely to produce the formatting inconsistencies or "guesses" typical of Zero-Shot prompting.
* Structural Integrity: Unlike simpler techniques, CoT allows for the separation of the "thought" process from the final "golden answer," ensuring

[See: Comprehensive Comparison of Prompting Techniques](chapters/02-theory/index.md#comprehensive-comparison-of-prompting-techniques)

While techniques like Self-Consistency or Multi-Persona Prompting offer higher reliability, they were deemed less efficient for this stage due to significantly higher complexity, computational costs and latency. CoT provides the optimal balance between reasoning depth and token efficiency for clinical document classification.

| **Feature** | **Standard Prompt** | **Chain of Thought Prompt** |
|-------------|---------------------|-----------------------------|
| **Processing Style**	| Pattern matching & Direct Extraction	| Logical deduction & Evidence-first |
| **Accuracy** | High for simple reports | Superior for complex, conflicting reports |
| **Hallucination Risk** | Moderate (may guess missing values) | Lower (reasoning step identifies gaps) |
| **Token Usage** | Low (Cost-efficient) | Higher (More verbose output) |
| **Auditability** | Difficult (Only the result is visible) | Transparent (You see why it chose a category) |

### System Prompt: Clinical Data Extraction (CoT)

In a medical context, this is particularly valuable because it forces the LLM to identify the evidence in the text before committing to a category or a medication status. This reduces "lazy" extractions where a model might miss a nuance (like a medication being discontinued).

**Used prompt:**

```text
Role: You are an expert Medical Registrar. Extract data into a structured JSON format.

Constraints:
1. Factuality: Extract information ONLY if explicitly stated. 
2. Language: Content values must be in the original document language (German).
3. Format: Output ONLY a single valid JSON object.

Available Categories: You MUST choose one or more from this specific list: 
["Onkologie", "Neurologie", "Psychiatrie", "Kardiologie", "Innere Medizin", "Chirurgie", "Orthopädie", "Ophthalmologie", "Dermatologie"]

Methodology: Use the "internal_monologue" to analyze the text step-by-step before populating the final fields.

Output Schema:
{
 "internal_monologue": {
  "1": "Identify the documents creation date and author or institutions",
  "2": "List diagnoses and primary reason",
  "3": "Locate numerical metrics",
  "4": "Distinguish current vs. advised medication",
  "5": "Identify follow-up instructions"
 },
 "structured_health_record": {
  "categories": ["Must be from the list above"],
  "date_and_source": "YYYY-MM-DD; Institution/Doctor",
  "diagnosis": "Documented diagnosis",
  "relevant_metrics": "Lab values and vitals",
  "medications": {
      "current": "What the patient is already taking",
      "advised": "New prescriptions or changes"
  },
  "follow_up": "Next steps"
 }
}

Source Text:
{document}
```

[Gold Standard Example (CoT Approach)](chapters/06-appendix.md#appendix-gold-standard-example-cot-approach)

### Ground Truth Generation and Annotation Platform
To facilitate the seamless generation and validation of these answers, we developed a dedicated web application. This platform serves three primary functions:

* **Accessibility:** It allows researchers and medical experts to access the data and provide feedback from any location at any time.
* **Centralized Storage:** It records both the raw LLM outputs (Silver Answers) and the subsequent expert feedback/corrections.
* **Data Pipeline Integration:** The application is designed to automatically export these validated results into the specific input format required by our evaluation framework, ensuring a smooth transition from annotation to model benchmarking.

The platform consits of following Components:

**Session Framework**

The core of the platform is organized into Sessions. A Session acts as the functional container for processing input documents into "Silver Answers" and managing the subsequent expert annotation process.

**Input Documents**

This component manages the medical corpora, specifically the GraSCCo raw text files. Users can upload or reference specific documents that require clinical document classification or data extraction.

**Configuration & Prompt Engineering**

The platform allows for sophisticated prompt management. While it supports single-prompt execution, it is optimized for Prompt Chaining—breaking complex medical tasks into subtasks (e.g., Extraction -> Filtering -> Formatting) to isolate errors and improve reliability.
To ensure clinical accuracy, users can fine-tune the following model parameters:
* Temperature: Controls randomness. For medical extraction, a lower range of 0.2–0.5 is recommended to ensure deterministic, consistent, and predictable outputs.
* Max Output Tokens: Defines the response length. We recommend 1024–2048 for concise outputs or 4096–8192 for detailed clinical extractions
* Top-K Sampling: Limits the model to the $K$ most likely tokens. A setting of 10–40 balances consistency with the flexibility needed for medical terminology.
* Top-P (Nucleus Sampling): Selects tokens based on a cumulative probability $P$. A value of 0.8–0.9 is ideal for maintaining clinical accuracy while allowing for varied medical phrasing.

**Execution & Metrics**

This module provides real-time visibility into the generation process. It tracks Execution Status and critical performance metrics, including:
* Token Consumption: Monitoring input and output volume.
* Cost & Quality: Assessing the financial efficiency and the perceived reliability of the "Silver Answers".

**Results & Annotation**

Once execution is complete, the platform displays the generated answers for each input document. This interface is designed for the human-in-the-loop phase, allowing medical experts to:
* Review execution details for each document.
* Annotate and provide feedback to correct hallucinations or omissions.
* Download the final validated results in a standardized exchange format for use in the study’s evaluation framework.

**Administrative Modules**

Beyond the session workflow, the platform includes User Management to control expert access and API Configuration to query sessions and results.

## Selecting Smaller Large Language Models (SLM) for the Evaluation

The objective is to identify a set of 5 SLMs that can run locally on consumer-grade hardware while maintaining enough semantic understanding to process (synthetic) clinical texts.

While a comprehensive understanding of general-purpose context may be disregarded, it important that the models demonstrate a robust understanding of clinical context and the ability to perform precise information extraction. Furthermore, our selection criteria for SLMs are not strictly limited to models with specialized medical pre-training. Rather, we aim to investigate the inherent suitability and performance of general-purpose models within this specialized domain.

Because we are evaluating SLMs answers against "Silver/Golden Answers" derived from a larger model (Gemini) and human verification, the selected SLMs must be capable of strict instruction following to ensure their outputs can be parsed and scored by our custom evaluation framework. The selection procedure prioritizes models that show "emergent" reasoning capabilities usually reserved for larger models, while remaining compressible enough to fit in local (V)RAM.  [See: Selection of Prompting Technique: Chain-of-Thought](#selection-of-prompting-technique-chain-of-thought-cot)

### Procedure: Selection Criteria for 'suitable' Clinical SLMs

To filter the hundreds of available open-source models down to a manageable set, we use this five criteria in order.

**1. Hardware-Aware Parameter Efficiency**

* **Criterion:** Models must have between 7B to 20B paramters that support 4-bit or 8-bit quantization
* **Why:** A standard laptop/desktop with 16Gb Memory (shared or dedicated VRAM) cannot run a 20B model at 16-bit full precision (FP16).
For Example: 
    * A 7B model requires ~16GB RAM at FP16 but only 5GB to 6GB at 4-bit quantization
    * A 14B model requires ~30GB at FP16 but fits into 10GB to 12GB at 4-bit, making it feasable for profssional consumer desktops
    * Hence a 18B model at 4-bit quantization will still meet the criterion
* **Selection:** Exclude any models <=18B consider choosing higher bit-quantization for smaller models.
[LLM Model Parameters 2025](https://local-ai-zone.github.io/guides/what-is-ai-model-3b-7b-30b-parameters-guide-2025.html)

**2. High Reasoning & Knwledge Benchmark Scores**

* **Criterion:** Prioritize models with high scores on MMLU-Pro disciplines Biology, Chemistry, Health and Psychology
* **Why:**  Clinical text annotation is not just text generation. It is a reasoning task. Standard benchmarks like MMLU are becoming saturated and less discriminative. MMLU-Pro better distinguish models that "understand" complex topics versus those that just guess.
* **Selection:** Based on the MMLU-Pro Leaderboardsé: Select models that outperform in Biology, Chemistry, Health and Psychology and provide "Reasoning" or "Thinking" to reduce hallucination. See Table below.

**3. Instruction Following & Output Structure**

* **Criterion:** Select "Instruct" or "Chat" rather than base models
* **Why:** We compare SLM output against Silver/Golden Answers. If the SLM cannot follow instructions, we simply get the output of a "completion engine not an assistant. Base trained models lack of intent recognition.
* **Selection:** Choose the "Instruct" or "Chat" variants

**4. Context Window Capacity**

* **Criterion:** Minimum context window of 8k tokens (preferably 32k+ or higher)
* **Why:** Clinical notes can be lengthy. If a diagnosis or generally a peatient report exceeds the model's context window, the model will "forget" early information, leading to missed health infomration annotations. Newer architectures support massive context windows, allowing the model to read a full report in one pass
* **Selection:** Discard models with <8k context limits

**5. License & Data Sovereignity**

* **Criterion:** Permissive licenses (Apache 2.0, MIT) allowing local commercial use
* **Why:** The primary advantage of SLMs in healthcare is data sovereignty—running locally so patient data never leaves the machine. Open-source models allow to inspect the model and ensure no data is sent to external APIs.
* **Selection:** Model is truly open source (and does not require any API calls)

### Selection Steps 1. - 3.

[MMLU-Pro Leaderboard (filtered)](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)

Evaluation Based on benchmarks in disciplines: Biology, Chemistry, Health and Psychology and maximum parameters 18B, Qualifier: Chat or Instruct Models:

| Models | Qualifier | Model Size (B) | Data Source | Overall | Biology | Chemistry | Health | Psychology | Average selected Disciplines |
|--------|-----------|----------------|-------------|---------|---------|-----------|--------|------------|------------------------------|
| Gemma-2-9B-it | Instruct | 9 | TIGER-Lab | 0.5208 | 0.7587 | 0.4664 | 0.5844 | 0.6617 | 0.6178 |
| GLM-4-9B-Chat | Chat | 9 | TIGER-Lab | 0.4801 | 0.7015 | 0.4117 | 0.5379 | 0.6165 | 0.5669 |
| EXAONE-3.5-7.8B-Instruct | Instruct | 7.8 | TIGER-Lab | 0.4624 | 0.7308 | 0.3719 | 0.4707 | 0.5965 | 0.542475 |
| Mistral-Nemo-Instruct-2407 | Instruct | 12 | TIGER-Lab | 0.4481 | 0.6583 | 0.3445 | 0.5281 | 0.6165 | 0.53685 |
| Qwen2-7B-Instruct | Instruct | 7 | TIGER-Lab | 0.4724 | 0.6625 | 0.3772 | 0.4645 | 0.6128 | 0.52925 |
| Llama-3.1-8B-Instruct | Instruct | 8 | TIGER-Lab | 0.4425 | 0.6304 | 0.3763 | 0.5073 | 0.6003 | 0.528575 |
| Yi-1.5-9B-Chat | Chat | 9 | TIGER-Lab | 0.4595 | 0.6667 | 0.3949 | 0.4352 | 0.594 | 0.5227 |
| Phi-3.5-mini-instruct | Instruct | 3.8 | TIGER-Lab | 0.4787 | 0.7057 | 0.4125 | 0.5244 | 0.4188 | 0.51535 |
| Llama-3-8B-Instruct | Instruct | 8 | TIGER-Lab | 0.4098 | 0.6653 | 0.28 | 0.4902 | 0.594 | 0.507375 |
| Granite-3.1-8B-Instruct | Instruct | 8 | TIGER-Lab | 0.4103 | 0.5746 | 0.3145 | 0.4707 | 0.5739 | 0.483425 |
| EXAONE-3.5-2.4B-Instruct | Instruct | 2.4 | TIGER-Lab | 0.391 | 0.6541 | 0.3171 | 0.3851 | 0.5038 | 0.465025 |
| Qwen1.5-14B-Chat | Chat | 14 | TIGER-Lab | 0.3802 | 0.6151 | 0.2615 | 0.4218 | 0.5251 | 0.455875 |
| Ministral-8B-Instruct | Instruct | 8 | TIGER-Lab | 0.3793 | 0.59 | 0.2641 | 0.4328 | 0.5163 | 0.4508 |
| Yi-1.5-6B-Chat | Chat | 6 | TIGER-Lab | 0.3823 | 0.5746 | 0.3074 | 0.3362 | 0.5013 | 0.429875 |
| DeepSeek-Coder-V2-Lite-IT | Instruct | 16 | TIGER-Lab | 0.4157 | 0.5007 | 0.4293 | 0.2995 | 0.4687 | 0.42455 |
| DeepseekMath-7B-Instruct | Instruct | 7 | TIGER-Lab | 0.353 | 0.46 | 0.4108 | 0.2506 | 0.3947 | 0.379025 |
| Granite-3.1-2B-Instruct | Instruct | 2 | TIGER-Lab | 0.3197 | 0.5007 | 0.2412 | 0.3056 | 0.4411 | 0.37215 |

### Selection Step 4.

Context windows >=8k

| Models | Qualifier | Context Window | License | Size (B) | Overall | Biology | Chemistry | Health | Psychology | Average selected Disciplines| 
|--------|-----------|----------------|---------|----------|---------|---------|-----------|--------|------------|-----------------------------| 
| Gemma-2-9B-it | Instruct | 8k | Gemma Terms | 9 | 0.5208 | 0.7587 | 0.4664 | 0.5844 | 0.6617 | 0.6178 | 
| GLM-4-9B-Chat | Chat | 128k | MIT | 9 | 0.4801 | 0.7015 | 0.4117 | 0.5379 | 0.6165 | 0.5669 | 
| EXAONE-3.5-7.8B-IT | Instruct | 32k | EXAONE NC | 7.8 | 0.4624 | 0.7308 | 0.3719 | 0.4707 | 0.5965 | 0.542475 | 
| Mistral-Nemo-IT-2407 | Instruct | 128k | Apache 2.0 | 12 | 0.4481 | 0.6583 | 0.3445 | 0.5281 | 0.6165 | 0.53685 | 
| Qwen2-7B-Instruct | Instruct | 32k | Apache 2.0 | 7 | 0.4724 | 0.6625 | 0.3772 | 0.4645 | 0.6128 | 0.52925 | 
| Llama-3.1-8B-IT | Instruct | 128k | Llama 3.1 | 8 | 0.4425 | 0.6304 | 0.3763 | 0.5073 | 0.6003 | 0.528575 | 
| Phi-3.5-mini-instruct | Instruct | 128k | MIT | 3.8 | 0.4787 | 0.7057 | 0.4125 | 0.5244 | 0.4188 | 0.51535 | 
| Llama-3-8B-Instruct | Instruct | 8k | Llama 3 | 8 | 0.4098 | 0.6653 | 0.28 | 0.4902 | 0.594 | 0.507375 | 
| Granite-3.1-8B-IT | Instruct | 128k | Apache 2.0 | 8 | 0.4103 | 0.5746 | 0.3145 | 0.4707 | 0.5739 | 0.483425 | 
| EXAONE-3.5-2.4B-IT | Instruct | 32k | EXAONE NC | 2.4 | 0.391 | 0.6541 | 0.3171 | 0.3851 | 0.5038 | 0.465025 | 
| Qwen1.5-14B-Chat | Chat | 32k | Apache 2.0 | 14 | 0.3802 | 0.6151 | 0.2615 | 0.4218 | 0.5251 | 0.455875 | 
| Ministral-8B-Instruct | Instruct | 128k | Mistral | 8 | 0.3793 | 0.59 | 0.2641 | 0.4328 | 0.5163 | 0.4508 | 
| DeepSeek-Coder-V2-IT | Instruct | 128k | DeepSeek | 16 | 0.4157 | 0.5007 | 0.4293 | 0.2995 | 0.4687 | 0.42455 | 
| Granite-3.1-2B-IT | Instruct | 128k | Apache 2.0 | 2 | 0.3197 | 0.5007 | 0.2412 | 0.3056 | 0.4411 | 0.37215 |

### Selection Step 5.

**Remaining Permissive Open-Source models:**

| Models | Qualifier | Context Window | License | Size (B) | Overall | Biology | Chemistry | Health | Psychology | Average selected Disciplines|
|--------|-----------|----------------|---------|----------|---------|---------|-----------|--------|------------|-----------------------------|
| GLM-4-9B-Chat | Chat | 128k | MIT | 9 | 0.4801 | 0.7015 | 0.4117 | 0.5379 | 0.6165 | 0.5669 |
| Mistral-Nemo-IT-2407 | Instruct | 128k | Apache 2.0 | 12 | 0.4481 | 0.6583 | 0.3445 | 0.5281 | 0.6165 | 0.53685 |
| Qwen2-7B-Instruct | Instruct | 32k | Apache 2.0 | 7 | 0.4724 | 0.6625 | 0.3772 | 0.4645 | 0.6128 | 0.52925 |
| Phi-3.5-mini-instruct | Instruct | 128k | MIT | 3.8 | 0.4787 | 0.7057 | 0.4125 | 0.5244 | 0.4188 | 0.51535 |
| Llama-3-8B-Instruct | Instruct | 8k | Llama 3 | 8 | 0.4098 | 0.6653 | 0.28 | 0.4902 | 0.594 | 0.507375 |
| Granite-3.1-8B-IT | Instruct | 128k | Apache 2.0 | 8 | 0.4103 | 0.5746 | 0.3145 | 0.4707 | 0.5739 | 0.483425 |
| Qwen1.5-14B-Chat | Chat | 32k | Apache 2.0 | 14 | 0.3802 | 0.6151 | 0.2615 | 0.4218 | 0.5251 | 0.455875 |
| DeepSeek-Coder-V2-IT | Instruct | 128k | DeepSeek | 16 | 0.4157 | 0.5007 | 0.4293 | 0.2995 | 0.4687 | 0.42455 |
| Granite-3.1-2B-IT | Instruct | 128k | Apache 2.0 | 2 | 0.3197 | 0.5007 | 0.2412 | 0.3056 | 0.4411 | 0.37215 |

**Comparison of Licenses used remainging from Step 4:**

| Model Family | Specific Licenses Mentioned | Open Source? | Commercial Use | External API Required? | Key Restrictions & Notes |
|--------------|-----------------------------|--------------|----------------|------------------------|--------------------------|
| Permissive | MIT / Apache 2.0 | Yes | Unrestricted | No (Local execution) | "Do whatever you want" licenses; zero downstream legal obligations. |
| Gemma | Gemma Terms of Use | No (Open Weights) | Permitted | No (Local weights available) | Prohibits use for unlicensed professional advice or violating safety policies. |
| Llama (3.x) | Llama 3.1 Community License | No (Open Weights) | Permitted (with caps) | No (Local execution supported) | Requires a special license if users exceed 700M monthly active users. |
| DeepSeek | DeepSeek Model License | No (Open Weights) | Permitted | No (Local weights available) | Allows modifications and derivative works, including model distillation. |
| EXAONE | EXAONE Non-Commercial (NC) | No | Prohibited | No | Strictly restricted to research and experimental purposes only. |
| Mistral | Mistral AI Non-Production / Commercial | No | Restricted / Tiered | Optional (API vs local) | Smaller models are often Apache 2.0; flagship models require commercial agreements. |

**If we want to use models under Llama 3.1, Gemma or Qwen license we need to integrate following NOTICE text:**

```
ATTRIBUTION NOTICE

- If using Gemma: "Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms".
- If using Llama 3.1: "Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved".

EULA Compliance Template

Section X: AI Usage and Compliance
X.1 License Grant and Pass-Down Terms. Licensor grants Customer a limited license to use the Software incorporating [Insert Model Name, e.g., Gemma 2 / Llama 3.1]. This Software is subject to the [Insert Model Terms, e.g., Gemma Terms of Use / Llama 3.1 Community License], which are incorporated herein by reference.

X.2 Professional Advice Disclaimer. The Software is an automated tool and is NOT a substitute for professional medical, legal, financial, or other licensed advice. Customer agrees that:
- Output will not be used as authoritative for the unlicensed practice of medicine, law, or financial services.
- All high-stakes outputs must be reviewed and authorized by a qualified human professional before any action is taken.

X.3 Prohibited Use & Safety. Customer shall not use the Software to:
- Generate or facilitate illegal activities, violence, or terrorism.
- Engage in harassment, bullying, or unlawful discrimination.
- Create malicious code, malware, or viruses.
- Deceive or mislead others, including the creation of disinformation or fake reviews.

X.4 Local Deployment and Liability. As the Software is deployed locally on Customer’s private infrastructure, Customer assumes all risk associated with the use and distribution of the Software and its results. Customer shall indemnify and hold harmless [Your Company Name] and the Model Provider (e.g., Google/Meta) from any third-party claims arising out of Customer’s breach of these safety or professional advice policies.

X.5 Termination for Misuse. [Your Company Name] reserves the right to terminate this Agreement immediately and without notice if Customer is found to be in violation of the safety or acceptable use policies mandated by the Model Provider.
```
### Results

**TBD with @kindofwhat**










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

#### llm-validator

To facilitate the systematic evaluation described in Phase III and IV, a purpose-built evaluation framework — *llm-validator* — was developed as part of this research. The tool serves as the central instrumentation layer for capturing, executing, and assessing LLM interactions across multiple models and prompting strategies.

**Technology Choice.** The framework is implemented in Java 21 using the Quarkus application framework, with LangChain4j for LLM integration and an Angular-based web interface for result inspection. The deliberate choice of a JVM-based stack over the more prevalent Python ecosystem in the LLM domain is motivated by the project's alignment with healthcare IT environments: Java remains the dominant technology in enterprise and clinical information systems in Switzerland and the DACH region. By building the evaluation tooling on this stack, the resulting artefact is not only a research instrument but also a reusable component that can be integrated into existing institutional infrastructure without introducing foreign runtime dependencies.

**Evaluation Pipeline.** The core contribution of the tool lies in its multi-dimensional evaluation pipeline. Test cases — each comprising a clinical query, an optional system prompt, and a golden answer — are organised into *Test Runs* and executed in batch against one or more models. The framework then applies two categories of evaluation metrics:

- **Statistical metrics** (no LLM required): Token-level F1 score, Levenshtein similarity, and embedding-based semantic similarity provide quantitative baselines for output comparison.
- **G-Eval metrics** (LLM-as-a-Judge): Following the G-Eval framework, configurable judge prompts assess *answer relevancy*, *faithfulness*, *hallucination*, and *correctness* against the golden answers established in Phase II. These metrics are stored as database-backed definitions and can be extended without code changes.

Additionally, the system supports *expert evaluation*, allowing a human reviewer to provide qualitative scores — closing the loop between automated assessment and domain expertise.

<!-- TODO: Add screenshots of the llm-validator UI showing test run configuration and evaluation results -->

![G-Eval algorithm: CoT evaluation steps are generated once and cached, then applied per test case with probability-weighted scoring via logprobs or multi-sample fallback.](assets/03-GEval-Algorithm.png){#fig:geval-algorithm width=75%}

#### The Logprobs Problem in G-Eval 

The central mechanism of G-Eval is probability-weighted scoring: rather than taking the LLM's generated score at face value, the token log-probabilities of the score tokens (e.g. "1" through "5") are extracted and a weighted average is computed [@liu2023geval]. This approach significantly reduces the known scoring bias of LLMs and is the primary reason for G-Eval's superior human correlation compared to naive LLM-as-a-Judge approaches.

However, the `logprobs` feature that enables this weighted scoring is not uniformly supported across LLM providers. Table \ref{tab:logprobs-compat} summarises the current compatibility landscape.

| Provider | Logprobs | Notes |
|----------|----------|-------|
| OpenAI (standard models) | Yes | gpt-4o, gpt-4.1-mini etc. via `/v1/chat/completions` |
| OpenAI (reasoning models) | **No** | o-series, gpt-5-mini — `logprobs` not supported, `temperature` fixed at 1.0 |
| vLLM (self-hosted) | Yes | Any HuggingFace model; logprobs reflect raw model output before post-processing |
| Together.ai | Yes | Open-weight models via OpenAI-compatible API |
| Ollama | **No** | Logprobs only on native `/api/generate`, not on OpenAI-compatible `/v1/chat/completions` |
| LM Studio | **Partial** | Accepts `top_logprobs` on `/v1/responses` (since v0.3.26, Jan 2026) but returns empty arrays in practice |
| llama.cpp server | **No** | Returns `null` for logprobs on `/v1/chat/completions` |

: Logprobs compatibility by LLM provider (as of February 2026) {#tab:logprobs-compat}

Particularly problematic is the incompatibility with reasoning models (OpenAI o-series, gpt-5-mini, gpt-5-nano). These models employ an internal reasoning phase that consumes tokens from the `max_completion_tokens` budget before any visible output is produced. For a task that merely requires a single integer score, reasoning models are architecturally unsuitable: they spend hundreds of tokens on internal deliberation for a trivial decision — while supporting neither `logprobs` nor configurable `temperature` values.

This problem also affects existing reference implementations. DeepEval, the most widely used Python implementation of G-Eval, works around the issue with a hardcoded list of reasoning models for which it falls back to plain JSON extraction without probability weighting — which de facto is no longer G-Eval but a simple LLM-as-a-Judge approach. Several open issues document this limitation: reasoning models break G-Eval entirely^[<https://github.com/confident-ai/deepeval/issues/1358>], custom (non-OpenAI) models never receive weighted summation^[<https://github.com/confident-ai/deepeval/issues/1831>], and the fallback from weighted to unweighted scoring occurs silently without warning^[<https://github.com/confident-ai/deepeval/issues/1029>].

A promising alternative for local execution is vLLM, a high-throughput self-hosted inference engine that provides full logprobs support on its OpenAI-compatible API for any HuggingFace model. While vLLM returns logprobs from the model's raw output (before temperature scaling or penalty adjustments), this is sufficient for G-Eval scoring where the probability distribution over score tokens is the quantity of interest.

**Fallback strategy.** For providers without logprobs support, the G-Eval paper defines an alternative method: *multi-sample estimation* with $n=20$ independent calls at `temperature=1.0`, where each response is parsed for an integer score and the results are averaged [@liu2023geval]. This procedure approximates the probability distribution through sampling and thus remains faithful to the G-Eval algorithm — albeit at significantly higher cost (factor 20 compared to the logprobs variant).

**Consequence for judge model selection.** The choice of judge model for G-Eval evaluation is therefore constrained: either a non-reasoning cloud model with logprobs support is used (e.g. gpt-4o-mini), a self-hosted vLLM instance serves as judge, or the cost-intensive multi-sample fallback is required. For this study, an auto-detection strategy is implemented that first attempts the logprobs path and automatically falls back to multi-sample upon failure — enabling both cloud APIs and local models to serve as judges.

