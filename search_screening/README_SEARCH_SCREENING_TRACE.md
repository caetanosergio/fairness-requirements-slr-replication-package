# Search screening trace

This folder documents how the SLR screening process moved from the initial search retrieval to the final analytical corpus.

## Actual study flow

The full review began with **4,010 initial records** retrieved from IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar. After staged filtering and screening, the study concluded with **107 final primary studies**.

Full count flow:

**4,010 -> 2,406 -> 802 -> 267 -> 107 (database-screened set) + 30 snowballing additions -> 137 QA-assessed studies -> 107 final primary studies**

## Replication-package demonstration flow

For the sake of replication, this package demonstrates the search and screening trace most concretely with the **802-study title/abstract pool**, because this stage is directly inspectable from the available attached metadata files and record-level screening decisions. This means:

- **802 is a replication-oriented demonstration subset**, not the initial retrieval size.
- **4,010 is the actual initial retrieval count used in the study**.
- **107 is the actual final included corpus used in the synthesis**.

## Source metadata

Metadata was extracted from attached source database exports:

- IEEE Xplore: BibTeX files
- ACM Digital Library: BibTeX files
- SpringerLink: CSV files
- ScienceDirect: BibTeX files
- Google Scholar: supporting evidence files preserved as search evidence

## Key files

- `Fairness_RE_SLR_Source_Database_Metadata_Extracted.csv`
- `Fairness_RE_SLR_Source_Database_Metadata_Deduplicated.csv`
- `Fairness_RE_SLR_Title_Abstract_Screening_Metadata_802.csv`
- `Fairness_RE_SLR_802_Record_Level_Screening_Decisions.csv`
- `Fairness_RE_SLR_Record_Level_Screening_Decisions.csv`
- `Fairness_RE_SLR_802_to_107_Screening_Flow.csv`
- `Fairness_RE_SLR_Primary_Studies_107.csv`
- `Fairness_RE_SLR_Final_107_Record_Map.csv`
- `Fairness_RE_SLR_Search_Demonstration_Steps.csv`

## Visual demonstration

See `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf` for a PRISMA-style diagram that mirrors the manuscript figure while clearly indicating that the package demonstrates the 802 -> 107 portion for inspectability and replication.
