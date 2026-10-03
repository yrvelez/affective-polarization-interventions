# Testing 33 Student-Designed Interventions to Reduce Affective Polarization

*Yamil Velez · 2026-10-03 · N = 4,547 analysed of 6,086 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: 12/12 claims supported](figures/badges/review.svg) ![plan: reconstructed](figures/badges/registration.svg) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.82](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-03; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.82, 418k tokens in and 58k out. Cite as: Velez, Y. (2026). Testing 33 Student-Designed Interventions to Reduce Affective Polarization [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/affective-polarization-interventions
>
> **No pre-registration. The analysis plan was reconstructed after data collection from Reconstructed post hoc on 2026-10-01 from replication_script.R; not pre-registered.** Every test below is post hoc or exploratory.

<!-- fd:section id=abstract -->
## Abstract

This study asks whether short, student-designed interventions can reduce affective polarization or support for undemocratic practices among US adults. In an online survey experiment, 32 interventions (videos, articles, images, quizzes) were each compared with a pure control; a 33rd arm, a GPT-3 chatbot, was excluded after technical failures. Of 6,086 raw respondents, 4,547 passed the sample filters, and the models use fewer because of missing data. One intervention was nominally significant for affective polarization: the Perception gap video lowered the post-treatment thermometer-based measure by 2.3 points (95% CI [−4.3, −0.4], p = 0.019, two-sided), in an uncorrected, post hoc analysis, so the estimate is likely inflated. An approximate pooled estimate across arms was 0.8 points lower than control (95% CI [−1.4, −0.2]). Support for undemocratic practices showed no distinguishable pooled difference (−0.015, 95% CI [−0.044, +0.014]). The analysis was not pre-registered, many arms are small, and tests were uncorrected.

<!-- fd:section id=findings -->
## Key findings

- In this post hoc analysis, one of 32 interventions, the Perception gap video, was nominally significant for affective polarization: 2.3 points lower than control (95% CI [−4.3, −0.4], p = 0.019, uncorrected).
- The pooled estimate across the 32 arms for affective polarization is 0.8 points lower than control (95% CI [−1.4, −0.2]). It is approximate, because the arms share one control group.
- Support for undemocratic practices was not distinguishable from control when pooled across arms: −0.015 (95% CI [−0.044, +0.014]). No single arm stood out among the 32.
- Nothing was pre-registered and 64 tests were uncorrected, so the one nominally significant arm may be a chance finding with an inflated estimate; many arms have fewer than 100 respondents.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 32 arms and a control group; online panel, US. 6,086 responses were collected and 4,547 are analysed after the exclusions `partisan in ['Democrat','Republican']; arm != 'T33'`. The plan was supplied by the authors and is not pre-registered. Identifier and free-text columns removed before any model saw the data: RecordedDate.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 4,547 analysed). Respondents are randomly assigned to 33 arms: Cooperation infographic, Bipartisan bills graph, Bipartisan elite quotes, Shared values exercise, Cross-partisan dialogue guide, Meta-dehumanization correction, Perception survey (form), Common-ground articles, Patriotic article, 14th Amendment video, Congressional softball video, iSideWith quiz, Rick and Morty perspective-taking, Brené Brown empathy video, Perception gap video, 'What makes an American' video, McCain defends Obama video, Egyptian revolution video, Cross-partisan friendship TED talk, American history video, Party-tailored videos, Jubilee free speech panel, Jubilee video, Media-profits-from-division image, Shared priorities (Pew) table, Bipartisan legislation examples, Common threat (Russia), Pro-democracy excerpt, Biden–DeSantis cooperation, Scandals, both parties (labeled), Scandals (labels revealed later), Perception gap quiz, against the control group Control. Cooperation infographic: Image: Infographic on Americans wanting to work together Bipartisan bills graph: Image: Graph showing bipartisan bill passage rates Bipartisan elite quotes: Text: Bipartisan elite quotes (Obama, Reagan, McCain, Sanders, Trump, Clinton) Shared values exercise: Interactive: Values elicitation + policy support statistics by party Cross-partisan dialogue guide: Text: Abortion dialogue guide + docuseries about cross-partisan talks Meta-dehumanization correction: Text: Meta-dehumanization correction (300% overestimate statistic) Perception survey (form): Interactive: Google Forms political perception survey Common-ground articles: Text: Articles on bipartisan common ground (TheHill + PublicConsultation) Patriotic article: Text: 'What Makes America Great' patriotic article 14th Amendment video: Video: 14th Amendment privacy rights: bipartisan implications (abortion, vaccines, data) Congressional softball video: Video: Bipartisan congressional softball game + cross-party cooperation videos iSideWith quiz: Interactive: iSideWith political quiz Rick and Morty perspective-taking: Video: Rick and Morty perspective-taking: imagine being opposite party member Brené Brown empathy video: Video: RSA Brené Brown empathy video: empathy vs sympathy Perception gap video: Video: Perception gap video with misperception data 'What makes an American' video: Video: Street interviews on 'what makes an American' + superordinate identity McCain defends Obama video: Video: McCain defending Obama at 2008 rally: 'He's a decent family man' Egyptian revolution video: Video: Egyptian revolution aftermath: cautionary tale of polarization Cross-partisan friendship TED talk: Video: Ted Talk: cross-partisan friendship during 2016 election American history video: Video: American history chronology: shared national heritage Party-tailored videos: Video: Partisan-specific videos (different content by party) Jubilee free speech panel: Video: Jubilee panel: liberals and conservatives discuss free speech Jubilee video: Video: Jubilee video (J7We_PYASzc) Media-profits-from-division image: Image: Media critique: corporations profit from division Shared priorities (Pew) table: Text: Pew table showing shared partisan priorities Bipartisan legislation examples: Text: Bipartisan legislation examples (NCLB, ACA, TCJA, IRA) Common threat (Russia): Text: Russia nuclear threat + reflection on cross-party reliance Pro-democracy excerpt: Text: Pro-democracy excerpt (CNN for Dems, Fox for Reps) Biden–DeSantis cooperation: Text: Biden-DeSantis Hurricane Ian cooperation Scandals, both parties (labeled): Text: Political scandals from both parties (labels visible) Scandals (labels revealed later): Text: Political scandals (labels redacted, then revealed) Perception gap quiz: Interactive: Perception Gap Quiz 'as an independent' Outcomes: Affective polarization after treatment, Support for undemocratic practices.


The plan was not pre-registered; it was reconstructed from a replication script, so every test here is post hoc. The sample is a US online panel: 6,086 raw respondents, 4,547 after filtering, and 3,825 (H1) and 3,953 (H2) in the models, with the remainder lost to missing pre- or post-treatment values. The GPT-3 chatbot arm (technical failures) was excluded, and the analysis keeps only Democrats and Republicans, so independents are dropped. Each of 32 interventions was compared with control. Arm sizes run from 48 to 641 (H1) and 51 to 662 (H2). The 32 arms are tested on two outcomes, 64 tests in all. Estimates are in native scale units.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=unregistered outcome=post_ap -->
### H1. Affective polarization after treatment

*Each intervention changes post_ap relative to control.*  
*Post hoc, not pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

The Perception gap video, the largest arm at 641 respondents, was nominally significant: 2.3 points lower than control (95% CI [−4.3, −0.4], two-sided p = 0.019), uncorrected and post hoc. The control mean was 41.5 on the thermometer-based measure. The 'What makes an American' video (−2.6, 95% CI [−5.4, 0.1]) came close but was not distinguishable from zero. All 32 arms are shown in the table, and the others had intervals spanning zero. The approximate pooled estimate was 0.8 points lower (95% CI [−1.4, −0.2], p = 0.005). It treats arms as independent although they share one control, so it is approximate. The outcome's SD is not reported here, so no standardised effects are given.

Pooling the 32 arm effects with a random-effects model gives -0.819 (SE 0.291, p = 0.005; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H1)

```
post_ap ~ C(arm_code, Treatment(reference='T0')) + pre_ap
OLS | weights = ipw_weight | HC2 robust SEs | N = 3825 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Cooperation infographic | -1.153 | 1.592 | 0.4690 | [-4.273, 1.968] | 90 | no |
| Bipartisan bills graph | 0.377 | 1.522 | 0.8044 | [-2.607, 3.361] | 106 | no |
| Bipartisan elite quotes | -0.152 | 1.470 | 0.9179 | [-3.032, 2.729] | 94 | no |
| Shared values exercise | 0.860 | 1.690 | 0.6110 | [-2.453, 4.173] | 78 | no |
| Cross-partisan dialogue guide | -1.760 | 3.204 | 0.5827 | [-8.039, 4.519] | 68 | no |
| Meta-dehumanization correction | -0.024 | 1.633 | 0.9885 | [-3.225, 3.178] | 221 | no |
| Perception survey (form) | 0.172 | 1.743 | 0.9212 | [-3.243, 3.588] | 85 | no |
| Common-ground articles | -1.627 | 1.868 | 0.3837 | [-5.288, 2.034] | 67 | no |
| Patriotic article | -2.101 | 1.277 | 0.0999 | [-4.604, 0.402] | 330 | no |
| 14th Amendment video | -1.562 | 1.494 | 0.2960 | [-4.490, 1.367] | 62 | no |
| Congressional softball video | -2.437 | 1.954 | 0.2124 | [-6.268, 1.393] | 64 | no |
| iSideWith quiz | 0.357 | 1.304 | 0.7843 | [-2.198, 2.912] | 65 | no |
| Rick and Morty perspective-taking | -0.968 | 1.540 | 0.5297 | [-3.987, 2.051] | 58 | no |
| Brené Brown empathy video | -2.181 | 1.594 | 0.1714 | [-5.306, 0.944] | 163 | no |
| Perception gap video | -2.333 | 0.995 | 0.0191 | [-4.283, -0.382] | 641 | yes |
| 'What makes an American' video | -2.647 | 1.403 | 0.0592 | [-5.397, 0.102] | 149 | no |
| McCain defends Obama video | -0.689 | 2.592 | 0.7903 | [-5.769, 4.391] | 88 | no |
| Egyptian revolution video | -0.181 | 2.478 | 0.9416 | [-5.039, 4.676] | 72 | no |
| Cross-partisan friendship TED talk | 0.756 | 1.978 | 0.7024 | [-3.122, 4.633] | 71 | no |
| American history video | 1.311 | 2.277 | 0.5649 | [-3.153, 5.774] | 66 | no |
| Party-tailored videos | 0.838 | 1.581 | 0.5963 | [-2.262, 3.937] | 72 | no |
| Jubilee free speech panel | -1.875 | 2.151 | 0.3832 | [-6.090, 2.339] | 48 | no |
| Jubilee video | 0.098 | 2.068 | 0.9624 | [-3.955, 4.151] | 121 | no |
| Media-profits-from-division image | -2.629 | 2.097 | 0.2101 | [-6.740, 1.482] | 100 | no |
| Shared priorities (Pew) table | -0.088 | 1.480 | 0.9524 | [-2.989, 2.812] | 66 | no |
| Bipartisan legislation examples | 0.895 | 1.706 | 0.5998 | [-2.448, 4.238] | 68 | no |
| Common threat (Russia) | -0.961 | 1.765 | 0.5860 | [-4.419, 2.497] | 76 | no |
| Pro-democracy excerpt | -0.579 | 1.473 | 0.6940 | [-3.466, 2.307] | 60 | no |
| Biden–DeSantis cooperation | -0.734 | 1.277 | 0.5654 | [-3.237, 1.769] | 77 | no |
| Scandals, both parties (labeled) | -0.391 | 1.782 | 0.8265 | [-3.884, 3.102] | 140 | no |
| Scandals (labels revealed later) | -1.395 | 1.677 | 0.4053 | [-4.682, 1.891] | 73 | no |
| Perception gap quiz | 0.498 | 2.671 | 0.8521 | [-4.736, 5.732] | 57 | no |

<!-- fd:hyp id=H2 tag=unregistered outcome=post_udp -->
### H2. Support for undemocratic practices

*Each intervention changes post_udp relative to control.*  
*Post hoc, not pre-registered.*

![H2: effect by arm](figures/H2_arms.png)

No arm among the 32 shown moved support for undemocratic practices in a way distinguishable from control. Estimates ranged from −0.16 to +0.14 on a scale where the control mean was 2.75. The closest was the McCain defends Obama video (+0.14, 95% CI [−0.02, 0.31], two-sided p = 0.082). The pooled estimate was −0.015 (95% CI [−0.044, +0.014], p = 0.309). These intervals are inconclusive. Without an outcome SD or a stated smallest effect of interest, they cannot be called tight, and small effects for individual arms are not excluded.

Pooling the 32 arm effects with a random-effects model gives -0.015 (SE 0.015, p = 0.309; tau² 0.0000, I² 0.00). The arms share one control group, so this pooled standard error is approximate.

#### Details: model and estimates by arm (H2)

```
post_udp ~ C(arm_code, Treatment(reference='T0')) + pre_udp
OLS | weights = ipw_weight | HC2 robust SEs | N = 3953 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Cooperation infographic | 0.048 | 0.082 | 0.5579 | [-0.113, 0.209] | 94 | no |
| Bipartisan bills graph | 0.046 | 0.075 | 0.5415 | [-0.102, 0.194] | 110 | no |
| Bipartisan elite quotes | -0.115 | 0.088 | 0.1917 | [-0.289, 0.058] | 96 | no |
| Shared values exercise | -0.076 | 0.088 | 0.3859 | [-0.248, 0.096] | 81 | no |
| Cross-partisan dialogue guide | -0.125 | 0.088 | 0.1572 | [-0.298, 0.048] | 71 | no |
| Meta-dehumanization correction | -0.038 | 0.063 | 0.5431 | [-0.162, 0.085] | 227 | no |
| Perception survey (form) | 0.090 | 0.089 | 0.3122 | [-0.085, 0.266] | 88 | no |
| Common-ground articles | 0.029 | 0.119 | 0.8076 | [-0.205, 0.263] | 68 | no |
| Patriotic article | -0.058 | 0.058 | 0.3202 | [-0.172, 0.056] | 339 | no |
| 14th Amendment video | -0.086 | 0.075 | 0.2476 | [-0.233, 0.060] | 62 | no |
| Congressional softball video | 0.038 | 0.086 | 0.6568 | [-0.130, 0.206] | 65 | no |
| iSideWith quiz | -0.018 | 0.085 | 0.8289 | [-0.185, 0.148] | 67 | no |
| Rick and Morty perspective-taking | -0.063 | 0.090 | 0.4891 | [-0.240, 0.115] | 61 | no |
| Brené Brown empathy video | -0.071 | 0.073 | 0.3294 | [-0.215, 0.072] | 171 | no |
| Perception gap video | -0.006 | 0.054 | 0.9089 | [-0.113, 0.100] | 662 | no |
| 'What makes an American' video | 0.058 | 0.074 | 0.4287 | [-0.086, 0.203] | 156 | no |
| McCain defends Obama video | 0.144 | 0.083 | 0.0817 | [-0.018, 0.306] | 88 | no |
| Egyptian revolution video | -0.006 | 0.079 | 0.9437 | [-0.161, 0.150] | 74 | no |
| Cross-partisan friendship TED talk | 0.034 | 0.105 | 0.7454 | [-0.172, 0.240] | 72 | no |
| American history video | -0.065 | 0.080 | 0.4176 | [-0.222, 0.092] | 67 | no |
| Party-tailored videos | -0.116 | 0.124 | 0.3481 | [-0.358, 0.126] | 72 | no |
| Jubilee free speech panel | -0.051 | 0.101 | 0.6129 | [-0.249, 0.147] | 51 | no |
| Jubilee video | -0.003 | 0.073 | 0.9689 | [-0.145, 0.139] | 124 | no |
| Media-profits-from-division image | 0.145 | 0.102 | 0.1551 | [-0.055, 0.344] | 106 | no |
| Shared priorities (Pew) table | -0.008 | 0.100 | 0.9332 | [-0.205, 0.188] | 69 | no |
| Bipartisan legislation examples | -0.030 | 0.085 | 0.7254 | [-0.196, 0.137] | 70 | no |
| Common threat (Russia) | 0.034 | 0.089 | 0.7049 | [-0.141, 0.208] | 81 | no |
| Pro-democracy excerpt | -0.156 | 0.126 | 0.2150 | [-0.404, 0.091] | 60 | no |
| Biden–DeSantis cooperation | -0.092 | 0.107 | 0.3892 | [-0.303, 0.118] | 81 | no |
| Scandals, both parties (labeled) | -0.007 | 0.082 | 0.9355 | [-0.167, 0.154] | 144 | no |
| Scandals (labels revealed later) | -0.019 | 0.084 | 0.8166 | [-0.183, 0.145] | 78 | no |
| Perception gap quiz | 0.032 | 0.104 | 0.7569 | [-0.172, 0.236] | 58 | no |

![Planned treatment effects](figures/registered_effects.png)

<!-- fd:section id=exploratory -->
## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

_None produced._

<!-- fd:section id=related -->
## Related work

The retrieved works are entirely off-topic relative to the study's hypotheses about interventions changing post_ap and post_udp relative to control; none of them address the relevant outcome variables or intervention framework, so no prior findings can be drawn on to support or contest H1 or H2.

Retrieved works (OpenAlex; queries: affective polarization intervention reduction experiment; democratic norms malleability persuasion intervention; affective polarization stability identity motivated reasoning resistant; backfire effect political attitudes persuasion failure; multi-arm experimental design feeling thermometer affective polarization):

- Nicolas Gisin, G. Ribordy, Wolfgang Tittel, Hugo Zbinden (2002). Quantum cryptography. Reviews of Modern Physics. https://doi.org/10.1103/revmodphys.74.145
- Michael J. Mitchell, Margaret M. Billingsley, Rebecca M. Haley, Marissa E. Wechsler (2020). Engineering precision nanoparticles for drug delivery. Nature Reviews Drug Discovery. https://doi.org/10.1038/s41573-020-0090-8
- Johan Alwall, Rikkert Frederix, Stefano Frixione, Valentin Hirschi (2014). The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations. Journal of High Energy Physics. https://doi.org/10.1007/jhep07(2014)079
- David K. Sherman, Geoffrey L. Cohen (2006). The Psychology of Self‐defense: Self‐Affirmation Theory. Advances in experimental social psychology. https://doi.org/10.1016/s0065-2601(06)38004-5
- Constantine Sedikides, Aiden P. Gregg (2008). Self-Enhancement: Food for Thought. Perspectives on Psychological Science. https://doi.org/10.1111/j.1745-6916.2008.00068.x
- John R. Hibbing, Kevin B. Smith, John R. Alford (2014). Differences in negativity bias underlie variations in political ideology. Behavioral and Brain Sciences. https://doi.org/10.1017/s0140525x13001192
- Filomena Maggino (2023). Encyclopedia of Quality of Life and Well-Being Research. . https://doi.org/10.1007/978-3-031-17299-1
- Didier Sornette (2014). Physics and financial economics (1776–2014): puzzles, Ising and agent-based models. Reports on Progress in Physics. https://doi.org/10.1088/0034-4885/77/6/062001
- Brit M. Quandt, Lukas J. Scherer, Luciano Fernandes Boesel, Martin Wolf (2014). Body‐Monitoring and Health Supervision by Means of Optical Fiber‐Based Sensing Systems in Medical Textiles. Advanced Healthcare Materials. https://doi.org/10.1002/adhm.201400463
- Christian Lukas Degen, Friedemann Reinhard, Paola Cappellaro (2017). Quantum sensing. Reviews of Modern Physics. https://doi.org/10.1103/revmodphys.89.035002

<!-- fd:section id=limitations -->
## Limitations

Nothing was pre-registered, so all tests are post hoc and the choice of outcomes and models came from a script. Sixty-four tests were run without correction. Under the null, about 1.6 false positives are expected at the 5% level, and the chance of at least one is about 81%, so one nominal hit is weak evidence and its estimate is likely inflated. Many arms have 60 to 100 respondents, so their intervals are wide. Of 6,086 raw respondents, 4,547 passed filters and the models use 3,825 (H1) and 3,953 (H2); the reasons for these losses are not examined, so selective attrition cannot be ruled out. Results concern immediate attitudes in an online panel.

<!-- fd:section id=review round=1 -->
## Peer review

*Automated review. Reviewers and models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `anthropic/claude-sonnet-5.5`, advanced:statistics `anthropic/claude-sonnet-5.5`, orchestrator `anthropic/claude-sonnet-5.5`. Registered analyses are never changed to satisfy a reviewer; robustness checks sit beside them.*

**Review outcome.** Round 1: 12 of 12 claims supported by the results after the authors' revision; 8 analytical issues open for a robustness round.

**Review synthesis.** The tables support a narrow reading: one of 32 arms (Perception gap video, -2.33, CI [-4.28,-0.38], p=0.019) is nominally significant on affective polarization, and no arm differs on undemocratic-practice support. The study is post hoc, uncorrected, and has only 229 controls. The pooled -0.8 estimate comes from an approximate random-effects model that ignores the shared control, so its p=0.005 is not reliable. The most important caveat is that the single nominal hit is consistent with chance among 64 uncorrected tests, and the sample flow (4,547 vs 3,825/3,953 modelled) is unexplained.

#### A1 · high · Robustness check proposed

*Results H1 / Design.* Pooled estimate treats arms as independent despite shared control: The random-effects pooled result (−0.819, SE 0.291, p=0.005; tau²=0, I²=0) ignores that all arms share one control group of 229. The text admits the SE is 'approximate', yet the abstract and key findings headline p=0.005. The estimate is also a pooled arm average, not a pooled treated-vs-control contrast. Its precision is likely overstated.

**Disposition.** Same as R2: a single pooled contrast or omnibus joint test is estimable from existing data.

#### A2 · high · Robustness check proposed

*Design and data.* Exclusions and attrition undocumented; analysed N varies: Of 6,086 raw respondents, 4,547 were analysed, and the model N is 3,825 (H1) and 3,953 (H2). The reasons for dropping respondents are not given beyond the partisan filter and the removal of arm T33. Missingness in the post outcomes and in the weights is not reported. Differential attrition across arms could bias the estimates. The exclusion of the GPT-3 arm is mentioned only in passing.

**Disposition.** A by-arm attrition table and a differential-missingness test can be computed from the raw data.

#### A3 · high · Robustness check proposed

*Results H1.* Control group small; control mean and arm means inconsistent with adjusted estimates: Only 229 controls anchor all 32 contrasts. The model is adjusted for pre_ap with IPW, but the table's raw mean_arm minus mean_control differs a lot from the estimates. For example, T2 has mean 45.4 vs control 41.5 (+3.9), yet the estimate is +0.38. This suggests large baseline imbalance or weighting effects, which the text does not discuss. Unweighted means are presumably reported.

**Disposition.** Balance checks and weighted/unweighted and with/without covariate fits use existing data.

#### A4 · high · Unresolved

*Design and data.* Randomisation and arm-size imbalance not described: Arm sizes range from about 48 to 660, with the Perception gap video at 641 against typical arms of 60–100. The allocation mechanism is not explained, nor is whether arms were run concurrently. If arms were fielded at different times, comparison with a shared control is confounded. Treatment content differs in length and format, with no manipulation checks.

**Disposition.** Randomisation procedure and fielding timing cannot be verified from the tables; balance tests can only partly help.

#### A7 · high · Robustness check proposed

*Results H1 / Limitations.* Pooled estimate treats shared-control arms as independent: The random-effects pooled estimate (-0.819, SE 0.291, p=0.005) combines 32 arm effects that all share one control group (n=229), so the arm estimates are positively correlated. The report admits the SE is 'approximate', but the abstract and key findings still headline p=0.005. With tau²=0 and I²=0, this is effectively a fixed-effect average. The SE is likely too small, and a meaningful pooled effect is overstated.

**Disposition.** Duplicate of R2/A1: fit the pooled any-treatment indicator with HC2 SEs.

#### A8 · high · Editorial

*Results H1 / Abstract.* Single significant arm among 32 emphasised; winner's curse: The Perception gap video (p=0.019) is one of 32 uncorrected tests. Under the null, about 1.6 nominal hits are expected, and the p-value is far from any Bonferroni threshold (0.05/32≈0.0016). The point estimate of -2.3 is likely inflated. The abstract's wording 'clearly reduced' is too strong. Under the no-correction policy this is a limitation, not an error.

**Disposition.** Replace 'clearly reduced' with 'nominally significant' and state the expected false positives; adjusted p-values are declined under the no-correction policy.

#### A9 · high · Robustness check proposed

*Design and data / Limitations.* Differing sample sizes and unexamined attrition and weighting: The analysed N is 4,547 but the models use N=3,825 (H1) and N=3,953 (H2), so about 700 further observations are lost to missing pre/post data. The report does not explain this. The control group has only 229 respondents against 641 in the Perception gap arm, so the control is imprecise and the n(arm) imbalance is unaddressed. IPW weights are used without being described. The exclusion of non-partisans changes the estimand.

**Disposition.** Attrition by arm, weight description and unweighted re-fit use existing data.

#### R1 · high · Editorial

*Design / H1 / H2 sample sizes.* The analysed N is reported as 4,547, but the models use N=3,825 (H1) and 3,953 (H2). The 32 arm sizes in the H1 table sum to well under 3,825. The report never explains the gap, which suggests missing pre-treatment or outcome data. The 'arm sizes 60 to 660' and 'about 1,500 missing' statements also don't match this.

**Disposition.** A sample-flow table and corrected N and arm-size statements are needed; the data on losses may be partly recoverable but this is a reporting fix.

#### R2 · high · Robustness check proposed

*H1/H2 pooled estimates.* The pooled effects (-0.8 and -0.015) come from a random-effects meta-analysis of arm estimates that share one control group. The report admits the SE is approximate, yet it uses p=0.005 as a headline. Tau² = 0 and I² = 0 look degenerate. Pooled significance is also stated more strongly than the single-arm results justify. The pooled value of -0.8 is far smaller than most arm estimates, and the arm estimates do not obviously average to it.

**Disposition.** A pooled any-treatment vs control regression with robust SEs can be fitted on the same data.

#### R3 · high · Declined

*Abstract / Key findings.* The report says only the Perception gap video 'clearly reduced' polarization (p=0.019) and calls this a 'chance finding', but the tests are not multiplicity-corrected. The 'What makes an American' video (−2.6, p=0.059) has a larger point estimate. There is no adjusted p-value, so the 'clearly reduced' wording overstates the evidence.

**Disposition.** The plan specifies no multiplicity correction, so adjusted p-values would change the analysis; soften the wording and flag the lack of correction instead.

#### A10 · medium · Robustness check proposed

*Results H2.* Null interpretation lacks equivalence or power framing: The text says the pooled CI 'rules out large effects', but the scale is not benchmarked (control mean 2.75, SD not given). Individual arm CIs of about ±0.2 are not interpreted against any smallest effect of interest. The arm-level 'no effect' is therefore uninterpretable. The arm-level range of '−0.13 to +0.14' also omits the observed -0.156 and +0.145.

**Disposition.** Outcome SD, standardised effects and minimum detectable effects can be computed from existing data; correct the quoted range.

#### A11 · medium · Editorial

*Limitations / Key findings.* Test count is stated inconsistently: The report says '64 tests' (32 per outcome × 2). But the H1 table has 32 rows, and the arm lists total 32 interventions against the 33-arm design text. The T33/GPT-3 exclusion and the 33-arm description are confusing. The 'one in 32 is what chance would produce' claim is also loose: the expected count is 1.6 and P(≥1) is about 0.8.

**Disposition.** Clarify the arm and test counts and state the chance expectation exactly.

#### A5 · medium · Declined

*Results H1/H2.* Uncorrected multiplicity and inconsistent claims about the single hit: There are 64 uncorrected tests (the multiple-testing policy is 'none', which was the authors' choice). The Perception gap video p=0.019 would not survive any correction. The abstract says it 'clearly reduced' affective polarization, which is stronger than the evidence warrants, even though caveats appear later. The H2 text also says 'rule out large effects' without a stated threshold.

**Disposition.** Corrections conflict with the plan's 'none' multiplicity policy; only soften wording and state the smallest effect of interest.

#### A6 · medium · Editorial

*Results H1.* Outcome scaling and sign interpretation unclear: The Intercept of 3.67 in the H1 model, with a control mean of 41.5, shows that pre_ap is a strong predictor. Whether higher values mean more polarization is not defined, and the thermometer-based measure is not specified. The 2.3-point effect is not put in standardized units.

**Disposition.** Define the outcome, its direction and the SD; standardised effects follow from existing data.

#### R4 · medium · Robustness check proposed

*Design / model spec.* The models use ipw_weight inverse-probability weights, and the report never says what they correct for. Weights, HC2 SEs and pre-treatment covariates are all choices lifted from the script and not justified. The weights likely relate to the missing-data handling, but this is unexplained.

**Disposition.** Unweighted and complete-case re-fits can be added as robustness checks, and the weights described.

#### R5 · medium · Editorial

*Design / exclusions.* The exclusion 'arm != T33' (the GPT-3 chatbot arm) is mentioned only in passing. The text also says '32 interventions' in the abstract against '33 arms' in the design section. The restriction to Democrats and Republicans drops independents without discussion.

**Disposition.** State the T33 and independents exclusions and reconcile 32 vs 33 arms in the text.

#### R6 · medium · Editorial

*Results prose (H1/H2).* The text says 'the other arms shown' and 'no arm in the displayed rows', although the table lists all 32 arms. The '64 tests' count also isn't shown in the results.

**Disposition.** Fix 'displayed rows' wording and state the test count.

#### R7 · low · Editorial

*Related work / figures.* The retrieved literature is irrelevant (physics papers, etc.). A leftover 'Planned treatment effects' figure appears even though nothing was planned.

**Disposition.** Remove the off-topic citations and the 'Planned treatment effects' figure.

#### Claim checks

| Claim | Where | Verdict | Evidence | After revision |
|---|---|---|---|---|
| Only one intervention clearly reduced affective polarization | Abstract | **overstated** | H1 table: Perception gap video -2.333, p=0.0191, one of 32 uncorrected tests; 'What makes an American' is -2.647, p=0.059. | **supported**: One intervention was nominally significant for affective polarization: the Perception gap video lowered the post-treatment thermometer-based measure by 2.3 points ... in an uncorrected, post hoc analysis, so the estimate is likely inflated |
| Perception gap video lowered the measure by 2.3 points (95% CI [−4.3, −0.4], p = 0.019) | Abstract | **supported** | H1 table: -2.333, SE 0.995, CI [-4.283,-0.382], p=0.0191. | **supported**: Perception gap video lowered ... by 2.3 points (95% CI [−4.3, −0.4], p = 0.019, two-sided) |
| Pooled across all interventions, affective polarization was 0.8 points lower (CI [−1.4, −0.2], p = 0.005) | Abstract | **overstated** | Random-effects pooled -0.819, SE 0.291, p=0.005, but arms share one control (n=229) so the SE is understated; tau²=0 is degenerate. | **supported**: An approximate pooled estimate across arms was 0.8 points lower than control (95% CI [−1.4, −0.2]) |
| Support for undemocratic practices showed no distinguishable pooled difference (−0.015, CI [−0.044, +0.014]) | Abstract | **supported** | H2 pooled -0.015, SE 0.015, p=0.309; same shared-control SE caveat. | **supported**: Support for undemocratic practices showed no distinguishable pooled difference (−0.015, 95% CI [−0.044, +0.014]) |
| no individual arm ... differed clearly from control | Abstract | **supported** | H2 table: smallest p is McCain video 0.082; all supported=no. | **supported**: No arm among the 32 shown moved support for undemocratic practices in a way distinguishable from control |
| The other arms shown had intervals spanning zero | H1 | **supported** | All other 31 H1 CIs include 0; 'What makes an American' upper bound 0.102. | **supported**: All 32 arms are shown in the table, and the others had intervals spanning zero |
| Estimates ranged roughly from −0.13 to +0.14 | H2 | **unsupported** | H2 table: min -0.156 (Pro-democracy excerpt), max +0.145 (Media-profits image). | **supported**: Estimates ranged from −0.16 to +0.14 on a scale where the control mean was 2.75 |
| The Perception gap video, the largest arm at 641 respondents | H1 | **supported** | H1 n(arm)=641, the largest. | **supported**: The Perception gap video, the largest arm at 641 respondents |
| arm sizes range from roughly 60 to 660 | Design | **overstated** | H1 n(arm) runs from 48 (Jubilee free speech panel) to 641; 662 appears in H2. | **supported**: Arm sizes run from 48 to 641 (H1) and 51 to 662 (H2) |
| These intervals ... rule out large effects in the pooled case | H2 | **overstated** | Pooled CI [-0.044,0.014] but no outcome SD or smallest effect of interest is given. | **supported**: These intervals are inconclusive. Without an outcome SD ... they cannot be called tight |
| one significant arm out of 32 is about what chance could produce | Limitations | **overstated** | Expected false positives are 1.6 at alpha .05; P(at least one) is about 0.81. | **supported**: Under the null, about 1.6 false positives are expected at the 5% level, and the chance of at least one is about 81% |
| About 1,500 raw respondents are missing from the analysis sample | Limitations | **overstated** | 6,086-4,547 = 1,539, but models use N=3,825 (H1) and 3,953 (H2), so about 2,100-2,260 are absent from the models. | **supported**: Of 6,086 raw respondents, 4,547 passed filters and the models use 3,825 (H1) and 3,953 (H2) |

#### Editorial guidance and the authors' response

| # | Guidance | Response |
|---|---|---|
| G1 | Replace 'clearly reduced' with 'nominally significant (p=0.019), uncorrected, post hoc' everywhere, including the Abstract and Key findings. | Applied as in K1, including abstract and takeaways. |
| G2 | Add a sample-flow table by arm (raw, partisan filter, T33 removal, missing pre/post, per-model N) and fix the '60-660' and '1,500 missing' statements. | Partly done: the flow is given in prose, and the table cannot be added without data. |
| G3 | Replace the approximate random-effects pooled result with a pooled any-treatment vs control regression with robust SEs, or label it clearly as approximate. | Pooled estimate labelled approximate. |
| G4 | Describe the IPW weights and add unweighted and complete-case sensitivity results. | Not done: no IPW or sensitivity results are in the supplied materials. |
| G5 | Define the outcome direction and SD, give standardised effects, and correct the H2 range to -0.16 to +0.14. | Corrected the H2 range. Outcome SD and standardised effects are not available, and this is stated. |
| G6 | Remove the irrelevant citations and the 'Planned treatment effects' figure; say all 32 arms are shown and reconcile 32 vs 33 arms. | Stated that all 32 arms are shown and reconciled the arm counts. The figure and citations are outside my sections. |

#### Claims reworded in revision

- **K1.** Abstract now says nominally significant (p=0.019), uncorrected, post hoc, likely inflated; 'clearly' removed.
- **K2.** Pooled figure labelled approximate in the abstract, takeaways and H1, noting the shared control; no new regression added since no such result is in the tables.
- **K3.** H2 range corrected to −0.16 to +0.14.
- **K4.** Arm sizes stated as 48 to 641 (H1) and 51 to 662 (H2).
- **K5.** Dropped the 'rule out large effects' claim; noted no SD or smallest effect of interest is available.
- **K6.** Stated expected 1.6 false positives and about 81% chance of at least one.
- **K7.** Flow reported to model Ns, 3,825 and 3,953, from 6,086 raw and 4,547 filtered.

#### Unresolved questions

- **U1.** Were arms randomised and fielded concurrently with the control, and is the Perception gap effect robust in a preregistered replication with adequate power? Allocation and fielding details are not in the tables, and a single uncorrected nominal hit among 32 needs new data to confirm.
- **U2.** Does differential attrition between raw and analysed samples bias the arm contrasts? Reasons for the loss of roughly 2,000 respondents cannot be reconstructed from the tables. Taken up by the proposed extensions *Does the Perception gap effect hold across partisanship and baseline polarization?* and *Sample-flow and attrition audit from existing data*.


<!-- fd:section id=potential -->
## Research potential

*An assessment by the pipeline of what this study can still become: what stands, why it may not have landed, the debates it bears on, and which follow-up is worth running. Written after the review; the proposed extensions below are built from it.*

**What stands.** Tested 32 distinct interventions against one shared control in a single fielding, so arms are directly comparable and the cost of each is the same. Pre-treatment covariate adjustment (pre_ap, pre_udp) with HC2 robust SEs and weights, which tightens estimates. Reported all 64 arm-by-outcome estimates and said openly that the single hit (Perception gap, p = 0.019) is uncorrected and likely inflated. The Perception gap video was also the largest arm (n = 641 on H1), so its interval (SE 0.995) is the tightest of the arms.

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Most arms have 48-110 respondents against a control of 229, so per-arm SEs of 1.3-3.2 points cannot detect effects under about 4 points. A true effect of about 2 points would be missed in nearly all arms. | H1 arm SEs range 0.995 (n=641) to 3.204 (n=68); the control has n=229; only the Perception gap arm has SE under 1.2. |
| Analysis | With 64 uncorrected, unregistered tests, one nominal hit is what chance alone would produce (about 81% chance of at least one false positive). The estimate is likely inflated by the winner's curse. | Perception gap: -2.333, p=0.0191, CI [-4.283, -0.382]; the limitations section puts the family-wise chance of at least one false positive at about 81%. |
| Design | The 32 interventions differ in format, length, and mechanism, so no arm tests a mechanism. A pooled effect across heterogeneous arms is hard to interpret. The shared control also leaves arm contrasts correlated. | Arms mix videos, texts, images, and quizzes; pooled H1 is -0.819 (SE 0.291) with tau2=0 and I2=0, which is approximate because of the shared control. |
| Sample | About 1,540 of the 6,086 respondents were lost to filters and a further 600-700 to missing pre/post values. The reasons are unexamined, so differential attrition across arms may bias contrasts. Independents are excluded entirely. | N=6,086 raw, 4,547 after filters, 3,825 (H1) and 3,953 (H2) in the models; editor's U2. |
| Measurement | The outcome SD and direction are not reported, so effects cannot be standardised. The 2.3-point change is on a thermometer-based scale with control mean 41.5, and the H2 effects are tiny against an unknown SD. | Report: 'The outcome's SD is not reported here'; H2 range -0.16 to +0.14 against a control mean of 2.75. |

**Verdict.** Run one follow-up, and run the preregistered replication of the Perception gap video first. The current evidence is one uncorrected hit (-2.3, p=0.019) among 64 tests, most arms are underpowered, and H2 shows nothing. Run the zero-cost attrition audit first, since it determines whether the existing contrasts can be trusted. The retrieved literature is off-topic, so no genuine debate can be named; the theoretical brief is a placeholder pending a proper search. The moderator study on party and baseline polarization only makes sense if the replication holds.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the pipeline from these results, each answering one of the reasons the study did not land (see Research potential). 1 survey design(s) ship as an importable Qualtrics file (`extensions/<id>.qsf`: in Qualtrics, Create project, Survey, How do you want to start: Import a QSF file); non-survey follow-ups are plans. Advanced: with a Qualtrics API token and the local Qualtrics MCP server, `filedrawer build-extension . <id>` creates the draft directly. They are proposals, not findings.*

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Does the Perception gap effect hold across partisanship and baseline polarization?

The source found one nominal hit, the Perception gap video (-2.3 points, 95% CI [-4.3, -0.4], p = 0.019, uncorrected), after partisan filters removed independents and with no moderator examined. Of 6,086 raw respondents only 4,547 passed filters, with reasons unexamined. This design reruns video vs control including independents and leaners, stratifies on party and baseline thermometer tercile, and tracks attrition by arm.

**Why this one.** Addresses the sample failure: independents were dropped and no moderator was examined.

*Answers the open reviewer question U2 (see Peer review).*

**Hypothesis.** The video lowers affective polarization relative to control, more among strong partisans and the high baseline tercile; the effect is smaller or null among pure independents.

**Design.** Perception gap video vs. Control; primary outcome: Post-treatment in-party minus out-party thermometer difference (for independents, absolute difference between party thermometers).

**Power.** About 1500 per arm to detect 2.4 at 80% power (Interaction tests need about twice the n of the main effect; 1500 per arm gives subgroup cells of about 500, and an MDE of roughly 2.4 points per subgroup, near the observed -2.3.).

Files: [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt) · [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) (3 media stimuli to supply after import)

#### Details: open items before fielding (generalizability_conditional)

- Hosting of the Perception gap video file and its exact length.
- IRB approval number and participant compensation.
- Platform implementation of stratified randomization.
- Supply media: video1: video stimulus to supply (Perception gap video showing misperceptions of the other party, about 5 minutes)
- Supply media: pre_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90
- Supply media: post_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90

<!-- fd:ext id=theoretical_debate kind=observational label=theoretical_debate -->
### Theoretical debate: Perception-Gap Correction vs. Superordinate Identity: A 2×2 Factorial Test of Additive vs. Substitutive Mechanisms for Reducing Affective Polarization

The source study's single nominally significant arm (Perception-gap video, −2.3 points, p = 0.019 uncorrected) and a second near-significant arm (a superordinate-identity / 'What makes an American' video, −2.647, p = 0.059) point to two distinct theoretical mechanisms—correcting intergroup misperceptions versus activating a shared national identity—that the literature treats as competing explanations for reducing affective polarization. Because the source study ran each arm independently against a shared control, it cannot tell whether these mechanisms operate on the same psychological resource (substitutive) or on independent channels (additive), which is the core unresolved question in the intergroup-contact and misperception-correction literatures.

**Why this one.** It fixes nothing yet. A debate brief needs a new literature search on correcting misperceptions versus superordinate identity or empathy.

**Hypothesis.** The perception-gap correction and superordinate-identity interventions have substitutive (negative interaction) effects on affective polarization, indicating they operate through a shared psychological mechanism rather than independent channels.

**Design.** Individual US adults (self-identified partisans or leaners) recruited from an online panel; the unit of analysis is the person, with 4 experimental cells (control, perception-gap only, superordinate-identity only, both). Exposure: A 2×2 factorial manipulation: Factor A = perception-gap correction (Perception-gap video vs. no video); Factor B = superordinate identity (What-makes-an-American video vs. no video). Variation is induced by random assignment to one of four conditions: (1) control (no video), (2) perception-gap video only, (3) superordinate-identity video only, (4) both videos. The 'both' condition presents the two videos in a counterbalanced order. Outcome: Post-treatment affective polarization measured as the mean of the two party-thermometer scores (0–100), lower = less polarized. Secondary outcome: support for undemocratic practices (same scale as source study). Measured immediately after the video manipulation, before any delay.

**Identification.** Compare the four cell means in a 2×2 ANOVA / OLS regression. The main effect of Factor A (perception-gap) is the average effect of the perception-gap video across both levels of Factor B; the main effect of Factor B is analogous. The interaction term tests whether the two interventions' effects are additive (interaction ≈ 0) or substitutive (interaction < 0, meaning the combined effect is less than the sum of the individual effects, implying they draw on the same psychological resource). Identification requires that randomization balances observed and unobserved confounders across the four cells, and that the two videos differ only in their intended theoretical mechanism (no systematic differences in length, tone, or production quality).

**Data.** Pew Research Center American Trends Panel (ATP) or Qualtrics Panel (US adult sample, opt-in, demographically weighted): provides the respondent pool, pre-treatment affective-polarization thermometer scores, and demographic covariates.; Source-study intervention videos: the 'Perception gap' video (student-produced, ~2 min, shows how partisans misperceive each other's views) and the 'What makes an American' video (student-produced, ~2 min, emphasizes shared national identity and common values). Both are available from the source study's supplementary materials or the research team's repository.; Pre-treatment affective-polarization thermometer (0–100) for both parties, measured in the survey before randomization, to serve as a baseline covariate and to define the sample (e.g., exclude those with no partisan identification).

**Analysis.** Primary estimator: OLS regression of post-treatment affective polarization on the two binary treatment indicators (perception-gap, superordinate-identity) and their interaction, plus pre-treatment polarization, party identification, age, sex, and education as covariates. Standard errors clustered at the individual level (no clustering needed for a simple RCT). Pre-specified tests: (1) the interaction term (perception-gap × superordinate-identity) — the primary test of additivity vs. substitutivity; (2) the main effect of the perception-gap factor, averaged across levels of the superordinate-identity factor. Both tested at α = 0.05 two-sided, with the interaction as the primary hypothesis. A secondary analysis will repeat the model with the undemocratic-practices outcome. Power: with n ≈ 600 per cell (2,400 total), SE ≈ 1.0 for a cell mean, the design has 80% power to detect a 2.3-point difference in a main effect and approximately 60% power to detect a 2.3-point interaction (substitutive effect), given the larger SE of the interaction term. If the true effects are smaller than the inflated source-study estimates, power for the interaction will be lower; a sensitivity analysis at 1.5-point effects will be reported.

Files: [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: open items before fielding (theoretical_debate)

- Differential video quality or length between the two student-produced videos could confound the content manipulation; mitigation: pre-test both videos for perceived quality and length, and trim or re-edit if they differ by more than 15 seconds.
- Order effects in the 'both' cell: the first video may prime the response to the second; mitigation: counterbalance video order within the 'both' cell and include order as a covariate.
- Demand characteristics: participants may guess the hypothesis and respond accordingly; mitigation: use a cover story ('we are testing how different types of short videos affect political attitudes') and include attention checks.
- Multiple testing: with two primary outcomes and a 2×2 design (4 tests per outcome), a Bonferroni or FDR correction is needed; the interaction test is the primary hypothesis and should be tested first.
- Panel attrition between pre- and post-treatment waves; mitigation: track and report attrition by cell, and use inverse-probability weighting if differential.

<!-- fd:ext id=data_to_collect kind=observational label=data_to_collect -->
### Data to collect: Sample-flow and attrition audit from existing data

The source study reports that 6,086 raw respondents were reduced to 4,547 after filters and further to 3,825 in the H1 model, but the reasons for these losses are never examined. If attrition is differential across the 33 arms—e.g., if the Perception gap video arm loses a disproportionate share of high-polarization respondents—the 2.3-point estimate could be an artifact of who remained rather than a treatment effect.

**Why this one.** Addresses the sample failure and U2 at no fielding cost.

*Answers the open reviewer question U2 (see Peer review).*

**Hypothesis.** Attrition from 6,086 to 3,825 is balanced across arms, and the Perception gap coefficient of −2.3 points (95% CI [−4.3, −0.4]) remains statistically distinguishable from zero under inverse-probability weighting for differential attrition.

**Design.** The unit of analysis is the individual respondent. The sample is the full set of 6,086 raw respondents (or 4,547 if only the filtered file is available), stratified by the 33 arms (32 interventions + 1 control). Exposure: Arm assignment (which of the 33 interventions the respondent was randomized to). Variation comes from the original randomization in the fielded experiment. Outcome: Two outcomes: (1) Affective polarization, measured as the post-treatment average thermometer score toward the out-party (the H1 outcome); (2) Support for undemocratic practices (the H2 outcome). Additionally, the attrition indicator itself is treated as an outcome in the balance tests: a binary flag for whether a respondent is present in the final H1 analysis sample (N=3,825) versus dropped at any stage.

**Identification.** Compare attrition rates and pre-treatment covariate means across arms. If attrition is independent of arm (i.e., the probability of being in the final sample does not depend on which intervention was received, conditional on passing filters), then the complete-case H1 estimate is unbiased. The audit tests this by (a) comparing attrition proportions across arms with a chi-square or logistic regression, and (b) comparing pre-treatment covariates (baseline polarization, partisanship, demographics) between those retained and those dropped, within each arm. If attrition is balanced, the original estimate stands; if not, the complete-case estimate is reinterpreted as a local effect on the retained subpopulation.

**Data.** The replication script and associated data files from the source study (available via the authors' OSF or GitHub repository, or by direct request to the lead author). Specifically: the raw respondent-level dataset containing arm assignment, all filter flags (partisan self-ID, attention-check pass/fail, T33 chatbot exclusion flag), pre-treatment and post-treatment thermometer scores, and the undemocratic-practices scale.; The analysis script (R or Python) that produced the H1 and H2 models, which encodes the exact filter logic and missing-data handling used to arrive at N=3,825 and N=3,953.

**Analysis.** Step 1: Reconstruct the sample-flow table. For each of the 33 arms, tabulate: (a) raw N, (b) N after partisan filter, (c) N after T33 exclusion, (d) N with non-missing pre-treatment score, (e) N with non-missing post-treatment score (final H1 N). This yields a 33-row table with cumulative attrition at each stage. Step 2: Test balance in attrition. Fit a logistic regression: I(in final H1 sample) ~ arm + pre-treatment polarization + partisanship + age + gender + education. The arm coefficients test whether attrition differs by arm beyond what is explained by pre-treatment covariates. Report the maximum absolute standardized difference in attrition rates across arms. Step 3: Rerun H1 two ways. (i) Unweighted OLS: post-treatment polarization ~ arm dummies + pre-treatment polarization, using all 3,825 complete cases (this is the original estimate). (ii) Complete-case with attrition weights: inverse-probability weights where the propensity to be in the final sample is estimated from the logistic model in Step 2; re-estimate the arm effects with these weights. Step 4: Compare the Perception gap coefficient across the three specifications (original, unweighted complete-case, IPW-weighted). Pre-specified decision rule: if the IPW-weighted Perception gap coefficient's 95% CI includes zero, conclude the original estimate is not robust to differential attrition. If the coefficient shifts by more than 1.0 point between unweighted and IPW, flag the estimate as attrition-sensitive. Standard errors: cluster by arm (33 clusters) to account for the shared control group. Pre-specified tests: (1) the logistic attrition-balance test (Step 2), (2) the IPW-weighted Perception gap coefficient with its 95% CI (Step 4).

Files: [diagram](extensions/data_to_collect.svg) · [plain-text description](extensions/data_to_collect.txt)

#### Details: open items before fielding (data_to_collect)

- If the raw data file does not include the pre-filter 6,086 rows (only the 4,547 filtered), the audit cannot examine the partisan-filter stage and is limited to the 4,547-to-3,825 reduction.
- If the replication script applies filters sequentially without saving intermediate flags, it may be impossible to decompose attrition into its component stages (partisan filter, T33 exclusion, missing pre-treatment, missing post-treatment).
- With 33 arms and some arms having fewer than 100 respondents, the attrition balance tests will have low power to detect moderate differential attrition in small arms.
- The audit cannot rule out that attrition is driven by the treatment itself (e.g., a respondent who watched the Perception gap video dropped out because the video was unpleasant), which would be a post-randomization selection problem that no reweighting can fully fix.


<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on the journal site.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. (2026). Testing 33 Student-Designed Interventions to Reduce Affective Polarization [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/affective-polarization-interventions

```bibtex
@unpublished{velez2026affective,
  author = {Yamil Velez},
  title = {Testing 33 Student-Designed Interventions to Reduce Affective Polarization},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/affective-polarization-interventions},
  howpublished = {The File Drawer},
  url = {https://github.com/yrvelez/affective-polarization-interventions}
}
```

A `CITATION.cff` file with the same metadata sits at the root of the repository.

### Plan fidelity

Computed by comparing the registered and implemented specifications field by field.

| Analysis | Tag | Registered | Implemented | Justification |
|---|---|---|---|---|
| H1 | **unregistered** | as planned | as planned |  |
| H2 | **unregistered** | as planned | as planned |  |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H1 / outcomes.post_ap: "post_ap, affective polarization after treatment = in-party minus out-party feeling thermometer" -> Used the precomputed post_ap column (Derived column exists in the data)

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `CITATION.cff`
- `README.md`
- `RUN.md`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/data_to_collect.json`
- `extensions/data_to_collect.svg`
- `extensions/data_to_collect.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `extensions/theoretical_debate.json`
- `extensions/theoretical_debate.svg`
- `extensions/theoretical_debate.txt`
- `figures/E1_heterogeneity_partisan.png`
- `figures/E3_component_items.png`
- `figures/H1_arms.png`
- `figures/H2_arms.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/provenance.svg`
- `figures/badges/registration.svg`
- `figures/badges/release.svg`
- `figures/badges/review.svg`
- `figures/design.svg`
- `figures/design.txt`
- `figures/registered_effects.png`
- `filedrawer.config.yaml`
- `original/replication_script.R`
- `pap.json`
- `pap.md`
- `provenance/ctx_snapshot.json`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `results.prev/E1_party_heterogeneity.csv`
- `results.prev/E2_attention_check_robustness.csv`
- `results.prev/E3_placebo_pre_ap.csv`
- `results.prev/H1.csv`
- `results.prev/H1_arms.csv`
- `results.prev/H2.csv`
- `results.prev/H2_arms.csv`
- `results.prev/analysis_tags.csv`
- `results.prev/registered_summary.csv`
- `review.json`
- `review.md`
- `run.log`
- `run.sh`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/04_debug.py`
- `study.json`
- `survey.qsf`
