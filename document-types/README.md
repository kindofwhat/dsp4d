# Document Types & Workflows

**Goal:** Define 5-10 medical document types with clear type → action workflows

## Overview

This directory contains definitions of medical document types and their associated clinical workflows. Each document type has:
1. **Definition**: What the document is, what it contains
2. **Workflow**: Type → Action mappings (what actions to take based on findings)
3. **Examples**: Sample documents (anonymized/synthetic)

## Document Types (Target: 5-10)

### Confirmed Types

1. **X-Ray Results** (`definitions/x-ray-results.md`)
   - Plain radiography findings
   - Actions: Surgery, specialist referral, follow-up imaging, no action

2. **Lab Reports** (`definitions/lab-reports.md`)
   - Blood work, urinalysis, cultures, metabolic panels
   - Actions: Urgent hospitalization, medication adjustment, follow-up, no action

3. **Medical Imaging Reports** (`definitions/imaging-reports.md`)
   - CT, MRI, ultrasound findings
   - Actions: Surgery, specialist referral, follow-up imaging, no action

4. **Prescriptions** (`definitions/prescriptions.md`)
   - Medication orders, renewals, changes
   - Actions: Approve, clarify, deny/alternative, forward to specialist

5. **Referrals** (`definitions/referrals.md`)
   - Specialist consultation requests
   - Actions: Approve, request tests first, deny/manage, redirect specialist

### Potential Additional Types (expand to 10)

6. **Pathology Reports**
   - Biopsy results, tissue analysis
   - Actions: Oncology referral, surgery, monitoring, benign/no action

7. **ECG/EKG Results**
   - Electrocardiogram findings
   - Actions: Cardiology urgent, medication, follow-up ECG, normal

8. **Consultation Notes**
   - Specialist visit summaries
   - Actions: Implement recommendations, schedule follow-up, order tests

9. **Discharge Summaries**
   - Hospital discharge instructions
   - Actions: Schedule follow-up, adjust medications, order home health

10. **Vaccine Records**
    - Immunization documentation
    - Actions: Update records, schedule boosters, no action needed

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
