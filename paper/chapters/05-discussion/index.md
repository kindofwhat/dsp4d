<!-- #D-INTRO — AI-generated (Claude, Feb 2026) — see paper/INSTRUCTIONS.md -->

# Discussion

## Interpretation of Results

<!-- #D-SIZE — update numbers from #R-TAB-COMPOSITE when JSON changes -->
### Model Size Does Not Linearly Predict Performance

The results challenge the assumption that larger models necessarily produce better outputs for clinical extraction tasks. While Gemini 2.5 Pro — the largest model — achieves the highest composite score (0.470), the ranking among SLMs reveals no consistent correlation between parameter count and output quality. Granite 3.3 with only 2B parameters (composite: 0.390) outperforms GLM4:9b (0.363), Qwen2:7b (0.360), and Phi3.5:3.8b (0.338) — models with two to four times as many parameters. Similarly, Mistral-Nemo at 12B parameters (0.330) ranks second-to-last, performing below the 2B Granite model on both statistical and LLM-as-a-Judge metrics.

This finding suggests that architecture, training data composition, and instruction-tuning quality matter more than raw parameter count for structured medical extraction tasks.

<!-- #D-CLOUD — update numbers from #R-TAB-COMPOSITE when JSON changes -->
### Cloud Models Retain an Advantage — But the Gap Is Narrower Than Expected

GPT-5-nano, despite being marketed as a "nano" model, achieves the highest semantic similarity across all models (0.861) and a 100% pass rate on this metric. It closely matches the 27B Gemma3 model on the overall composite score (0.419 vs. 0.416). This indicates that recent cloud-optimised small models benefit from distillation techniques and training data quality that local open-weight models have not yet matched.

However, the gap between the best cloud model (Gemini: 0.470) and the best local SLM (Gemma3:27b: 0.416) is only 13% — a margin that may be bridgeable through context engineering strategies such as Few-Shot prompting or RAG, which were not applied in this Zero-Shot evaluation.

<!-- #D-FORMAT — update numbers from #R-TAB-JSON when JSON changes -->
### The Format Compliance Problem

The most critical practical finding is the systematic failure of smaller models to produce structurally valid JSON output. Llama3:8b scores 0.000 on JSON structural similarity across all 62 test cases — it never produces output matching the expected schema. Mistral-Nemo (0.059) and Phi3.5 (0.103) also exhibit severe structural compliance issues.

This has direct implications for clinical deployment: even when a model semantically "understands" the content (as evidenced by high semantic similarity scores), the output cannot be programmatically processed if it does not conform to the expected structure. In a production system, this would require either post-processing heuristics or a format-correction layer — both of which add complexity and potential failure modes.

Notably, Gemma3:27b (0.372) and Gemini 2.5 Pro (0.440) are the only models that consistently produce structured output, suggesting that reliable JSON generation in a Zero-Shot setting may require either larger model capacity or explicit format training.

<!-- #D-SEMANTIC — update numbers from #R-TAB-SEMANTIC when JSON changes -->
### Semantic Understanding Is Preserved Across Model Sizes

Despite the structural compliance issues, semantic similarity scores remain relatively high across all models (0.650–0.861), with the exception of Llama3:8b. This indicates that even small models (Granite 2B: 0.843, Phi3.5: 0.797) capture the medical content and its meaning to a reasonable degree. The bottleneck is not comprehension but instruction following — specifically, the ability to adhere to a prescribed output format while simultaneously extracting and condensing clinical information.

<!-- #D-MISTRAL — update numbers from #R-TAB-JUDGE when JSON changes -->
### Mistral-Nemo: An Outlier

Mistral-Nemo (12B) underperforms its parameter class significantly. Its DAG medical extraction quality score (0.261) is the lowest of all models — worse than Granite at 2B (0.528). Combined with its near-zero JSON structural similarity (0.059), this suggests that the model's instruction-following capability for structured extraction in German clinical texts is inadequate despite its size. This reinforces the observation that model selection for domain-specific tasks cannot rely on parameter count alone.

## Implications for Clinical Practice

The results carry several implications for the deployment of local LLMs in clinical settings:

1. **Viability of local deployment:** The semantic understanding scores (>0.75 for most models) demonstrate that local SLMs can extract medically relevant content from clinical documents. This validates the fundamental premise of the DSP4D project — that data-sovereign AI processing on local hardware is feasible.

2. **Format compliance as gating criterion:** For automated pipeline integration (e.g., updating patient records), JSON structural validity is a non-negotiable requirement. Based on the Zero-Shot results, only Gemma3:27b among the local SLMs achieves acceptable structural compliance. Smaller models would require either Few-Shot examples demonstrating the exact output format or a dedicated format-correction step.

3. **Model selection should be task-driven:** The wide variance in performance across models of similar size (e.g., Granite 2B outperforming Mistral-Nemo 12B) indicates that model selection for clinical use cases must be empirically validated rather than inferred from benchmarks or parameter counts.

<!-- #D-RQ — update numbers from #R-TAB-PASS when JSON changes -->
## Addressing the Research Questions

**RQ1: What is the minimum model size for reliable document classification (>95% accuracy)?**

No model — including Gemini 2.5 Pro — achieves a 95% pass rate across all metrics. However, when focusing on the clinically most relevant metrics (LLM-Judge correctness and semantic similarity), Gemini 2.5 Pro reaches 90.3% and 93.5% respectively. Among local SLMs, Granite 3.3:2b achieves 100% pass rate on semantic similarity but only 58.1% on LLM-Judge correctness. The 95% threshold is not met by any local model in a Zero-Shot configuration. Context engineering strategies (Few-Shot, RAG) remain to be evaluated.

**RQ2: How do different context engineering strategies affect the size-accuracy trade-off?**

This evaluation presents the Zero-Shot baseline only. The impact of Few-Shot learning, RAG, and Long-Context strategies on the size-accuracy trade-off is subject to subsequent evaluation phases.

**RQ3: Can sub-3B parameter models achieve clinical safety standards with appropriate context?**

Granite 3.3 (2B) demonstrates promising semantic comprehension (0.843 similarity, 100% pass rate) but falls short on structural compliance (0.254 JSON similarity). In a Zero-Shot setting, sub-3B models cannot yet meet clinical safety standards across all dimensions. Whether Few-Shot examples can close this gap — particularly for format compliance — is a key question for subsequent phases.

<!-- #D-LIMITS — mostly static, update only if methodology changes -->
## Limitations

1. **Single prompting strategy:** All results reflect a Zero-Shot configuration. The system prompt used for the SLM evaluation differs from the CoT prompt used for Silver Answer generation (it omits the chain-of-thought reasoning structure). Performance may improve substantially with Few-Shot examples or explicit CoT instructions.

2. **Silver Answer bias:** The reference answers were generated by a large model (Gemini) and only partially validated by a medical expert. As AI-generated Silver Answers — not expert-authored Golden Answers — they carry inherent bias: evaluation metrics favour outputs that resemble the Silver Answer's style and phrasing, which may disadvantage models that express the same medical content differently.

3. **Single evaluation run:** Each model-document combination was executed once. Stochastic variation in model outputs is not captured. Self-Consistency (multiple runs with majority voting) was not applied.

4. **Hardware heterogeneity:** Local SLMs were executed on a single machine via Ollama, while cloud models used provider-optimised infrastructure. Latency comparisons are therefore not directly comparable across these deployment modes.

5. **German clinical text:** The evaluation is specific to German-language clinical documents from the GraSCCo corpus. Generalisability to other languages or clinical text types is not established.

6. **Metric thresholds:** The near-zero pass rates on lexical metrics (BLEU, ROUGE, Token F1) across all models — including the reference Gemini model — suggest that the pass thresholds for these metrics may be miscalibrated for this extraction task, where semantically equivalent but lexically diverse outputs are expected.

<!-- #D-FUTURE — static -->
## Future Work

1. **Context engineering evaluation:** Systematic evaluation of Few-Shot, RAG, and Long-Context strategies across all models to quantify the impact of context engineering on the size-accuracy trade-off — particularly for format compliance in small models.

2. **Prompt optimisation for SLMs:** The current system prompt was designed for a SOTA model. Adapting prompts specifically for smaller models (e.g., simpler instructions, explicit format examples) may yield disproportionate improvements.

3. **Self-Consistency runs:** Applying the multi-sample estimation approach (5–10 runs per document) to assess output stability and reduce stochastic variance.

4. **Expanded expert validation:** Involving multiple medical experts to elevate Silver Answers to true Golden Answers and reduce single-annotator bias.

5. **Fine-tuning exploration:** Investigating whether task-specific fine-tuning of small models (2–7B) on a subset of validated reference answers can close the format compliance gap observed in Zero-Shot evaluation.
