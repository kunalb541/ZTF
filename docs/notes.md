# Project notes (2020)

These are the original working notes for the project, transcribed from
`DIARY.docx` (kept alongside this file for the record).

- Sample size is **not complete**. The bulk JSON API couldn't be used, so the
  alerts were paged one request at a time — a full download run took about
  **27 minutes**.
- The full-resolution FITS images were downloaded for inspection, but disk
  space ran out before the image set could be completed.
- **Total number of alerts collected: ~35,000.**

## What the saved dataset actually contains

Recomputed from the committed arrays in `data/arrays/`:

| Property            | Value                                   |
| ------------------- | --------------------------------------- |
| Alerts collected    | 35,077                                  |
| Observation span    | 2018-07-13 → 2020-02-26 (JD 2458312.97–2458905.64) |
| Magnitude (magpsf)  | 13.35 – 21.09                           |
| RealBogus (rb)      | 0.05 – 1.00                             |
| FWHM (median)       | 1.69 px                                 |
| Sky region          | RA 8.69°–12.67°, Dec 39.77°–42.77° (around M31) |
| Filters             | ZTF-*g* (14,902 alerts), ZTF-*r* (20,175 alerts) |
