# P003 — Torralba2011

> **GitHub-readable study coding note.** This file reformats the original extraction fields into a structured property-table style for easier reviewer inspection.

## At a glance

| Field | Value |
|---|---|
| **Study ID** | P003 |
| **Citation** | Torralba2011 |
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
| **Protected attributes / groups** | Not demographic; fairness is defined among multiple customers (stakeholders) with competing priorities. |

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
| **Threshold value** | Not specified in provided excerpt (no fixed acceptance threshold; trade-offs explored via Pareto sets). |

## 4. Operationalization and measurement

| Property | Coding / Evidence |
|---|---|
| **Operationalization present** | ✅ **Yes** |
| **Decision rule tied to metric** | ⚪ **Unclear** |
| **Fairness notions** | - Other<br>- Procedural fairness |
| **Metrics used** | Multi-objective optimisation objectives encoding different notions of fairness across customers in requirements assignment / next-release planning; solution quality explored via Pareto trade-offs and visualization. |
| **Measurement procedure** | Formulate requirements assignment/next release planning with multiple customers and implementation costs; apply search-based multi-objective optimisation to explore solution space and fairness trade-offs among customers; visualize the space; validate on real-world datasets (e.g., Motorola requirements) and stress-test datasets. |
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

... many customers, each with their own view on the sets of requirements to be prioritized ...

### Specification snippet

The search explores the space of possible allocations of requirements for the next release of the system ... explore trade offs and tensions between the customers ...

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

Provided excerpt describes multi-customer requirements fairness analysis using multi-objective optimisation (search-based) to explore trade-offs among customers (NRP/release planning); validated on real-world datasets (Motorola handset requirements with 4 service-provider customers) and stress-test datasets. No monitoring/revision lifecycle aspects described. Note: the pasted excerpt appears to match Finkelstein et al. RE’08 (DOI 10.1109/RE.2008.61) even though this row's Citation key is Torralba2011.

---

*This Markdown version was reformatted for GitHub readability. The content preserves the original study-level coding fields while grouping them into reviewer-friendly sections.*
