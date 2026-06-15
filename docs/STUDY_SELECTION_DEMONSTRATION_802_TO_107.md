# Study Selection Demonstration (802 -> 107)

This document explains the relationship between the **full study-selection flow** reported in the manuscript and the **metadata-backed demonstration flow** provided in this replication package.

## Important clarification

For the sake of replication, this package demonstrates the screening process most concretely with **802 studies** because this is the stage for which the narrowed metadata and record-level screening decisions are easiest to inspect from the attached source exports.

- **Demonstration subset in this package:** 802 records
- **Actual initial retrieval in the study:** 4,010 records
- **Actual final included corpus:** 107 primary studies

So, **802 is only a demonstration subset for replication and readability**. It is **not** the actual initial retrieval size of the study.

## Actual study flow

The full SLR search and screening process reported in the manuscript was:

1. **4,010 initial records** retrieved from IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar.
2. **2,406 records** remained after deduplication and short-paper filtering.
3. **802 records** entered title/abstract screening.
4. **267 records** remained after introduction/conclusion screening.
5. **107 records** remained as the database-screened set after full-text screening.
6. **30 additional studies** were added through snowballing, yielding **137 studies** for the final QA/integration stage.
7. **107 primary studies** were retained in the final analytical corpus.

## Why this package focuses on 802 -> 107

The full 4,010-record process is documented in the package through counts, search logs, and source-level metadata. However, for a compact and inspectable record-level demonstration, the package focuses on the **802 -> 107** segment because it is the clearest metadata-backed subset for showing:

- how title/abstract screening was narrowed;
- how introduction/conclusion screening further reduced the pool;
- how full-text decisions produced the database-screened set;
- how snowballing was integrated; and
- how final QA/integration yielded the 107 included studies.

## Files to inspect

- `data/search_screening/Fairness_RE_SLR_802_to_107_Screening_Flow.csv`
- `data/search_screening/Fairness_RE_SLR_802_Record_Level_Screening_Decisions.csv`
- `data/search_screening/Fairness_RE_SLR_Search_Demonstration_Steps.csv`
- `data/search_screening/Fairness_RE_SLR_Source_Metadata_Examples.csv`
- `docs/STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf`

## Figure note

The figure included in `STUDY_SELECTION_DEMONSTRATION_802_TO_107.pdf` mirrors the organization of the manuscript study-selection figure while adding a replication note: the package demonstrates the **802 -> 107** portion for inspectability, but the **actual study ran from 4,010 to 107**.
