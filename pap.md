# Analysis plan (reconstructed post hoc — NOT pre-registered)

No pre-registration for this study was found. This plan was written on 2026-10-01, after data collection,
from the existing analysis (`replication_script.R`), so the pipeline can run. Every analysis below is post
hoc; "registered" tags in the report only mean "matches this reconstructed plan".

## Design

Online survey experiment (Columbia IRB AAAU3946) testing 33 interventions designed by students in an
Experimental Design course. Respondents were assigned to one arm (`arm`, T0–T33). T0 is the control.
Assignment shares changed across fielding batches (`batch`).

## Sample and exclusions

- Partisans only, including leaners: keep `partisan` in `Democrat`, `Republican`.
- Exclude `arm == 'T33'` (broken intervention).
- Complete cases on the outcome and its pre-treatment measure.

## Outcomes

- Primary: `post_ap`, affective polarization after treatment = in-party minus out-party feeling
  thermometer (0–100 scales). Lower = less polarized. Pre-treatment covariate: `pre_ap`.
- Secondary: `post_udp`, mean of four items on support for undemocratic practices (1–7). Pre-treatment
  covariate: `pre_udp`.

## Hypotheses

- H1: Each intervention (T1–T32) reduces `post_ap` relative to control (T0).
- H2: Each intervention (T1–T32) reduces `post_udp` relative to control (T0).

## Estimation

WLS of the outcome on arm indicators (T0 = reference) plus the pre-treatment measure, weighted by
`ipw_weight` (1 / the arm's share of the analysis sample), HC2 robust standard errors, two-sided tests at
α = 0.05, no multiple-testing correction.

## Robustness

Because assignment shares varied by batch, re-estimate H1 adding batch fixed effects (`batch`).
