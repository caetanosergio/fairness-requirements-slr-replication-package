# Screening and Search Log README

This folder documents how the SLR search was reduced from **4,010 initial records** to **107 final primary studies**.

## Core files

- `Fairness_RE_SLR_Search_Runs.csv`: source-level retrieval counts and evidence files.
- `Fairness_RE_SLR_Screening_Flow.csv`: stage-level counts.
- `Fairness_RE_SLR_Screening_Reduction_Steps.csv`: transition-by-transition reduction counts.
- `Fairness_RE_SLR_Record_Level_Screening_Decisions.csv`: 4,010-row record-level screening trace.
- `Fairness_RE_SLR_Primary_Studies_107.csv`: final analytical corpus.
- `Fairness_RE_SLR_Final_107_Record_Map.csv`: mapping between final included studies and screening-trace rows.
- `raw_search_exports/*.csv`: source-specific 4,010-record skeleton exports for GitHub inspection.
- `raw/search_screenshots/*.zip`: screenshot evidence supplied for each database/source.

## Reduction flow

| Stage | Records remaining | Records removed | Basis |
|---|---:|---:|---|
| Initial retrieval | 4,010 | 0 | Records retrieved from IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar. |
| After deduplication and short-paper filtering | 2,406 | 1,604 | Duplicates and records below the page-length criterion removed. |
| Title/abstract screening | 802 | 1,604 | Clearly irrelevant records removed. |
| Introduction/conclusion screening | 267 | 535 | Records not sufficiently related to fairness requirements / AI systems removed. |
| Full-text assessment | 137 | 130 | Full papers assessed against inclusion/exclusion and QA criteria. |
| Final primary studies | 107 | 30 | Final peer-reviewed studies included in synthesis. |

## Important note about excluded-record metadata

## Metadata basis

This package now uses **source-database metadata extracted from the attached BibTeX and CSV exports** supplied for IEEE Xplore, ACM Digital Library, SpringerLink, and ScienceDirect, together with supporting Google Scholar evidence. The central metadata files are:

- `Fairness_RE_SLR_Source_Database_Metadata_Extracted.csv`
- `Fairness_RE_SLR_Source_Database_Metadata_Deduplicated.csv`
- `Fairness_RE_SLR_Title_Abstract_Screening_Metadata_802.csv`
- `Fairness_RE_SLR_802_Record_Level_Screening_Decisions.csv`

These files are intended to demonstrate, in a reproducible way, how the inspectable screening trace moves from **802 records to 107 final primary studies**, while still documenting the **full study-level counts from 4,010 initial records to 107 included studies**.

## Why the package demonstrates 802 -> 107

For the sake of replication, the package includes a **worked 802-record demonstration** because this stage is directly backed by the narrowed metadata and record-level screening decisions derived from the attached source files. The **actual study** began with **4,010 initial records** and ended with **107 final primary studies**. The 802-record trace is therefore a **demonstration subset for transparency and inspectability**, not the full initial retrieval.

The actual flow remains:

- Initial retrieval: 4,010 records
- After deduplication and short-paper filtering: 2,406 records
- Title/abstract screening pool: 802 records
- After introduction/conclusion screening: 267 records
- Database-screened set after full-text decisions: 107 records
- Snowballing additions merged for downstream assessment: 30 records
- QA/integration pool: 137 records
- Final primary studies: 107 records

See also:

- `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.md`
- `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf`
- `data/search_screening/Fairness_RE_SLR_Search_Demonstration_Steps.csv`
- `data/search_screening/Fairness_RE_SLR_802_to_107_Screening_Flow.csv`
