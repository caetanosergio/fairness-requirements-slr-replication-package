# Data dictionary

This dictionary summarizes the main fields appearing in the CSV exports. The exact set of fields may differ across RQ-specific files because each export is tailored to a different analysis view.

| Field | Description |
|---|---|
| `Study` | Internal study identifier used in the SLR corpus, usually P### plus citation short name. |
| `Acceptance criteria stated` | Whether pass/fail or acceptability criteria are stated. |
| `Citation` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `DES content` | Whether or how the study discusses system-design-level fairness. |
| `DES explicit requirement` | Explicitness of design-level fairness requirements. |
| `DES snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Data Type` | Data modality or type used in the study. |
| `Decision rule tied to metric` | Whether the study links metric results to an engineering decision rule. |
| `Deployment Status` | Whether the study is conceptual, prototype, deployed, or otherwise characterized. |
| `Domain` | Application domain coded for the study. |
| `ENV content` | Whether or how the study discusses environment-level fairness context. |
| `ENV explicit requirement` | Explicitness of environment-level fairness requirements. |
| `ENV snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Elicitation artifact` | Artifact produced or used for elicitation when reported. |
| `Elicitation method` | Method used for elicitation when reported. |
| `Elicitation present` | Whether elicitation of fairness concerns or requirements is present. |
| `Elicitation snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `End-to-end coverage` | Extent to which the study covers the end-to-end fairness requirements lifecycle. |
| `Failure modes` | Coded failure modes such as missing thresholds, drift not addressed, or no ownership. |
| `Fairness notions` | Fairness notions discussed or operationalized. |
| `Gap summary (1 sentence)` | One-sentence analytical summary of the gap represented by the study. |
| `Governance maturity` | Coded maturity of governance support. |
| `Measurement procedure` | Procedure used to compute or evaluate fairness. |
| `Metrics used` | Fairness metrics, criteria, or operational measures used. |
| `Monitoring present` | Whether post-deployment or ongoing monitoring is present. |
| `Monitoring signals` | Signals, metrics, or conditions monitored over time. |
| `Monitoring snippet` | Supporting excerpt/summary for monitoring coding. |
| `Notes` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Operationalization present` | Whether fairness is operationalized into measurable or actionable artifacts. |
| `Protected attrs / groups` | Protected or sensitive attributes/groups considered. |
| `QA notes` | Reviewer notes supporting the QA score. |
| `QA pass` | Whether the study passed the QA threshold. |
| `QA score` | Quality-assessment score. |
| `QA1 Defined objectives/requirements` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA10 Future directions/implications` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA2 Approach described in detail` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA3 Representation/operationalization specified` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA4 Cross-domain vs domain-scoped` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA5 Practical/research value` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA6 Trade-offs discussed` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA7 Stakeholders/elicitation addressed` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA8 Validation/evaluation discussed` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `QA9 Limitations/threats/ethics` | Quality-assessment criterion coding, using the rubric reported in the manuscript/appendix. |
| `Revision ownership defined` | Whether owners/responsible roles for revision are defined. |
| `Revision present` | Whether revision/adaptation/change management is present. |
| `Revision snippet` | Supporting excerpt/summary for revision coding. |
| `Revision trigger defined` | Whether explicit triggers for revision are defined. |
| `SOC content` | Whether or how the study discusses sociotechnical fairness concerns. |
| `SOC explicit requirement` | Explicitness of sociotechnical-level fairness requirements. |
| `SOC snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Spec explicitness/testability` | Whether the fairness specification is explicit and testable. |
| `Spec snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Specification format` | Type of specification artifact or representation. |
| `Specification present` | Whether fairness specification is present. |
| `Stakeholders Mentioned` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Study ID` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `System Type` | Type of AI/ML system or task when coded. |
| `Threshold value` | Specific threshold/tolerance values when reported. |
| `Thresholds stated` | Whether thresholds or tolerances are stated. |
| `Trade-offs managed` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Validation method` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Validation snippet` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Validation/testing present` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Venue Type` | Coded field used in the SLR extraction database; see the codebook and manuscript for interpretation. |
| `Year` | Publication year. |


## Search and screening files

### `data/search_screening/Fairness_RE_SLR__Screening_Search_Log.csv`
Combined audit log. Use `log_type` to filter rows:
- `SearchRun`: source-level search records and retrieved counts.
- `ScreeningStage`: stage-level screening flow from 4,010 records to 107 final primary studies.
- `IncludedPrimaryStudy`: final 107 included studies.

### `data/search_screening/Fairness_RE_SLR_Search_Runs.csv`
Source-level table with database/source name, URL, query-set pointer, run date, date range, retrieved count, evidence file, and notes.

### `data/search_screening/Fairness_RE_SLR_Search_Query_Set.csv`
Query-set table listing the search phrases and verbatim query templates adapted across databases.

### `data/search_screening/Fairness_RE_SLR_Screening_Flow.csv`
Stage-level screening counts used to explain the movement from initial retrievals to the final primary corpus.

### `data/search_screening/Fairness_RE_SLR_Primary_Studies_107.csv`
Final analytical corpus of 107 studies with key coding fields.

### `data/search_screening/Fairness_RE_SLR_Coding_Pass_to_Final_Corpus_Audit.csv`
Audit view linking broader coding-pass exports to the final 107-study corpus.


## Search and screening trace fields

### `Fairness_RE_SLR_Record_Level_Screening_Decisions.csv`

- `record_id`: unique record identifier generated from source and row number.
- `source_database`: retrieval source.
- `title`, `authors`, `year`, `venue`, `doi_or_url`: bibliographic metadata when available; for excluded records these may be unavailable because the uploaded source evidence consisted of screenshots rather than full bibliographic exports.
- `search_query`: query set used to retrieve the record.
- `retrieved_date`: search date.
- `duplicate_status`: deduplication and short-paper filtering status.
- `page_count_status`: short-paper/page-count eligibility note.
- `title_abstract_decision`: title/abstract screening outcome.
- `intro_conclusion_decision`: introduction/conclusion screening outcome.
- `full_text_decision`: full-text assessment outcome.
- `qa_score`: quality-assessment score for final included studies when available.
- `final_inclusion_status`: final status in the 107-study analytical corpus or exclusion stage.
- `exclusion_reason`: reason/basis for exclusion stage.
- `notes`: notes on metadata availability and trace construction.
- `final_study_id`: P-code for final primary studies where applicable.
- `final_citation_key`: citation key for final primary studies where applicable.
- `evidence_file`: screenshot archive supporting the source-level search run.
