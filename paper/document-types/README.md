# Document Types & Workflows (GraSCCo Based)

**Goal:** Map clinical narratives from the **Graz Synthetic Clinical text Corpus (GraSCCo)** to clear classification types and action workflows.

## Overview

This directory contains definitions of clinical document types and associated workflows as represented in the GraSCCo corpus. GraSCCo provides synthetic German clinical texts that allow for realistic evaluation of:
1. **Clinical Findings**: Extraction of diagnoses and symptoms.
2. **Workflow Actions**: Determining the next clinical step (e.g., follow-up, surgery).

## Document Types in GraSCCo
testtest

We utilize the categorization provided by GraSCCo (or derived from its clinical narratives), focusing on:
- **Discharge Summaries (Entlassungsbriefe)**
- **Diagnostic Reports**
- **Clinical Progress Notes**
- (Additional types as extracted from the Zenodo dataset)

## Workflow Structure

Each workflow follows this pattern:

```
Document Type → Classification → Finding Severity → Recommended Action
```

### Example: X-Ray Results Workflow

```
X-Ray Result
├── Acute Fracture → URGENT: Orthopedic surgery consult within 48h
├── Suspicious Mass → Schedule CT scan + oncology referral within 1 week
├── Mild Degenerative → Schedule routine orthopedic consult within 4 weeks
└── Normal Findings → No action required, file in patient record
```

## Directory Structure

```
document-types/
├── README.md                          # This file
├── definitions/                       # What each type is
│   ├── x-ray-results.md
│   ├── lab-reports.md
│   ├── imaging-reports.md
│   ├── prescriptions.md
│   ├── referrals.md
│   ├── pathology-reports.md (optional)
│   ├── ecg-results.md (optional)
│   ├── consultation-notes.md (optional)
│   ├── discharge-summaries.md (optional)
│   └── vaccine-records.md (optional)
└── workflows/                         # Type → Action mappings
    ├── x-ray-workflow.md
    ├── lab-workflow.md
    ├── imaging-workflow.md
    ├── prescription-workflow.md
    └── referral-workflow.md
```

## Definition Template

Each `definitions/*.md` file should contain:

```markdown
# [Document Type Name]

## Description
What this document type is, what information it contains.

## Typical Content
- Key fields/sections
- Common findings
- Critical information to extract

## Urgency Levels
- URGENT: Requires immediate action (same day)
- HIGH: Action within 1 week
- MEDIUM: Action within 4 weeks
- LOW: Routine, no specific timeline
- NONE: No action required

## Common Findings & Actions
List typical findings and their corresponding actions

## Example Document Structure
Show what a typical document looks like (anonymized)

## Classification Challenges
What makes this document type hard to classify or interpret?
```

## Workflow Template

Each `workflows/*.md` file should contain:

```markdown
# [Document Type] Workflow

## Decision Tree

[ASCII or mermaid diagram showing: finding → action]

## Action Categories

### URGENT Actions
- [List urgent actions with criteria]

### Routine Actions
- [List routine actions with criteria]

### No Action
- [Criteria for no action required]

## Edge Cases
- Ambiguous findings
- Multiple simultaneous findings
- Conflicting information

## Safety Considerations
- What errors could be harmful?
- What findings must never be missed?
```

## Task Checklist

- [ ] Define 5 core document types (x-ray, lab, imaging, prescription, referral)
- [ ] Write detailed definitions for each core type
- [ ] Create workflow diagrams for each core type
- [ ] Identify 3-5 additional document types (expand to 10 total)
- [ ] Validate document types with medical expert
- [ ] Create sample anonymized documents for each type
- [ ] Document classification challenges per type

## Clinical Expert Input Needed

- [ ] Validate document type categories
- [ ] Review action appropriateness
- [ ] Identify common edge cases
- [ ] Provide realistic example documents (anonymized)
- [ ] Define urgency levels per finding type

## Notes

- **Synthetic data only**: All example documents must be synthetic/anonymized
- **Clinical accuracy**: Workflows must be medically appropriate
- **Actionable**: Each finding must map to a clear, specific action
- **Testable**: Workflows must be measurable (classification accuracy, action appropriateness)
