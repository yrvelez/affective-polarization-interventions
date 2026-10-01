# Analysis plan (reconstructed post hoc — NOT pre-registered)

No pre-registration for this study was found. This plan was written on 2026-10-01, after data collection,
from the original analysis behind the published results, so the pipeline can run. Every analysis below is post
hoc; "registered" tags in the report only mean "matches this reconstructed plan".

## Design

Online survey experiment (Columbia IRB AAAU3946) fielded on Lucid Theorem, November 9–25, 2022, testing
33 interventions designed by students in a Fall 2022 Experimental Design course. Respondents were assigned
to one arm (`arm`, T0–T33); T0 is a pure control ("Please continue."). The design was adaptive
(Offer-Westort, Coppock & Green 2021): assignment shares changed across fielding batches (`batch`).
Interventions span four modalities: video (e.g. a perception-gap video, a Brené Brown empathy video,
Jubilee panels), text/articles (e.g. meta-dehumanization correction, bipartisan legislation examples,
scandals from both parties), images (e.g. a cooperation infographic, a media-profits-from-division image)
and interactive tasks (e.g. a perception-gap quiz, the iSideWith quiz). T33, a GPT-3 chatbot, failed
technically.

## Sample and exclusions

- Finished responses only (`Finished == 1`).
- Partisans only: keep `partisan` in `Democrat`, `Republican`, where party is the in-party the survey
  assigned each respondent (`group1`), as in the original analysis.
- Exclude `arm == 'T33'` (broken intervention).
- Complete cases on the outcome and its pre-treatment measure.

## Outcomes

- Primary: `post_ap`, affective polarization after treatment = in-party minus out-party feeling
  thermometer (0–100 scales). Lower = less polarized. Pre-treatment covariate: `pre_ap`.
- Secondary: `post_udp`, mean of the answered items among four on support for undemocratic practices (1–7). Pre-treatment
  covariate: `pre_udp`.

## Hypotheses

- H1: Each intervention (T1–T32) changes `post_ap` relative to control (T0); the expected direction is a reduction, tested two-sided.
- H2: Each intervention (T1–T32) changes `post_udp` relative to control (T0); the expected direction is a reduction, tested two-sided.

## Estimation

WLS of the outcome on arm indicators (T0 = reference) plus the pre-treatment measure, weighted by
`ipw_weight` (1 / the arm's share among all finished respondents, as in the published analysis), HC2 robust
standard errors, normal-based two-sided tests at α = 0.05, no multiple-testing correction.

## Robustness

Because assignment shares varied by batch, re-estimate H1 adding batch fixed effects (`batch`).
