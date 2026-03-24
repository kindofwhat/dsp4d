# Related Work {#sec:related-work}

This following chapter reviews related work on LLM evaluation in medical contexts, scaling laws for small language models, and context engineering strategies that inform the methodology of this study.

## LLM in the Context of Medical Science

The application of Large Language Models (LLMs) in medicine is an evolution of clinical Natural Language Processing (NLP), which gained significant momentum with the release of specialized models like ClinicalBERT [@alsentzer2019publicly]. While early models focused on entity recognition and extraction, modern LLMs offer the potential to summarize charts and suggest clinical actions. However, their integration into clinical workflows is constrained by critical requirements for accuracy, data privacy, and data sovereignty.

### Privacy, Security, and Data Sovereignty

These risks directly motivate the local deployment constraint in our methodology (Chapter \ref{sec:methodology}) and inform the model selection criteria. The use of cloud-based LLMs in healthcare introduces significant risks that have been documented since the early days of transformer models.  

*   **Data Leakage and Memorization:** Foundational research has shown that LLMs can memorize and inadvertently "regurgitate" sensitive training data, including personally identifiable information (PII) [@carlini2021extracting]. In a medical context, this poses a risk of exposing protected health information (PHI) through model outputs.
*   **Adversarial Vulnerabilities:** Modern aligned models are susceptible to adversarial attacks, such as prompt injection, which can bypass safety filters and potentially lead to the disclosure of sensitive context or the generation of incorrect medical advice [@zou2023universal].
*   **Ethical and Regulatory Gaps:** A 2025 scoping review identifies a persistent lack of ethical oversight and informed consent in many LLM-based medical studies, highlighting an urgent need for privacy-preserving architectures [@Zhong2025Considerations].

To mitigate these risks, researchers are exploring **Data Sovereignty**—the principle that health data should remain under the control of the originating institution or the patient. This has led to two main research directions:

1.  **On-Device Deployment:** Operating models entirely on local hardware (e.g., Jetson Nano) to ensure no sensitive data ever leaves the clinical environment [@wu2025dualstage]. We use customer hardware in our work which are deployable locally.
2.  **Privacy-Preserving Training:** Techniques like "Whispered Tuning" and differential privacy are being developed to prevent PII memorization during model adaptation [@Singh2024WhisperedTuning]. This is out of scope for our work, since we rely on pretrained public models.

## Scaling Laws and Model Efficiency {#sec:scaling-laws}

Given the hardware constraints of on-device deployment for sensitive medical data, a central question is: what is the smallest pre-trained model that can reliably perform clinical document classification? The answer depends not only on parameter count, but also on model generation and — as Section \ref{sec:context-engineering} explores — context engineering strategies that can augment smaller models at inference time. The following subsections trace how scaling laws have evolved to make this question increasingly tractable.

Early scaling laws — notably by Kaplan et al. [@kaplan2020scaling] and Hoffmann et al. [@hoffmann2022training] — established that language model performance follows predictable power-law relationships with model size and training data. However, these findings predate the current generation of highly optimized small models and do not fully capture the capabilities of modern SLMs.

### The Rise of Small Language Models

A comprehensive survey by Lu et al. (2024) benchmarked 59 SLMs (100M–5B parameters) across commonsense reasoning, problem-solving, and mathematics tasks. SLM performance improved by 10–14% across these tasks between 2022 and 2024, while the LLaMA-7B series — used as a reference for open-source LLMs — improved by only 7.5% over the same period [@lu2024slmsurvey, Section 3.2]. This demonstrates that modern SLMs, through optimized architectures and high-quality training data, are rapidly closing the gap with models several times their size.

### Capability Density and the Densing Law

Xiao et al. (2025) formalize this trend through the concept of *capability density* — defined as capability per parameter. Their empirical analysis reveals a "densing law": capability density approximately doubles every 3.5 months [@xiao2025densing]. This trajectory indicates that equivalent performance can be achieved with exponentially fewer parameters over time, making local deployment increasingly viable.

### Edge Deployment Considerations

Recent work specifically addresses SLM deployment on resource-constrained devices. Hassanpour et al. (2025) systematically evaluate SLMs for edge scenarios, examining the trade-offs between model size, quantization levels, and task performance [@hassanpour2025edge]. Their findings confirm that sub-4B parameter models can achieve practical utility for domain-specific tasks when properly configured — a key consideration for medical applications where data must remain on-device.

### A Note on Terminology

The term "Small Language Model" warrants clarification. In current usage, "small" refers exclusively to parameter count — not to training data scope. A 3B parameter model trained on trillions of web-scale tokens is considered "small" only relative to 70B+ frontier models. This stands in contrast to *domain-specific* models such as ClinicalBERT or PubMedBERT, which are smaller in both parameters and training scope, having been trained on specialized medical corpora. Throughout this thesis, the term SLM refers to language models with fewer than 100 billion parameters, regardless of their training data origin — consistent with the boundary used by Lu et al. [@lu2024slmsurvey] in their comprehensive SLM survey. This broader definition encompasses both general-purpose compact models (Phi, Qwen, Llama) and domain-specialized models, allowing for comparison across deployment scenarios.

## Context Engineering Strategies {#sec:context-engineering}

The performance of language models — whether large frontier models or compact SLMs — is not determined solely by parameter count or training data. The quality of model outputs depends critically on how tasks are formulated and presented at inference time. This principle, known as **prompt engineering** or **context engineering**, has emerged as a fundamental discipline for extracting reliable, accurate responses from language models.

### The Importance of Prompt Engineering for High-Quality Answers

Prompt engineering is the systematic practice of designing, refining, and optimizing the instructions and context provided to a language model to elicit desired outputs. In medical applications where accuracy is paramount, effective prompt engineering can mean the difference between a model producing clinically useful summaries and generating unreliable or hallucinated content.

**Why Prompt Engineering Matters:**

1. **Bridging the Capability Gap:** Even state-of-the-art models require carefully structured prompts to consistently produce high-quality outputs. A poorly formulated prompt can cause a capable model to underperform, while a well-engineered prompt can enable even smaller models to achieve surprisingly strong results. This is particularly relevant when deploying SLMs in resource-constrained environments where model size is limited by hardware constraints.[@kojima2022large] [@zhao2021calibrate]

2. **Improving Traceability:** Language models are prone to generating plausible-sounding but factually incorrect information — a phenomenon known as hallucination [@ji2023survey]. While standard CoT prompting does not inherently reduce hallucination rates [@dhuliawala2023chainofverification], it exposes the model's reasoning steps, enabling reviewers to trace extracted information back to the source document and identify unsupported claims.


3. **Ensuring Consistency and Reproducibility:** Medical documentation requires standardized formats and terminology. Without explicit guidance through prompts, models may produce outputs in inconsistent formats, use non-standard terminology, or omit critical information. Structured prompting techniques ensure that outputs conform to required schemas and clinical standards. [@ning2024skeletonofthought] [@shinn2023reflexion]

**Maximizing Limited Resources:** For SLMs deployed on edge devices, prompt engineering becomes even more critical. Since these models have fewer parameters and potentially less training data than frontier models, carefully designed prompts can compensate for architectural limitations by providing explicit reasoning frameworks and domain-specific context. (Lu et al. 2024) [@hassanpour2025edge]

5. **Enabling Transparent Reasoning:** When using LLMs to generate reference answers for evaluation purposes — as in this study, where a SOTA model produces structured reference extractions called *silver answers* (see Section \ref{sec:golden-answer-generation} for formal definitions) — prompt engineering is essential for ensuring that these references are accurate, complete, and scientifically defensible. Chain-of-Thought (CoT) prompting, in particular, allows models to expose their reasoning process, making it possible to verify the logical steps that led to a conclusion. This transparency is crucial for scientific validation: rather than accepting a model's output as a black box, researchers can inspect the intermediate reasoning steps to identify potential errors, biases, or hallucinations. Zero-shot CoT, which requires no task-specific examples, offers the additional advantage of generalizability across diverse medical documents without the need for manual example curation.[@kojima2022large] [@wu2022promptchainer]

A comprehensive comparison of 20 prompting techniques is provided in [Appendix: Comprehensive Comparison of Prompting Techniques](#appendix-promp-techs). Based on this analysis, Chain-of-Thought (CoT) was selected for the following reasons.

### Chain-of-Thought: The Selected Technique for Generating Silver Answers

Among the prompting techniques analysed, **Chain-of-Thought (CoT) prompting** was selected for generating silver answers from medical documents. CoT balances transparency, generalizability, and accuracy for the following reasons:

**Transparent reasoning.** CoT explicitly exposes the model's reasoning steps, enabling researchers to trace how diagnoses, medications, and follow-up actions were extracted from the source text [@wei2022chain]. This audit trail is essential for scientific validation of silver answers.

**Zero-shot generalizability.** Zero-Shot CoT — achieved by instructing the model to reason step by step — eliminates the need for task-specific examples [@kojima2022large]. This allows the same prompt structure to generalise across the diverse medical specialties represented in the GraSCCo corpus (see Section \ref{sec:data-source}) without introducing selection bias through manually curated examples.

**Traceability over hallucination reduction.** It is important to note that CoT does not inherently reduce hallucination rates — Dhuliawala et al. found that standard CoT prompting fails to improve factual accuracy and may even increase incorrect outputs compared to few-shot baselines [@dhuliawala2023chainofverification]. However, CoT's value lies in *traceability*: by forcing the model to articulate its reasoning, each extracted field can be traced back to evidence in the source document, making hallucinations *detectable* rather than hidden. For active hallucination mitigation, Chain-of-Verification (CoVe) [@dhuliawala2023chainofverification] adds an explicit self-check step after CoT reasoning — a promising extension for future work.

**Simplicity and reproducibility.** Unlike multi-stage pipelines (prompt chaining) or computationally expensive approaches (self-consistency with 5–10× sampling), CoT requires only a single inference pass — reducing costs and enhancing reproducibility.

Alternative techniques such as prompt chaining, self-consistency, and multi-persona prompting offer additional guarantees but at substantially higher complexity and computational cost. For the scope of this study, CoT provides sufficient reasoning structure while remaining feasible for both large LLMs (silver answer generation) and smaller SLMs (evaluation phase). The concrete prompt design is detailed in Chapter \ref{sec:methodology}. 

More sophisticated variants — such as Tree-of-Thought [@yao2023treethoughts], Chain-of-Verification [@dhuliawala2023chainofverification], and Self-Consistency [@wang2023selfconsistency] — extend CoT with branching, self-correction, or multi-sample voting. These techniques are acknowledged as promising directions for future work (Chapter \ref{sec:discussion}) but fall outside the scope of this initial evaluation, which deliberately uses standard Zero-Shot CoT to establish an unaugmented baseline.