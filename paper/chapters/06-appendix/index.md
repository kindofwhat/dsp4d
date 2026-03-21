# Appendices

## Comprehensive Comparison of Prompting Techniques {#appendix-promp-techs}

| Technique                |                                                                    |
|--------------------------|----------------------------------------------------------------------|
| Zero-Shot Prompting | **Description:** Asking the model to perform a task without examples|
||**Application to Medical Silver Answers:** "Extract all diagnoses from this text."|
||**Pros for Medical Records:** Fast and low token cost. Useful for checking the baseline capability of a model.|
||**Cons / Risks:** High risk of hallucination and format inconsistency. The model may guess the required medical style incorrectly. |
||**References:** [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Few-Shot Prompting | **Description:** Providing examples (input-output pairs) within the prompt.
||**Application to Medical Silver Answers:** "Style Guide: You provide 3 examples of GraSCCo raw text and the corresponding perfect "Silver Answer" format. (possible after first supervision session)"|
||**Pros for Medical Records:** Essential for enforcing the specific syntax and brevity required for the Silver Answers.|
||**Cons / Risks:** The model may overfit to the examples and ignore the nuance of the new input.|
||**References:** [@brown2020language], [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Chain-of-Thought (CoT) | **Description:** Instructing the model to generate intermediate reasoning steps.
||**Application to Medical Silver Answers:** Clinical Reasoning: "First, list all medications found. Second, check if they are current or historical. Finally, output the list."|
||**Pros for Medical Records:** Critical for connecting implied symptoms to explicit medical codes. Reduces "skipping" of details.|
||**Cons / Risks:** Increases token usage. Requires parsing to separate the "thought" from the "silver answer."|
||**References:** [@wei2022chain], [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Self-Consistency | **Description:** Generating multiple outputs for the same prompt and selecting the most frequent one.|
||**Application to Medical Silver Answers:** Validation: Generate the summary 5 times. If "Diabetes Type 2" appears in 5/5, keep it. If "Hypertension" appears in 1/5, discard it.|
||**Pros for Medical Records:** The best statistical defense against hallucinations. Essential for creating a robust "Gold Standard".|
||**Cons / Risks:** Computationally expensive (requires N times the inference cost).|
||**References:** [@wang2023selfconsistency], [@k2view2024prompttechniques] |
| Skeleton-of-Thought (SoT) | **Description:** Generating a skeleton/outline first, then expanding points in parallel.|
||**Application to Medical Silver Answers:** Structure Planning: 1. Generate list of headers (Dx, Rx). 2. Fill sections in parallel.|
||**Pros for Medical Records:** Accelerates generation speed (up to 2.39x). Good for long, structured discharge summaries.|
||**Cons / Risks:** Suited for writing new content, less proven for extracting specific facts from existing chaos.|
||**References:** [@ning2024skeletonofthought] |
| Prompt Chaining | **Description:** Breaking a task into subtasks where output A becomes input B.|
||**Application to Medical Silver Answers:** Workflow: 1. Extraction Prompt -> 2. Filtering Prompt -> 3. Formatting Prompt.|
||**Pros for Medical Records:** High reliability. Isolates errors. Allows for intermediate transformation (e.g., cleaning citations).|
||**Cons / Risks:** Requires building a controller application (state management) between prompts.|
||**References:** [@dairai2024promptguide], [@wu2022promptchainer] |
| Role / Persona Prompting | **Description:** Assigning a specific role/profession to the AI.|
||**Application to Medical Silver Answers:** Context Setting: "You are a Senior Chief Physician at a Swiss hospital..."|
||**Pros for Medical Records:** Drastically improves tone and handling of medical abbreviations/jargon.|
||**Cons / Risks:** Can lead to verbosity if the persona is too "chatty."|
||**References:** [@siemens2024promptengineering], [@dairai2024promptguide], [@k2view2024prompttechniques] |
| Multi-Persona Prompting | **Description:** Simulating a discussion between multiple agents (e.g., Drafter & Reviewer).|
||**Application to Medical Silver Answers:** Quality Assurance: Agent A extracts data; Agent B reviews it for missing info; Agent C finalizes.|
||**Pros for Medical Records:** Simulates a "four-eyes principle" (peer review), reducing errors through internal debate.|
||**Cons / Risks:** High latency and token cost; complex to orchestrate.|
||**References:** [@prompthub2024multipersona] |
| Tree of Thoughts (ToT) | **Description:** Exploring multiple reasoning paths and backtracking.|
||**Application to Medical Silver Answers:** Complex Triage: Exploring different diagnostic possibilities before committing to one.|
||**Pros for Medical Records:** Useful for complex differential diagnosis problems.|
||**Cons / Risks:** Likely overkill for extraction tasks where the answer is explicitly in the text.|
||**References:** [@yao2023tree] |
| Retrieval Augmented Generation (RAG) | **Description:** Retrieving external data to ground the generation.|
||**Application to Medical Silver Answers:** Fact Checking: Using a vector DB to validate if an extracted drug name exists in RxNorm.|
||**Pros for Medical Records:** Prevents hallucination of non-existent drugs; ensures terminology standardization.|
||**Cons / Risks:** Requires external database infrastructure. And a document base.|
||**References:** [@k2view2024prompttechniques], [@dairai2024promptguide] |
| Automatic Prompt Engineer (APE) | **Description:** Using an LLM to generate and optimize prompts.|
||**Application to Medical Silver Answers:** Asking GPT-4 to write the optimal prompt for analyzing GraSCCo texts.|
||**Pros for Medical Records:** Saves time on trial-and-error.|
||**Cons / Risks:** The resulting prompt might be obscure/hard to interpret.|
||**References:** [@dairai2024promptguide] |
| Generated Knowledge Prompting | **Description:** Asking the model to generate relevant knowledge before answering.|
||**Application to Medical Silver Answers:** "List common side effects of Ibuprofen, then summarize the patient's complaints regarding medication."|
||**Pros for Medical Records:** Can help if the medical text is ambiguous (e.g., vague symptoms), providing context for the summary.|
||**Cons / Risks:** Risk of generating false knowledge (hallucinated medical facts) which then contaminates the summary.|
||**References:** [@dairai2024promptguide] |
| Automatic Reasoning and Tool-use | **Description:** Allowing the LLM to use external tools (calculators, APIs).|
||**Application to Medical Silver Answers:** Calculating cumulative dosage or converting units (e.g., mg to g) found in the text.|
||**Pros for Medical Records:** Ensures mathematical accuracy in the medical record (e.g., total radiation dose).|
||**Cons / Risks:** Adds complexity; the model might fail to invoke the tool correctly.|
||**References:** [@schick2023toolformer] |
| Active-Prompt | **Description:** Selecting the most uncertain examples for human annotation to teach the model.|
||**Application to Medical Silver Answers:** Identifying GraSCCo texts where the model is "unsure" and asking a doctor to manually create the Silver Answer.|
||**Pros for Medical Records:** Maximizes the value of human expert time (efficient annotation).|
||**Cons / Risks:** Requires a human-in-the-loop workflow.|
||**References:** [@dairai2024promptguide] |
| Directional Stimulus Prompting | **Description:** Using a separate small model to generate "hints" or keywords to guide the main LLM.|
||**Application to Medical Silver Answers:** Extracting keywords (e.g., "Heart", "Attack") first, then feeding them to the LLM to generate the summary.|
||**Pros for Medical Records:** Can focus the model on specific medical sections (e.g., "Focus only on cardiac events").|
||**Cons / Risks:** Requires training or prompting an auxiliary policy model.|
||**References:** [@dairai2024promptguide] |
| Program-Aided Language Models (PAL) | **Description:** Generating code to solve reasoning steps.|
||**Application to Medical Silver Answers:** Writing a Python script to extract and sort dates of admission from the text.|
||**Pros for Medical Records:** Extremely precise for structured data extraction (dates, dosages).|
||**Cons / Risks:** Fails if the medical text is too unstructured or uses ambiguous natural language.|
||**References:** [@dairai2024promptguide] |
| ReAct (Reasoning + Acting) | **Description:** Interleaving reasoning traces with action execution.|
||**Application to Medical Silver Answers:** "Thought: I need to check if this drug interacts with... Action: Search drug database."|
||**Pros for Medical Records:** Good for clinical decision support agents.|
||**Cons / Risks:** Overly complex for the specific task of generating static Silver Answers from text.|
||**References:** [@yao2023react], [@dairai2024promptguide] |
| Reflexion | **Description:** An agent reflecting on past mistakes to improve future responses.|
||**Application to Medical Silver Answers:** The model generates a summary, checks it against rules, critiques itself ("I missed the date"), and rewrites.|
||**Pros for Medical Records:** Improves quality iteratively without human intervention.|
||**Cons / Risks:** Can get stuck in loops if the self-critique is flawed.|
||**References:** [@shinn2023reflexion], [@siemens2024promptengineering] |
| Multimodal CoT | **Description:** Chain-of-Thought with images and text.|
||**Application to Medical Silver Answers:** Analyzing X-rays alongside the radiology report.|
||**Pros for Medical Records:** Essential if the GraSCCo corpus contained images (it does not, it is text-based).|
||**Cons / Risks:** Not applicable to text-only medical corpora.|
||**References:** [@dairai2024promptguide] |
| Graph-Prompting | **Description:** Representing data as a graph structure within the prompt.|
||**Application to Medical Silver Answers:** Mapping patient symptoms to a knowledge graph of diseases.|
||**Pros for Medical Records:** Good for understanding relationships (Symptom A -> Disease B).|
||**Cons / Risks:** Text-to-Graph conversion is difficult and error-prone.|
||**References:** [@besta2024graphofthoughts] |
| Meta-Prompting | **Description:** Asking the model to assume a persona or higher-level view.|
||**Application to Medical Silver Answers:** "Act as a senior medical consultant reviewing a junior doctor's note."|
||**Pros for Medical Records:** Can improve the tone and professionality of the output.|
||**Cons / Risks:** Mostly affects style, less impact on factual extraction accuracy.|
||**References:** [@k2view2024prompttechniques], [@dairai2024promptguide] |

## MMLU-Pro Benchmark Leaderboard

[MMLU-Pro Benchmark Leaderboard (filtered)](https://artificialanalysis.ai/evaluations/mmlu-pro?models=apriel-v1-5-15b-thinker%2Capriel-v1-6-15b-thinker%2Cqwen3-vl-8b-reasoning%2Cdeepseek-r1-qwen3-8b%2Cqwen3-14b-instruct-reasoning%2Cdeepseek-r1-distill-qwen-14b%2Cfalcon-h1r-7b%2Cnvidia-nemotron-nano-12b-v2-vl-reasoning%2Cnvidia-nemotron-nano-9b-v2-reasoning%2Cllama-3-1-nemotron-nano-4b-reasoning%2Cqwen3-4b-instruct-reasoning%2Cqwen3-vl-4b-reasoning%2Cqwen3-8b-instruct-reasoning%2Cdeepseek-r1-distill-llama-8b%2Cjamba-reasoning-3b%2Colmo-3-7b-think%2Cdeepseek-r1-distill-qwen-1-5b%2Cexaone-4-0-1-2b-reasoning%2Cqwen3-1.7b-instruct-reasoning%2Cqwen3-0.6b-instruct-reasoning&model-filters=open-source%2Ctiny-models%2Csmall-models%2Creasoning-models)

Filter: Size Class: Tiny, Small; Open Weights: Open Source; Reasoning: Reasoning; Paramters Count: <=18B

![MMLU-Pro Benchmark Leaderboard Results](assets/03-Methodology-MMLU-Pro-Benchmark-Leaderboard-Results.png)

This "Gold Standard" example now includes the **Internal Monologue**, which is the hallmark of the Chain of Thought (CoT) approach. It demonstrates how the model "thinks" through the German syntax before committing to the structured fields.

---

## Appendix: Gold Standard Example (CoT Approach){#appendix-gold-standard}

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

```{=latex}
\begin{landscape}
\footnotesize
```

| Models                     | Qualifier | Model Size (B) | Data Source | Overall | Biology | Chemistry | Health | Psychology | Avg. sel. Disciplines |
|----------------------------|-----------|----------------|-------------|---------|---------|-----------|--------|------------|-----------------------|
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

```{=latex}
\normalsize
\end{landscape}
```

### Selection Step 4.

Context windows >=8k

```{=latex}
\begin{landscape}
\footnotesize
```

| Models                     | Qualifier | Context Window | License | Size (B) | Overall | Biology | Chemistry | Health | Psychology | Avg. sel. Disciplines |
|----------------------------|-----------|----------------|---------|----------|---------|---------|-----------|--------|------------|-----------------------|
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

```{=latex}
\normalsize
\end{landscape}
```

### Selection Step 5.

**Remaining Permissive Open-Source models:**

```{=latex}
\begin{landscape}
\footnotesize
```

| Models                     | Qualifier | Context Window | License | Size (B) | Overall | Biology | Chemistry | Health | Psychology | Avg. sel. Disciplines |
|----------------------------|-----------|----------------|---------|----------|---------|---------|-----------|--------|------------|-----------------------|
| GLM-4-9B-Chat | Chat | 128k | MIT | 9 | 0.4801 | 0.7015 | 0.4117 | 0.5379 | 0.6165 | 0.5669 |
| Mistral-Nemo-IT-2407 | Instruct | 128k | Apache 2.0 | 12 | 0.4481 | 0.6583 | 0.3445 | 0.5281 | 0.6165 | 0.53685 |
| Qwen2-7B-Instruct | Instruct | 32k | Apache 2.0 | 7 | 0.4724 | 0.6625 | 0.3772 | 0.4645 | 0.6128 | 0.52925 |
| Phi-3.5-mini-instruct | Instruct | 128k | MIT | 3.8 | 0.4787 | 0.7057 | 0.4125 | 0.5244 | 0.4188 | 0.51535 |
| Llama-3-8B-Instruct | Instruct | 8k | Llama 3 | 8 | 0.4098 | 0.6653 | 0.28 | 0.4902 | 0.594 | 0.507375 |
| Granite-3.1-8B-IT | Instruct | 128k | Apache 2.0 | 8 | 0.4103 | 0.5746 | 0.3145 | 0.4707 | 0.5739 | 0.483425 |
| Qwen1.5-14B-Chat | Chat | 32k | Apache 2.0 | 14 | 0.3802 | 0.6151 | 0.2615 | 0.4218 | 0.5251 | 0.455875 |
| DeepSeek-Coder-V2-IT | Instruct | 128k | DeepSeek | 16 | 0.4157 | 0.5007 | 0.4293 | 0.2995 | 0.4687 | 0.42455 |
| Granite-3.1-2B-IT | Instruct | 128k | Apache 2.0 | 2 | 0.3197 | 0.5007 | 0.2412 | 0.3056 | 0.4411 | 0.37215 |

```{=latex}
\normalsize
\end{landscape}
```

**Comparison of Licenses used remaining from Step 4:**

| Model Family | Specific Licenses Mentioned | Open Source? | Commercial Use | External API Required? | Key Restrictions & Notes |
|--------------|-----------------------------|--------------|----------------|------------------------|--------------------------|
| Permissive | MIT / Apache 2.0 | Yes | Unrestricted | No (Local execution) | "Do whatever you want" licenses; zero downstream legal obligations. |
| Gemma | Gemma Terms of Use | No (Open Weights) | Permitted | No (Local weights available) | Prohibits use for unlicensed professional advice or violating safety policies. |
| Llama (3.x) | Llama 3.1 Community License | No (Open Weights) | Permitted (with caps) | No (Local execution supported) | Requires a special license if users exceed 700M monthly active users. |
| DeepSeek | DeepSeek Model License | No (Open Weights) | Permitted | No (Local weights available) | Allows modifications and derivative works, including model distillation. |
| EXAONE | EXAONE Non-Commercial (NC) | No | Prohibited | No | Strictly restricted to research and experimental purposes only. |
| Mistral | Mistral AI Non-Production / Commercial | No | Restricted / Tiered | Optional (API vs local) | Smaller models are often Apache 2.0; flagship models require commercial agreements. |


<!-- #A-JSON-SIM — AI-generated (Claude, Feb 2026) — algorithm from JsonSimilarityMetric.java + JsonFlattener.java -->

## Appendix: JSON Structural Similarity Algorithm {#appendix-json-sim}

A custom metric was developed to assess how well a model's JSON output conforms to the expected schema, independent of content correctness. Unlike lexical metrics (BLEU, ROUGE) that treat the output as flat text, this metric operates on the JSON structure itself.

The algorithm proceeds in four steps:

1. **JSON extraction and flattening.** Both the model output and the Silver Answer are preprocessed: markdown code fences are stripped, and the JSON content is extracted by bracket-matching. The resulting JSON objects are then recursively flattened into leaf-path maps using dot notation for objects and bracket notation for arrays (e.g., `structured_health_record.medications.current` or `structured_health_record.categories[0]`). Configurable paths (e.g., `internal_monologue`) can be excluded from comparison.

2. **Array alignment.** JSON arrays pose a challenge because the model may output the same elements in a different order. The algorithm identifies array base paths, groups their children by index, and performs greedy best-match alignment: for each element in the Silver Answer's array, the response element with the highest average Levenshtein similarity across shared sub-fields is selected as the match.

3. **Leaf-by-leaf comparison.** For each aligned path, the leaf values are compared using normalised Levenshtein similarity ($1 - \frac{d(s_1, s_2)}{\max(|s_1|, |s_2|)}$). Missing fields in the response score 0.0; matching `null` values on both sides score 1.0.

4. **Aggregation.** The overall score is the arithmetic mean across all leaf-pair similarities. Sub-scores are also computed per top-level key, enabling inspection of which sections (e.g., `diagnosis` vs. `medications`) the model handles well or poorly.

A score of 0.0 indicates either that the model output could not be parsed as JSON at all, or that none of the expected paths were present. A score of 1.0 indicates perfect structural and content match at every leaf.

### Core Implementation

**JSON flattening** (recursive leaf-path extraction):

```java
private static void flattenNode(String prefix, JsonNode node,
        Map<String, String> result, int depth) {
    if (node.isObject()) {
        Iterator<Map.Entry<String, JsonNode>> fields = node.fields();
        while (fields.hasNext()) {
            var entry = fields.next();
            String childPrefix = prefix.isEmpty()
                ? entry.getKey() : prefix + "." + entry.getKey();
            flattenNode(childPrefix, entry.getValue(), result, depth + 1);
        }
    } else if (node.isArray()) {
        for (int i = 0; i < node.size(); i++) {
            flattenNode(prefix + "[" + i + "]", node.get(i), result, depth + 1);
        }
    } else if (node.isNull()) {
        result.put(prefix, null);
    } else {
        result.put(prefix, node.asText());
    }
}
```

**Leaf comparison and aggregation** (per-path Levenshtein similarity):

```java
for (var entry : alignedGolden.entrySet()) {
    String path = entry.getKey();
    String goldenValue = entry.getValue();
    String responseValue = alignedResponse.get(path);

    if (responseValue == null && goldenValue == null) {
        leafScores.put(path, 1.0);
    } else if (responseValue == null) {
        leafScores.put(path, 0.0);
        missingInResponse.add(path);
    } else {
        leafScores.put(path,
            levenshteinSimilarity(goldenValue, responseValue));
    }
}

double overallScore = leafScores.values().stream()
        .mapToDouble(Double::doubleValue)
        .average().orElse(0.0);
```

<!-- #A-DAG — AI-generated (Claude, Feb 2026) — algorithm from DAG engine + medical_extraction_quality graph -->

## Appendix: DAG-Based Medical Extraction Quality Algorithm {#appendix-dag}

To evaluate the clinical quality of model outputs beyond what statistical metrics can capture, a Directed Acyclic Graph (DAG) evaluation metric was developed. Unlike single-prompt LLM-as-a-Judge approaches that ask one broad question, the DAG metric decomposes the evaluation into multiple specialised assessment tasks — each executed by the judge LLM — and aggregates their results through a graph of conditional judgements.

### DAG Execution Engine

The DAG execution engine traverses a graph of four node types:

- **Task nodes** present the judge LLM with specific evaluation instructions and a subset of the evaluation context (actual output, expected output, original input). The LLM's response is stored as accumulated context for downstream nodes.
- **Binary judgement nodes** ask the judge LLM a yes/no question based on accumulated context. The result determines which branch (true/false child) is followed — enabling conditional evaluation paths.
- **Non-binary judgement nodes** present the judge LLM with multiple verdict options (e.g., "fully compliant", "minor issues", "significant issues"). The LLM selects the most appropriate verdict, routing to the corresponding child node.
- **Verdict nodes** are terminal leaves that carry a predefined numeric score (0.0–1.0).

When a graph has multiple root nodes, their branches are executed in parallel (using virtual threads) and the final score is the arithmetic mean of all branch scores. A short-circuit mechanism terminates evaluation early if any branch returns 0.0.

### Medical Extraction Quality Graph

The specific DAG graph used for the `dag_medical_extraction_quality` metric evaluates four parallel dimensions:

1. **Format compliance** (structural branch): A task node analyses the output for JSON validity, presence of required top-level keys (`internal_monologue`, `structured_health_record`), and schema conformance. A binary judgement then splits:
   - If valid JSON: a non-binary judgement rates schema compliance as *fully compliant* (1.0), *minor issues* (0.7), or *significant issues* (0.3).
   - If invalid JSON: a non-binary judgement classifies the output as *recoverable* (0.15) or *garbage* (0.0).

2. **Factual accuracy** (content branch): A task node performs field-by-field comparison against the Silver Answer, marking each field as CORRECT, PARTIALLY_CORRECT, MISSING, or HALLUCINATED. A non-binary judgement then rates overall accuracy as *highly accurate* (1.0), *mostly accurate* (0.75), *partially accurate* (0.4), or *inaccurate* (0.1). Hallucinations are penalised most severely.

3. **Completeness** (coverage branch): A task node counts populated vs. expected fields. A non-binary judgement rates completeness as *complete* (1.0), *mostly complete* (0.7), or *incomplete* (0.3).

4. **Medical terminology** (language branch): A task node evaluates whether the output uses professional medical shorthand, standard abbreviations, and maintains language consistency with the input document. A non-binary judgement rates terminology as *excellent* (1.0), *adequate* (0.6), or *poor* (0.2).

The final score is the average of all four branch scores, yielding a value between 0.0 and 1.0 that captures format compliance, factual fidelity, extraction completeness, and domain-appropriate language in a single metric.

### Core Implementation

**Node dispatch** (sealed interface with pattern matching):

```java
private DAGExecutionResult executeNode(DAGNode node,
        EvaluationContext context,
        Map<String, String> accumulatedContext,
        List<TraceEntry> trace) {
    return switch (node) {
        case TaskNode task ->
            executeTask(task, context, accumulatedContext, trace);
        case BinaryJudgementNode binary ->
            executeBinaryJudgement(binary, context,
                accumulatedContext, trace);
        case NonBinaryJudgementNode nonBinary ->
            executeNonBinaryJudgement(nonBinary, context,
                accumulatedContext, trace);
        case VerdictNode verdict ->
            executeVerdict(verdict, context,
                accumulatedContext, trace);
    };
}
```

**Parallel branch execution** (virtual threads with short-circuit on zero score):

```java
private DAGExecutionResult executeParallelBranches(
        List<DAGNode> branches, EvaluationContext context,
        Map<String, String> accumulatedContext,
        List<TraceEntry> trace) {
    var executor = Executors.newVirtualThreadPerTaskExecutor();
    List<CompletableFuture<DAGExecutionResult>> futures =
        branches.stream()
            .map(branch -> CompletableFuture.supplyAsync(() ->
                executeNode(branch, context,
                    new HashMap<>(accumulatedContext),
                    new ArrayList<>()), executor))
            .toList();

    CompletableFuture.allOf(
        futures.toArray(new CompletableFuture[0])).join();

    double totalScore = 0.0;
    int count = 0;
    for (var future : futures) {
        DAGExecutionResult result = future.join();
        trace.addAll(result.trace());
        if (result.score() == 0.0) {
            return new DAGExecutionResult(0.0, trace, true);
        }
        totalScore += result.score();
        count++;
    }
    return new DAGExecutionResult(
        count > 0 ? totalScore / count : 0.0, trace, false);
}
```

## Implementation Description: Silver Answers App {#appendix-silver-answers}

### Executive Summary

The Silver Answers App is a cloud-based web application designed to automate the generation and evaluation of AI-powered document analyses using Google's Gemini large language model. The system implements a session-based architecture that enables researchers to systematically process document collections through configurable prompt chains, evaluate results, and iteratively refine their analytical approaches. Built on a modern full-stack architecture, the application integrates Google Cloud Platform services for AI processing and persistent storage, providing a scalable solution for document analysis research.

### System Architecture

#### Architectural Overview

The application follows a three-tier architecture pattern:

**Presentation Layer (Frontend)**
- Single-page React application (React 18.2.0)
- Component-based UI with four primary panels
- Real-time state management and progress tracking
- Responsive design with custom dark mode styling

**Application Layer (Backend)**
- Node.js/Express RESTful API server (Express 4.18.2)
- Service-oriented architecture with separation of concerns
- Middleware for error handling, CORS, and rate limiting
- Asynchronous processing with progress callbacks

**Data & AI Layer (Cloud Services)**
- Google Cloud Vertex AI for Gemini API integration
- Google Cloud Storage (GCS) for persistent data storage
- Configuration management through cloud-based JSON files
- Service account-based authentication and authorization

#### Technology Stack

**Frontend Technologies:**
- React 18.2.0 - Component framework
- Axios 1.6.0 - HTTP client for API communication
- react-beautiful-dnd 13.1.1 - Drag-and-drop functionality for prompt reordering
- react-modal 3.16.1 - Modal dialog management
- Custom CSS with CSS variables for theming

**Backend Technologies:**
- Node.js with Express 4.18.2 - Web server framework
- @google-cloud/vertexai 1.1.0 - Gemini API integration
- @google-cloud/storage 7.7.0 - Cloud storage client
- google-auth-library 9.6.0 - Authentication
- express-rate-limit 7.1.5 - API rate limiting
- dotenv 16.3.1 - Environment configuration

**Cloud Infrastructure:**
- Google Cloud Platform (GCP) Project: cas-gen-ki
- Vertex AI API - Gemini 2.5 Flash model
- Cloud Storage - Document and configuration persistence
- Service Account authentication with IAM roles

### Core Components

#### Frontend Architecture

The frontend implements a four-panel layout with an additional session management overlay:

##### Session Manager Component
**Purpose:** Orchestrates work sessions that bind document bases, prompt sets, and generation results together.

**Key Features:**
- Session creation with optional document base and prompt set selection
- Session switching with automatic state restoration
- Session history tracking (creation date, modification date, generation runs)
- Auto-loading of single sessions for improved UX
- Deletion with cascade handling of dependent resources

**State Management:**
```javascript
- currentSession: Active session object
- sessions: Array of all available sessions
- Session metadata: name, docBaseId, promptSetId, status, history
```

##### Document Base (DocsBase) Component
**Purpose:** Manages document collections that serve as input for AI processing.

**Key Features:**
- JSON file upload with URL-based document references (Zenodo integration)
- Folder upload with text file content embedding
- Document preview modal with content display
- Document base selection and switching
- File count and metadata display

**Data Model:**
```javascript
{
  id: "docbase-{timestamp}",
  name: "Document collection name",
  data: {
    files: {
      count: number,
      entries: {
        "filename": {
          id: string,
          size: number,
          mimetype: string,
          links: { content: url }
        }
      }
    }
  },
  uploadedAt: ISO timestamp
}
```

##### Prompt Engineering Component
**Purpose:** Enables creation and configuration of prompt chains for document processing.

**Key Features:**
- Prompt creation (System and User types)
- Drag-and-drop reordering with visual feedback
- Prompt deletion with confirmation
- Generation initiation with progress tracking
- Token estimation and analysis preview
- Prompt set saving for reusability

**Prompt Chain Execution:**
1. System prompts set context/instructions for the AI
2. User prompts provide specific questions/tasks
3. Prompts execute sequentially, with each output feeding into the next
4. Cumulative context grows with each step (document + previous results)

##### Prospect Answers Component
**Purpose:** Displays generation results with expandable document details.

**Key Features:**
- Hierarchical result display (generation → documents → steps)
- Expandable/collapsible document sections
- Intermediate step visualization
- Final answer highlighting
- Status indicators (completed, failed, processing)
- Token usage statistics per document

##### Answer Details Component
**Purpose:** Provides detailed view and rating interface for individual results.

**Key Features:**
- Full answer display with formatting
- Star rating system (1-5 stars)
- Comment field for qualitative feedback
- Human input/correction field for ground truth
- Rating persistence to session
- Timestamp tracking for evaluations

#### Backend Architecture

##### Server Configuration (server.js)
**Responsibilities:**
- Express application initialization
- Middleware configuration (CORS, JSON parsing, rate limiting)
- Route registration for all API endpoints
- Configuration loading from GCS on startup
- Error handling middleware
- Health check endpoint

**Rate Limiting:**
- 60 requests per minute per IP address
- Applied to all /api/* endpoints
- Configurable through config.json

##### Service Layer

**Gemini Service (services/gemini.js)**
- Vertex AI client initialization with authentication
- Token estimation (1 token $\approx$ 4 characters)
- Token limit validation (30,000 input tokens for Gemini 1.5 Flash)
- Content generation with system instructions
- Document chain processing with cumulative context
- Comprehensive logging of API requests and responses
- Safety rating monitoring

**Key Algorithm - Document Chain Processing:**
```
For each document:
  currentInput = documentContent
  For each prompt in chain:
    If prompt.type == "system":
      systemInstruction = prompt.content
      userPrompt = currentInput
    Else:
      systemInstruction = null
      userPrompt = currentInput + "\n\n" + prompt.content
    
    response = callGeminiAPI(userPrompt, systemInstruction)
    
    Store result with metadata
    
    currentInput = documentContent + "\n\n--- Previous Analysis ---\n" + response
  
  Return all results + final answer
```

**Processor Service (services/processor.js)**
- Document content fetching from URLs (Zenodo)
- Multi-document batch processing
- Progress callback system for real-time updates
- Error handling with partial result preservation
- Support for both URL-based and text-based documents

**Storage Service (services/storage.js)**
- GCS file upload/download operations
- File listing with prefix filtering
- File deletion
- JSON serialization/deserialization
- Error handling for cloud operations

##### Route Layer

**Documents Routes (routes/documents.js)**
- `GET /api/documents` - List all document bases from GCS
- `POST /api/documents/upload` - Upload JSON with URL references
- `POST /api/documents/upload-folder` - Upload folder with text content
- `GET /api/documents/:id` - Get specific document base
- `GET /api/documents/:id/files` - Get files in document base
- `DELETE /api/documents/:id` - Delete document base

**Sessions Routes (routes/sessions.js)**
- `GET /api/sessions` - List all sessions (sorted by last modified)
- `POST /api/sessions` - Create new session
- `GET /api/sessions/:id` - Get session with full details
- `PUT /api/sessions/:id` - Update session metadata
- `POST /api/sessions/:id/results` - Add generation results
- `POST /api/sessions/:id/prompts` - Add prompt to session
- `PUT /api/sessions/:id/prompts/reorder` - Reorder session prompts
- `DELETE /api/sessions/:id/prompts/:promptId` - Delete session prompt
- `DELETE /api/sessions/:id` - Delete session (with cascade options)

**Generation Routes (routes/generation.js)**
- `POST /api/generation/analyze` - Analyze token usage without generation
- `POST /api/generation/start` - Start asynchronous generation process
- `GET /api/generation/:id/status` - Get generation progress
- `GET /api/generation/results` - List all generation results
- `GET /api/generation/results/:id` - Get specific generation result

**Ratings Routes (routes/ratings.js)**
- `POST /api/ratings` - Save rating (updates session)
- `GET /api/ratings/:generationId/:documentId` - Get specific rating

**Prompt Sets Routes (routes/prompt-sets.js)**
- `GET /api/prompt-sets` - List all saved prompt sets
- `POST /api/prompt-sets` - Create new prompt set
- `GET /api/prompt-sets/:id` - Get specific prompt set
- `PUT /api/prompt-sets/:id` - Update prompt set
- `DELETE /api/prompt-sets/:id` - Delete prompt set

### Data Flow and Processing Pipeline

#### Session-Based Workflow

**Phase 1: Session Initialization**
1. User creates new session or selects existing session
2. User selects/uploads document base (optional at creation)
3. User selects/creates prompt set (optional at creation)
4. System creates session object in GCS
5. Frontend loads session state and associated resources

**Phase 2: Configuration**
1. User uploads/selects document base if not already set
2. System parses document metadata and stores in GCS
3. User creates/loads prompts for the session
4. System validates prompt chain configuration
5. User can preview token usage estimates

**Phase 3: Generation**
1. User initiates generation process
2. Backend creates unique generation ID
3. For each document in parallel or sequence:
   - Fetch document content (from URL or embedded text)
   - Process through prompt chain sequentially
   - Each prompt builds on previous results
   - Track token usage per step
   - Store intermediate results
4. Aggregate results and save to session
5. Update session history (run count, timestamps)
6. Return results to frontend with progress updates

**Phase 4: Evaluation**
1. User reviews generated answers in Prospect Answers panel
2. User selects document for detailed view
3. User provides rating (1-5 stars)
4. User adds optional comment
5. User provides optional human correction/ground truth
6. System saves rating to session in GCS
7. Rating metadata includes timestamp for tracking

**Phase 5: Iteration**
1. User analyzes results and ratings
2. User modifies prompts based on feedback
3. User re-runs generation (creates new result entry in session)
4. System preserves all previous results for comparison
5. User compares results across generation runs

#### Prompt Chain Processing

The system implements a sequential prompt chain where each prompt's output becomes part of the input for the next prompt:

**Initial State:**
```
Input = Document Content
```

**After Prompt 1 (System):**
```
System Instruction: "You are an expert analyst..."
User Prompt: Document Content
Output: Analysis_1
```

**After Prompt 2 (User):**
```
System Instruction: null
User Prompt: Document Content + "\n\n--- Previous Analysis ---\n" + Analysis_1 +
"\n\nExtract key findings..."
Output: Analysis_2
```

**After Prompt N:**
```
Input = Document Content + All Previous Analyses
Output = Final Answer
```

**Token Growth Pattern:**
- Prompt 1: ~D tokens (document size)
- Prompt 2: ~D + O1 tokens (document + output 1)
- Prompt 3: ~D + O1 + O2 tokens
- Prompt N: ~D + O1 + O2 + ... + O(N-1) tokens

This cumulative approach allows for multi-step reasoning but requires careful token management.

#### Data Persistence Strategy

**Google Cloud Storage Structure:**
```
gs://cas-gen-ki-golden-answers/
|-- config.json                          # Application configuration
|-- docbases/                            # Reusable document collections
|   |-- docbase-1234567890.json
|   `-- docbase-1234567891.json
|-- prompt-sets/                         # Reusable prompt configurations
|   |-- prompt-set-1234567890.json
|   `-- prompt-set-1234567891.json
`-- sessions/                            # Work sessions with results
    |-- session-1234567890.json
    `-- session-1234567891.json
```

**Persistence Characteristics:**
- All data stored as JSON in GCS
- Atomic writes with timestamp-based IDs
- No database required - file-based storage
- Automatic versioning through GCS
- Lazy loading on application startup
- In-memory caching for active session

### Integration with Google Cloud Platform

#### Authentication and Authorization

**Service Account Configuration:**

- Service account: `golden-answers-engine@cas-gen-ki.iam.gserviceaccount.com`
- Key file: JSON credentials stored locally (not in version control)
- Environment variable: `GOOGLE_APPLICATION_CREDENTIALS`

**IAM Roles:**

- `roles/aiplatform.user` - Vertex AI API access for Gemini
- `roles/storage.objectAdmin` - GCS bucket operations (scoped to specific bucket)

**Authentication Flow:**

1. Application loads service account key from environment variable
2. GoogleAuth library creates authenticated client
3. Client used for both Vertex AI and Storage API calls
4. Token refresh handled automatically by SDK

#### Vertex AI Integration

**Model Configuration:**

```json
{
  "model": "gemini-2.5-flash",
  "generationConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 2048,
    "topK": 40,
    "topP": 0.95
  }
}
```

**API Request Structure:**

```javascript
{
  systemInstruction: {
    role: "system",
    parts: [{ text: "System prompt content" }]
  },
  contents: [{
    role: "user",
    parts: [{ text: "User prompt content" }]
  }]
}
```

**Response Handling:**

- Extract text from response.candidates[0].content.parts[0].text
- Monitor finishReason for completion status
- Check safetyRatings for content filtering
- Log token usage estimates
- Handle errors with detailed messages

#### Cloud Storage Integration

**Bucket Configuration:**

- Bucket name: `cas-gen-ki-golden-answers`
- Region: `europe-west6` (Switzerland)
- Storage class: Standard
- Access: Private (service account only)

**File Operations:**

- Upload: JSON.stringify → Buffer → GCS file.save()
- Download: GCS file.download() → Buffer → JSON.parse()
- List: bucket.getFiles({ prefix: 'folder/' })
- Delete: file.delete()

**Error Handling:**

- Retry logic for transient failures
- Fallback to default configuration if config.json unavailable
- Graceful degradation for missing files
- Detailed error logging

### Key Features and Capabilities

#### Session Management

**Benefits:**

- **Reusability:** Document bases and prompt sets can be reused across sessions
- **Continuity:** Resume work from any previous point
- **Organization:** Logical grouping of related work
- **Comparison:** Run same documents with different prompts
- **History:** Complete audit trail of all generation runs

**Session Lifecycle:**

1. Created with name and optional resources
2. Active during configuration and generation
3. Updated with each generation run
4. Archived when work complete
5. Deletable with cascade options

#### Prompt Engineering

**Prompt Types:**

- **System Prompts:** Set AI behavior, role, and constraints
- **User Prompts:** Provide specific tasks and questions

**Capabilities:**

- Visual drag-and-drop reordering
- Real-time token estimation
- Prompt validation
- Save as reusable prompt sets
- Load from existing prompt sets

**Best Practices Supported:**

- Chain-of-thought prompting through sequential steps
- Role-based prompting with system instructions
- Iterative refinement through multiple runs
- A/B testing with different prompt configurations

#### Document Processing

**Supported Formats:**

- JSON with URL references (Zenodo integration)
- Folder upload with text files
- Direct text content embedding

**Processing Features:**

- Batch processing of multiple documents
- Parallel or sequential execution
- Progress tracking with real-time updates
- Partial result preservation on errors
- Token usage tracking per document

#### Result Evaluation

**Rating System:**

- 1-5 star quantitative rating
- Free-text comment field
- Human correction/ground truth field
- Timestamp tracking
- Persistent storage in session

**Analysis Features:**

- View intermediate prompt results
- Compare across generation runs
- Export results for external analysis
- Token usage statistics
- Processing time metrics

#### Token Management

**Estimation:**

- Rough approximation: 1 token $\approx$ 4 characters
- Real-time calculation during prompt configuration
- Warning system for approaching limits

**Limits:**

- Input: ~30,000 tokens (Gemini 1.5 Flash)
- Output: Configurable (default 2,048 tokens)
- Warnings at 80% of limits
- Errors when limits exceeded

**Tracking:**

- Per-prompt token counts
- Per-document cumulative totals
- Per-generation aggregate statistics
- Detailed logging for analysis

### Security and Performance

#### Security Measures

**Authentication:**

- Service account with minimal required permissions
- Key file excluded from version control (.gitignore)
- Environment-based configuration
- No hardcoded credentials

**API Security:**

- CORS configuration for allowed origins
- Rate limiting (60 requests/minute)
- Input validation on all endpoints
- Error messages without sensitive data exposure

**Data Protection:**

- Private GCS bucket access
- Service account-only permissions
- No public endpoints for data access
- Secure credential storage

#### Performance Optimizations

**Frontend:**

- Component-level state management
- Lazy loading of large datasets
- Debounced user inputs
- Optimistic UI updates
- Efficient re-rendering with React keys

**Backend:**

- Asynchronous processing for long-running tasks
- Progress callbacks for real-time updates
- In-memory configuration caching
- Connection pooling for GCS
- Efficient JSON parsing

**API:**

- Rate limiting to prevent abuse
- Request timeout configuration
- Batch operations where possible
- Minimal data transfer (pagination ready)

### Error Handling and Logging

#### Error Handling Strategy

**Frontend:**

- Try-catch blocks around API calls
- User-friendly error messages
- Fallback UI states
- Error boundary components (ready for implementation)

**Backend:**

- Centralized error handler middleware
- Specific error types (validation, authentication, API)
- Graceful degradation
- Partial result preservation

**Cloud Integration:**

- Retry logic for transient failures
- Fallback configurations
- Detailed error context
- User notification of failures

#### Logging System

**Console Logging:**

- Request/response details for Gemini API
- Token usage statistics
- Processing progress
- Error stack traces
- Performance metrics

**Log Levels:**

- INFO: Normal operations
- WARN: Approaching limits, fallbacks used
- ERROR: Failures requiring attention

**Logged Information:**

- API request parameters
- Token estimates and actuals
- Processing times
- Success/failure rates
- User actions (session creation, generation runs)

### Deployment and Configuration

#### Environment Configuration

**Backend (.env):**
```
GOOGLE_APPLICATION_CREDENTIALS=./gcp-service-account.json
GCP_PROJECT_ID=xxxxxx
GCP_PROJECT_NAME=xxx-xxx-xxx
GCS_CONFIG_BUCKET=xxx-xxx-xxx-xxx-xxx
GCS_CONFIG_FILE=config.json
PORT=3001
NODE_ENV=development
ALLOWED_ORIGINS=http://localhost:3000
```

**Frontend:**
```
REACT_APP_API_URL=http://localhost:3001/api
```

**Cloud Configuration (config.json in GCS):**
```json
{
  "gcpProject": "xxxxxxxxxx",
  "gcpProjectName": "cas-gen-ki",
  "gcpLocation": "us-central1",
  "geminiModel": "gemini-2.5-flash",
  "geminiConfig": {
    "temperature": 0.7,
    "maxOutputTokens": 2048,
    "topK": 40,
    "topP": 0.95
  },
  "rateLimit": {
    "requestsPerMinute": 60
  }
}
```

#### Deployment Process

**Prerequisites:**
1. Node.js 18+ installed
2. GCP account with billing enabled
3. Service account created with proper roles
4. GCS bucket created
5. Configuration file uploaded to GCS

**Backend Deployment:**
```bash
cd backend
npm install
cp .env.example .env
# Edit .env with actual values
npm start
```

**Frontend Deployment:**
```bash
cd frontend
npm install
npm start
```

**Production Considerations:**
- Use process manager (PM2) for backend
- Build optimized frontend bundle
- Configure reverse proxy (nginx)
- Set up SSL/TLS certificates
- Enable production logging
- Configure monitoring and alerts

### Research Applications

#### Use Cases

**Prompt Engineering Research:**
- Test different prompt formulations
- Compare system vs. user prompt effectiveness
- Analyze chain-of-thought vs. direct prompting
- Measure impact of prompt order

**Document Analysis:**
- Batch process research papers
- Extract structured information
- Generate summaries and insights
- Compare AI vs. human analysis

**Model Evaluation:**
- Rate AI-generated outputs
- Collect human corrections
- Build ground truth datasets
- Measure improvement over iterations

**Iterative Refinement:**
- Track prompt evolution
- Compare results across sessions
- Identify optimal configurations
- Document best practices

#### Data Collection

**Quantitative Metrics:**
- Star ratings (1-5 scale)
- Token usage statistics
- Processing times
- Success/failure rates
- Generation run counts

**Qualitative Data:**
- User comments on results
- Human corrections/ground truth
- Prompt configurations
- Session notes and descriptions

**Exportable Data:**
- Session JSON files
- Generation results
- Rating datasets
- Token usage reports

### Future Enhancement Opportunities

#### Potential Improvements

**Architecture:**
- Database integration for better querying
- Real-time collaboration features
- Webhook support for external integrations
- Microservices decomposition for scalability

**Features:**
- Bulk operations across multiple sessions
- Advanced analytics dashboard
- Export to various formats (CSV, PDF)
- Template library for common tasks
- Version control for prompts
- A/B testing framework

**AI Integration:**
- Support for multiple AI models
- Model comparison features
- Automatic prompt optimization
- Embedding-based document search
- RAG (Retrieval-Augmented Generation) support

**User Experience:**
- Advanced filtering and search
- Customizable dashboards
- Keyboard shortcuts
- Batch rating interface
- Mobile-responsive design improvements

#### Scalability Considerations

**Current Limitations:**
- File-based storage (not optimized for high concurrency)
- In-memory state management
- Sequential document processing
- Manual session management

**Scaling Strategies:**
- Implement database (PostgreSQL, Firestore)
- Add caching layer (Redis)
- Implement job queue (Bull, Cloud Tasks)
- Horizontal scaling with load balancer
- CDN for static assets
- Serverless functions for processing


## Appendix: G-Eval Investigation {#appendix-geval}

G-Eval [@liu2023geval] uses probability-weighted scoring: rather than taking the LLM's generated score at face value, the token log-probabilities of the score tokens (e.g. "1" through "5") are extracted and a weighted average is computed. This approach significantly reduces the known scoring bias of LLMs.

![G-Eval algorithm: CoT evaluation steps are generated once and cached, then applied per test case with probability-weighted scoring via logprobs or multi-sample fallback.](../../assets/03-GEval-Algorithm.png){#fig:geval-algorithm width=75%}

### The Logprobs Compatibility Problem

The `logprobs` feature that enables this weighted scoring is not uniformly supported across LLM providers. The following table summarises the compatibility landscape.

| Provider | Logprobs | Notes |
|----------|----------|-------|
| OpenAI (standard models) | Yes | gpt-4o, gpt-4.1-mini etc. via `/v1/chat/completions` |
| OpenAI (reasoning models) | **No** | o-series, gpt-5-mini — `logprobs` not supported, `temperature` fixed at 1.0 |
| vLLM (self-hosted) | Yes | Any HuggingFace model; logprobs reflect raw model output before post-processing |
| Together.ai | Yes | Open-weight models via OpenAI-compatible API |
| Ollama | **No** | Logprobs only on native `/api/generate`, not on OpenAI-compatible `/v1/chat/completions` |
| LM Studio | **No** | Accepts `top_logprobs` on `/v1/responses` (since v0.3.26, Jan 2026) but returns empty arrays in practice |
| llama.cpp server | **No** | Returns `null` for logprobs on `/v1/chat/completions` |

: Logprobs compatibility by LLM provider (as of February 2026) {#tab:logprobs-compat}

Particularly problematic is the incompatibility with reasoning models (OpenAI o-series, gpt-5-mini, gpt-5-nano). These models employ an internal reasoning phase that consumes tokens from the `max_completion_tokens` budget before any visible output is produced. For a task that merely requires a single integer score, reasoning models are architecturally unsuitable.

This problem also affects existing reference implementations. DeepEval, the most widely used Python implementation of G-Eval, works around the issue with a hardcoded list of reasoning models for which it falls back to plain JSON extraction without probability weighting — which de facto is no longer G-Eval but a simple LLM-as-a-Judge approach.

### Fallback Strategy

For providers without logprobs support, the G-Eval paper defines an alternative method: *multi-sample estimation* with $n=20$ independent calls at `temperature=1.0`, where each response is parsed for an integer score and the results are averaged [@liu2023geval]. This procedure approximates the probability distribution through sampling — albeit at significantly higher cost (factor 20). Practically this turned out to be problematic since this led to rejected API calls (Vertex AI) or unacceptable performance (local LM Studio).

A promising alternative for local execution is vLLM, a high-throughput self-hosted inference engine that provides full logprobs support on its OpenAI-compatible API for any HuggingFace model. Due to time constraints, vLLM was not integrated into the evaluation pipeline.

### Consequence for Judge Model Selection

The choice of judge model for G-Eval evaluation is therefore constrained: either a non-reasoning cloud model with logprobs support is used (e.g. gpt-4o-mini), a self-hosted vLLM instance serves as judge, or the cost-intensive multi-sample fallback is required. For this study, an auto-detection strategy is implemented that first attempts the logprobs path and automatically falls back to multi-sample upon failure — enabling both cloud APIs and local models to serve as judges. In practice, the evaluation relies primarily on direct LLM-as-a-Judge scoring via the DAG metric.
