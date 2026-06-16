# P007 — Sweeney2013

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P007 |
| **Citation** | Sweeney2013 |
| **Year** | 2013 |
| **Domain** | Hiring |
| **Deployment status** | `Deployed` |
| **QA pass** | ✅ **Pass** |
| **QA score** | 9 |

## 1. Study identity

| Property | Coding / Evidence |
|---|---|
| **Venue type** | `Conference` |
| **System type** | Decision support |
| **Data type** | `Text` |
| **Protected attributes / groups** | Race (proxy via black-identifying vs white-identifying names); also references other protected characteristics in Title VII (race, color, religion, sex, national origin) and mentions gender examples, but main analysis is black vs white name association. |

## 2. Requirements-engineering coverage

| Property | Coding / Evidence |
|---|---|
| **ENV content** | ✅ **Yes** |
| **ENV explicit requirement** | ✅ **Yes** |
| **DES content** | ✅ **Yes** |
| **DES explicit requirement** | 🟨 **Partial** |
| **SOC content** | ✅ **Yes** |
| **SOC explicit requirement** | 🟨 **Partial** |
| **End-to-end coverage** | 🟨 **Partial** |

## 3. Elicitation and specification

| Property | Coding / Evidence |
|---|---|
| **Elicitation present** | ⬜ **No** |
| **Specification present** | ✅ **Yes** |
| **Specification format** | Constraint (formal/informal), Policy/rule |
| **Specification explicitness / testability** | Explicit + testable |
| **Acceptance criteria stated** | ✅ **Yes** |
| **Thresholds stated** | ✅ **Yes** |
| **Threshold value** | Adverse impact threshold = 80% (EEOC 80% rule); examples compute 77% (Reuters) and 40% (Google). |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ✅ **Yes** |
| **Fairness notions** | - Contextual/legal compliance<br>- Other<br>- Outcome parity<br>- Procedural fairness |
| **Metrics used** | Adverse impact ratio (EEOC 80% rule) computed from group rates; chi-square tests for statistical significance; group-conditional rates of negative vs neutral ad sentiment; ad delivery discrimination assessed on ad impressions for racially associated names (black- vs white-identifying). |
| **Measurement procedure** | Construct racially associated first-name lists from prior studies; harvest 2,184 full names; collect ads shown on http://Google.com and http://Reuters.com (cache/cookies cleared, varying time/IP/browser); classify ads as negative if containing “arrest” or “criminal” else neutral; compare group rates via chi-square and compute adverse impact ratio on neutral (or negative) rates; interpret <80 as disproportionate effect; report examples and aggregate counts. |
| **Trade-offs managed** | ⚪ **Unclear** |

## 5. Validation, monitoring, revision, and governance

| Property | Coding / Evidence |
|---|---|
| **Validation / testing present** | ✅ **Yes** |
| **Validation method** | Audit, Offline evaluation |
| **Monitoring present** | ⬜ **No** |
| **Revision present** | ⬜ **No** |
| **Revision trigger defined** | ⬜ **No** |
| **Revision ownership defined** | ⬜ **No** |
| **Governance maturity** | ⬜ **Absent** |
| **Failure modes** | - Drift not addressed<br>- No revision process/ownership<br>- Other |

## 6. Evidence snippets

### ENV snippet

The paper grounds discrimination in U.S. civil rights law (Title VII) and uses the EEOC adverse impact test (80% rule) as a normative/legal criterion for disproportionate effect across protected groups.

### DES snippet

It operationalizes discrimination in ad delivery by defining protected/comparison groups (black- vs white-identifying names), classifying ad sentiment (negative if “arrest/criminal”, neutral otherwise), and testing disparate impact and statistical significance on ad impressions.

### SOC snippet

It frames harms as reputational and opportunity impacts (employment and trust contexts) and discusses responsibility across advertiser, platform, and societal click behavior; proposes integrating bias tests into ad exchange quality scoring to align delivery with societal norms.

### Specification snippet

Use the EEOC adverse impact test: compute ratio of (smaller affected%)/(larger affected%) and compare to 80; e.g., for neutral ads 40/52 = 77% (<80) indicating disproportionate effect. Also proposes suppressing ads with adverse impact score < 80.

### Validation snippet

Empirical audit/measurement study of ad delivery: 2,184 names, 5,337 ads captured; reports statistically significant disparities and adverse impact ratios, with archived datasets for replication.

## 7. Gap summary

### One-sentence gap summary

Provides a concrete, legally grounded, testable operationalization of disparate impact in ad delivery (80% rule + statistical tests) and proposes embedding it into ad exchange scoring, but does not specify ongoing monitoring/revision processes to maintain fairness as ads, user behavior, and platforms evolve.

## 8. Quality assessment

| Property | Coding / Evidence |
|---|---|
| **QA pass** | ✅ **Pass** |
| **QA score** | 9 |
| **QA1 Defined objectives / requirements** | ✅ `Y` |
| **QA2 Approach described in detail** | ✅ `Y` |
| **QA3 Representation / operationalization specified** | ✅ `Y` |
| **QA4 Cross-domain vs domain-scoped** | ✅ `Y` |
| **QA5 Practical / research value** | ✅ `Y` |
| **QA6 Trade-offs discussed** | 🟨 `P` |
| **QA7 Stakeholders / elicitation addressed** | ✅ `Y` |
| **QA8 Validation / evaluation discussed** | ✅ `Y` |
| **QA9 Limitations / threats / ethics** | 🟨 `P` |
| **QA10 Future directions / implications** | ✅ `Y` |

## 9. QA notes

### Reviewer coding note

Empirical audit of discrimination in online ad delivery using racially associated names as a proxy for protected groups; operationalizes disparate impact with EEOC’s 80% rule and statistical tests; provides measurable decision rule (suppress/discount ads with adverse impact <80) that could be embedded into ad exchange scoring. Focuses on detection/assessment and a high-level mitigation concept, but does not define an implementation-ready monitoring/revision governance process for sustained compliance in dynamic ad systems.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
