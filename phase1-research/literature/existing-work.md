# Current Research on LLM Size vs Performance and Open-Source Models in Leaderboards

## Executive Summary
Recent research reveals a paradigm shift in LLM development, with the "densing law" showing that equivalent performance can be achieved with exponentially fewer parameters over time. RAG technology demonstrates 10-30% performance improvements for smaller models, while leaderboards increasingly integrate open-source models alongside commercial offerings.

## 1. Key Research Findings on LLM Size vs Performance

### 1.1 The "Densing Law" Discovery (2024-2025)
Recent research introduces 'capability density', defined as capability per parameter, showing that **capability density doubles approximately every 3.5 months** [1]. This means the parameter size of LLMs with equivalent performance is halved approximately every 3.5 months. For example, MiniCPM-1-2.4B released on 1 February 2024, can achieve comparable or even superior performance with Mistral-7B released on 27 September 2023 [1].

### 1.2 Evolution of Scaling Laws
The field has evolved through several key phases:
- **Kaplan Scaling Laws (2020)**: Initial focus on parameter count as primary driver
- **Chinchilla Laws (2022)**: Model size and training tokens should be scaled in equal proportions [2]
- **Current Understanding**: About two-thirds of improvements in LLM performance over the last decade came from increases in model scale [3]

### 1.3 Diminishing Returns and Trade-offs
Research identifies critical trade-offs in model scaling:

| Trade-off | Small Models | Large Models |
|-----------|--------------|--------------|
| **Speed vs. Accuracy** | Faster inference, lower latency for real-time applications | Higher accuracy on complex tasks but slower generation |
| **Cost vs. Performance** | Cost-effective for simpler tasks | Massive computational resources required |
| **Scalability** | Easy deployment on edge devices | Requires specialized infrastructure |

Key finding: "While increasing LLM model size generally leads to better performance, there's a point of diminishing returns. Beyond a certain size, the gains in accuracy or reasoning become minimal compared to the costs" [4].

### 1.4 Test-Time Compute Revolution (2024)
OpenAI's o1 models represent a paradigm shift, using **chains of thought** generation before providing answers. This compute-optimal scaling strategy emphasizes text generation steps over pure model size, yielding better results for reasoning tasks [5].

## 2. RAG's Impact on Smaller Models

### 2.1 Quantified Performance Improvements
Recent RAG implementations show substantial gains:
- **MRAG**: 10% improvement in retrieval success ratio on exact matches, 25% boost on category matches [6]
- **Fusion RAG**: 10-30% accuracy gains over standard RAG [6]
- **RAFT**: Outperforms traditional RAG in specialized domains like medicine [7]

### 2.2 Cost-Effectiveness Analysis
"A well-designed RAG system can actually be more cost-effective than an enormous model that tries to absorb all knowledge internally" [8]. This is particularly relevant for:
- Domain-specific applications
- Privacy-sensitive deployments
- Resource-constrained environments

### 2.3 Architecture Innovations in RAG (2024)

| Innovation | Description | Impact |
|------------|-------------|--------|
| **Speculative RAG** | Parallel processing with smaller specialized models | Reduced latency |
| **RAFT** | Combines RAG with fine-tuning using synthetic datasets | Domain specialization |
| **Adaptive Retrieval** | Dynamic retrieval based on query complexity | Optimized resource usage |
| **GraphRAG** | Knowledge graph integration | Improved multi-hop reasoning |

## 3. Leaderboard Treatment of Open-Source Models

### 3.1 Major Open-Source Focused Leaderboards

#### Hugging Face Open LLM Leaderboard
- **Focus**: Exclusively open-source models
- **Benchmarks**: IFEval, BBH, MATH, GPQA, MUSR, MMLU-PRO [9]
- **Features**: Filtering by official provider status, edge optimization [10]

#### Vellum LLM Leaderboard
- **Scope**: Both commercial and open-source models
- **Metrics**: Capabilities, price, context window [11]
- **Update Frequency**: Models released after April 2024

#### Artificial Analysis Leaderboard
- **Coverage**: Over 100 models
- **Unique Features**: Inference speed, latency, cost per token analysis
- **Comparison Tools**: Direct performance vs. cost trade-off visualizations

### 3.2 Evaluation Methodologies
Modern leaderboards employ diverse evaluation approaches:
- **Mechanical Benchmarks**: Traditional accuracy metrics
- **Human Judgment**: LMSYS Chatbot Arena using crowdsourced preferences [10]
- **Task-Specific Evaluation**: Code generation, multimodal capabilities
- **RAG-Specific Metrics**: Context relevance, answer faithfulness

### 3.3 Top Performing Open Models (2024)

| Model Family | Parameter Range | Key Strengths |
|--------------|-----------------|---------------|
| Llama 3 | 8B-70B | General purpose, wide language support |
| Mistral/Mixtral | 7B-8x7B | Efficiency, MoE architecture |
| DeepSeek | Various | Strong reasoning capabilities |
| Phi-3 | 1B-14B | Small but capable, edge-optimized |
| Gemma | 2B-27B | Google's architecture, good multilingual |

## 4. Implications for Sensitive Data Applications

### 4.1 Sweet Spot Analysis
For sensitive data handling with RAG:
- **Optimal Range**: 7B-13B parameters with RAG
- **Performance**: Can match 70B+ models for specific tasks
- **Deployment**: Feasible for on-premise, air-gapped environments

### 4.2 Evaluation Framework Recommendations
1. **RAGAS**: RAG-specific metrics (context relevance, faithfulness)
2. **Security Metrics**: Data leakage tests, prompt injection resistance
3. **Performance Benchmarks**: Latency, throughput, memory usage
4. **Domain-Specific Tests**: Medical, financial, legal accuracy

## 5. Future Trajectories

### 5.1 Near-term Predictions (2025)
- Model sizes for equivalent performance will continue halving every 3.5 months
- RAG will become standard for production deployments
- Hybrid approaches (RAG + fine-tuning) will dominate specialized applications

### 5.2 Research Directions
- **Tensor-based Reranking**: More sophisticated retrieval mechanisms
- **Multimodal RAG**: Integration of vision-language models
- **Federated Learning**: Distributed training for privacy-sensitive applications

## References

[1] Xiao et al. (2025). "Densing law of LLMs". Nature Machine Intelligence. Available at: https://www.nature.com/articles/s42256-025-01137-0

[2] Bidry, M. (2024). "Is it possible for smaller language models to outperform larger ones?". Medium. Available at: https://medium.com/@mahmoud.bidry11/is-it-possible-for-smaller-language-models-to-outperform-larger-ones-a5e1dae0f6eb

[3] (2024). "Beyond Bigger Models: The Evolution of Language Model Scaling Laws". Medium. Available at: https://medium.com/@aiml_58187/beyond-bigger-models-the-evolution-of-language-model-scaling-laws-d4bc974d3876

[4] Label Your Data (2024). "LLM Model Size: Parameters, Training, and Compute Needs in 2025". Available at: https://labelyourdata.com/articles/llm-model-size

[5] Dataiku (2024). "A Dizzying Year for Language Models: 2024 in Review". Available at: https://blog.dataiku.com/a-dizzying-year-for-language-models-2024-in-review

[6] Jain, M. (2024). "2024 was mostly about RAG. The Survey". Medium. Available at: https://medium.com/@j13mehul/2024-was-mostly-about-rag-c744bd0a2654

[7] Springer (2025). "Retrieval-Augmented Generation (RAG)". Business & Information Systems Engineering. Available at: https://link.springer.com/article/10.1007/s12599-025-00945-3

[8] Paul, R. (2025). "Improving LLM Performance - Scaling vs. Retrieval vs. Fine-Tuning". Available at: https://www.rohan-paul.com/p/improving-llm-performance-scaling

[9] Hugging Face (2024). "Open LLM Leaderboard". Available at: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

[10] Suzuki (2025). "LLM Model Selection Made Easy: The Most Useful Leaderboards for Real-World Applications". DEV Community. Available at: https://dev.to/suzuki0430/llm-model-selection-made-easy-the-most-useful-leaderboards-for-real-world-applications-27go

[11] Vellum (2025). "LLM Leaderboard 2025". Available at: https://www.vellum.ai/llm-leaderboard

## Additional Academic References

- Chen et al. (2024). "Benchmarking large language models in retrieval-augmented generation". AAAI Conference on Artificial Intelligence.
- Es et al. (2023). "RAGAS: Automated evaluation of retrieval augmented generation". arXiv:2309.15217.
- Lewis et al. (2020). "Retrieval-augmented generation for knowledge-intensive NLP tasks". Advances in Neural Information Processing Systems.
- Yu et al. (2024). "Evaluation of Retrieval-Augmented Generation: A Survey". arXiv:2405.07437.
- Zhang et al. (2024). "RAFT: Adapting Language Model for Domain Specific RAG". arXiv preprint.