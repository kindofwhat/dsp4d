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

TBD what else do we discuss here?

### Comprehensive Comparison of Prompting Techniques
This table evaluates techniques based on their ability to extract accurate, structured "Ground Truth" (Golden Answers) from the GraSCCo medical corpus. The comparison of techniques is equally relevant for prompting the set of smaller LLMs in the evaluation phase.

| Technique | Description | Application to Medical Golden Answers | Pros for Medical Records | Cons / Risks | References |
|-----------|-------------|---------------------------------------|--------------------------|--------------|------------|
| Zero-Shot Prompting | Asking the model to perform a task without examples. | "Extract all diagnoses from this text." | Fast and low token cost. Useful for checking the baseline capability of a model. | High risk of hallucination and format inconsistency. The model may guess the required medical style incorrectly. | [Prompt Engineering Guide](https://www.promptingguide.ai/)<br>[Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Few-Shot Prompting | Providing examples (input-output pairs) within the prompt. | "Style Guide: You provide 3 examples of GraSCCo raw text and the corresponding perfect "Golden Answer" format.<br>(possible after first supervision session)" | Essential for enforcing the specific syntax and brevity required for the Golden Answers. | The model may overfit to the examples and ignore the nuance of the new input. | [Language Models are Few-Shot Learners (NeurIPS)](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)<br>[Prompt Engineering Guide](https://www.promptingguide.ai/)<br>[Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Chain-of-Thought (CoT) | Instructing the model to generate intermediate reasoning steps. | Clinical Reasoning: "First, list all medications found. Second, check if they are current or historical. Finally, output the list." | Critical for connecting implied symptoms to explicit medical codes. Reduces "skipping" of details. | Increases token usage. Requires parsing to separate the "thought" from the "golden answer." | [Chain of Thought Prompting Elicits reasoning (arXiv)](https://arxiv.org/pdf/2201.11903)<br>[Prompt Engineering Guide](https://www.promptingguide.ai/)<br>[Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Self-Consistency | Generating multiple outputs for the same prompt and selecting the most frequent one. | Validation: Generate the summary 5 times. If "Diabetes Type 2" appears in 5/5, keep it. If "Hypertension" appears in 1/5, discard it. | The best statistical defense against hallucinations. Essential for creating a robust "Gold Standard". | Computationally expensive (requires N times the inference cost). | [Self-Consistency Improves Chain of Thought (arXiv)](https://arxiv.org/pdf/2203.11171)<br>[Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Skeleton-of-Thought (SoT) | Generating a skeleton/outline first, then expanding points in parallel. | Structure Planning: 1. Generate list of headers (Dx, Rx). 2. Fill sections in parallel. | Accelerates generation speed (up to 2.39x). Good for long, structured discharge summaries. | Suited for writing new content, less proven for extracting specific facts from existing chaos. | [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://arxiv.org/pdf/2307.15337)<br>[[ICLR 2024] Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation (GitHub)](https://github.com/imagination-research/sot) |
| Prompt Chaining | Breaking a task into subtasks where output A becomes input B. | Workflow: 1. Extraction Prompt -> 2. Filtering Prompt -> 3. Formatting Prompt. | High reliability. Isolates errors. Allows for intermediate transformation (e.g., cleaning citations). | Requires building a controller application (state management) between prompts. | [Prompt Engineering Guide: Prompt Chaining (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb)<br>[PromptChainer Paper (arXiv)](https://arxiv.org/pdf/2203.06566) |
| Role / Persona Prompting | Assigning a specific role/profession to the AI. | Context Setting: "You are a Senior Chief Physician at a Swiss hospital..." | Drastically improves tone and handling of medical abbreviations/jargon. | Can lead to verbosity if the persona is too "chatty." | [Prompt Engineering: Part 2 - Best Practices for Software Developers in Digital Industries](https://blogs.sw.siemens.com/thought-leadership/prompt-engineering-part-2-best-practices-for-software-developers-in-digital-industries/)<br>[Prompt Engineering Guide](https://www.promptingguide.ai/)<br>[Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Multi-Persona Prompting | Simulating a discussion between multiple agents (e.g., Drafter & Reviewer). | Quality Assurance: Agent A extracts data; Agent B reviews it for missing info; Agent C finalizes. | Simulates a "four-eyes principle" (peer review), reducing errors through internal debate. | High latency and token cost; complex to orchestrate. | [Exploring Multi-Persona Prompting for Better Outputs](https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs) |
| Tree of Thoughts (ToT) | Exploring multiple reasoning paths and backtracking. | Complex Triage: Exploring different diagnostic possibilities before committing to one. | Useful for complex differential diagnosis problems. | Likely overkill for extraction tasks where the answer is explicitly in the text. | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/pdf/2305.10601)<br>[[NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://github.com/princeton-nlp/tree-of-thought-llm) |
| Retrieval Augmented Generation (RAG) | Retrieving external data to ground the generation. | Fact Checking: Using a vector DB to validate if an extracted drug name exists in RxNorm. | Prevents hallucination of non-existent drugs; ensures terminology standardization. | Requires external database infrastructure. And a document base. | [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/)<br>[Prompt Engineering Guide: Prompt Chaining (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb) |
| Automatic Prompt Engineer (APE) | Using an LLM to generate and optimize prompts. | Asking GPT-4 to write the optimal prompt for analyzing GraSCCo texts. | Saves time on trial-and-error. | The resulting prompt might be obscure/hard to interpret. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Generated Knowledge Prompting | Asking the model to generate relevant knowledge before answering. | "List common side effects of Ibuprofen, then summarize the patient's complaints regarding medication." | Can help if the medical text is ambiguous (e.g., vague symptoms), providing context for the summary. | Risk of generating false knowledge (hallucinated medical facts) which then contaminates the summary. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Automatic Reasoning and Tool-use | Allowing the LLM to use external tools (calculators, APIs). | Calculating cumulative dosage or converting units (e.g., mg to g) found in the text. | Ensures mathematical accuracy in the medical record (e.g., total radiation dose). | Adds complexity; the model might fail to invoke the tool correctly. | [Toolformer: Language Models Can Teach Themselves to Use Tools (arXiv)](https://arxiv.org/pdf/2302.04761) |
| Active-Prompt | Selecting the most uncertain examples for human annotation to teach the model. | Identifying GraSCCo texts where the model is "unsure" and asking a doctor to manually create the Golden Answer. | Maximizes the value of human expert time (efficient annotation). | Requires a human-in-the-loop workflow. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Directional Stimulus Prompting | Using a separate small model to generate "hints" or keywords to guide the main LLM. | Extracting keywords (e.g., "Heart", "Attack") first, then feeding them to the LLM to generate the summary. | Can focus the model on specific medical sections (e.g., "Focus only on cardiac events"). | Requires training or prompting an auxiliary policy model. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Program-Aided Language Models (PAL) | Generating code to solve reasoning steps. | Writing a Python script to extract and sort dates of admission from the text. | Extremely precise for structured data extraction (dates, dosages). | Fails if the medical text is too unstructured or uses ambiguous natural language. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| ReAct (Reasoning + Acting) | Interleaving reasoning traces with action execution. | "Thought: I need to check if this drug interacts with... Action: Search drug database." | Good for clinical decision support agents. | Overly complex for the specific task of generating static Golden Answers from text. | [REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS (arXiv)](https://arxiv.org/pdf/2210.03629)<br>[Prompt Engineering Guide: ReAct Prompting (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb) |
| Reflexion | An agent reflecting on past mistakes to improve future responses. | The model generates a summary, checks it against rules, critiques itself ("I missed the date"), and rewrites. | Improves quality iteratively without human intervention. | Can get stuck in loops if the self-critique is flawed. | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/pdf/2303.11366)<br>[Prompt Engineering: Part 2 - Best Practices for Software Developers in Digital Industries](https://blogs.sw.siemens.com/thought-leadership/prompt-engineering-part-2-best-practices-for-software-developers-in-digital-industries/) |
| Multimodal CoT | Chain-of-Thought with images and text. | Analyzing X-rays alongside the radiology report. | Essential if the GraSCCo corpus contained images (it does not, it is text-based). | Not applicable to text-only medical corpora. | [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Graph-Prompting | Representing data as a graph structure within the prompt. | Mapping patient symptoms to a knowledge graph of diseases. | Good for understanding relationships (Symptom A -> Disease B). | Text-to-Graph conversion is difficult and error-prone. | [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/pdf/2308.09687) |
| Meta-Prompting | Asking the model to assume a persona or higher-level view. | "Act as a senior medical consultant reviewing a junior doctor's note." | Can improve the tone and professionality of the output. | Mostly affects style, less impact on factual extraction accuracy. | [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/)<br>[Prompt Engineering Guide](https://www.promptingguide.ai/) |
