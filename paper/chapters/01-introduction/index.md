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


The healthcare sector currently faces a dual mandate: increasing operational efficiency while upholding rigorous standards for patient safety and data privacy. For general practitioners (GPs), this pressure manifests as an intensified administrative workload. Beyond direct patient consultations, GPs frequently spend hours triaging laboratory reports, managing insurance correspondence, and updating patient records. This administrative tail—often managed after clinic hours—leads to significant cognitive fatigue and systemic latency in patient care.

The strategic challenge lies in automating these documentation workflows to alleviate physician burnout without compromising Data Sovereignty. Traditional cloud-based AI solutions introduce immense regulatory complexity; in many jurisdictions, the sensitivity of medical data explicitly prohibits the use of external servers. Consequently, there is an urgent need for automation that functions independently of external online services and operates without the need for prohibitively expensive, enterprise-grade hardware.

Generative Artificial Intelligence (GenAI) offers a potential resolution to this tension. By deploying locally hosted Large Language Models (LLMs), high-performance AI functionality can be delivered in a decentralized manner, entirely severed from external connectivity. This architecture ensures that sensitive data remains on the physician’s local workstation. This project addresses the critical imperative to identify a resource-efficient paradigm for GenAI, bridging the gap between advanced automation and strict local data governance on standard hardware.
  
## Motivation

The operational reality of modern general practice is defined by a growing imbalance between clinical care and clerical overhead. The time required to review complex documentation and generate correspondence is no longer a mere inconvenience; it is a primary driver of physician burnout that diminishes time available for patient interaction. While automated systems could theoretically absorb this burden, their integration is stalled by a technological dilemma regarding medical confidentiality.

The primary barrier to adopting GenAI in healthcare is the architectural reliance of State-of-the-Art (SOTA) models on cloud infrastructure. While commercial LLMs possess the reasoning capabilities required to triage medical data, they typically require the transmission of Protected Health Information (PHI) to third-party servers. In many legal frameworks, this creates an unacceptable risk profile and often constitutes a direct violation of data protection regulations. Practitioners are thus forced into a false dichotomy: leverage powerful cloud-based tools at the risk of non-compliance, or forego AI assistance entirely to maintain security. Currently, there is a lack of validated frameworks for deploying high-quality AI models within a secure, local practice environment using standard hardware.

To bridge this gap, this thesis develops and validates an algorithmic selection framework designed to identify the most resource-efficient LLMs for local deployment. The objective is to automate documentation and correspondence tasks while ensuring absolute data sovereignty. This research establishes a necessary balance between computational efficiency—specifically inference speed and memory footprint—and semantic accuracy, ensuring that decentralized processing does not compromise the reliability of medical outputs.

## Research Questions

1. What is the minimum model size for reliable clinical document classification in a Zero-Shot setting?
2. Which context engineering strategy is most effective for generating high-quality reference answers from medical documents, and how does the choice of strategy influence downstream evaluation?
3. Can sub-3B parameter models achieve clinically acceptable extraction quality on standard consumer hardware?
