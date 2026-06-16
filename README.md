# Fairness Requirements SLR Replication Package

This repository contains the replication materials for the manuscript:

**A Systematic Exploration of Fairness Requirements, Modeling, and Operationalization in Engineering AI-Based Software Systems**

The review analyzes fairness as an explicit, testable, traceable, monitorable, and revisable requirements engineering concern for AI-based sociotechnical systems. The final manuscript reports a final corpus of **107 peer-reviewed primary studies** published between **1996 and 2025**. This package is intended to support reviewer inspection and post-publication reproducibility.

## What is included

Some file-dense materials are provided either as folders or ZIP archives to support reviewer inspection while avoiding GitHub browser upload limits. The source-database evidence is organized by database folder, including ACM Digital Library, IEEE Xplore, SpringerLink, ScienceDirect, and Google Scholar. Search screenshot evidence is provided in `search_screenshots/`. The formatted study-level notes are provided in `per_study_notes/`, while the full coding-pass notes are archived in `per_study_notes_all_coding_pass.zip`.

```text
fairness-requirements-slr-replication-package/
├── README.md
├── LICENSE.md
├── CITATION.cff
├── Fairness_RE_SLR_Extraction_Database.pdf
├── coded_csv/
├── final_dataset/
├── search_screening/
├── docs/
├── metadata/
├── ocr_text_by_screenshot/
├── per_study_notes/
├── scripts/
├── search_screenshots/
├── ACM Digital Library/
├── Google Scholar/
├── IEEE Xplore/
├── ScienceDirect/
├── SpringerLink/
└── per_study_notes_all_coding_pass.zip
```

## Data files

| File                                   | Data rows | Columns |
| -------------------------------------- | --------: | ------: |
| `coded_csv/Papers_coded.csv`           |       110 |      65 |
| `coded_csv/RQ1_levels.csv`             |       107 |      65 |
| `coded_csv/RQ2_operationalization.csv` |       110 |      65 |
| `coded_csv/RQ3_overtime.csv`           |        10 |      65 |
| `coded_csv/Data_Extraction.csv`        |       110 |      65 |
| `coded_csv/Domain.csv`                 |       110 |      65 |

Notes:

* `final_dataset/fairness_slr_results.xlsx` is the workbook-style extraction database supplied with the package.
* `coded_csv/RQ1_levels.csv`, `coded_csv/RQ2_operationalization.csv`, and `coded_csv/RQ3_overtime.csv` provide RQ-specific analysis views.
* Some raw CSV exports preserve earlier coding-pass records; the manuscript's final analytical corpus is **107 studies**. The package keeps the raw exports transparent rather than silently deleting records.

## PDF and exported views

PDF/exported views are provided directly in the repository and in the `docs/` folder for convenient inspection of the study-selection process, extraction database, and coding evidence.

Key PDF/exported views include:

* `Fairness_RE_SLR_Extraction_Database.pdf`
* `docs/Figure4_Study_Selection_Replication_Demo_802.pdf`
* `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf`

These files support visual inspection of the extraction database, study-selection flow, and replication-oriented 802-record screening demonstration.

## Per-study notes

The `per_study_notes/` folder includes formatted Markdown notes for study-level inspection. These notes provide example study-level coding, gap summaries, QA notes, evidence snippets, and structured tables for readability on GitHub.

The full coding-pass note archive is also preserved as:

* `per_study_notes_all_coding_pass.zip`

## Reproducing basic checks

Run the validation script from the repository root:

```bash
python scripts/validate_replication_package.py
```

Run the CSV summary script:

```bash
python scripts/summarize_csv_counts.py
```

These scripts do not require external dependencies beyond Python 3.

## Main analysis axes

The review organizes the coding around two complementary axes:

1. **Level axis: ENV / DES / SOC**
   This axis captures where fairness is grounded: deployment environment, system design, and sociotechnical deployment.

2. **Lifecycle axis: ELICIT / SPEC / OPER / VALID / MON / REVISE**
   This axis captures how fairness is engineered over time as a requirements lifecycle.

## Transparency materials

The package includes:

* coded CSV exports;
* final workbook export;
* RQ-specific analysis views;
* source-database metadata;
* search and screening logs;
* study-selection demonstration files;
* per-study notes;
* source-database export evidence;
* search screenshot evidence;
* file manifest;
* SHA-256 checksums;
* data dictionary;
* validation scripts;
* reproduction and GitHub upload instructions.

## How to cite

Please cite the manuscript and this repository if reusing the data after publication. A draft `CITATION.cff` file is included and should be updated with the final DOI/repository URL after publication.

## Search screening trace and source metadata

This package includes source-database metadata extracted from the uploaded database exports for **IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect**, and **Google Scholar evidence files**. The bibliographic metadata were extracted from the available BibTeX and CSV files in the attached source-database ZIPs.

### Actual study flow

The manuscript-level screening flow is:

1. **4,010** initial records retrieved from IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar.
2. **2,406** records after deduplication and short-paper filtering.
3. **802** records retained after title/abstract screening.
4. **267** records retained after introduction/conclusion screening.
5. **107** records retained from the main database-search route before snowballing merge.
6. **30** additional records retained from snowballing after snowballing-specific screening.
7. **137** studies in the consolidated full-text assessment set.
8. **107** final peer-reviewed primary studies retained for coding and synthesis.

### Replication-package demonstration note

For the sake of replication, inspectability, and package size, the **record-level demonstration** in this package is centered on the **802-study stage**. In other words, the package provides an inspectable record-level trace showing how the **802 title/abstract candidates** were reduced step by step to the final **107 primary studies**.

This means:

* **802 is a demonstration subset for traceability**, not the initial corpus size.
* The **actual study** began with **4,010 initial records** and ended with **107 final primary studies**.
* The package preserves **both** the full summary flow and the 802-record demonstration trace.

### Key files

* `search_screening/Fairness_RE_SLR_Screening_Flow.csv` — full summary flow for the study.
* `search_screening/Fairness_RE_SLR_Screening_Reduction_Steps.csv` — reduction-step summary with counts and reasons.
* `search_screening/Fairness_RE_SLR_Search_Runs.csv` — source-by-source search-run summary.
* `search_screening/Fairness_RE_SLR_Source_Database_Metadata_Extracted.csv` — all extracted records from available BibTeX/CSV source exports.
* `search_screening/Fairness_RE_SLR_Source_Database_Metadata_Deduplicated.csv` — deduplicated source-export metadata.
* `search_screening/Fairness_RE_SLR_Title_Abstract_Screening_Metadata_802.csv` — metadata-backed 802-record title/abstract screening pool.
* `search_screening/Fairness_RE_SLR_802_Record_Level_Screening_Decisions.csv` — record-level trace for the 802-screened candidates through the later reduction stages.
* `search_screening/Fairness_RE_SLR_802_to_107_Screening_Flow.csv` — compact 802-to-107 screening flow.
* `search_screening/Fairness_RE_SLR_Source_Metadata_Examples.csv` — examples extracted directly from the source database metadata files.
* `search_screening/Fairness_RE_SLR_Search_Demonstration_Steps.csv` — step-by-step search demonstration.
* `docs/Figure4_Study_Selection_Replication_Demo_802.tex` and `docs/Figure4_Study_Selection_Replication_Demo_802.pdf` — replication-oriented diagram matching the study-selection flow while clarifying that the package demonstrates the **802-record** trace.
* `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.tex` and `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf` — study-selection demonstration document.
* `ACM Digital Library/`, `IEEE Xplore/`, `SpringerLink/`, `ScienceDirect/`, and `Google Scholar/` — extracted BibTeX/CSV export files and source-database evidence.
* `search_screenshots/` — screenshot evidence supporting the search-screening trace.

The package does **not** include copyrighted full-text PDFs of the 4,010 retrieved records. It provides metadata, screening decisions, study-selection traceability, and final coded extraction data instead.
