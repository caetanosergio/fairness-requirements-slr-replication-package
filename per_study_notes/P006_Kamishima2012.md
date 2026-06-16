# P006 — Kamishima2012

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P006 |
| **Citation** | Kamishima2012 |
| **Year** | 2012 |
| **Domain** | `General` |
| **Deployment status** | `Prototype` |
| **QA pass** | ✅ **Pass** |
| **QA score** | 9.5 |

## 1. Study identity

| Property | Coding / Evidence |
|---|---|
| **Venue type** | `Conference` |
| **System type** | Classification |
| **Data type** | `Tabular` |
| **Protected attributes / groups** | Sensitive feature S such as gender, race, religion, ethnicity, handicaps, political convictions; experiments use gender (Male/Female) on Adult/Census Income. |

## 2. Requirements-engineering coverage

| Property | Coding / Evidence |
|---|---|
| **ENV content** | ✅ **Yes** |
| **ENV explicit requirement** | 🟨 **Partial** |
| **DES content** | ✅ **Yes** |
| **DES explicit requirement** | ✅ **Yes** |
| **SOC content** | ✅ **Yes** |
| **SOC explicit requirement** | 🟨 **Partial** |
| **End-to-end coverage** | 🟨 **Partial** |

## 3. Elicitation and specification

| Property | Coding / Evidence |
|---|---|
| **Elicitation present** | ⬜ **No** |
| **Specification present** | ✅ **Yes** |
| **Specification format** | Constraint (formal/informal) |
| **Specification explicitness / testability** | Explicit + testable |
| **Acceptance criteria stated** | ⬜ **No** |
| **Thresholds stated** | 🟨 **Partial** |
| **Threshold value** | No fixed acceptance threshold; fairness controlled by regularization strength η (examples η=5,15,30) and reported resulting NPI/CVS values. |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ⚪ **Unclear** |
| **Fairness notions** | - Contextual/legal compliance<br>- Other<br>- Outcome parity<br>- Procedural fairness |
| **Metrics used** | Prejudice Index (PI) as mutual information between predicted outcome Y and sensitive feature S using induced distribution P̂; Normalized PI (NPI); also reports Calders–Verwer score (CVS) = Pr[Y=High\|S=Male] − Pr[Y=High\|S=Female]; Underestimation index (UEI) via Hellinger distance between sample P̃ and induced P̂; regularized learning objective: −log-likelihood + η·R_PR(D,Θ) + (λ/2)\|\|Θ\|\|^2 where R_PR approximates PI using sample means. |
| **Measurement procedure** | Train probabilistic discriminative model (logistic regression) and add prejudice remover regularizer R_PR that approximates PI using sample estimates of P̂(y\|s) and P̂(y); tune η to trade off accuracy vs fairness; evaluate via 5-fold cross-validation on Adult/Census Income (sensitive=gender) and compute Acc, NPI, UEI, CVS, and efficiency PI/MI; compare to baselines LR/LRns/NB/NBns and CV2NB. |
| **Trade-offs managed** | ✅ **Yes** |

## 5. Validation, monitoring, revision, and governance

| Property | Coding / Evidence |
|---|---|
| **Validation / testing present** | ✅ **Yes** |
| **Validation method** | Offline evaluation |
| **Monitoring present** | ⬜ **No** |
| **Revision present** | ⬜ **No** |
| **Revision trigger defined** | ⬜ **No** |
| **Revision ownership defined** | ⬜ **No** |
| **Governance maturity** | ⬜ **Absent** |
| **Failure modes** | - Drift not addressed<br>- No revision process/ownership<br>- No thresholds / acceptance criteria<br>- Other |

## 6. Evidence snippets

### ENV snippet

They motivate fairness as a social and legal requirement in high-stakes determinations (credit, insurance, employment) and discuss indirect discrimination / red-lining as a real-world risk even when sensitive features are removed.

### DES snippet

They formalize unfairness as statistical dependence between predictions and sensitive features, define PI/NPI (mutual information) and propose the Prejudice Remover regularizer added to logistic regression to enforce independence Y ⟂⟂ S, controlled by η.

### SOC snippet

They connect unfairness to societal harm, privacy-like leakage of sensitive information, and discuss socially responsible mining; however, governance processes (monitoring/revision ownership) are not specified.

### Specification snippet

Indirect prejudice removal target is independence between outcome and sensitive feature: require Y ⟂⟂ S (enforced by minimizing prejudice index PI = Σ_{y,s} P̂(y,s) ln(P̂(y,s)/(P̂(y)P̂(s))).

### Validation snippet

They empirically evaluate PR regularizer within logistic regression on Adult/Census Income using 5-fold cross-validation and report accuracy vs fairness (NPI/CVS) trade-offs, comparing with CV2NB and other baselines.

## 7. Gap summary

### One-sentence gap summary

Provides a precise, testable operationalization of unfairness as statistical dependence (PI/NPI) and an efficient regularization mechanism to reduce indirect discrimination with evaluated accuracy–fairness trade-offs, but does not address deployment-time monitoring or revision to maintain fairness under drift or changing contexts.

## 8. Quality assessment

| Property | Coding / Evidence |
|---|---|
| **QA pass** | ✅ **Pass** |
| **QA score** | 9.5 |
| **QA1 Defined objectives / requirements** | ✅ `Y` |
| **QA2 Approach described in detail** | ✅ `Y` |
| **QA3 Representation / operationalization specified** | ✅ `Y` |
| **QA4 Cross-domain vs domain-scoped** | ✅ `Y` |
| **QA5 Practical / research value** | ✅ `Y` |
| **QA6 Trade-offs discussed** | ✅ `Y` |
| **QA7 Stakeholders / elicitation addressed** | ✅ `Y` |
| **QA8 Validation / evaluation discussed** | ✅ `Y` |
| **QA9 Limitations / threats / ethics** | 🟨 `P` |
| **QA10 Future directions / implications** | ✅ `Y` |

## 9. QA notes

### Reviewer coding note

Proposes a fairness-aware regularization approach (prejudice remover) for probabilistic discriminative models, operationalizing unfairness as mutual information between predicted outcome and sensitive feature (PI/NPI) and defining additional diagnostics (UEI, latent prejudice). Provides explicit objective function with tunable η for accuracy–fairness trade-off and evaluates on Adult/Census Income (gender) against CV2NB and baselines. No deployment monitoring or revision/change control is described; fairness is treated as an offline training objective without acceptance thresholds beyond selecting η.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
