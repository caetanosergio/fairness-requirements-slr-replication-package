# P002 — Finkelstein2008

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P002 |
| **Citation** | Finkelstein2008 |
| **Year** | 2008 |
| **Domain** | `General` |
| **Deployment status** | `Prototype` |
| **QA pass** | ✅ **Pass** |
| **QA score** | 7.5 |

## 1. Study identity

| Property | Coding / Evidence |
|---|---|
| **Venue type** | `Conference` |
| **System type** | Decision support |
| **Data type** | `Tabular` |
| **Protected attributes / groups** | Not demographic; stakeholders are multiple customers (e.g., four mobile telephony service providers) with competing priorities. |

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
| **Acceptance criteria stated** | ⬜ **No** |
| **Thresholds stated** | ⚪ **Unclear** |
| **Threshold value** | Not specified in excerpt (fairness captured via Pareto trade-offs rather than fixed thresholds). |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ⚪ **Unclear** |
| **Fairness notions** | - Other<br>- Procedural fairness |
| **Metrics used** | Fairness notions among multiple customers operationalized as multi-objective optimisation objectives over requirement selections (NRP/release planning) balancing customer priorities and implementation cost; solution space explored via search-based optimisation and visualized graphically. |
| **Measurement procedure** | Model requirements selection as Next Release Problem with multiple customers and costs; apply meta-heuristic/multi-objective optimisation to explore Pareto-optimal allocations reflecting different fairness notions/trade-offs; visualize solution space; validate on Motorola dataset (35 requirements; 4 service providers; cost estimates) and additional stress-test datasets. |
| **Trade-offs managed** | ✅ **Yes** |

## 5. Validation, monitoring, revision, and governance

| Property | Coding / Evidence |
|---|---|
| **Validation / testing present** | ✅ **Yes** |
| **Validation method** | Offline evaluation |
| **Monitoring present** | ⬜ **No** |
| **Revision present** | ⬜ **No** |
| **Governance maturity** | ⬜ **Absent** |
| **Failure modes** | - Drift not addressed<br>- No revision process/ownership<br>- No thresholds / acceptance criteria<br>- Other |

## 6. Evidence snippets

### ENV snippet

Requirements engineering for multiple customers, each of whom have competing and often conflicting priorities, raises issues of negotiation, mediation and conflict resolution.

### DES snippet

This paper uses a multi-objective optimisation approach to support investigation of the trade-offs in various notions of fairness between multiple customers.

### SOC snippet

... many customers, each with their own view on the sets of requirements to be prioritized ... attempt to please all of the people all of the time.

### Specification snippet

The search explores the space of possible allocations of requirements for the next release of the system ... to explore trade offs and tensions between the customers in an attempt to satisfy multi definitions of fairness.

### Validation snippet

Results are presented to validate the approach using two real-world data sets and also using data sets created specifically to stress test the approach.

## 7. Gap summary

### One-sentence gap summary

Analyzes fairness as multi-stakeholder trade-offs in requirements assignment using multi-objective optimisation and empirical validation, but does not define monitoring or revision mechanisms to keep fairness criteria valid over time.

## 8. Quality assessment

| Property | Coding / Evidence |
|---|---|
| **QA pass** | ✅ **Pass** |
| **QA score** | 7.5 |
| **QA1 Defined objectives / requirements** | ✅ `Y` |
| **QA2 Approach described in detail** | 🟨 `P` |
| **QA3 Representation / operationalization specified** | ✅ `Y` |
| **QA4 Cross-domain vs domain-scoped** | ✅ `Y` |
| **QA5 Practical / research value** | ✅ `Y` |
| **QA6 Trade-offs discussed** | ✅ `Y` |
| **QA7 Stakeholders / elicitation addressed** | ✅ `Y` |
| **QA8 Validation / evaluation discussed** | ✅ `Y` |
| **QA9 Limitations / threats / ethics** | ⬜ `N` |
| **QA10 Future directions / implications** | ⬜ `N` |

## 9. QA notes

### Reviewer coding note

Focuses on fairness in allocating/prioritizing requirements across multiple customers with conflicting priorities; uses multi-objective (search-based) optimisation to explore trade-offs among fairness notions; validates on Motorola multi-customer dataset and synthetic stress tests. Not about protected groups; no monitoring/revision process described.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
