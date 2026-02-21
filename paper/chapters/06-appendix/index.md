# Appendices
## MMLU-Pro Benchmark Leaderboard

[MMLU-Pro Benchmark Leaderboard (filtered)](https://artificialanalysis.ai/evaluations/mmlu-pro?models=apriel-v1-5-15b-thinker%2Capriel-v1-6-15b-thinker%2Cqwen3-vl-8b-reasoning%2Cdeepseek-r1-qwen3-8b%2Cqwen3-14b-instruct-reasoning%2Cdeepseek-r1-distill-qwen-14b%2Cfalcon-h1r-7b%2Cnvidia-nemotron-nano-12b-v2-vl-reasoning%2Cnvidia-nemotron-nano-9b-v2-reasoning%2Cllama-3-1-nemotron-nano-4b-reasoning%2Cqwen3-4b-instruct-reasoning%2Cqwen3-vl-4b-reasoning%2Cqwen3-8b-instruct-reasoning%2Cdeepseek-r1-distill-llama-8b%2Cjamba-reasoning-3b%2Colmo-3-7b-think%2Cdeepseek-r1-distill-qwen-1-5b%2Cexaone-4-0-1-2b-reasoning%2Cqwen3-1.7b-instruct-reasoning%2Cqwen3-0.6b-instruct-reasoning&model-filters=open-source%2Ctiny-models%2Csmall-models%2Creasoning-models)

Filter: Size Class: Tiny, Small; Open Weights: Open Source; Reasoning: Reasoning; Paramters Count: <=18B
![MMLU-Pro Benchmark Leaderboard Reults](assets/03-Methgodology-MMLU-Pro-Benchmark-Leaderboard-Results.png)

This "Gold Standard" example now includes the **Internal Monologue**, which is the hallmark of the Chain of Thought (CoT) approach. It demonstrates how the model "thinks" through the German syntax before committing to the structured fields.

---

## Appendix: Gold Standard Example (CoT Approach)

Below is the processing of the same kardiologische report, but utilizing the **Klinische Analyse** to ensure clinical accuracy.

### Input: Sample Clinical Report (GraSCCo-Style)

**Bericht vom 14.03.2025 – Kardiologische Gemeinschaftspraxis Dr. Müller**

**Anamnese:** 68-jähriger Patient stellt sich zur Verlaufskontrolle bei bekannter arterieller Hypertonie und stabiler Angina Pectoris vor. Aktuell klagt der Patient über gelegentliches Herzstolpern.

**Befunde:** RR 145/90 mmHg, Puls 72/min (arrhythmisch). EKG zeigt neu aufgetretenes Vorhofflimmern. Labor: LDL 110 mg/dl, Kreatinin 0,9 mg/dl.

**Medikation:** Bisher Bisoprolol 5mg 1-0-0 und ASS 100mg 0-1-0.

**Beurteilung:** Umstellung der Antikoagulation aufgrund des Vorhofflimmerns notwendig.

**Plan:** Absetzen von ASS 100mg. Neuansetzung von Apixaban 5mg 1-0-1. Echokardiographie in 2 Wochen zur Klärung der Klappenfunktion.

---

### Output: Golden Answer (CoT)

### Klinische Analyse (Internal Monologue)

1. **Datum/Quelle:** Der Bericht ist datiert auf den 14.03.2025. Aussteller ist Dr. Müller (Kardiologie).
2. **Kategorisierung:** Da es sich um eine kardiologische Praxis handelt und Herzrhythmusstörungen (Vorhofflimmern) sowie Hypertonie behandelt werden, sind "Kardiologie" und "Innere Medizin" die passenden Fachbereiche.
3. **Diagnosen:** Bekannt sind Hypertonie und Angina Pectoris. Neu hinzu kommt "Vorhofflimmern" (dokumentiert via EKG).
4. **Messwerte:** RR (145/90), Puls (72, arrhythmisch), LDL (110) und Kreatinin (0,9) sind explizit gelistet.
5. **Medikation-Logik:** * *Status Quo:* Bisoprolol und ASS 100mg.
* *Änderung:* Der Text sagt "Absetzen von ASS" und "Neuansetzung von Apixaban". Bisoprolol wird nicht erwähnt, bleibt also Teil der aktuellen Medikation.
* *Wichtig:* Apixaban ist die neue Empfehlung aufgrund des Vorhofflimmerns.
6. **Follow-up:** Der Plan sieht eine Echokardiographie in 2 Wochen vor.

---

### Structured Health Record Update

1. **Categories:** Kardiologie, Innere Medizin
2. **Date and Source:** 14.03.2025; Kardiologische Gemeinschaftspraxis Dr. Müller
3. **Diagnosis:** Arterielle Hypertonie, stabile Angina Pectoris, neu aufgetretenes Vorhofflimmern (EKG-gesichert)
4. **Relevant metrics:** RR: 145/90 mmHg; Puls: 72/min (arrhythmisch); LDL: 110 mg/dl; Kreatinin: 0,9 mg/dl
5. **Current or adviced medications:** * **Aktuelle Medikation:** Bisoprolol 5mg (1-0-0)
* **Empfohlene/Verschriebene Medikation:** Apixaban 5mg (1-0-1); *Hinweis: ASS 100mg wurde abgesetzt.*
6. **Follow up:** Echokardiographie in 2 Wochen zur Klärung der Klappenfunktion.

---

### Evaluation of the CoT Benefit

As seen in section **5**, the CoT process allowed the model to explicitly realize that **ASS 100mg** is no longer "Current" but is part of the "Change" logic. Without CoT, a model might simply list all three drugs under "Current" because they all appear in the text.

## Appendix: Drilldown for SLM Selection for Evaluation

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