# P005 — Kamiran2012

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P005 |
| **Citation** | Kamiran2012 |
| **Year** | 2012 |
| **Domain** | `General` |
| **Deployment status** | `Prototype` |
| **QA pass** | ✅ **Pass** |
| **QA score** | 9.5 |

## 1. Study identity

| Property | Coding / Evidence |
|---|---|
| **Venue type** | `Journal` |
| **System type** | Classification |
| **Data type** | `Tabular` |
| **Protected attributes / groups** | One binary sensitive attribute S with deprived value b and favored value w (examples: gender/sex, ethnicity/race; also mentions age, religion, etc. in motivation). |

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
| **Acceptance criteria stated** | 🟨 **Partial** |
| **Thresholds stated** | ⬜ **No** |
| **Threshold value** | No normative acceptance threshold for disc is specified in excerpt (goal is typically disc = 0; experiments report resulting discrimination percentages). |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ⚪ **Unclear** |
| **Fairness notions** | - Contextual/legal compliance<br>- Other<br>- Outcome parity |
| **Metrics used** | Discrimination measure disc as difference in positive outcome rates between favored group (S=w) and deprived group (S=b); trade-off analysis between accuracy and discrimination; preprocessing interventions: suppression (remove S + correlated attrs), massaging (relabel M instances using ranker), reweighing (instance weights W(s,c)=Pexp/Pobs), sampling (uniform and preferential) to match expected unbiased group sizes. |
| **Measurement procedure** | Compute disc on labeled datasets and on classifier predictions using group-conditional positive rates; estimate on independent test sets / via 10-fold cross-validation; for massaging compute M = disc(D)\|Db\|\|Dw\|/\|D\| and relabel top-ranked promotion (b,−) and demotion (w,+) candidates; for reweighing compute weights by expected vs observed joint frequencies of (S,Class); for sampling resample DP/DN/FP/FN groups to expected sizes, optionally preferentially near decision boundary using a ranker. |
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

They ground the problem in unlawful discrimination and explicitly reference anti-discrimination legislation, motivating the need for non-discriminatory classifiers learned from biased historical data.

### DES snippet

They define discrimination as a measurable constraint (difference in positive outcome rates across sensitive groups) and propose data preprocessing methods (suppression, massaging, reweighing, sampling) to reduce discrimination while maintaining accuracy.

### SOC snippet

They discuss legal accountability concerns (avoid using sensitive attribute at prediction time) and practical deployment scenarios (employment, healthcare surveys, credit) where discriminatory impacts matter.

### Specification snippet

disc_{S=b}(C,D) := P(C(X)=+ \| X(S)=w) − P(C(X)=+ \| X(S)=b) (difference in positive prediction rates between favored and deprived groups).

### Validation snippet

They implement techniques in a modified Weka and report experiments on real-life datasets (Census Income, Communities & Crimes, Dutch census), using 10-fold cross-validation and measuring accuracy and discrimination on unmodified test folds.

## 7. Gap summary

### One-sentence gap summary

Provides a rigorous, testable operationalization of non-discrimination for binary sensitive attributes and effective preprocessing techniques with empirical evaluation, but does not define deployment-time monitoring or revision mechanisms to maintain non-discrimination under drift or changing contexts.

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

Defines a concrete, testable discrimination metric (difference in positive outcome rates between favored vs deprived groups) and frames the task as accuracy + non-discrimination optimization; surveys and extends preprocessing techniques (suppression, massaging, reweighing, sampling) and provides theoretical accuracy–discrimination trade-off analysis plus empirical evaluation in Weka on multiple real datasets. Does not address post-deployment monitoring or revision/change management; acceptance is treated as reducing disc toward 0 rather than specifying a governance threshold.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
