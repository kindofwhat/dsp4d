#!/usr/bin/env python3
"""Generate results charts for the DSP4D paper."""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')

# Data from results tables
models = [
    'Gemini 2.5 Pro', 'Gemma3:27b', 'Kimi-K2.5', 'GPT-5-nano',
    'Qwen3.5-35B-A3B', 'Granite3.3:2b', 'Mistral-Nemo',
    'GLM4:9b', 'Qwen2:7b', 'Phi3.5:3.8b', 'Llama3:8b'
]

sizes = [
    'Large (Cloud)', '27B', 'Large (Cloud)', 'Small (Cloud)',
    '35B (MoE 3B)', '2B', '12B', '9B', '7B', '3.8B', '8B'
]

# Composite overall scores
overall = [0.468, 0.409, 0.398, 0.395, 0.390, 0.344, 0.339, 0.335, 0.315, 0.303, 0.300]

# Per-metric data for radar chart
sem_sim =   [0.835, 0.790, 0.818, 0.861, 0.829, 0.843, 0.794, 0.732, 0.765, 0.795, 0.650]
dag =       [0.569, 0.510, 0.576, 0.510, 0.505, 0.407, 0.424, 0.425, 0.419, 0.356, 0.387]
llm_judge = [0.752, 0.671, 0.597, 0.537, 0.513, 0.415, 0.553, 0.466, 0.382, 0.481, 0.434]
json_sim =  [0.457, 0.362, 0.374, 0.335, 0.371, 0.258, 0.065, 0.231, 0.178, 0.098, 0.129]

# Colors - distinguish cloud vs local
colors = []
for s in sizes:
    if 'Cloud' in s:
        colors.append('#4361ee')  # blue for cloud
    elif 'MoE' in s:
        colors.append('#7209b7')  # purple for MoE
    else:
        colors.append('#f72585')  # pink for local SLMs

# ─── Figure 1: Overall Ranking Bar Chart ───

fig1, ax1 = plt.subplots(figsize=(10, 5))

# Sort by overall score (already sorted)
y_pos = np.arange(len(models))
bars = ax1.barh(y_pos, [o * 100 for o in overall], color=colors, height=0.6)

# Labels
ax1.set_yticks(y_pos)
ax1.set_yticklabels([f'{m} ({s})' for m, s in zip(models, sizes)], fontsize=9)
ax1.invert_yaxis()
ax1.set_xlabel('Overall Composite Score (%)', fontsize=10)
ax1.set_xlim(0, 70)

# Add percentage labels
for bar, val in zip(bars, overall):
    ax1.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height()/2,
             f'{val*100:.1f}%', va='center', fontsize=9)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4361ee', label='Cloud'),
    Patch(facecolor='#7209b7', label='MoE (local)'),
    Patch(facecolor='#f72585', label='Local SLM'),
]
ax1.legend(handles=legend_elements, loc='lower right', fontsize=9)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
plt.tight_layout()
fig1.savefig('assets/04-overall-ranking.png', dpi=200, bbox_inches='tight')
print('Saved: assets/04-overall-ranking.png')


# ─── Figure 2: Radar Chart (Top 5 models) ───

fig2, ax2 = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

categories = ['DAG\nExtraction', 'LLM-Judge\nField Comp.', 'JSON\nSimilarity', 'Semantic\nSimilarity']
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # close the polygon

# Top 5 models
top5_idx = [0, 1, 2, 3, 4]
top5_colors = ['#4361ee', '#f72585', '#4361ee', '#4361ee', '#7209b7']
top5_labels = ['Gemini 2.5 Pro', 'Gemma3:27b', 'Kimi-K2.5', 'GPT-5-nano', 'Qwen3.5-35B-A3B']

for idx, color, label in zip(top5_idx, top5_colors, top5_labels):
    values = [dag[idx], llm_judge[idx], json_sim[idx], sem_sim[idx]]
    values += values[:1]
    ax2.plot(angles, values, 'o-', linewidth=1.5, color=color, label=label, markersize=4)
    ax2.fill(angles, values, alpha=0.05, color=color)

ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=10)
ax2.set_ylim(0, 1.0)
ax2.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax2.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=8)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

plt.tight_layout()
fig2.savefig('assets/04-metric-profile-radar.png', dpi=200, bbox_inches='tight')
print('Saved: assets/04-metric-profile-radar.png')

print('Done.')
