# Related Work

## LLM in the Context of Medical Science

The application of Large Language Models (LLMs) in medicine is an evolution of clinical Natural Language Processing (NLP), which gained significant momentum with the release of specialized models like ClinicalBERT [@alsentzer2019publicly]. While early models focused on entity recognition and extraction, modern LLMs offer the potential to summarize charts and suggest clinical actions. However, their integration into clinical workflows is constrained by critical requirements for accuracy, data privacy, and data sovereignty.

### Privacy, Security, and Data Sovereignty

These risks directly motivate the local deployment constraint in our methodology (Chapter 3) and inform the model selection criteria. The use of cloud-based LLMs in healthcare introduces significant risks that have been documented since the early days of transformer models.  

*   **Data Leakage and Memorization:** Foundational research has shown that LLMs can memorize and inadvertently "regurgitate" sensitive training data, including personally identifiable information (PII) [@carlini2021extracting]. In a medical context, this poses a risk of exposing protected health information (PHI) through model outputs.
*   **Adversarial Vulnerabilities:** Modern aligned models are susceptible to adversarial attacks, such as prompt injection, which can bypass safety filters and potentially lead to the disclosure of sensitive context or the generation of incorrect medical advice [@zou2023universal].
*   **Ethical and Regulatory Gaps:** A 2025 scoping review identifies a persistent lack of ethical oversight and informed consent in many LLM-based medical studies, highlighting an urgent need for privacy-preserving architectures [@Zhong2025Considerations].

To mitigate these risks, researchers are exploring **Data Sovereignty**—the principle that health data should remain under the control of the originating institution or the patient. This has led to two main research directions:

1.  **On-Device Deployment:** Operating models entirely on local hardware (e.g., Jetson Nano) to ensure no sensitive data ever leaves the clinical environment [@wu2025dualstage]. We use customer hardware in our work which are deployable locally.
2.  **Privacy-Preserving Training:** Techniques like "Whispered Tuning" and differential privacy are being developed to prevent PII memorization during model adaptation [@Singh2024WhisperedTuning]. This is out of scope for our work, since we rely on pretrained public models.

## Scaling Laws and Model Efficiency

Given the hardware constraints of on-device deployment for sensitive medical data, a central question is: what is the smallest pre-trained model that can reliably perform clinical document classification? The answer depends not only on parameter count, but also on model generation and — as Section 2.4 explores — context engineering strategies that can augment smaller models at inference time. The following subsections trace how scaling laws have evolved to make this question increasingly tractable.

Early scaling laws — notably by Kaplan et al. [@kaplan2020scaling] and Hoffmann et al. [@hoffmann2022training] — established that language model performance follows predictable power-law relationships with model size and training data. However, these findings predate the current generation of highly optimized small models and do not fully capture the capabilities of modern SLMs.

### The Rise of Small Language Models

A comprehensive survey by Lu et al. (2024) benchmarked 59 SLMs (100M–5B parameters) across commonsense reasoning, mathematics, and in-context learning tasks. Their findings reveal substantial performance improvements: SLMs improved by 10–13% between 2022 and 2024, outpacing larger models which improved by only 7.5% over the same period [@lu2024slmsurvey]. Notably, the Phi-3 model (3.8B parameters) achieves 69% on MMLU — performance comparable to Mixtral 8x7B and GPT-3.5. This demonstrates that modern SLMs, through optimized architectures and high-quality training data, can compete with models several times their size.

### A Note on Terminology

The term "Small Language Model" warrants clarification. In current usage, "small" refers exclusively to parameter count — not to training data scope. A 3B parameter model trained on trillions of web-scale tokens is considered "small" only relative to 70B+ frontier models. This stands in contrast to *domain-specific* models such as ClinicalBERT or PubMedBERT, which are smaller in both parameters and training scope, having been trained on specialized medical corpora. Throughout this thesis, the term SLM refers to language models with fewer than 100 billion parameters, regardless of their training data origin — consistent with the boundary used by Lu et al. [@lu2024slmsurvey] in their comprehensive SLM survey. This broader definition encompasses both general-purpose compact models (Phi, Qwen, Llama) and domain-specialized models, allowing for comparison across deployment scenarios.

### Capability Density and the Densing Law

Xiao et al. (2025) formalize this trend through the concept of *capability density* — defined as capability per parameter. Their empirical analysis reveals a "densing law": capability density approximately doubles every 3.5 months [@xiao2025densing]. This trajectory indicates that equivalent performance can be achieved with exponentially fewer parameters over time, making local deployment increasingly viable.

### Edge Deployment Considerations

Recent work specifically addresses SLM deployment on resource-constrained devices. Hassanpour et al. (2025) systematically evaluate SLMs for edge scenarios, examining the trade-offs between model size, quantization levels, and task performance [@hassanpour2025edge]. Their findings confirm that sub-4B parameter models can achieve practical utility for domain-specific tasks when properly configured — a key consideration for medical applications where data must remain on-device.

## Context Engineering Strategies

The performance of language models — whether large frontier models or compact SLMs — is not determined solely by parameter count or training data. The quality of model outputs depends critically on how tasks are formulated and presented at inference time. This principle, known as **prompt engineering** or **context engineering**, has emerged as a fundamental discipline for extracting reliable, accurate responses from language models.

### The Importance of Prompt Engineering for High-Quality Answers

Prompt engineering is the systematic practice of designing, refining, and optimizing the instructions and context provided to a language model to elicit desired outputs. In medical applications where accuracy is paramount, effective prompt engineering can mean the difference between a model producing clinically useful summaries and generating unreliable or hallucinated content.

**Why Prompt Engineering Matters:**

1. **Bridging the Capability Gap:** Even state-of-the-art models require carefully structured prompts to consistently produce high-quality outputs [@brown2020language]. A poorly formulated prompt can cause a capable model to underperform, while a well-engineered prompt can enable even smaller models to achieve surprisingly strong results — particularly relevant when deploying SLMs in resource-constrained environments.

2. **Reducing Hallucinations:** Language models are prone to generating plausible-sounding but factually incorrect information — a phenomenon known as hallucination [@ji2023survey]. In medical contexts, prompt engineering techniques such as chain-of-thought reasoning help ground model outputs in verifiable facts and reduce the risk of fabricated content.

3. **Ensuring Consistency and Reproducibility:** Medical documentation requires standardized formats and terminology. Structured prompting techniques ensure that outputs conform to required schemas and clinical standards [@bsharat2023principled].

4. **Maximizing Limited Resources:** For SLMs deployed on edge devices, carefully designed prompts can compensate for architectural limitations by providing explicit reasoning frameworks and domain-specific context [@lu2024slmsurvey].

5. **Enabling Transparent Reasoning:** Chain-of-Thought (CoT) prompting allows models to expose their reasoning process, making it possible to verify the logical steps that led to a conclusion [@wei2022chain; @kojima2022large]. This transparency is crucial for scientific validation and is the basis for generating the reference answers (silver answers) in this study.

The following sections detail specific prompt engineering techniques and their application to medical text processing, with particular emphasis on methods that enable reliable extraction of structured information from clinical narratives.

A comprehensive comparison of 20 prompting techniques is provided in [Appendix: Comprehensive Comparison of Prompting Techniques](#appendix-promp-techs). Based on this analysis, Chain-of-Thought (CoT) was selected for the following reasons.

### Chain-of-Thought: The Selected Technique for Generating Silver Answers

Among the prompting techniques analysed, **Chain-of-Thought (CoT) prompting** was selected for generating silver answers from medical documents. CoT balances transparency, generalizability, and accuracy for the following reasons:

**Transparent reasoning.** CoT explicitly exposes the model's reasoning steps, enabling researchers to trace how diagnoses, medications, and follow-up actions were extracted from the source text [@wei2022chain]. This audit trail is essential for scientific validation of silver answers.

**Zero-shot generalizability.** Zero-Shot CoT — achieved by instructing the model to reason step by step — eliminates the need for task-specific examples [@kojima2022large]. This allows the same prompt structure to generalise across the diverse medical specialties represented in GraSCCo without introducing selection bias through manually curated examples.

**Reduced hallucination.** By forcing the model to articulate and justify each extraction step, CoT makes it harder to fabricate information — the model must explicitly link each extracted field to evidence in the source document. While CoT itself does not guarantee hallucination-free output, it provides the structural foundation for verification-based techniques such as Chain-of-Verification [@dhuliawala2023chainofverification], which adds an explicit self-check step after the initial CoT reasoning to detect and correct unsupported claims.

**Simplicity and reproducibility.** Unlike multi-stage pipelines (prompt chaining) or computationally expensive approaches (self-consistency with 5–10× sampling), CoT requires only a single inference pass — reducing costs and enhancing reproducibility.

Alternative techniques such as prompt chaining, self-consistency, and multi-persona prompting offer additional guarantees but at substantially higher complexity and computational cost. For the scope of this study, CoT provides sufficient reasoning structure while remaining feasible for both large LLMs (silver answer generation) and smaller SLMs (evaluation phase). The concrete prompt design is detailed in Chapter 3.

