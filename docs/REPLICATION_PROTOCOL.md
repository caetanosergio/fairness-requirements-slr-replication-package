# Replication protocol

This replication package is organized to allow reviewers and readers to inspect the evidence base behind the systematic literature review.

## Review objective

The review examines how fairness is treated as an explicit, testable, traceable, monitorable, and revisable requirement in AI-based sociotechnical systems.

## Search and selection overview

The manuscript reports a search over IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar. Google Scholar was used as a supplementary recall-oriented source. The final manuscript reports 107 peer-reviewed primary studies between 1996 and 2025.

## Coding dimensions

The main coding dimensions are:

- ENV / DES / SOC content and explicitness;
- elicitation, specification, operationalization, validation/testing, monitoring, and revision;
- thresholds, acceptance criteria, metric-linked decision rules;
- governance, ownership, revision triggers, and failure modes;
- QA scores and QA pass/fail status.

## Reviewer-use workflow

1. Open `data/final_dataset/fairness_slr_results.xlsx` for the full workbook-style dataset.
2. Inspect RQ-specific CSV files in `data/coded_csv/`.
3. Inspect PDF snapshots in `exports/pdf_views/` for visual views of the database.
4. Check example per-study notes in `data/per_study_notes/`.
5. Run `python scripts/validate_replication_package.py` to verify required files and checksums.

## Important note on raw exports

Some CSV exports may contain records from earlier coding passes or broader extraction views. The final manuscript analysis uses the final corpus of 107 peer-reviewed studies. Raw exports are kept to preserve transparency and auditability.


## Source-database metadata extraction

The replication package now includes metadata extracted from the uploaded source-database screenshots for ACM Digital Library, IEEE Xplore, SpringerLink, ScienceDirect, and Google Scholar. The file `data/search_screening/Fairness_RE_SLR_Source_Database_Metadata_Extracted.csv` records visible bibliographic information shown by the source databases, including title, authors, year, venue, DOI/URL when displayed, source, screenshot evidence, query text, and retrieval count.

The package also preserves the complete 4,010-to-107 screening trace in `Fairness_RE_SLR_Record_Level_Screening_Decisions.csv`, the search-run summaries, the screening reduction steps, and the final 107-study map. Full paper PDFs are not redistributed.
