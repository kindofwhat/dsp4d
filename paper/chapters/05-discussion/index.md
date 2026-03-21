<!-- #D-INTRO — AI-generated (Claude, Feb 2026) — see paper/INSTRUCTIONS.md -->

# Discussion

## Interpretation of Results

<!-- #D-SIZE — update numbers from #R-TAB-COMPOSITE when JSON changes -->
### Model Size Does Not Linearly Predict Performance

The results challenge the assumption that larger models necessarily produce better outputs for clinical extraction tasks. While Gemini 2.5 Pro — the largest model — achieves the highest composite score (0.468), the ranking among SLMs reveals no consistent correlation between parameter count and output quality. Granite 3.3 with only 2B parameters (composite: 0.344) outperforms GLM4:9b (0.335), Qwen2:7b (0.315), Phi3.5:3.8b (0.303), and Llama3:8b (0.300) — models with two to four times as many parameters. Similarly, Mistral-Nemo at 12B parameters (0.339) performs only marginally better than the 2B Granite model. Notably, Qwen3.5-35B-A3B — a MoE model with only 3B active parameters — achieves 0.390, ranking ahead of all dense SLMs and closely matching GPT-5-nano (0.395).

This finding suggests that architecture, training data composition, and instruction-tuning quality matter more than raw parameter count for structured medical extraction tasks. The MoE architecture in particular demonstrates that efficient parameter utilisation can compensate for a smaller active parameter budget.

<!-- #D-CLOUD — update numbers from #R-TAB-COMPOSITE when JSON changes -->
### Cloud Models Retain an Advantage — But the Gap Is Narrower Than Expected

GPT-5-nano, despite being marketed as a "nano" model, achieves the highest semantic similarity across all models (0.861) and a 100% pass rate on this metric. However, its LLM-as-a-Judge scores (DAG: 0.510, LLM-Judge: 0.537) place it below Gemma3:27b (0.510/0.671) and Kimi-K2.5 (0.576/0.597) on clinical extraction quality, resulting in an overall composite of 0.395. Kimi-K2.5, hosted at the Swiss provider Infomaniak, achieves 0.398 — demonstrating that data-sovereign cloud deployment with comparable performance is feasible.

The gap between the best cloud model (Gemini: 0.468) and the best local SLM (Gemma3:27b: 0.409) is only 14% — a margin that may be bridgeable through context engineering strategies such as Few-Shot prompting or RAG, which were not applied in this Zero-Shot evaluation.

<!-- #D-FORMAT — update numbers from #R-TAB-JSON when JSON changes -->
### The Format Compliance Problem

The most critical practical finding is the systematic difficulty of smaller models to produce structurally valid JSON output. Mistral-Nemo (0.065), Phi3.5 (0.098), and Llama3 (0.129) exhibit severe structural compliance issues with high variance and frequent zero-score cases.

This has direct implications for clinical deployment: even when a model semantically "understands" the content (as evidenced by high semantic similarity scores), the output cannot be programmatically processed if it does not conform to the expected structure. In a production system, this would require either post-processing heuristics or a format-correction layer — both of which add complexity and potential failure modes.

Gemini 2.5 Pro (0.457) is the only model with no zero-score cases. Kimi-K2.5 (0.374), Qwen3.5-35B-A3B (0.371), and Gemma3:27b (0.362) also achieve strong mean scores, suggesting that reliable JSON generation in a Zero-Shot setting requires either large model capacity, MoE architectures, or explicit format training.

<!-- #D-SEMANTIC — update numbers from #R-TAB-SEMANTIC when JSON changes -->
### Semantic Understanding Is Preserved Across Model Sizes

Despite the structural compliance issues, semantic similarity scores remain relatively high across all models (0.650–0.861). This indicates that even small models (Granite 2B: 0.843, Qwen3.5-35B-A3B: 0.829, Phi3.5: 0.795) capture the medical content and its meaning to a reasonable degree. The bottleneck is not comprehension but instruction following — specifically, the ability to adhere to a prescribed output format while simultaneously extracting and condensing clinical information.

<!-- #D-MISTRAL — update numbers from #R-TAB-JUDGE when JSON changes -->
### Mistral-Nemo: An Outlier

Mistral-Nemo (12B) underperforms its parameter class significantly. Its JSON similarity score (0.065) is the second-lowest of all models, and its DAG score (0.424) remains below that of the 2B Granite model (0.407) despite having six times more parameters. While its LLM-Judge score (0.553) is mid-range, the overall composite (0.339) places it below Granite 3.3:2b (0.344). This suggests that the model's instruction-following capability for structured extraction in German clinical texts is inadequate despite its size, reinforcing the observation that model selection for domain-specific tasks cannot rely on parameter count alone.

The metric correlation analysis (Chapter 4, Figure \ref{fig:metric-correlation}) further supports these observations: LLM-as-a-Judge metrics show low correlation with lexical measures (r = 0.10–0.27), confirming that clinical extraction quality cannot be approximated by surface-level overlap metrics alone. Notably, JSON similarity correlates more strongly with the DAG metric (r = 0.45) than with any lexical metric, suggesting that format compliance and content quality are interdependent.

## Implications for Clinical Practice

The results carry several implications for the deployment of local LLMs in clinical settings:

1. **Viability of local deployment:** The semantic understanding scores (>0.75 for most models) demonstrate that local SLMs can extract medically relevant content from clinical documents. This validates the fundamental premise of the DSP4D project — that data-sovereign AI processing on local hardware is feasible.

2. **Format compliance as gating criterion:** For automated pipeline integration (e.g., updating patient records), JSON structural validity is a non-negotiable requirement. Based on the Zero-Shot results, Gemma3:27b and Qwen3.5-35B-A3B among the local models achieve acceptable structural compliance. Smaller dense models would require either Few-Shot examples demonstrating the exact output format or a dedicated format-correction step.

3. **Model selection should be task-driven:** The wide variance in performance across models of similar size (e.g., Granite 2B outperforming Mistral-Nemo 12B) indicates that model selection for clinical use cases must be empirically validated rather than inferred from benchmarks or parameter counts.

<!-- #D-RQ — update numbers from #R-TAB-PASS when JSON changes -->
## Addressing the Research Questions

**RQ1: What is the minimum model size for reliable clinical document classification in a Zero-Shot setting?**

No model — including Gemini 2.5 Pro — achieves a 95% pass rate across all metrics. When focusing on semantic similarity, GPT-5-nano and Granite 3.3:2b both achieve 100% pass rates, while Gemini 2.5 Pro reaches 93.5%. On the LLM-Judge metric, Gemini 2.5 Pro leads with 75.8%, followed by Gemma3:27b at 66.1%. The overall pass rates are notably lower than in previous evaluation runs due to the stricter GPT-4o-mini-based judge metrics: Gemini 2.5 Pro achieves 30.8% overall, Gemma3:27b 26.8%, and Kimi-K2.5 25.0%. Among local SLMs, Granite 3.3:2b reaches only 19.2% overall despite its 100% semantic similarity pass rate, highlighting the gap between semantic comprehension and structural/clinical extraction quality. In a Zero-Shot configuration, reliable classification across all quality dimensions requires at least a 27B model (Gemma3) or cloud-tier inference. Future work should investigate whether Few-Shot or RAG strategies can lower this threshold for smaller models.

**RQ2: Which context engineering strategy is most effective for generating high-quality reference answers, and how does it influence downstream evaluation?**

This study applied context engineering at two distinct levels. In Phase II, Chain-of-Thought (CoT) prompting was selected over 15 alternative strategies following a systematic comparison. CoT was chosen for its transparent reasoning process, zero-shot generalizability, and reduced hallucination risk — properties that are particularly valuable for medical text extraction where auditability is essential. The structured CoT prompt with an explicit internal monologue proved effective for generating clinically defensible silver answers from the GraSCCo corpus: the reasoning trace allowed verification that the model correctly distinguished current from discontinued medications, identified implicit diagnoses, and avoided fabricating clinical details.

In Phase III, the SLMs were evaluated in a Zero-Shot configuration to establish an unaugmented baseline. This deliberate separation allows the impact of context engineering to be measured in subsequent phases: the Zero-Shot results reported here serve as the control condition against which Few-Shot, RAG, and Long-Context strategies can be compared. Early indications — particularly the severe format compliance failures of smaller models — suggest that context engineering at the SLM evaluation level (e.g., Few-Shot examples demonstrating the expected JSON schema) may yield disproportionate improvements for structural quality.

**RQ3: Can sub-3B parameter models achieve clinically acceptable extraction quality on standard consumer hardware?**

Granite 3.3 (2B) demonstrates promising semantic comprehension (0.843 similarity, 100% pass rate) but falls short on structural compliance (0.258 JSON similarity). Interestingly, Qwen3.5-35B-A3B with only 3B active parameters (MoE architecture) achieves 0.371 JSON similarity and 0.390 overall composite — demonstrating that efficient architectures can significantly outperform dense models of similar active parameter count. In a Zero-Shot setting, dense sub-3B models capture the medical content but cannot reliably produce structured output that would be programmatically processable in a clinical pipeline. The bottleneck is not comprehension but instruction following — a capability that is known to improve significantly with Few-Shot examples and explicit format demonstrations. Whether targeted context engineering can close this gap is a key question for subsequent phases.

## Validity of the Evaluation Benchmark

A central methodological decision in this study is the use of LLM-generated *silver answers* rather than expert-authored *golden answers* as the evaluation benchmark. Three arguments support the validity of silver answers for this study's purposes.

**Relative comparison remains valid.** The primary objective is not to measure absolute clinical accuracy but to *rank* models against each other under identical conditions. Since all models are evaluated against the same reference, any systematic bias in the silver answers affects all models equally and cancels out in relative comparisons. A model that scores higher against a silver answer also demonstrates better instruction following, structural compliance, and content extraction — regardless of whether the reference itself is perfect.

**Consistent baseline across 62 test cases.** The target use case — a general practitioner updating a patient's health record from incoming specialist reports — defines a relatively narrow extraction task with limited interpretive ambiguity: the relevant diagnoses, medications, metrics, and follow-up actions are typically stated explicitly in the source text. Nevertheless, manually authoring 62 golden answers with the required JSON structure would demand significant expert time and would itself introduce variability depending on the annotator's thoroughness and attention. A SOTA model with CoT reasoning produces a consistent, reproducible baseline across all test cases, ensuring that performance differences between evaluated models reflect genuine capability gaps rather than annotation inconsistencies.

**Methodological mitigation through Chain-of-Thought.** The silver answers were not generated naively. The CoT prompt forces the model to expose its reasoning — identifying evidence in the source text before committing to structured fields. This internal monologue provides an audit trail that makes the silver answers more transparent than opaque single-pass extractions: a reviewer can trace each extracted field back to the model's reasoning and the corresponding passage in the source document.

**Acknowledged limitation.** Two forms of bias must be considered. First, lexical metrics (BLEU, ROUGE, Token F1) inherently reward surface-level similarity to the reference text — a model that paraphrases the same medical content differently will score lower regardless of correctness. This is a property of the metrics themselves and is partially mitigated by including semantic similarity alongside lexical measures. Second, LLM-as-a-Judge evaluation introduces the well-documented self-preference bias: LLM judges tend to favour outputs stylistically similar to their own generations [@panickssery2024llmevaluatorsrecognizefavor]. Since the silver answers were generated by Gemini while the judge is GPT-4o-mini, these two biases do not compound directly — but neither can be fully eliminated.

<!-- #D-LIMITS — mostly static, update only if methodology changes -->
## Limitations

1. **Single prompting strategy:** All results reflect a Zero-Shot configuration. The system prompt used for the SLM evaluation differs from the CoT prompt used for Silver Answer generation (it omits the chain-of-thought reasoning structure). Performance may improve substantially with Few-Shot examples or explicit CoT instructions.

2. **Silver Answer bias:** The reference answers were generated by a large model (Gemini) and only partially validated by a medical expert. As AI-generated Silver Answers — not expert-authored Golden Answers — they carry inherent bias: evaluation metrics favour outputs that resemble the Silver Answer's style and phrasing, which may disadvantage models that express the same medical content differently.

3. **Single evaluation run:** Each model-document combination was executed once. Stochastic variation in model outputs is not captured. Self-Consistency (multiple runs with majority voting) was not applied. The token cost of the LLM-as-a-Judge metrics (~6,000–10,000 tokens per interaction; see [Appendix: Token Cost per Evaluation Interaction](#appendix-token-cost)) makes multi-run approaches expensive: a 10-run self-consistency evaluation across all models and test cases would require 40–70 million judge tokens.

4. **Hardware heterogeneity:** Local SLMs were executed on a single machine via Ollama, while cloud models used provider-optimised infrastructure. Latency comparisons are therefore not directly comparable across these deployment modes.

5. **German clinical text:** The evaluation is specific to German-language clinical documents from the GraSCCo corpus. Generalisability to other languages or clinical text types is not established.

6. **Metric thresholds:** The overall pass rates are notably low even for top-performing models (Gemini: 30.8%), partly because the stricter GPT-4o-mini-based judge metrics and lexical metrics apply thresholds that may be overly demanding for this extraction task, where semantically equivalent but lexically diverse outputs are expected.

<!-- #D-FUTURE — static -->
## Future Work

1. **Context engineering evaluation:** Systematic evaluation of Few-Shot, RAG, and Long-Context strategies across all models to quantify the impact of context engineering on the size-accuracy trade-off — particularly for format compliance in small models.

2. **Prompt optimisation for SLMs:** The current system prompt was designed for a SOTA model. Adapting prompts specifically for smaller models (e.g., simpler instructions, explicit format examples) may yield disproportionate improvements.

3. **Self-Consistency runs:** Applying the multi-sample estimation approach (5–10 runs per document) to assess output stability and reduce stochastic variance.

4. **Expanded expert validation:** Involving multiple medical experts to elevate Silver Answers to true Golden Answers and reduce single-annotator bias.

5. **Fine-tuning exploration:** Investigating whether task-specific fine-tuning of small models (2–7B) on a subset of validated reference answers can close the format compliance gap observed in Zero-Shot evaluation.
