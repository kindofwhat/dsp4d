# Initial Project Brainstorming

**Purpose:** Early-stage brainstorming, meeting notes, and project ideation before formal structure was established.

## Contents

This directory contains the initial thoughts and discussions that led to the DSP4D project:

- Meeting notes from workshop with Beni (November 4, 2025)
- Initial ideas for semester thesis topics
- Early brainstorming on use cases
- Rough problem statements before formalization

## Key Concepts That Emerged

### Smart Search Idea
- Principle: Re-search documents using the answer generated
- Advantage: Relatively new research approach, scientifically interesting and implementable
- Related to: Data sovereignty and AI

### Medical Use Case (Ärzte Appliance)
- **Motivation**: Doctors overwhelmed with digital information after 18:00
  - Need: Quick summaries and next action items from lengthy reports
- **Requirements**:
  - Data sensitivity (HIPAA/GDPR compliance)
  - LLM in practice with RAG
  - Structured reports (potential for fine-tuning)
  - Integration with Electronic Patient Dossier (EPD)
  - Communication via hin.ch platform
- **Prototype/MVP Focus**: Classification/abstract generation with data sovereignty procedures (DSP)

### Core Research Question
**"How small can a model be while still extracting relevant information from sensitive documents?"**

Considerations:
- PocketLLM on USB stick, Raspberry Pi, or mobile phone
- WebLLM in browser
- Evaluation frameworks available
- Finding the breakpoint/threshold

### Other Initial Ideas
- Can LLMs be compressed/pruned while maintaining performance?
- Tool experimentation and evaluation

## How These Ideas Evolved

These initial brainstorming sessions evolved into the formal 3-month research project documented in `project.md`:

**Title:** LLM Size Optimization for Sensitive Data Processing with RAG

**Focus Areas (from initial ideas):**
1.  Medical document summarization (Ärzte Appliance use case)
2.  Data sovereignty procedures for sensitive data
3.  Finding optimal model size threshold
4.  RAG impact on smaller models
5.  On-device deployment (Raspberry Pi, edge devices)

**What Changed:**
- Expanded to include financial and legal scenarios (not just medical)
- Formalized evaluation framework (RAGAS, benchmarks)
- Added comprehensive security testing
- Structured into 5 phases with clear deliverables

## Historical Context

This directory preserves the "raw" ideation phase. Keep it for:
- Understanding project genesis
- Tracing how requirements evolved
- Reference for future related projects
- Documenting stakeholder input (Beni's 3 doctors)

## Related Documents

- **Formal Project Plan**: `../project.md`
- **Thesis Proposal**: `../Themenantrag Gen KI 1.0 HS25-Sprecher-Haegler.docx`
- **Structured Research**: `../phase1-research/`
- **Use Case Details**: `../phase2-test-design/scenarios/medical-diagnosis.md`

---

*Note: This directory is kept for historical reference. Active development follows the phase-based structure.*
