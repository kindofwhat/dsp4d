# Theory / State of Research

Evaluating the performance of language models requires quantifiable metrics that capture both accuracy and semantic quality. While subjective assessment remains valuable, reproducible benchmarks enable systematic comparison across models and configurations. This section reviews established evaluation frameworks — from classical NLP metrics through modern LLM-based assessment methods — and situates them within the medical domain where accuracy requirements are particularly stringent.

## Evaluations in Classical Text Analysis

In classical natural language processing (NLP) and information retrieval, evaluation relies heavily on comparing system output against a "gold standard" or ground truth. These metrics are particularly relevant for classification tasks, such as identifying clinical intent or extracting specific medical entities.

### String Similarity & Edit Distance

When exact matches are too strict, string similarity metrics quantify the difference between two sequences.

*   **Levenshtein Distance** (or Edit Distance) counts the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word or text string into the other [@levenshtein1966binary]. This is valuable for correcting typos or measuring near-matches in entity extraction.

### Classification Metrics

For tasks involving categorization, the confusion matrix serves as the foundation for most metrics, tracking true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN) [@manning2008introduction].

*   **Accuracy** measures the overall correctness of the model but can be misleading in unbalanced datasets, which are common in medical contexts (e.g., rare diseases).
*   **Precision** (Positive Predictive Value) measures the proportion of identified positive cases that were actually correct. In a clinical setting, high precision minimizes false alarms.
*   **Recall** (Sensitivity) measures the proportion of actual positive cases that were identified. High recall is critical in medicine to ensure no pathology is overlooked.
*   **F1-Score** provides the harmonic mean of precision and recall, offering a balanced view when finding a compromise is necessary [@sokolova2009systematic].

### Generation Metrics

For tasks involving text generation, such as summarizing findings or suggesting actions, classical n-gram based metrics are often employed:

*   **BLEU (Bilingual Evaluation Understudy)** measures the precision of n-grams in the generated text compared to reference texts. While popular, it is often criticized for focusing only on exact matches and ignoring semantic meaning [@papineni2002bleu].
*   **METEOR (Metric for Evaluation of Translation with Explicit ORdering)** improves upon BLEU by incorporating stemming and synonym matching, resulting in better correlation with human judgment [@banerjee2005meteor].
*   **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** focuses on recall, measuring how much of the reference text appears in the generated output, widely used for summarization [@lin2004rouge].

While these metrics provide objective, reproducible scores, they often correlate poorly with human judgment for complex reasoning tasks, necessitating more advanced evaluation paradigms.

### Semantic & Embedding-based Metrics

To overcome the limitations of exact n-gram matching, semantic metrics utilize word or sentence embeddings to measure similarity in meaning rather than just surface form.

*   **BERTScore** computes a similarity score for each token in the candidate sentence with each token in the reference sentence using contextual embeddings (e.g., from BERT). This allows for a more robust evaluation of paraphrases and synonyms [@zhang2020bertscore].
*   **Word Mover's Distance (WMD)** and its variants (like MoverScore) measure the minimum "distance" required to move the embedded words of one document to the other. This approach captures semantic distance effectively, even when no words overlap [@kusner2015word; @zhao2019moverscore].

### LLM-Based Evaluation (LLM-as-a-Judge)

Recent advances have shifted towards using Large Language Models themselves as evaluators, a paradigm known as "LLM-as-a-Judge". This approach uses the reasoning capabilities of capable models (such as GPT-5) to assess the quality of generated text based on complex criteria such as helpfulness, safety, and coherence, often achieving higher correlation with human judgment than traditional metrics.

*   **G-Eval** is a framework that uses LLMs with Chain-of-Thought (CoT) reasoning to evaluate generated text. By decomposing the evaluation task into a series of steps, it provides fine-grained scores that align closely with human preference [@liu2023geval].
*   **GPTScore** evaluates texts by calculating the probability of the generated text given a specific instruction or context, using the model's own likelihood scores as a proxy for quality [@fu2024gptscore].
*   **Prometheus** is an open-source LLM specifically fine-tuned for evaluation purposes. It allows for custom evaluation criteria and feedback generation, offering a cost-effective alternative to using proprietary models like GPT-4 as judges [@kim2024prometheus2].
*   **Ragas** (Retrieval Augmented Generation Assessment) is a framework specifically designed for evaluating RAG pipelines. It defines metrics such as *context precision*, *faithfulness*, and *answer relevancy*, using an LLM to verify if the generated answer is grounded in the retrieved documents and if it actually answers the user's question [@es2024ragas].
*    **DAG** (Deep Acyclical Graph) metric evaluates according to a graph with different answer types (yes/no, nummerical) which implies a COT approach. It is based on the ideas of DeepEval framework but has been implemented from scratch. 

### Evaluation Challenges

Despite the proliferation of evaluation frameworks, assessing LLM quality remains a central limitation in the field. The metrics described above each carry inherent weaknesses that complicate reproducible benchmarking.

**Weakness of Traditional Metrics.** Automated measures such as BLEU and ROUGE correlate only weakly with human judgment in many contexts [@reiter2018structured]. These metrics rely on n-gram overlap and fail to capture semantic equivalence, coherence, or reasoning quality. A generated response may convey the correct meaning through paraphrasing yet receive a low score due to lexical divergence from the reference text. Conversely, a response with high word overlap may be factually incorrect or incoherent. This limitation is particularly acute in medical contexts, where semantic accuracy matters more than surface-level similarity.

**Bias in LLM-as-a-Judge.** While LLM-based evaluation addresses some limitations of traditional metrics, it introduces new biases. Research has identified a *self-preference bias*: models systematically favor outputs generated by themselves or similar architectures over those from other models [@panickssery2024llmevaluatorsrecognizefavor]. Additionally, a *length bias* causes LLM judges to prefer longer responses regardless of quality, conflating verbosity with helpfulness [@saito2024lengthbias]. These biases undermine the reliability of automated evaluation pipelines and complicate cross-model comparisons.

**Data Contamination.** Many established benchmarks (MMLU, HellaSwag, GSM8K) are publicly available on the internet, raising the risk that models have encountered test items during pre-training [@sainz2024datacontamination]. When benchmark data appears in training corpora, evaluation scores become inflated and no longer reflect genuine generalization capability. This contamination problem is difficult to detect and increasingly prevalent as training datasets grow to encompass ever-larger portions of the web. For medical applications, this raises questions about whether reported performance on clinical benchmarks reflects true capability or mere memorization.

These challenges underscore the need for multi-faceted evaluation approaches that combine automated metrics with human assessment, use held-out test sets, and interpret results with appropriate caution. 

For the present study, these limitations are partially mitigated by our reliance on relative rather than absolute metric comparisons; nevertheless, they remain relevant considerations when interpreting results.


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

| Technique |                                                                               |
|-----------|-------------------------------------------------------------------------------|
| Zero-Shot Prompting | **Description:** Asking the model to perform a task without examples|
||**Application to Medical Silver Answers:** "Extract all diagnoses from this text."|
||**Pros for Medical Records:** Fast and low token cost. Useful for checking the baseline capability of a model.|
||**Cons / Risks:** High risk of hallucination and format inconsistency. The model may guess the required medical style incorrectly. |
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Chain-of-Thought (CoT) | **Description:** Instructing the model to generate intermediate reasoning steps.
||**Application to Medical Silver Answers:** Clinical Reasoning: "First, list all medications found. Second, check if they are current or historical. Finally, output the list."|
||**Pros for Medical Records:** Critical for connecting implied symptoms to explicit medical codes. Reduces "skipping" of details.|
||**Cons / Risks:** Increases token usage. Requires parsing to separate the "thought" from the "silver answer."|
||**References:** [Chain of Thought Prompting Elicits reasoning (arXiv)](https://arxiv.org/pdf/2201.11903), [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Prompt Chaining | **Description:** Breaking a task into subtasks where output A becomes input B.|
||**Application to Medical Silver Answers:** Workflow: 1. Extraction Prompt -> 2. Filtering Prompt -> 3. Formatting Prompt.|
||**Pros for Medical Records:** High reliability. Isolates errors. Allows for intermediate transformation (e.g., cleaning citations).|
||**Cons / Risks:** Requires building a controller application (state management) between prompts.|
||**References:** [Prompt Engineering Guide: Prompt Chaining (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb), [PromptChainer Paper (arXiv)](https://arxiv.org/pdf/2203.06566) |
| Multi-Persona Prompting | **Description:** Simulating a discussion between multiple agents (e.g., Drafter & Reviewer).|
||**Application to Medical Silver Answers:** Quality Assurance: Agent A extracts data; Agent B reviews it for missing info; Agent C finalizes.|
||**Pros for Medical Records:** Simulates a "four-eyes principle" (peer review), reducing errors through internal debate.|
||**Cons / Risks:** High latency and token cost; complex to orchestrate.|
||**References:** [Exploring Multi-Persona Prompting for Better Outputs](https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs) |
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

