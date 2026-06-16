# P006 — Kamishima2012

Acceptance criteria stated: No
Citation: Kamishima2012
DES content: Yes
DES explicit requirement: Yes
DES snippet: They formalize unfairness as statistical dependence between predictions and sensitive features, define PI/NPI (mutual information) and propose the Prejudice Remover regularizer added to logistic regression to enforce independence Y ⟂⟂ S, controlled by η.
Data Type: Tabular
Decision rule tied to metric: Unclear
Deployment Status: Prototype
Domain: General
ENV content: Yes
ENV explicit requirement: Partial
ENV snippet: They motivate fairness as a social and legal requirement in high-stakes determinations (credit, insurance, employment) and discuss indirect discrimination / red-lining as a real-world risk even when sensitive features are removed.
Elicitation present: No
End-to-end coverage: Partial
Failure modes: Drift not addressed, No revision process/ownership, No thresholds / acceptance criteria, Other
Fairness notions: Contextual/legal compliance, Other, Outcome parity, Procedural fairness
Gap summary (1 sentence): Provides a precise, testable operationalization of unfairness as statistical dependence (PI/NPI) and an efficient regularization mechanism to reduce indirect discrimination with evaluated accuracy–fairness trade-offs, but does not address deployment-time monitoring or revision to maintain fairness under drift or changing contexts.
Governance maturity: Absent
Measurement procedure: Train probabilistic discriminative model (logistic regression) and add prejudice remover regularizer R_PR that approximates PI using sample estimates of P̂(y|s) and P̂(y); tune η to trade off accuracy vs fairness; evaluate via 5-fold cross-validation on Adult/Census Income (sensitive=gender) and compute Acc, NPI, UEI, CVS, and efficiency PI/MI; compare to baselines LR/LRns/NB/NBns and CV2NB.
Metrics used: Prejudice Index (PI) as mutual information between predicted outcome Y and sensitive feature S using induced distribution P̂; Normalized PI (NPI); also reports Calders–Verwer score (CVS) = Pr[Y=High|S=Male] − Pr[Y=High|S=Female]; Underestimation index (UEI) via Hellinger distance between sample P̃ and induced P̂; regularized learning objective: −log-likelihood + η·R_PR(D,Θ) + (λ/2)||Θ||^2 where R_PR approximates PI using sample means.
Monitoring present: No
Operationalization present: Yes
Protected attrs / groups: Sensitive feature S such as gender, race, religion, ethnicity, handicaps, political convictions; experiments use gender (Male/Female) on Adult/Census Income.
QA notes: Proposes a fairness-aware regularization approach (prejudice remover) for probabilistic discriminative models, operationalizing unfairness as mutual information between predicted outcome and sensitive feature (PI/NPI) and defining additional diagnostics (UEI, latent prejudice). Provides explicit objective function with tunable η for accuracy–fairness trade-off and evaluates on Adult/Census Income (gender) against CV2NB and baselines. No deployment monitoring or revision/change control is described; fairness is treated as an offline training objective without acceptance thresholds beyond selecting η.
QA pass: Pass
QA score: 9.5
QA1 Defined objectives/requirements: Y
QA10 Future directions/implications: Y
QA2 Approach described in detail: Y
QA3 Representation/operationalization specified: Y
QA4 Cross-domain vs domain-scoped: Y
QA5 Practical/research value: Y
QA6 Trade-offs discussed: Y
QA7 Stakeholders/elicitation addressed: Y
QA8 Validation/evaluation discussed: Y
QA9 Limitations/threats/ethics: p
Revision ownership defined: No
Revision present: No
Revision trigger defined: No
SOC content: Yes
SOC explicit requirement: Partial
SOC snippet: They connect unfairness to societal harm, privacy-like leakage of sensitive information, and discuss socially responsible mining; however, governance processes (monitoring/revision ownership) are not specified.
Spec explicitness/testability: Explicit + testable
Spec snippet: Indirect prejudice removal target is independence between outcome and sensitive feature: require Y ⟂⟂ S (enforced by minimizing prejudice index PI = Σ_{y,s} P̂(y,s) ln(P̂(y,s)/(P̂(y)P̂(s))).
Specification format: Constraint (formal/informal)
Specification present: Yes
Stakeholders Mentioned: Affected groups, Developers, Other, Regulators
Study ID: P006
System Type: Classification
Threshold value: No fixed acceptance threshold; fairness controlled by regularization strength η (examples η=5,15,30) and reported resulting NPI/CVS values.
Thresholds stated: Partial
Trade-offs managed: Yes
Validation method: Offline evaluation
Validation snippet: They empirically evaluate PR regularizer within logistic regression on Adult/Census Income using 5-fold cross-validation and report accuracy vs fairness (NPI/CVS) trade-offs, comparing with CV2NB and other baselines.
Validation/testing present: Yes
Venue Type: Conference
Year: 2012