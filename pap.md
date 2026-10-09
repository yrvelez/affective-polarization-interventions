# Analysis plan (pre-registered: OSF k2nwj)

Transcribed from the OSF Preregistration "Affective Polarization and Support for Undemocratic Practices: An
Adaptive Experiment" (https://osf.io/k2nwj, DOI 10.17605/OSF.IO/K2NWJ), registered 2022-11-15. The registration
states it was made before analysis of the data; a pilot of N = 350 had been collected for an in-class exercise.

## Design

Online survey experiment on Lucid (Columbia IRB AAAU3946), fielded November 2022, testing interventions designed
by students in an experimental design course. Respondents are assigned to one arm (`arm`): T0 is a pure control
("Please continue."), T1-T32 are the registered interventions. T33, a GPT-3 chatbot added later, failed
technically and is not among the registered interventions. The design is adaptive with a control arm
(Offer-Westort, Coppock & Green 2021): equal assignment probabilities for a burn-in of N = 1,350, then batches of
about 500 with more probability on promising arms while reserving sample for the control group. Stopping rule:
4,000 responses or a best-performing arm with probability > .9.

The registration states no directional hypotheses: the aim is to select the best-performing intervention.

## Outcomes

- Primary: `post_ap`, affective polarization = in-party minus out-party feeling thermometer (0-100), the in-party
  being the party the survey assigned each respondent (`group1`; leaners are assigned to the party they lean to).
- Secondary: `post_udp`, support for undemocratic practices, mean of the answered items of the 4-item scale (1-7).

## Sample and exclusions (registered)

- Pure independents are excluded: keep `partisan` in `Democrat`, `Republican`.
- Inattentive respondents are screened out with the one-item screener at the start of the survey (it asks for
  both "extremely interested" and "very interested"): keep `screener_pass == 1`.
- Finished responses only; `arm != 'T33'` (not a registered intervention).
- Missing data: listwise deletion on the outcome and the covariates.

## Hypotheses

- H1: the effect of each intervention (T1-T32) on `post_ap` relative to control (T0), two-sided.
- H2: the effect of each intervention (T1-T32) on `post_udp` relative to control (T0), two-sided.

## Estimation (registered)

Regression of the outcome on arm indicators (T0 = reference), weighted to account for differential probabilities
of treatment assignment, adjusting for the pre-treatment measures of affective polarization (`pre_ap`) and support
for undemocratic practices (`pre_udp`). HC2 robust standard errors (as in `estimatr`), two-sided tests at alpha =
0.05. The registration specifies no multiple-testing correction.

Weights: the registration does not give them. The authors' analysis weights each respondent by `ipw_weight` =
1 / the arm's share among all finished respondents; the per-batch assignment probabilities were not stored with the
data (batch is missing for about a third of finished respondents), so those weights are used.

## Registered but conditional or not run here

- Batch fixed effects are registered "in the event of significant trends in the control group". Run as a
  robustness check on H1 (add `batch` fixed effects).
- The posterior probability of the best-performing arm (simulation approach of osf.io/vdr4g) is registered but
  not computed by this pipeline.

## Exploratory (not registered)

- The authors' later analysis script (`original/replication_script.R`) adjusts each outcome only for its own
  pre-treatment measure; compare its estimates with the registered specification.
- A pooled summary across arms (random-effects across the 32 arm estimates) is not registered.
