# Related Work

## LLM in the Context of Medical Science

The application of Large Language Models (LLMs) in medicine is an evolution of clinical Natural Language Processing (NLP), which gained significant momentum with the release of specialized models like ClinicalBERT [@alsentzer2019publicly]. While early models focused on entity recognition and extraction, modern LLMs offer the potential to summarize charts and suggest clinical actions. However, their integration into clinical workflows is constrained by critical requirements for accuracy, data privacy, and data sovereignty.

### Privacy, Security, and Data Sovereignty

The use of cloud-based LLMs in healthcare introduces significant risks that have been documented since the early days of transformer models.

*   **Data Leakage and Memorization:** Foundational research has shown that LLMs can memorize and inadvertently "regurgitate" sensitive training data, including personally identifiable information (PII) [@carlini2021extracting]. In a medical context, this poses a risk of exposing protected health information (PHI) through model outputs.
*   **Adversarial Vulnerabilities:** Modern aligned models are susceptible to adversarial attacks, such as prompt injection, which can bypass safety filters and potentially lead to the disclosure of sensitive context or the generation of incorrect medical advice [@zou2023universal].
*   **Ethical and Regulatory Gaps:** A 2025 scoping review identifies a persistent lack of ethical oversight and informed consent in many LLM-based medical studies, highlighting an urgent need for privacy-preserving architectures [@Zhong2025Considerations].

To mitigate these risks, researchers are exploring **Data Sovereignty**—the principle that health data should remain under the control of the originating institution or the patient. This has led to two main research directions:

1.  **On-Device Deployment:** Operating models entirely on local hardware (e.g., Jetson Nano) to ensure no sensitive data ever leaves the clinical environment [@wu2025dualstage].
2.  **Privacy-Preserving Training:** Techniques like "Whispered Tuning" and differential privacy are being developed to prevent PII memorization during model adaptation [@Singh2024WhisperedTuning].

### Specialized Medical Applications

**Dual-stage and Lightweight Patient Chart Summarization**  
Wu et al. (2025) proposed a dual-stage system specifically for emergency departments. By using a Small Language Model (SLM) on embedded devices, they demonstrate that it is possible to provide actionable clinical summaries without cloud dependencies, thereby fulfilling the highest standards of data sovereignty [@wu2025dualstage].

**ELMTEX: Structured Clinical Information Extraction**  
Guluzade et al. (2024) showed that fine-tuned smaller models can outperform larger, general-purpose counterparts in extracting structured data from unstructured German clinical reports. Their work demonstrates that for specialized medical tasks, increased parameter count does not guarantee improved performance — a finding that supports the feasibility of local deployment [@guluzade2024elmtex].

**GraSCCo: A Foundation for Privacy-Preserving Research**  
The Graz Synthetic Clinical text Corpus (GraSCCo) remains a cornerstone for this research area. As a multiply-alienated German clinical corpus, it allows researchers to benchmark models on realistic medical narratives without the legal and ethical risks associated with real patient data [@modersohn2022grascco; @GraSCCo_PII_V2_2025].


## Scaling Laws and Model Efficiency

A central question for deploying LLMs in privacy-sensitive environments is: how small can a model be while maintaining acceptable performance? Early scaling laws suggested a straightforward trade-off, but recent developments in Small Language Models (SLMs) have significantly shifted expectations.

### Historical Context

Early work by Kaplan et al. (2020) and Hoffmann et al. (2022) established that language model performance follows predictable power-law relationships with model size and training data [@kaplan2020scaling; @hoffmann2022training]. While foundational, these findings predate the current generation of highly optimized small models and do not fully capture the capabilities of modern SLMs.

### The Rise of Small Language Models

A comprehensive survey by Lu et al. (2024) benchmarked 59 SLMs (100M–5B parameters) across commonsense reasoning, mathematics, and in-context learning tasks. Their findings reveal substantial performance improvements: SLMs improved by 10–13% between 2022 and 2024, outpacing larger models which improved by only 7.5% over the same period [@lu2024slmsurvey]. Notably, the Phi-3 model (3.8B parameters) achieves 69% on MMLU — performance comparable to Mixtral 8x7B and GPT-3.5. This demonstrates that modern SLMs, through optimized architectures and high-quality training data, can compete with models several times their size.

### A Note on Terminology

The term "Small Language Model" warrants clarification. In current usage, "small" refers exclusively to parameter count — not to training data scope. A 3B parameter model trained on trillions of web-scale tokens is considered "small" only relative to 70B+ frontier models. This stands in contrast to *domain-specific* models such as ClinicalBERT or PubMedBERT, which are smaller in both parameters and training scope, having been trained on specialized medical corpora. Throughout this thesis, the term SLM refers to language models with fewer than 100 billion parameters, regardless of their training data origin. This broader definition encompasses both general-purpose compact models (Phi, Qwen, Llama) and domain-specialized models, allowing for comparison across deployment scenarios.

### Capability Density and the Densing Law

Xiao et al. (2025) formalize this trend through the concept of *capability density* — defined as capability per parameter. Their empirical analysis reveals a "densing law": capability density approximately doubles every 3.5 months [@xiao2025densing]. This trajectory indicates that equivalent performance can be achieved with exponentially fewer parameters over time, making local deployment increasingly viable.

### Edge Deployment Considerations

Recent work specifically addresses SLM deployment on resource-constrained devices. Hassanpour et al. (2025) systematically evaluate SLMs for edge scenarios, examining the trade-offs between model size, quantization levels, and task performance [@hassanpour2025edge]. Their findings confirm that sub-4B parameter models can achieve practical utility for domain-specific tasks when properly configured — a key consideration for medical applications where data must remain on-device.

### Implications for This Study

These developments frame the research question: given hardware constraints of on-device deployment for sensitive medical data, what is the smallest pre-trained model that can reliably perform clinical document classification? The answer depends not only on parameter count, but also on model generation and — as the following section explores — context engineering strategies that can augment smaller models at inference time.

## Context Engineering Strategies

The performance of language models — whether large frontier models or compact SLMs — is not determined solely by parameter count or training data. The quality of model outputs depends critically on how tasks are formulated and presented at inference time. This principle, known as **prompt engineering** or **context engineering**, has emerged as a fundamental discipline for extracting reliable, accurate responses from language models.

### The Importance of Prompt Engineering for High-Quality Answers

Prompt engineering is the systematic practice of designing, refining, and optimizing the instructions and context provided to a language model to elicit desired outputs. In medical applications where accuracy is paramount, effective prompt engineering can mean the difference between a model producing clinically useful summaries and generating unreliable or hallucinated content.

**Why Prompt Engineering Matters:**

1. **Bridging the Capability Gap:** Even state-of-the-art models require carefully structured prompts to consistently produce high-quality outputs. A poorly formulated prompt can cause a capable model to underperform, while a well-engineered prompt can enable even smaller models to achieve surprisingly strong results. This is particularly relevant when deploying SLMs in resource-constrained environments where model size is limited by hardware constraints.

2. **Reducing Hallucinations:** Language models are prone to generating plausible-sounding but factually incorrect information — a phenomenon known as hallucination. In medical contexts, where errors can have serious consequences, prompt engineering techniques such as self-consistency checking and chain-of-thought reasoning help ground model outputs in verifiable facts and reduce the risk of fabricated content.

3. **Ensuring Consistency and Reproducibility:** Medical documentation requires standardized formats and terminology. Without explicit guidance through prompts, models may produce outputs in inconsistent formats, use non-standard terminology, or omit critical information. Structured prompting techniques ensure that outputs conform to required schemas and clinical standards.

4. **Maximizing Limited Resources:** For SLMs deployed on edge devices, prompt engineering becomes even more critical. Since these models have fewer parameters and potentially less training data than frontier models, carefully designed prompts can compensate for architectural limitations by providing explicit reasoning frameworks and domain-specific context.

5. **Enabling Transparent Reasoning:** When using LLMs to generate reference answers (silver answers) for evaluation purposes — as in this study — prompt engineering is essential for ensuring that these references are accurate, complete, and scientifically defensible. Chain-of-Thought (CoT) prompting, in particular, allows models to expose their reasoning process, making it possible to verify the logical steps that led to a conclusion. This transparency is crucial for scientific validation: rather than accepting a model's output as a black box, researchers can inspect the intermediate reasoning steps to identify potential errors, biases, or hallucinations. Zero-shot CoT, which requires no task-specific examples, offers the additional advantage of generalizability across diverse medical documents without the need for manual example curation.

The following sections detail specific prompt engineering techniques and their application to medical text processing, with particular emphasis on methods that enable reliable extraction of structured information from clinical narratives.

### Comprehensive Comparison of Prompting Techniques
This table evaluates techniques based on their ability to extract accurate, structured "Ground Truth" (Silver Answers) from the GraSCCo medical corpus. The comparison of techniques is equally relevant for prompting the set of smaller LLMs in the evaluation phase.

| Technique                |                                                                    |
|--------------------------|----------------------------------------------------------------------|
| Zero-Shot Prompting | **Description:** Asking the model to perform a task without examples|
||**Application to Medical Silver Answers:** "Extract all diagnoses from this text."|
||**Pros for Medical Records:** Fast and low token cost. Useful for checking the baseline capability of a model.|
||**Cons / Risks:** High risk of hallucination and format inconsistency. The model may guess the required medical style incorrectly. |
||**References:** [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Chain-of-Thought (CoT) | **Description:** Instructing the model to generate intermediate reasoning steps.
||**Application to Medical Silver Answers:** Clinical Reasoning: "First, list all medications found. Second, check if they are current or historical. Finally, output the list."|
||**Pros for Medical Records:** Critical for connecting implied symptoms to explicit medical codes. Reduces "skipping" of details.|
||**Cons / Risks:** Increases token usage. Requires parsing to separate the "thought" from the "silver answer."|
||**References:** [@wei2022chain], [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Prompt Chaining | **Description:** Breaking a task into subtasks where output A becomes input B.|
||**Application to Medical Silver Answers:** Workflow: 1. Extraction Prompt -> 2. Filtering Prompt -> 3. Formatting Prompt.|
||**Pros for Medical Records:** High reliability. Isolates errors. Allows for intermediate transformation (e.g., cleaning citations).|
||**Cons / Risks:** Requires building a controller application (state management) between prompts.|
||**References:** [@dairai2024promptguide], [@wu2022promptchainer] |
| Multi-Persona Prompting | **Description:** Simulating a discussion between multiple agents (e.g., Drafter & Reviewer).|
||**Application to Medical Silver Answers:** Quality Assurance: Agent A extracts data; Agent B reviews it for missing info; Agent C finalizes.|
||**Pros for Medical Records:** Simulates a "four-eyes principle" (peer review), reducing errors through internal debate.|
||**Cons / Risks:** High latency and token cost; complex to orchestrate.|
||**References:** [@prompthub2024multipersona] |
List truncated: [See: Comprehensive Comparison of Prompting Techniques](#appendix-promp-techs)

### Chain-of-Thought: The Optimal Technique for Generating Silver Answers

Among the diverse landscape of prompt engineering techniques, **Chain-of-Thought (CoT) prompting** emerges as the optimal choice for generating scientifically defensible silver answers from medical documents. While other techniques offer valuable capabilities, CoT uniquely balances transparency, generalizability, and accuracy — making it the technique of choice for this study.

#### Why Chain-of-Thought Wins

**1. Transparent Reasoning Process**

Unlike black-box approaches that produce direct answers, CoT explicitly exposes the model's reasoning steps. This transparency is essential for scientific validation: researchers can inspect the intermediate logic to verify correctness, identify potential errors, and understand how the model arrived at its conclusion. For medical text extraction, this means being able to trace how the model connected symptoms to diagnoses or medications to treatment plans.

**Source Evidence:** The foundational work on Chain-of-Thought prompting demonstrates that instructing models to generate intermediate reasoning steps dramatically improves performance on complex reasoning tasks [@wei2022chain]. G-Eval further validates this approach by using CoT reasoning to decompose evaluation tasks into verifiable steps [@liu2023geval].

**2. Zero-Shot Generalizability**

The breakthrough of **Zero-Shot CoT** — achieved simply by adding "Let's think step by step" to prompts — eliminates the need for task-specific examples. This is particularly valuable when working with diverse medical documents where manually curating representative examples for few-shot prompting would be impractical and potentially introduce selection bias. Zero-shot CoT allows the same prompt structure to generalize across different document types, medical specialties, and clinical scenarios without requiring domain-specific example curation.

**Source Evidence:** Research on zero-shot CoT shows that this simple prompting strategy enables large language models to perform complex reasoning without any task-specific demonstrations, achieving performance comparable to or exceeding few-shot approaches [@kojima2022large].

**3. Reduced Hallucination Through Explicit Reasoning**

By forcing the model to articulate its reasoning process, CoT naturally reduces hallucinations. The model must justify each step, making it more difficult to fabricate information. When extracting medical entities, the model must explicitly state where in the text it found each piece of information, creating an audit trail that can be verified against the source document.

**4. Simplicity and Reproducibility**

Unlike complex multi-stage pipelines (prompt chaining) or computationally expensive validation methods (self-consistency with multiple runs), CoT requires only a single inference pass with a straightforward prompt modification. This simplicity enhances reproducibility — a critical requirement for scientific research — and reduces computational costs, making it feasible even when working with resource-constrained SLMs.

**5. Compatibility with Other Techniques**

CoT serves as a foundational technique that can be combined with complementary approaches when needed. Role prompting can specify the medical expertise level, while self-consistency can validate CoT outputs through majority voting. However, CoT alone provides sufficient reasoning structure for most medical extraction tasks.

#### Application to Medical Silver Answers

For generating silver answers from GraSCCo medical documents, zero-shot CoT is applied as follows:

**Prompt Structure:**
```
You are analyzing a clinical document. Extract all relevant medical information.
Let's think step by step:

1. First, identify all mentioned diagnoses and their supporting evidence in the text
2. Second, list all medications with their dosages and administration routes
3. Third, note any procedures or treatments described
4. Finally, structure this information in the required JSON format

[Clinical document text]
```

**Value for This Study:**

* **Scientific Defensibility:** The exposed reasoning allows verification of extraction accuracy
* **Generalizability:** Works across diverse medical documents without example curation
* **Efficiency:** Single-pass inference suitable for both large LLMs and smaller SLMs
* **Transparency:** Enables identification of model limitations and systematic errors
* **Reproducibility:** Simple, well-documented approach that other researchers can replicate

#### Comparison with Alternative Techniques

**Prompt Chaining** offers modularity but introduces complexity through multi-stage orchestration and error propagation between stages. For medical extraction, the overhead of managing state between prompts outweighs the benefits when CoT can achieve similar decomposition within a single prompt.

**Self-Consistency** provides statistical validation through multiple sampling runs but multiplies computational costs by 5-10×. While valuable for critical applications, it is better positioned as an optional validation layer on top of CoT rather than a primary technique.

**Multi-Persona Prompting** simulates expert review but requires complex orchestration of multiple model calls and personas. The "four-eyes principle" it provides can be approximated more efficiently through careful CoT prompt design that instructs the model to verify its own reasoning.

**Conclusion:** Chain-of-Thought prompting, particularly in its zero-shot form, represents the optimal balance of transparency, efficiency, and accuracy for generating silver answers from medical documents. Its ability to expose reasoning while maintaining generalizability makes it the technique of choice for this study's evaluation framework.

