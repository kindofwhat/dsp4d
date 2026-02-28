# Instructions for Reproducing Results & Discussion Chapters

This file documents how the content in `paper/chapters/04-results/index.md` and `paper/chapters/05-discussion/index.md` was generated from the evaluation JSON, so it can be reproduced when the input data changes.

## Input File

**`paper/assets/questions_complete_evaluated.json`**

Structure:
```
{
  "formatVersion": "1.0",
  "exportedAt": "...",
  "testRun": { "name": "...", ... },
  "testCases": [
    {
      "question": "... (clinical document text) ...",
      "systemPrompt": "... (identical for all test cases) ...",
      "goldenAnswers": ["... (expected JSON output as string) ..."],
      "interactions": [
        {
          "model": "gemini-2.5-pro",
          "provider": "vertex",
          "response": "... (model output) ...",
          "latencyMs": 32558,
          "evaluationResults": [
            {
              "metricName": "bleu",
              "metricType": "STATISTICAL",
              "score": 0.083,
              "passed": false,
              "explanation": "..."
            },
            ...
          ]
        },
        ... (one interaction per model)
      ]
    },
    ... (62 test cases)
  ]
}
```

### Key dimensions
- **62 test cases** (GraSCCo clinical documents)
- **9 models** per test case (same set for all): gemini-2.5-pro, gpt-5-nano, gemma3:27b, granite3.3:2b, glm4:9b, llama3:8b, mistral-nemo:latest, phi3.5:3.8b, qwen2:7b-instruct
- **8 evaluation metrics** per interaction (as of Feb 2026 — G-Eval was removed):
  - Statistical (5): `bleu`, `rouge`, `levenshtein_similarity`, `token_f1`, `json_structural_similarity`
  - Embedding (1): `semantic_similarity`
  - LLM-as-a-Judge (2): `dag_medical_extraction_quality`, `llmjudge_correctness`

**If the metric set changes** (metrics added/removed), update the metric categorisation in both chapters and all tables.

## What Was Written

### Chapter 04 — Results (`paper/chapters/04-results/index.md`)

All content is data-driven. Sections and their data sources:

| Section | Content | Data extraction method |
|---------|---------|----------------------|
| Overview of Models and Evaluation Metrics | Model list, metric categorisation | Manual from JSON structure inspection |
| Statistical Metrics table | Mean score per model per statistical metric | Aggregated from JSON (see scripts below) |
| Embedding + LLM-as-a-Judge table | Mean score per model per embedding/judge metric | Aggregated from JSON |
| Composite Scores by Metric Category | Mean of metric averages grouped into Statistical/Embedding/Judge/Overall + latency | Aggregated from JSON |
| Pass Rates | % of test cases where `passed: true` per model per metric | Aggregated from JSON |
| JSON Structural Compliance | Mean/std/min/max of `json_structural_similarity` per model | Aggregated from JSON |
| Semantic Understanding vs. Format Compliance | Side-by-side of semantic sim vs. JSON sim vs. BLEU | Subset of aggregated data |
| Metric Correlation Analysis | Pearson correlation matrix + heatmap figure | Computed from all 558 data points (see image generation below) |
| Latency | Mean latencyMs per model | Aggregated from JSON |

### Chapter 05 — Discussion (`paper/chapters/05-discussion/index.md`)

Interpretive text referencing the numbers from Chapter 04. Sections:

- **Model Size Does Not Linearly Predict Performance** — references composite scores
- **Cloud Models Retain an Advantage** — references semantic similarity and composite gap
- **The Format Compliance Problem** — references JSON structural similarity
- **Semantic Understanding Is Preserved** — references semantic similarity range
- **Mistral-Nemo: An Outlier** — references DAG and JSON scores
- **Implications for Clinical Practice** — 3 points derived from results
- **Addressing the Research Questions** — RQ1/RQ2/RQ3 with specific numbers
- **Limitations** — 6 points (methodology-aware, not data-dependent)
- **Future Work** — 5 points

**When data changes:** Update all numbers in the discussion that reference specific scores. Search for decimal numbers like `0.470`, `0.390`, etc.

## Scripts Used to Extract Data

All scripts were run as inline Python via `cat JSON | python3 -c "..."`. The Python venv at `/Users/chrigel/Documents/workspace/bfh/venv/` has matplotlib/numpy.

### Aggregation script (produces all tables)

Run from the `dsp4d` project root:

```bash
cat paper/assets/questions_complete_evaluated.json | python3 -c "
import json, sys
from collections import defaultdict

data = json.load(sys.stdin)

stat_metrics = ['bleu', 'json_structural_similarity', 'levenshtein_similarity', 'rouge', 'token_f1']
embedding_metrics = ['semantic_similarity']
judge_metrics = ['dag_medical_extraction_quality', 'llmjudge_correctness']

scores = defaultdict(lambda: defaultdict(list))
latencies = defaultdict(list)
pass_rates = defaultdict(lambda: defaultdict(lambda: [0,0]))

for tc in data['testCases']:
    for inter in tc['interactions']:
        model = inter['model']
        latencies[model].append(inter['latencyMs'])
        for ev in inter['evaluationResults']:
            scores[model][ev['metricName']].append(ev['score'])
            pass_rates[model][ev['metricName']][1] += 1
            if ev.get('passed'):
                pass_rates[model][ev['metricName']][0] += 1

size_map = {
    'gemini-2.5-pro': 'Large (Cloud)', 'gpt-5-nano': 'Small (Cloud)',
    'gemma3:27b': '27B', 'glm4:9b': '9B', 'granite3.3:2b': '2B',
    'llama3:8b': '8B', 'mistral-nemo:latest': '12B',
    'phi3.5:3.8b': '3.8B', 'qwen2:7b-instruct': '7B'
}

# Sort by overall composite
results = []
for model in scores:
    stat = sum(sum(scores[model][m])/len(scores[model][m]) for m in stat_metrics) / len(stat_metrics)
    emb = sum(sum(scores[model][m])/len(scores[model][m]) for m in embedding_metrics) / len(embedding_metrics)
    judge = sum(sum(scores[model][m])/len(scores[model][m]) for m in judge_metrics) / len(judge_metrics)
    overall = sum(sum(scores[model][m])/len(scores[model][m]) for m in scores[model]) / len(scores[model])
    lat = sum(latencies[model])/len(latencies[model])
    results.append((model, size_map.get(model,'?'), stat, emb, judge, overall, lat))
results.sort(key=lambda x: -x[5])

print('=== COMPOSITE TABLE ===')
for model, size, stat, emb, judge, overall, lat in results:
    name = model.replace(':latest','').replace('-instruct','')
    print(f'| {name} | {size} | {stat:.3f} | {emb:.3f} | {judge:.3f} | {overall:.3f} | {lat:,.0f} |')

print('\n=== STATISTICAL METRICS TABLE ===')
for model, size, stat, emb, judge, overall, lat in results:
    name = model.replace(':latest','').replace('-instruct','')
    s = scores[model]
    print(f'| {name} | {size.split()[0]} | {sum(s[\"bleu\"])/len(s[\"bleu\"]):.3f} | {sum(s[\"rouge\"])/len(s[\"rouge\"]):.3f} | {sum(s[\"levenshtein_similarity\"])/len(s[\"levenshtein_similarity\"]):.3f} | {sum(s[\"token_f1\"])/len(s[\"token_f1\"]):.3f} | {sum(s[\"json_structural_similarity\"])/len(s[\"json_structural_similarity\"]):.3f} |')

print('\n=== EMBEDDING + JUDGE TABLE ===')
for model, size, stat, emb, judge, overall, lat in results:
    name = model.replace(':latest','').replace('-instruct','')
    s = scores[model]
    print(f'| {name} | {size.split()[0]} | {sum(s[\"semantic_similarity\"])/len(s[\"semantic_similarity\"]):.3f} | {sum(s[\"dag_medical_extraction_quality\"])/len(s[\"dag_medical_extraction_quality\"]):.3f} | {sum(s[\"llmjudge_correctness\"])/len(s[\"llmjudge_correctness\"]):.3f} |')

print('\n=== PASS RATES TABLE ===')
for model, size, stat, emb, judge, overall, lat in results:
    name = model.replace(':latest','').replace('-instruct','')
    pr = pass_rates[model]
    total_p = sum(pr[m][0] for m in pr)
    total_t = sum(pr[m][1] for m in pr)
    dag_p = pr['dag_medical_extraction_quality'][0]/pr['dag_medical_extraction_quality'][1]*100
    llm_p = pr['llmjudge_correctness'][0]/pr['llmjudge_correctness'][1]*100
    sem_p = pr['semantic_similarity'][0]/pr['semantic_similarity'][1]*100
    ov = total_p/total_t*100
    print(f'| {name} | {size.split()[0]} | {dag_p:.1f}% | {llm_p:.1f}% | {sem_p:.1f}% | {ov:.1f}% |')

print('\n=== LATENCY TABLE ===')
lat_sorted = sorted(results, key=lambda x: x[6])
for model, size, stat, emb, judge, overall, lat in lat_sorted:
    name = model.replace(':latest','').replace('-instruct','')
    print(f'| {name} | {lat:,.0f} | {size} |')

print('\n=== JSON STRUCTURAL SIMILARITY DISTRIBUTION ===')
import statistics
for model, size, stat, emb, judge, overall, lat in results:
    name = model.replace(':latest','').replace('-instruct','')
    vals = scores[model]['json_structural_similarity']
    avg = statistics.mean(vals)
    sd = statistics.stdev(vals) if len(vals) > 1 else 0
    mn, mx = min(vals), max(vals)
    print(f'| {name} | {avg:.3f} | {sd:.3f} | {mn:.3f} | {mx:.3f} |')
"
```

### Correlation heatmap generation

**Requires:** Python venv with `matplotlib` and `numpy`.
**Output:** `paper/assets/04-metric-correlation.png`

```bash
cd /Users/chrigel/Documents/workspace/bfh && source venv/bin/activate && python3 << 'PYEOF'
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('/Users/chrigel/Documents/workspace/bfh/dsp4d/paper/assets/questions_complete_evaluated.json') as f:
    data = json.load(f)

metric_names_order = [
    'dag_medical_extraction_quality',
    'llmjudge_correctness',
    'bleu',
    'levenshtein_similarity',
    'rouge',
    'semantic_similarity',
    'token_f1',
    'json_structural_similarity'
]
display_names = [
    'DAG Medical Extraction',
    'LLM-Judge Correctness',
    'BLEU',
    'Levenshtein Similarity',
    'ROUGE',
    'Semantic Similarity',
    'Token F1',
    'JSON Structural Sim.'
]

scores = {m: [] for m in metric_names_order}
for tc in data['testCases']:
    for inter in tc['interactions']:
        ev_map = {ev['metricName']: ev['score'] for ev in inter['evaluationResults']}
        for m in metric_names_order:
            scores[m].append(ev_map.get(m, 0.0))

n = len(metric_names_order)
corr = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        corr[i][j] = np.corrcoef(scores[metric_names_order[i]], scores[metric_names_order[j]])[0][1]

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1, aspect='equal')
ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(display_names, rotation=45, ha='right', fontsize=9)
ax.set_yticklabels(display_names, fontsize=9)
for i in range(n):
    for j in range(n):
        val = corr[i][j]
        color = 'white' if abs(val) > 0.6 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=9)
ax.set_title('Pearson Correlation Between Evaluation Metrics', fontsize=12, pad=15)
fig.colorbar(im, ax=ax, shrink=0.8)
plt.tight_layout()
plt.savefig('/Users/chrigel/Documents/workspace/bfh/dsp4d/paper/assets/04-metric-correlation.png',
            dpi=200, bbox_inches='tight')
print('Saved to paper/assets/04-metric-correlation.png')
PYEOF
```

## Section Markers

Both markdown files contain HTML comment markers (`<!-- #ID -->`) that identify AI-generated sections and their data dependencies. Use `grep -n '#R-\|#D-' paper/chapters/04-results/index.md paper/chapters/05-discussion/index.md` to locate all markers.

### Results chapter (`04-results/index.md`)

| Marker | Section | Data source | What to update |
|--------|---------|-------------|----------------|
| `#R-INTRO` | Chapter intro + metric overview | JSON structure | Metric count, metric names, categorisation |
| `#R-TAB-STAT` | Statistical metrics table | Aggregation script `STATISTICAL METRICS TABLE` | Replace table rows |
| `#R-TAB-JUDGE` | Embedding + Judge table | Aggregation script `EMBEDDING + JUDGE TABLE` | Replace table rows |
| `#R-TAB-COMPOSITE` | Composite scores table + summary text | Aggregation script `COMPOSITE TABLE` | Replace table rows + update inline numbers in paragraph below |
| `#R-TAB-PASS` | Pass rates table | Aggregation script `PASS RATES TABLE` | Replace table rows |
| `#R-TAB-JSON` | JSON structural similarity distribution | Aggregation script `JSON STRUCTURAL SIMILARITY DISTRIBUTION` | Replace table rows |
| `#R-TAB-SEMANTIC` | Semantic vs. Format table | Subset of stat + judge data | Replace table rows + inline numbers |
| `#R-CORRELATION` | Correlation heatmap + analysis | Heatmap script | Regenerate PNG, update r-values in text if they change |
| `#R-TAB-LATENCY` | Latency table | Aggregation script `LATENCY TABLE` | Replace table rows + inline numbers |

### Discussion chapter (`05-discussion/index.md`)

| Marker | Section | Depends on | Numbers to update |
|--------|---------|-----------|-------------------|
| `#D-SIZE` | Model Size vs. Performance | `#R-TAB-COMPOSITE` | Composite scores (0.470, 0.390, 0.363, etc.) |
| `#D-CLOUD` | Cloud Models Advantage | `#R-TAB-COMPOSITE` | Semantic sim (0.861), composites (0.419/0.416), gap % |
| `#D-FORMAT` | Format Compliance Problem | `#R-TAB-JSON` | JSON sim scores (0.000, 0.059, 0.103, 0.372, 0.440) |
| `#D-SEMANTIC` | Semantic Understanding | `#R-TAB-SEMANTIC` | Semantic sim range (0.650–0.861), individual scores |
| `#D-MISTRAL` | Mistral-Nemo Outlier | `#R-TAB-JUDGE` | DAG score (0.261 vs 0.528), JSON sim (0.059) |
| `#D-RQ` | Research Questions | `#R-TAB-PASS` | Pass rates (90.3%, 93.5%, 100%, 58.1%) |
| `#D-LIMITS` | Limitations | Methodology | Mostly static — update only if methodology changes |
| `#D-FUTURE` | Future Work | — | Static |

## Reproduction Checklist

When `questions_complete_evaluated.json` changes:

1. **Check structure**: Verify the metric list hasn't changed (`metricName` values in `evaluationResults`). If metrics were added/removed, update `metric_names_order` in the heatmap script and the categorisation (stat/embedding/judge) in the aggregation script, and update `#R-INTRO`.

2. **Run the aggregation script** (above). Copy output into the corresponding `#R-TAB-*` sections in `04-results/index.md`.

3. **Run the heatmap script** (above). This overwrites `paper/assets/04-metric-correlation.png`. Update the r-values in `#R-CORRELATION` text if they changed.

4. **Update the discussion chapter** (`05-discussion/index.md`). Use the marker table above to locate each `#D-*` section and update the referenced numbers from the corresponding `#R-*` source.

5. **Rebuild the PDF**: `cd paper && task build`

## Terminology

- **Silver Answers**: AI-generated reference answers (produced by Gemini). Used throughout chapters 04 and 05.
- **Golden Answers**: Only use when answers have been generated or fully validated by domain experts (medical professionals). The current dataset contains Silver Answers with partial expert validation.

## Generated Assets

| File | Generated by | Regenerate when |
|------|-------------|-----------------|
| `paper/assets/04-metric-correlation.png` | Heatmap script (matplotlib) | JSON input changes |
| `paper/chapters/04-results/index.md` | Manual text + aggregation script output | JSON input changes |
| `paper/chapters/05-discussion/index.md` | Manual interpretive text | Numbers change significantly |

## Dependencies

- Python 3.13+ (venv at `/Users/chrigel/Documents/workspace/bfh/venv/`)
- `matplotlib`, `numpy` (installed in venv)
- No other dependencies for data extraction (uses only stdlib `json`, `statistics`, `collections`)
