# P007 — Sweeney2013

Acceptance criteria stated: Yes
Citation: Sweeney2013
DES content: Yes
DES explicit requirement: Partial
DES snippet: It operationalizes discrimination in ad delivery by defining protected/comparison groups (black- vs white-identifying names), classifying ad sentiment (negative if “arrest/criminal”, neutral otherwise), and testing disparate impact and statistical significance on ad impressions.
Data Type: Text
Decision rule tied to metric: Yes
Deployment Status: Deployed
Domain: Hiring
ENV content: Yes
ENV explicit requirement: Yes
ENV snippet: The paper grounds discrimination in U.S. civil rights law (Title VII) and uses the EEOC adverse impact test (80% rule) as a normative/legal criterion for disproportionate effect across protected groups.
Elicitation present: No
End-to-end coverage: Partial
Failure modes: Drift not addressed, No revision process/ownership, Other
Fairness notions: Contextual/legal compliance, Other, Outcome parity, Procedural fairness
Gap summary (1 sentence): Provides a concrete, legally grounded, testable operationalization of disparate impact in ad delivery (80% rule + statistical tests) and proposes embedding it into ad exchange scoring, but does not specify ongoing monitoring/revision processes to maintain fairness as ads, user behavior, and platforms evolve.
Governance maturity: Absent
Measurement procedure: Construct racially associated first-name lists from prior studies; harvest 2,184 full names; collect ads shown on http://Google.com and http://Reuters.com (cache/cookies cleared, varying time/IP/browser); classify ads as negative if containing “arrest” or “criminal” else neutral; compare group rates via chi-square and compute adverse impact ratio on neutral (or negative) rates; interpret <80 as disproportionate effect; report examples and aggregate counts.
Metrics used: Adverse impact ratio (EEOC 80% rule) computed from group rates; chi-square tests for statistical significance; group-conditional rates of negative vs neutral ad sentiment; ad delivery discrimination assessed on ad impressions for racially associated names (black- vs white-identifying).
Monitoring present: No
Operationalization present: Yes
Protected attrs / groups: Race (proxy via black-identifying vs white-identifying names); also references other protected characteristics in Title VII (race, color, religion, sex, national origin) and mentions gender examples, but main analysis is black vs white name association.
QA notes: Empirical audit of discrimination in online ad delivery using racially associated names as a proxy for protected groups; operationalizes disparate impact with EEOC’s 80% rule and statistical tests; provides measurable decision rule (suppress/discount ads with adverse impact <80) that could be embedded into ad exchange scoring. Focuses on detection/assessment and a high-level mitigation concept, but does not define an implementation-ready monitoring/revision governance process for sustained compliance in dynamic ad systems.
QA pass: Pass
QA score: 9
QA1 Defined objectives/requirements: Y
QA10 Future directions/implications: Y
QA2 Approach described in detail: Y
QA3 Representation/operationalization specified: Y
QA4 Cross-domain vs domain-scoped: Y
QA5 Practical/research value: Y
QA6 Trade-offs discussed: p
QA7 Stakeholders/elicitation addressed: Y
QA8 Validation/evaluation discussed: Y
QA9 Limitations/threats/ethics: p
Revision ownership defined: No
Revision present: No
Revision trigger defined: No
SOC content: Yes
SOC explicit requirement: Partial
SOC snippet: It frames harms as reputational and opportunity impacts (employment and trust contexts) and discusses responsibility across advertiser, platform, and societal click behavior; proposes integrating bias tests into ad exchange quality scoring to align delivery with societal norms.
Spec explicitness/testability: Explicit + testable
Spec snippet: Use the EEOC adverse impact test: compute ratio of (smaller affected%)/(larger affected%) and compare to 80; e.g., for neutral ads 40/52 = 77% (<80) indicating disproportionate effect. Also proposes suppressing ads with adverse impact score < 80.
Specification format: Constraint (formal/informal), Policy/rule
Specification present: Yes
Stakeholders Mentioned: Affected groups, Auditors/Compliance, Developers, Other, Regulators
Study ID: P007
System Type: Decision support
Threshold value: Adverse impact threshold = 80% (EEOC 80% rule); examples compute 77% (Reuters) and 40% (Google).
Thresholds stated: Yes
Trade-offs managed: Unclear
Validation method: Audit, Offline evaluation
Validation snippet: Empirical audit/measurement study of ad delivery: 2,184 names, 5,337 ads captured; reports statistically significant disparities and adverse impact ratios, with archived datasets for replication.
Validation/testing present: Yes
Venue Type: Conference
Year: 2013