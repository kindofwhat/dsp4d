# Appendices

## Comprehensive Comparison of Prompting Techniques {#appendix-promp-techs}

| Technique |                                                                               |
|-----------|-------------------------------------------------------------------------------|
| Zero-Shot Prompting | **Description:** Asking the model to perform a task without examples|
||**Application to Medical Silver Answers:** "Extract all diagnoses from this text."|
||**Pros for Medical Records:** Fast and low token cost. Useful for checking the baseline capability of a model.|
||**Cons / Risks:** High risk of hallucination and format inconsistency. The model may guess the required medical style incorrectly. |
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Few-Shot Prompting | **Description:** Providing examples (input-output pairs) within the prompt.
||**Application to Medical Silver Answers:** "Style Guide: You provide 3 examples of GraSCCo raw text and the corresponding perfect "Silver Answer" format. (possible after first supervision session)"|
||**Pros for Medical Records:** Essential for enforcing the specific syntax and brevity required for the Silver Answers.|
||**Cons / Risks:** The model may overfit to the examples and ignore the nuance of the new input.|
||**References:** [Language Models are Few-Shot Learners (NeurIPS)](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf), [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Chain-of-Thought (CoT) | **Description:** Instructing the model to generate intermediate reasoning steps.
||**Application to Medical Silver Answers:** Clinical Reasoning: "First, list all medications found. Second, check if they are current or historical. Finally, output the list."|
||**Pros for Medical Records:** Critical for connecting implied symptoms to explicit medical codes. Reduces "skipping" of details.|
||**Cons / Risks:** Increases token usage. Requires parsing to separate the "thought" from the "silver answer."|
||**References:** [Chain of Thought Prompting Elicits reasoning (arXiv)](https://arxiv.org/pdf/2201.11903), [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Self-Consistency | **Description:** Generating multiple outputs for the same prompt and selecting the most frequent one.|
||**Application to Medical Silver Answers:** Validation: Generate the summary 5 times. If "Diabetes Type 2" appears in 5/5, keep it. If "Hypertension" appears in 1/5, discard it.|
||**Pros for Medical Records:** The best statistical defense against hallucinations. Essential for creating a robust "Gold Standard".|
||**Cons / Risks:** Computationally expensive (requires N times the inference cost).|
||**References:** [Self-Consistency Improves Chain of Thought (arXiv)](https://arxiv.org/pdf/2203.11171), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Skeleton-of-Thought (SoT) | **Description:** Generating a skeleton/outline first, then expanding points in parallel.|
||**Application to Medical Silver Answers:** Structure Planning: 1. Generate list of headers (Dx, Rx). 2. Fill sections in parallel.|
||**Pros for Medical Records:** Accelerates generation speed (up to 2.39x). Good for long, structured discharge summaries.|
||**Cons / Risks:** Suited for writing new content, less proven for extracting specific facts from existing chaos.|
||**References:** [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://arxiv.org/pdf/2307.15337), [[ICLR 2024] Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation (GitHub)](https://github.com/imagination-research/sot) |
| Prompt Chaining | **Description:** Breaking a task into subtasks where output A becomes input B.|
||**Application to Medical Silver Answers:** Workflow: 1. Extraction Prompt -> 2. Filtering Prompt -> 3. Formatting Prompt.|
||**Pros for Medical Records:** High reliability. Isolates errors. Allows for intermediate transformation (e.g., cleaning citations).|
||**Cons / Risks:** Requires building a controller application (state management) between prompts.|
||**References:** [Prompt Engineering Guide: Prompt Chaining (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb), [PromptChainer Paper (arXiv)](https://arxiv.org/pdf/2203.06566) |
| Role / Persona Prompting | **Description:** Assigning a specific role/profession to the AI.|
||**Application to Medical Silver Answers:** Context Setting: "You are a Senior Chief Physician at a Swiss hospital..."|
||**Pros for Medical Records:** Drastically improves tone and handling of medical abbreviations/jargon.|
||**Cons / Risks:** Can lead to verbosity if the persona is too "chatty."|
||**References:** [Prompt Engineering: Part 2 - Best Practices for Software Developers in Digital Industries](https://blogs.sw.siemens.com/thought-leadership/prompt-engineering-part-2-best-practices-for-software-developers-in-digital-industries/), [Prompt Engineering Guide](https://www.promptingguide.ai/), [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/) |
| Multi-Persona Prompting | **Description:** Simulating a discussion between multiple agents (e.g., Drafter & Reviewer).|
||**Application to Medical Silver Answers:** Quality Assurance: Agent A extracts data; Agent B reviews it for missing info; Agent C finalizes.|
||**Pros for Medical Records:** Simulates a "four-eyes principle" (peer review), reducing errors through internal debate.|
||**Cons / Risks:** High latency and token cost; complex to orchestrate.|
||**References:** [Exploring Multi-Persona Prompting for Better Outputs](https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs) |
| Tree of Thoughts (ToT) | **Description:** Exploring multiple reasoning paths and backtracking.|
||**Application to Medical Silver Answers:** Complex Triage: Exploring different diagnostic possibilities before committing to one.|
||**Pros for Medical Records:** Useful for complex differential diagnosis problems.|
||**Cons / Risks:** Likely overkill for extraction tasks where the answer is explicitly in the text.|
||**References:** [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/pdf/2305.10601), [[NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://github.com/princeton-nlp/tree-of-thought-llm) |
| Retrieval Augmented Generation (RAG) | **Description:** Retrieving external data to ground the generation.|
||**Application to Medical Silver Answers:** Fact Checking: Using a vector DB to validate if an extracted drug name exists in RxNorm.|
||**Pros for Medical Records:** Prevents hallucination of non-existent drugs; ensures terminology standardization.|
||**Cons / Risks:** Requires external database infrastructure. And a document base.|
||**References:** [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/), [Prompt Engineering Guide: Prompt Chaining (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb) |
| Automatic Prompt Engineer (APE) | **Description:** Using an LLM to generate and optimize prompts.|
||**Application to Medical Silver Answers:** Asking GPT-4 to write the optimal prompt for analyzing GraSCCo texts.|
||**Pros for Medical Records:** Saves time on trial-and-error.|
||**Cons / Risks:** The resulting prompt might be obscure/hard to interpret.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Generated Knowledge Prompting | **Description:** Asking the model to generate relevant knowledge before answering.|
||**Application to Medical Silver Answers:** "List common side effects of Ibuprofen, then summarize the patient's complaints regarding medication."|
||**Pros for Medical Records:** Can help if the medical text is ambiguous (e.g., vague symptoms), providing context for the summary.|
||**Cons / Risks:** Risk of generating false knowledge (hallucinated medical facts) which then contaminates the summary.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Automatic Reasoning and Tool-use | **Description:** Allowing the LLM to use external tools (calculators, APIs).|
||**Application to Medical Silver Answers:** Calculating cumulative dosage or converting units (e.g., mg to g) found in the text.|
||**Pros for Medical Records:** Ensures mathematical accuracy in the medical record (e.g., total radiation dose).|
||**Cons / Risks:** Adds complexity; the model might fail to invoke the tool correctly.|
||**References:** [Toolformer: Language Models Can Teach Themselves to Use Tools (arXiv)](https://arxiv.org/pdf/2302.04761) |
| Active-Prompt | **Description:** Selecting the most uncertain examples for human annotation to teach the model.|
||**Application to Medical Silver Answers:** Identifying GraSCCo texts where the model is "unsure" and asking a doctor to manually create the Silver Answer.|
||**Pros for Medical Records:** Maximizes the value of human expert time (efficient annotation).|
||**Cons / Risks:** Requires a human-in-the-loop workflow.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Directional Stimulus Prompting | **Description:** Using a separate small model to generate "hints" or keywords to guide the main LLM.|
||**Application to Medical Silver Answers:** Extracting keywords (e.g., "Heart", "Attack") first, then feeding them to the LLM to generate the summary.|
||**Pros for Medical Records:** Can focus the model on specific medical sections (e.g., "Focus only on cardiac events").|
||**Cons / Risks:** Requires training or prompting an auxiliary policy model.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Program-Aided Language Models (PAL) | **Description:** Generating code to solve reasoning steps.|
||**Application to Medical Silver Answers:** Writing a Python script to extract and sort dates of admission from the text.|
||**Pros for Medical Records:** Extremely precise for structured data extraction (dates, dosages).|
||**Cons / Risks:** Fails if the medical text is too unstructured or uses ambiguous natural language.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| ReAct (Reasoning + Acting) | **Description:** Interleaving reasoning traces with action execution.|
||**Application to Medical Silver Answers:** "Thought: I need to check if this drug interacts with... Action: Search drug database."|
||**Pros for Medical Records:** Good for clinical decision support agents.|
||**Cons / Risks:** Overly complex for the specific task of generating static Silver Answers from text.|
||**References:** [REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS (arXiv)](https://arxiv.org/pdf/2210.03629), [Prompt Engineering Guide: ReAct Prompting (GitHub)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb) |
| Reflexion | **Description:** An agent reflecting on past mistakes to improve future responses.|
||**Application to Medical Silver Answers:** The model generates a summary, checks it against rules, critiques itself ("I missed the date"), and rewrites.|
||**Pros for Medical Records:** Improves quality iteratively without human intervention.|
||**Cons / Risks:** Can get stuck in loops if the self-critique is flawed.|
||**References:** [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/pdf/2303.11366), [Prompt Engineering: Part 2 - Best Practices for Software Developers in Digital Industries](https://blogs.sw.siemens.com/thought-leadership/prompt-engineering-part-2-best-practices-for-software-developers-in-digital-industries/) |
| Multimodal CoT | **Description:** Chain-of-Thought with images and text.|
||**Application to Medical Silver Answers:** Analyzing X-rays alongside the radiology report.|
||**Pros for Medical Records:** Essential if the GraSCCo corpus contained images (it does not, it is text-based).|
||**Cons / Risks:** Not applicable to text-only medical corpora.|
||**References:** [Prompt Engineering Guide](https://www.promptingguide.ai/) |
| Graph-Prompting | **Description:** Representing data as a graph structure within the prompt.|
||**Application to Medical Silver Answers:** Mapping patient symptoms to a knowledge graph of diseases.|
||**Pros for Medical Records:** Good for understanding relationships (Symptom A -> Disease B).|
||**Cons / Risks:** Text-to-Graph conversion is difficult and error-prone.|
||**References:** [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/pdf/2308.09687) |
| Meta-Prompting | **Description:** Asking the model to assume a persona or higher-level view.|
||**Application to Medical Silver Answers:** "Act as a senior medical consultant reviewing a junior doctor's note."|
||**Pros for Medical Records:** Can improve the tone and professionality of the output.|
||**Cons / Risks:** Mostly affects style, less impact on factual extraction accuracy.|
||**References:** [Prompt engineering techniques: Top 6 for 2026](https://www.k2view.com/blog/prompt-engineering-techniques/), [Prompt Engineering Guide](https://www.promptingguide.ai/) |

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

## Appendix: Token Cost per Evaluation Interaction {#appendix-token-cost}

Each evaluation interaction requires approximately 6,000–10,000 tokens for the LLM-as-a-Judge metrics. This cost is driven by the structured medical data that must be included in every judge call.

**LLM-Judge metric (~3,000–5,000 tokens):**

- Prompt template and evaluation criteria: ~300–500 tokens
- `ACTUAL_OUTPUT` — the model's structured health record JSON: ~1,000–2,000 tokens
- `EXPECTED_OUTPUT` — the silver answer JSON: ~1,000–2,000 tokens
- `INPUT` — the original clinical document: ~500–1,000 tokens

**DAG metric (~3,000–7,000 tokens, depending on graph depth):**

- TaskNode call: injects `ACTUAL_OUTPUT` + `EXPECTED_OUTPUT` into the task prompt → ~2,000–4,000 tokens
- The task node's LLM response is added to `accumulatedContext`
- Each subsequent JudgementNode re-injects the accumulated context (including prior LLM responses) into its prompt → ~1,000–2,000 tokens per node
- Each additional node in the DAG adds further context, as the accumulated responses grow

**Total per interaction:** ~6,000–10,000 tokens across both metrics. For a full evaluation run of 62 test cases across 11 models, this amounts to approximately 4–7 million judge tokens — a significant cost factor that constrains the choice of judge model and the feasibility of multi-sample estimation approaches such as the G-Eval fallback strategy (which would multiply this cost by a factor of 20).

## Appendix: Evaluation Metrics Reference {#appendix-metrics-reference}

This section provides a concise reference for all evaluation metrics used in this study, including their mathematical definitions as implemented in the *llm-validator* framework.

All text-based metrics operate on normalised, lowercased token sequences. When multiple silver answers are available, the best score across all references is reported.

### BLEU (Bilingual Evaluation Understudy)

BLEU measures **precision** of n-grams: what fraction of the generated text's n-grams appear in the reference.

**Computation:**

1. For each $n \in \{1, 2, 3, 4\}$, compute clipped n-gram precision:
$$p_n = \frac{\sum_{\text{ngram}} \min(\text{count}_{\text{gen}}(\text{ngram}),\; \text{count}_{\text{ref}}(\text{ngram}))}{\sum_{\text{ngram}} \text{count}_{\text{gen}}(\text{ngram})}$$
   Clipping ensures that repeated n-grams in the output are not counted more often than they occur in the reference.

2. Compute the brevity penalty (BP) to penalise short outputs:
$$BP = \begin{cases} 1 & \text{if } |\text{gen}| \geq |\text{ref}| \\ e^{1 - |\text{ref}|/|\text{gen}|} & \text{otherwise} \end{cases}$$

3. Final score is the brevity-penalised geometric mean of all four precisions:
$$\text{BLEU} = BP \cdot \exp\!\left(\frac{1}{4}\sum_{n=1}^{4} \ln p_n\right)$$

**Range:** 0.0–1.0. **Pass threshold:** 0.3. **Interpretation:** Higher = more n-gram overlap with reference. Scores above 0.5 are considered strong for extraction tasks.

---

### ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

ROUGE measures **recall**: what fraction of the reference content appears in the generated output. Three variants are computed.

**ROUGE-1 and ROUGE-2** (unigram and bigram overlap):

$$\text{Precision}_n = \frac{|\text{ngrams}_{\text{gen}} \cap \text{ngrams}_{\text{ref}}|}{|\text{ngrams}_{\text{gen}}|}, \quad \text{Recall}_n = \frac{|\text{ngrams}_{\text{gen}} \cap \text{ngrams}_{\text{ref}}|}{|\text{ngrams}_{\text{ref}}|}$$

$$\text{F1}_n = \frac{2 \cdot \text{Precision}_n \cdot \text{Recall}_n}{\text{Precision}_n + \text{Recall}_n}$$

Note: the implementation uses **set-based** overlap (unique n-grams), not count-based — each n-gram is counted at most once.

**ROUGE-L** (Longest Common Subsequence):

Computes the length of the longest common subsequence (LCS) between generated and reference token sequences using dynamic programming, then derives an F1 score:

$$P_L = \frac{|LCS|}{|\text{gen}|}, \quad R_L = \frac{|LCS|}{|\text{ref}|}, \quad \text{ROUGE-L} = \frac{2 \cdot P_L \cdot R_L}{P_L + R_L}$$

**Primary score:** ROUGE-L. **Range:** 0.0–1.0. **Pass threshold:** 0.4.

---

### Token F1

Token F1 measures **set-based word overlap** between generated and reference text using precision, recall, and their harmonic mean.

**Computation:**

$$\text{Precision} = \frac{|\text{tokens}_{\text{gen}} \cap \text{tokens}_{\text{ref}}|}{|\text{tokens}_{\text{gen}}|}, \quad \text{Recall} = \frac{|\text{tokens}_{\text{gen}} \cap \text{tokens}_{\text{ref}}|}{|\text{tokens}_{\text{ref}}|}$$

$$\text{F1} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

Both inputs are tokenised and deduplicated (set-based), so repeated tokens do not inflate the score.

**Range:** 0.0–1.0. **Pass threshold:** 0.7. **Interpretation:** High precision = output doesn't contain irrelevant content. High recall = output covers the reference content. F1 balances both.

---

### Levenshtein Similarity

Measures **character-level** similarity by computing the minimum edit distance (insertions, deletions, substitutions) between the normalised texts.

**Computation:**

$$d(s_1, s_2) = \text{minimum edits to transform } s_1 \text{ into } s_2$$

$$\text{Similarity} = 1 - \frac{d(s_1, s_2)}{\max(|s_1|, |s_2|)}$$

**Range:** 0.0–1.0. **Pass threshold:** 0.8. **Interpretation:** Sensitive to formatting differences, ordering, and verbosity — even semantically identical outputs score low if phrased differently.

---

### Semantic Similarity

Measures **meaning-level** similarity by comparing embedding vectors of the generated and reference texts.

**Computation:**

1. Both texts are embedded using OpenAI's `text-embedding-3-small` model, producing high-dimensional vectors $\vec{a}$ and $\vec{b}$.

2. Cosine similarity is computed:
$$\text{sim}(\vec{a}, \vec{b}) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

**Range:** -1.0 to 1.0 (in practice 0.0–1.0 for natural language). **Pass threshold:** 0.75. **Interpretation:** Captures semantic equivalence regardless of lexical differences. Two outputs expressing the same medical content in different words will score high.

**Note:** This is the only statistical metric that requires an external API call (OpenAI embeddings), but it is deterministic — the same input always produces the same embedding.

---

### Metric Comparison Summary

| Metric | Granularity | Focus | Sensitive to | Robust to |
|--------|-------------|-------|--------------|-----------|
| BLEU | n-gram (1–4) | Precision | Word order, exact phrasing | — |
| ROUGE | n-gram + LCS | Recall | Missing content | Minor additions |
| Token F1 | Word (set) | Precision + Recall | Missing/extra words | Word order |
| Levenshtein | Character | Edit distance | Formatting, ordering | — |
| Semantic Sim. | Sentence embedding | Meaning | — | Paraphrasing, synonyms |
| JSON Sim. | JSON leaf paths | Structure + Content | Schema violations | Key ordering |

## Appendix: Pearson Correlation Coefficient {#appendix-pearson}

The Pearson correlation coefficient $r$ measures the strength and direction of the linear relationship between two variables. It is used in this study to analyse whether evaluation metrics capture similar or independent quality dimensions.

**Definition:**

Given $n$ paired observations $(x_i, y_i)$:

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

where $\bar{x}$ and $\bar{y}$ are the sample means.

**Range and interpretation:**

| $r$ value | Interpretation |
|-----------|----------------|
| 1.0 | Perfect positive linear relationship |
| 0.7–1.0 | Strong positive correlation |
| 0.4–0.7 | Moderate positive correlation |
| 0.1–0.4 | Weak positive correlation |
| -0.1–0.1 | No meaningful linear relationship |
| < -0.1 | Negative correlation (analogous bands) |

**Application in this study:** The correlation matrix (Figure \ref{fig:metric-correlation}) computes $r$ for every pair of metrics across all model-document interactions. Each observation is one interaction's score on two metrics. High correlation between two metrics (e.g., Levenshtein and ROUGE) indicates they capture similar quality aspects. Low correlation (e.g., DAG score and BLEU) suggests they measure fundamentally different dimensions — confirming the value of a multi-metric evaluation approach.

**Limitation:** Pearson correlation only captures *linear* relationships. Two metrics that are related but in a non-linear way (e.g., a threshold effect where semantic similarity is always high but JSON similarity is bimodal) would show low $r$ despite being meaningfully related.
