# P001 — Pedreschi2008

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P001 |
| **Citation** | Pedreschi2008 |
| **Year** | 2008 |
| **Domain** | Lending |
| **Deployment status** | `Conceptual` |
| **QA pass** | ✅ **Pass** |
| **QA score** | 7 |

## 1. Study identity

| Property | Coding / Evidence |
|---|---|
| **Venue type** | `Conference` |
| **System type** | Decision support |
| **Data type** | `Tabular` |
| **Protected attributes / groups** | Examples of potentially discriminatory itemsets include gender (female and not single), age (senior), job type (unskilled/unemployed), foreign worker; also discusses race/ethnicity in law examples and redlining via neighborhood/ZIP as proxy for race. |

## 2. Requirements-engineering coverage

| Property | Coding / Evidence |
|---|---|
| **ENV content** | ✅ **Yes** |
| **DES content** | ✅ **Yes** |
| **SOC content** | ✅ **Yes** |
| **End-to-end coverage** | 🟨 **Partial** |

## 3. Elicitation and specification

| Property | Coding / Evidence |
|---|---|
| **Elicitation present** | ⬜ **No** |
| **Specification present** | ✅ **Yes** |
| **Specification format** | Constraint (formal/informal) |
| **Specification explicitness / testability** | Explicit + testable |
| **Acceptance criteria stated** | ✅ **Yes** |
| **Thresholds stated** | ✅ **Yes** |
| **Threshold value** | α threshold (tunable; examples use α=3); also minsup/minconf thresholds for rule mining in experiments/plots. |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ✅ **Yes** |
| **Fairness notions** | - Contextual/legal compliance<br>- Other<br>- Procedural fairness |
| **Metrics used** | α-protection via extended lift elift = conf(A,B→C)/conf(B→C); strong α-protection via glift; detection of direct/indirect discrimination (redlining) in classification rules using PD/PND itemsets and background knowledge. |
| **Measurement procedure** | Define PD itemsets (downward closed set) and classify rules as PD/PND; compute confidence/support of rules; compute elift/glift to flag α-discriminatory rules; for indirect discrimination, use background association rules and Theorem 6.2 to infer lower bounds on discrimination of PD rules from PND rules + background knowledge; evaluate empirically on German Credit dataset. |
| **Trade-offs managed** | ⚪ **Unclear** |

## 5. Validation, monitoring, revision, and governance

| Property | Coding / Evidence |
|---|---|
| **Validation / testing present** | ✅ **Yes** |
| **Validation method** | Offline evaluation |
| **Monitoring present** | ⬜ **No** |
| **Revision present** | ⬜ **No** |
| **Governance maturity** | ⬜ **Absent** |
| **Failure modes** | - Drift not addressed<br>- No revision process/ownership<br>- Other |

## 6. Evidence snippets

### ENV snippet

In the context of civil rights law, discrimination refers to unfair or unequal treatment of people based on membership to a category or a minority ...

### DES snippet

In this paper, the notion of discriminatory classification rules is introduced and studied ... (strong) α-protection as a measure of the discriminatory power of a rule ...

### SOC snippet

Rules extracted from databases ... when used for decision tasks such as benefit or credit approval, can be discriminatory ...

### Specification snippet

For a given threshold α ≥ 0, we say that c is α-protective if elift(γ, δ) < α ... c is called α-discriminatory if elift(γ, δ) ≥ α.

### Validation snippet

An empirical assessment of the results on the German credit dataset is also provided.

## 7. Gap summary

### One-sentence gap summary

Provides a formal, testable operationalization of discrimination in rule-based data mining (α/strong α-protection) including proxy-based redlining via background knowledge, but does not cover deployment-time monitoring or revision of fairness requirements over time.

## 8. Quality assessment

| Property | Coding / Evidence |
|---|---|
| **QA pass** | ✅ **Pass** |
| **QA score** | 7 |
| **QA1 Defined objectives / requirements** | ✅ `Y` |
| **QA2 Approach described in detail** | ✅ `Y` |
| **QA3 Representation / operationalization specified** | ✅ `Y` |
| **QA4 Cross-domain vs domain-scoped** | ✅ `Y` |
| **QA5 Practical / research value** | ✅ `Y` |
| **QA6 Trade-offs discussed** | 🟨 `P` |
| **QA7 Stakeholders / elicitation addressed** | ⬜ `N` |
| **QA8 Validation / evaluation discussed** | ✅ `Y` |
| **QA9 Limitations / threats / ethics** | 🟨 `P` |
| **QA10 Future directions / implications** | ⬜ `N` |

## 9. QA notes

### Reviewer coding note

Introduces formal definitions for discriminatory classification rules (direct/indirect), PD/PND itemsets, and α-protection/strong α-protection using extended lift; shows naive removal of discriminatory attributes is insufficient when background knowledge enables proxy/redlining; provides inference theorem for indirect discrimination and empirical assessment on German Credit. No monitoring/revision lifecycle aspects beyond offline mining/auditing.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
