# Phase 3: Experimental Setup

**Duration:** Weeks 7-8
**Effort:** ~15 hours
**Status:** Not Started

## Objectives

1. Select model sizes to test (1B, 3B, 7B, 13B parameters)
2. Set up consistent inference environment
3. Implement basic RAG pipeline with vector database
4. Create reproducible retrieval settings
5. Establish baseline testing infrastructure

## Directory Structure

```
phase3-setup/
├── README.md                          # This file
├── models/                            # Model selection and setup
│   ├── model-selection.md            # Selected models with justification
│   ├── model-configs/                # Model configuration files
│   │   ├── llama-3.2-1b.yaml
│   │   ├── llama-3.2-3b.yaml
│   │   ├── mistral-7b.yaml
│   │   └── llama-3.1-13b.yaml
│   ├── quantization/                 # Quantization settings
│   │   ├── quantization-guide.md
│   │   └── benchmarks.md
│   └── download-scripts/             # Scripts to download models
│       └── download-models.sh
└── rag-implementation/                # RAG pipeline setup
    ├── rag-architecture.md           # RAG system design
    ├── vector-db/                    # Vector database setup
    │   ├── chromadb-setup.md
    │   ├── qdrant-setup.md
    │   └── comparison.md
    ├── embeddings/                   # Embedding model setup
    │   ├── embedding-selection.md
    │   └── embedding-configs/
    ├── chunking/                     # Document chunking strategies
    │   ├── chunking-strategy.md
    │   └── chunk-experiments.py
    ├── retrieval/                    # Retrieval configuration
    │   ├── retrieval-params.md       # k, similarity threshold, etc.
    │   └── retrieval-experiments.py
    └── pipeline-code/                # Core RAG implementation
        ├── requirements.txt
        ├── rag_pipeline.py           # Main RAG pipeline
        ├── indexing.py               # Document indexing
        └── retrieval.py              # Retrieval logic
```

## Key Deliverables

### Week 7: Model Selection & Setup (8 hours)

#### Model Selection Criteria

**Selected Model Sizes:**
- **1B parameters**: Llama 3.2 1B, Phi-3-mini
- **3B parameters**: Llama 3.2 3B, Phi-3-small
- **7B parameters**: Mistral 7B v0.3, Llama 3.1 7B
- **13B parameters**: Llama 3.1 13B, Vicuna 13B

**Selection Rationale:** (`models/model-selection.md`)
- Coverage of small (1B-3B), medium (7B), and larger (13B) ranges
- Focus on open-source models with strong leaderboard performance
- Llama 3.2 series for newest architecture
- Mistral for efficient MoE architecture
- Phi-3 for edge-optimized performance

#### Environment Requirements

- [ ] **Hardware Setup**
  - GPU: Minimum 24GB VRAM (for 13B models)
  - RAM: 32GB minimum
  - Storage: 100GB for models and datasets
  - Alternative: Cloud instances (A100, H100)

- [ ] **Software Environment**
  - Python 3.10+
  - PyTorch 2.x with CUDA support
  - HuggingFace Transformers
  - Quantization: bitsandbytes, GPTQ, or AWQ

- [ ] **Quantization Settings** (`models/quantization/`)
  - 4-bit quantization for 13B models
  - 8-bit for 7B models
  - FP16 for smaller models (1B-3B)
  - Document memory usage and latency impact

#### Consistent Inference Configuration

```yaml
# Example: llama-3.2-1b.yaml
model:
  name: "meta-llama/Llama-3.2-1B"
  quantization: "fp16"
  max_new_tokens: 512
  temperature: 0.1  # Low for deterministic responses
  top_p: 0.9
  repetition_penalty: 1.1

hardware:
  device: "cuda"
  precision: "fp16"
  batch_size: 1

generation:
  do_sample: false  # Greedy decoding for reproducibility
  num_beams: 1
  seed: 42
```

### Week 8: RAG Implementation (7 hours)

#### Vector Database Selection

- [ ] **Evaluate Options** (`rag-implementation/vector-db/comparison.md`)
  - **ChromaDB**: Simple, Python-native, good for prototyping
  - **Qdrant**: Production-ready, high performance, filter support
  - **Recommendation**: Start with ChromaDB for simplicity, migrate to Qdrant if needed

- [ ] **Setup Vector Database**
  - Install and configure chosen database
  - Test connection and basic operations
  - Document setup process

#### Embedding Model Selection

**Recommended Embedding Models:**
- **all-MiniLM-L6-v2**: Fast, 384 dimensions, good baseline
- **bge-base-en-v1.5**: Better performance, 768 dimensions
- **e5-large-v2**: Highest quality, 1024 dimensions

**Selection Criteria:** (`rag-implementation/embeddings/embedding-selection.md`)
- Balance between quality and speed
- Dimension size vs. accuracy trade-off
- Domain-specific embeddings for medical/legal/financial

#### Chunking Strategy

- [ ] **Chunking Parameters** (`rag-implementation/chunking/chunking-strategy.md`)
  - Chunk size: Test 256, 512, 1024 tokens
  - Overlap: 10-20% for context preservation
  - Method: Sentence-aware splitting (use langchain RecursiveCharacterTextSplitter)
  - Domain-specific: Respect document structure (paragraphs, sections)

- [ ] **Chunking Experiments** (`rag-implementation/chunking/chunk-experiments.py`)
  ```python
  # Test different chunking strategies
  chunk_sizes = [256, 512, 1024]
  overlap_ratios = [0.1, 0.15, 0.2]
  # Measure retrieval quality for each combination
  ```

#### Retrieval Configuration

- [ ] **Retrieval Parameters** (`rag-implementation/retrieval/retrieval-params.md`)
  - **k (number of documents)**: Test k=3, 5, 10
  - **Similarity threshold**: 0.7 (filter out low-relevance docs)
  - **Reranking**: Optional cross-encoder reranking for higher quality
  - **Metadata filtering**: Filter by document type, date, sensitivity level

- [ ] **Retrieval Experiments** (`rag-implementation/retrieval/retrieval-experiments.py`)
  ```python
  # Test retrieval quality with different k values
  for k in [3, 5, 10]:
      results = evaluate_retrieval(queries, k=k)
      # Measure: precision@k, recall@k, MRR
  ```

#### RAG Pipeline Implementation

**Core Components:** (`rag-implementation/pipeline-code/`)

1. **rag_pipeline.py** - Main RAG orchestration
```python
class RAGPipeline:
    def __init__(self, model, vector_db, embedding_model):
        # Initialize components

    def query(self, question: str, k: int = 5) -> dict:
        # 1. Embed question
        # 2. Retrieve top-k documents
        # 3. Format prompt with retrieved context
        # 4. Generate answer
        # 5. Return answer + metadata
```

2. **indexing.py** - Document indexing
```python
def index_documents(documents, vector_db, chunking_config):
    # 1. Chunk documents
    # 2. Generate embeddings
    # 3. Store in vector database
```

3. **retrieval.py** - Retrieval logic
```python
def retrieve(query, vector_db, k=5, threshold=0.7):
    # 1. Embed query
    # 2. Search vector database
    # 3. Filter by similarity threshold
    # 4. Return ranked documents
```

## Reproducibility Checklist

- [ ] **Environment Configuration**
  - Pin all package versions in `requirements.txt`
  - Document Python version
  - Document CUDA version and GPU model
  - Use virtual environment

- [ ] **Deterministic Settings**
  - Set random seeds (Python, NumPy, PyTorch, model)
  - Disable sampling (greedy decoding) for tests
  - Use fixed temperature (0.1) for consistency
  - Document all hyperparameters

- [ ] **Version Control**
  - Git track all configuration files
  - Version datasets (use DVC or Git LFS)
  - Tag model versions used in experiments
  - Document exact HuggingFace model IDs

## Testing Infrastructure

- [ ] **Smoke Tests**
  - Test each model loads correctly
  - Verify inference works with sample prompt
  - Test RAG pipeline end-to-end with 1 query
  - Verify vector database operations

- [ ] **Performance Baselines**
  - Measure inference latency per model
  - Measure memory usage per model
  - Test throughput (tokens/second)
  - Document baseline metrics

## Handoff to Phase 4

**Prerequisites for Phase 4:**
- All models downloaded and tested
- RAG pipeline implemented and verified
- Vector database indexed with Phase 2 documents
- Baseline performance metrics documented

**Artifacts to Deliver:**
1. Model configuration files for all selected models
2. Working RAG pipeline code with documentation
3. Indexed vector database with test documents
4. Environment setup guide and requirements.txt
5. Baseline performance benchmarks

## Resources

### Model Sources
- Hugging Face Model Hub: https://huggingface.co/models
- Llama models: https://huggingface.co/meta-llama
- Mistral models: https://huggingface.co/mistralai
- Phi-3 models: https://huggingface.co/microsoft

### RAG Tools
- LangChain: https://python.langchain.com/docs/use_cases/question_answering/
- ChromaDB: https://docs.trychroma.com/
- Qdrant: https://qdrant.tech/documentation/
- Sentence Transformers: https://www.sbert.net/

### Quantization Tools
- bitsandbytes: https://github.com/TimDettmers/bitsandbytes
- GPTQ: https://github.com/IST-DASLab/gptq
- AWQ: https://github.com/mit-han-lab/llm-awq

## Notes

- **Compute Resources**: Consider cloud instances if local GPU insufficient
- **Model Downloads**: Large files (5-25GB each), plan bandwidth/storage
- **Quantization Trade-offs**: Document accuracy vs. speed vs. memory
- **RAG Quality**: Retrieval quality is critical - test thoroughly before Phase 4
- **Reproducibility**: This is research - document everything!
