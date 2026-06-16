# P001 — Pedreschi2008

Acceptance criteria stated: Yes
Citation: Pedreschi2008
DES content: Yes
DES snippet: In this paper, the notion of discriminatory classification rules is introduced and studied ... (strong) α-protection as a measure of the discriminatory power of a rule ...
Data Type: Tabular
Decision rule tied to metric: Yes
Deployment Status: Conceptual
Domain: Lending
ENV content: Yes
ENV snippet: In the context of civil rights law, discrimination refers to unfair or unequal treatment of people based on membership to a category or a minority ...
Elicitation present: No
End-to-end coverage: Partial
Failure modes: Drift not addressed, No revision process/ownership, Other
Fairness notions: Contextual/legal compliance, Other, Procedural fairness
Gap summary (1 sentence): Provides a formal, testable operationalization of discrimination in rule-based data mining (α/strong α-protection) including proxy-based redlining via background knowledge, but does not cover deployment-time monitoring or revision of fairness requirements over time.
Governance maturity: Absent
Measurement procedure: Define PD itemsets (downward closed set) and classify rules as PD/PND; compute confidence/support of rules; compute elift/glift to flag α-discriminatory rules; for indirect discrimination, use background association rules and Theorem 6.2 to infer lower bounds on discrimination of PD rules from PND rules + background knowledge; evaluate empirically on German Credit dataset.
Metrics used: α-protection via extended lift elift = conf(A,B→C)/conf(B→C); strong α-protection via glift; detection of direct/indirect discrimination (redlining) in classification rules using PD/PND itemsets and background knowledge.
Monitoring present: No
Operationalization present: Yes
Protected attrs / groups: Examples of potentially discriminatory itemsets include gender (female and not single), age (senior), job type (unskilled/unemployed), foreign worker; also discusses race/ethnicity in law examples and redlining via neighborhood/ZIP as proxy for race.
QA notes: Introduces formal definitions for discriminatory classification rules (direct/indirect), PD/PND itemsets, and α-protection/strong α-protection using extended lift; shows naive removal of discriminatory attributes is insufficient when background knowledge enables proxy/redlining; provides inference theorem for indirect discrimination and empirical assessment on German Credit. No monitoring/revision lifecycle aspects beyond offline mining/auditing.
QA pass: Pass
QA score: 7
QA1 Defined objectives/requirements: Y
QA10 Future directions/implications: N
QA2 Approach described in detail: Y
QA3 Representation/operationalization specified: Y
QA4 Cross-domain vs domain-scoped: Y
QA5 Practical/research value: Y
QA6 Trade-offs discussed: p
QA7 Stakeholders/elicitation addressed: N
QA8 Validation/evaluation discussed: Y
QA9 Limitations/threats/ethics: p
Revision present: No
SOC content: Yes
SOC snippet: Rules extracted from databases ... when used for decision tasks such as benefit or credit approval, can be discriminatory ...
Spec explicitness/testability: Explicit + testable
Spec snippet: For a given threshold α ≥ 0, we say that c is α-protective if elift(γ, δ) < α ... c is called α-discriminatory if elift(γ, δ) ≥ α.
Specification format: Constraint (formal/informal)
Specification present: Yes
Study ID: P001
System Type: Decision support
Threshold value: α threshold (tunable; examples use α=3); also minsup/minconf thresholds for rule mining in experiments/plots.
Thresholds stated: Yes
Trade-offs managed: Unclear
Validation method: Offline evaluation
Validation snippet: An empirical assessment of the results on the German credit dataset is also provided.
Validation/testing present: Yes
Venue Type: Conference
Year: 2008