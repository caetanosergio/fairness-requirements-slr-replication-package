# P003 — Torralba2011

Acceptance criteria stated: No
Citation: Torralba2011
DES content: Yes
DES snippet: This paper uses a multi-objective optimisation approach to support investigation of the trade-offs in various notions of fairness between multiple customers.
Data Type: Tabular
Decision rule tied to metric: Unclear
Deployment Status: Prototype
Domain: General
ENV content: Yes
ENV snippet: Requirements engineering for multiple customers, each of whom have competing and often conflicting priorities, raises issues of negotiation, mediation and conflict resolution.
Elicitation present: No
End-to-end coverage: Partial
Failure modes: Drift not addressed, No revision process/ownership, No thresholds / acceptance criteria, Other
Fairness notions: Other, Procedural fairness
Gap summary (1 sentence): Analyzes fairness as multi-stakeholder trade-offs in requirements assignment using multi-objective optimisation and empirical validation, but does not define monitoring or revision mechanisms to keep fairness criteria valid over time.
Governance maturity: Absent
Measurement procedure: Formulate requirements assignment/next release planning with multiple customers and implementation costs; apply search-based multi-objective optimisation to explore solution space and fairness trade-offs among customers; visualize the space; validate on real-world datasets (e.g., Motorola requirements) and stress-test datasets.
Metrics used: Multi-objective optimisation objectives encoding different notions of fairness across customers in requirements assignment / next-release planning; solution quality explored via Pareto trade-offs and visualization.
Monitoring present: No
Notes: Check bibliographic metadata: Citation key for this row is Torralba2011, but excerpt references RE’08 paper (DOI 10.1109/RE.2008.61).
Operationalization present: Yes
Protected attrs / groups: Not demographic; fairness is defined among multiple customers (stakeholders) with competing priorities.
QA notes: Provided excerpt describes multi-customer requirements fairness analysis using multi-objective optimisation (search-based) to explore trade-offs among customers (NRP/release planning); validated on real-world datasets (Motorola handset requirements with 4 service-provider customers) and stress-test datasets. No monitoring/revision lifecycle aspects described. Note: the pasted excerpt appears to match Finkelstein et al. RE’08 (DOI 10.1109/RE.2008.61) even though this row's Citation key is Torralba2011.
QA pass: Pass
QA score: 7.5
QA1 Defined objectives/requirements: Y
QA10 Future directions/implications: N
QA2 Approach described in detail: p
QA3 Representation/operationalization specified: Y
QA4 Cross-domain vs domain-scoped: Y
QA5 Practical/research value: Y
QA6 Trade-offs discussed: Y
QA7 Stakeholders/elicitation addressed: Y
QA8 Validation/evaluation discussed: Y
QA9 Limitations/threats/ethics: N
Revision present: No
SOC content: Yes
SOC snippet: ... many customers, each with their own view on the sets of requirements to be prioritized ...
Spec explicitness/testability: Explicit + testable
Spec snippet: The search explores the space of possible allocations of requirements for the next release of the system ... explore trade offs and tensions between the customers ...
Specification format: Constraint (formal/informal)
Specification present: Yes
Study ID: P003
System Type: Decision support
Threshold value: Not specified in provided excerpt (no fixed acceptance threshold; trade-offs explored via Pareto sets).
Thresholds stated: Unclear
Trade-offs managed: Yes
Validation method: Offline evaluation
Validation snippet: Results are presented to validate the approach using two real-world data sets and also using data sets created specifically to stress test the approach.
Validation/testing present: Yes
Venue Type: Conference
Year: 2008