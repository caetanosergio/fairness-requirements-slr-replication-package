# P002 — Finkelstein2008

Acceptance criteria stated: No
Citation: Finkelstein2008
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
Measurement procedure: Model requirements selection as Next Release Problem with multiple customers and costs; apply meta-heuristic/multi-objective optimisation to explore Pareto-optimal allocations reflecting different fairness notions/trade-offs; visualize solution space; validate on Motorola dataset (35 requirements; 4 service providers; cost estimates) and additional stress-test datasets.
Metrics used: Fairness notions among multiple customers operationalized as multi-objective optimisation objectives over requirement selections (NRP/release planning) balancing customer priorities and implementation cost; solution space explored via search-based optimisation and visualized graphically.
Monitoring present: No
Operationalization present: Yes
Protected attrs / groups: Not demographic; stakeholders are multiple customers (e.g., four mobile telephony service providers) with competing priorities.
QA notes: Focuses on fairness in allocating/prioritizing requirements across multiple customers with conflicting priorities; uses multi-objective (search-based) optimisation to explore trade-offs among fairness notions; validates on Motorola multi-customer dataset and synthetic stress tests. Not about protected groups; no monitoring/revision process described.
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
SOC snippet: ... many customers, each with their own view on the sets of requirements to be prioritized ... attempt to please all of the people all of the time.
Spec explicitness/testability: Explicit + testable
Spec snippet: The search explores the space of possible allocations of requirements for the next release of the system ... to explore trade offs and tensions between the customers in an attempt to satisfy multi definitions of fairness.
Specification format: Constraint (formal/informal)
Specification present: Yes
Study ID: P002
System Type: Decision support
Threshold value: Not specified in excerpt (fairness captured via Pareto trade-offs rather than fixed thresholds).
Thresholds stated: Unclear
Trade-offs managed: Yes
Validation method: Offline evaluation
Validation snippet: Results are presented to validate the approach using two real-world data sets and also using data sets created specifically to stress test the approach.
Validation/testing present: Yes
Venue Type: Conference
Year: 2008