# Introduction

*A Note on the Craft*
```Text

Because we value the precision, structure, and flawless tone that modern 
technology provides, you may safely assume that the bulk of this text was 
meticulously woven by frontline AI.

However, we do maintain a strict "Human in the Loop" policy for brilliance.
Should you encounter a particularly extraordinary insight, a wicked bit
of wit, or a statement of profound cleverness, you may tip your hat to
us—the authors. We’ll take the credit for the soul; the machine can 
have the grammar.

```


General practitioners (GPs) spend significant time on administrative tasks — triaging laboratory reports, managing insurance correspondence, and updating patient records — time that is unavailable for direct patient care. Automating these documentation workflows with Generative AI (GenAI) is technically feasible, but the sensitivity of medical data prohibits the use of cloud-based solutions in many jurisdictions. This creates a practical constraint: AI-assisted document processing must function entirely on local hardware, without transmitting Protected Health Information (PHI) to external servers.

Locally deployed Large Language Models (LLMs) offer a potential resolution. By running inference on the physician’s workstation, data sovereignty is preserved by design. However, this raises a critical question: how small can a model be while maintaining clinically acceptable extraction quality on consumer-grade hardware? This thesis develops and validates a framework to answer that question — identifying the minimum viable model size for structured clinical document classification through systematic evaluation of eleven models across 62 test cases.

## Research Questions

1. What is the minimum model size for reliable clinical document classification in a Zero-Shot setting?
2. Which context engineering strategy is most effective for generating high-quality reference answers from medical documents, and how does the choice of strategy influence downstream evaluation?
3. Can sub-3B parameter models achieve clinically acceptable extraction quality on standard consumer hardware?