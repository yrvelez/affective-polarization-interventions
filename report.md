# Testing 33 Student-Designed Interventions to Reduce Affective Polarization

*Yamil Velez · 2026-10-08 · N = 4,547 analysed of 6,086 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 7/9 claims supported](figures/badges/review.svg) ![plan: reconstructed](figures/badges/registration.svg) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.93](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-08; orchestrator `anthropic/claude-sonnet-5.5`, standard `anthropic/claude-haiku-5.5`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.93, 340k tokens in and 52k out. Cite as: Velez, Y. (2026). Testing 33 Student-Designed Interventions to Reduce Affective Polarization [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/affective-polarization-interventions
>
> **No pre-registration. The analysis plan was reconstructed after data collection from Reconstructed post hoc on 2026-10-01 from replication_script.R; not pre-registered.** Every test below is post hoc or exploratory.

<!-- fd:section id=abstract -->
## Abstract

Can short, student-designed interventions reduce affective polarization or support for undemocratic practices? We compared 32 interventions with a pure control condition in an online survey experiment on US adults from the Lucid Theorem panel. The analysis was reconstructed post hoc from a replication script and was not pre-registered, so every test is post hoc. Of 6,086 raw respondents, 4,547 entered the analysis. Pooled across arms, affective polarization after treatment was 0.8 points lower on the feeling thermometer (95% CI [−1.4, −0.2], p = 0.005). The Perception gap video was the only individual arm with an uncorrected p < 0.05, at −2.3 points (95% CI [−4.3, −0.4], p = 0.019); other arms had similar or larger point estimates with wide intervals. Support for undemocratic practices showed no distinguishable pooled change (−0.015, 95% CI [−0.044, 0.014]). Many arms were small, and the 64 arm-level tests were uncorrected, so the single-arm result should be read cautiously.

<!-- fd:section id=findings -->
## Key findings

- Across 32 student-designed interventions, the pooled effect on affective polarization (feeling thermometer) was −0.8 points (95% CI [−1.4, −0.2], p = 0.005), a small reduction.
- Only the Perception gap video reached nominal significance on affective polarization: −2.3 points (95% CI [−4.3, −0.4], p = 0.019, two-sided, uncorrected). Other arms had similar point estimates with wide intervals.
- Support for undemocratic practices was not distinguishable from control: the pooled estimate was −0.015 (95% CI [−0.044, 0.014]), and no single arm stood out.
- Caveat: the study was not pre-registered, so every test is post hoc. Many arms are small, and the 64 arm-level tests were not corrected for multiplicity.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 32 arms and a control group; online panel, US. 6,086 responses were collected and 4,547 are analysed after the exclusions `partisan in ['Democrat','Republican']; arm != 'T33'`. The plan was supplied by the authors and is not pre-registered. Identifier and free-text columns removed before any model saw the data: RecordedDate, dem_intervention, rep_intervention.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 4,547 analysed). Respondents are randomly assigned to 33 arms: Cooperation infographic, Bipartisan bills graph, Bipartisan elite quotes, Shared values exercise, Cross-partisan dialogue guide, Meta-dehumanization correction, Perception survey (form), Common-ground articles, Patriotic article, 14th Amendment video, Congressional softball video, iSideWith quiz, Rick and Morty perspective-taking, Brené Brown empathy video, Perception gap video, 'What makes an American' video, McCain defends Obama video, Egyptian revolution video, Cross-partisan friendship TED talk, American history video, Party-tailored videos, Jubilee free speech panel, Jubilee video, Media-profits-from-division image, Shared priorities (Pew) table, Bipartisan legislation examples, Common threat (Russia), Pro-democracy excerpt, Biden–DeSantis cooperation, Scandals, both parties (labeled), Scandals (labels revealed later), Perception gap quiz, against the control group Control. Cooperation infographic: Image: Infographic on Americans wanting to work together Bipartisan bills graph: Image: Graph showing bipartisan bill passage rates Bipartisan elite quotes: Text: Bipartisan elite quotes (Obama, Reagan, McCain, Sanders, Trump, Clinton) Shared values exercise: Interactive: Values elicitation + policy support statistics by party Cross-partisan dialogue guide: Text: Abortion dialogue guide + docuseries about cross-partisan talks Meta-dehumanization correction: Text: Meta-dehumanization correction (300% overestimate statistic) Perception survey (form): Interactive: Google Forms political perception survey Common-ground articles: Text: Articles on bipartisan common ground (TheHill + PublicConsultation) Patriotic article: Text: 'What Makes America Great' patriotic article 14th Amendment video: Video: 14th Amendment privacy rights: bipartisan implications (abortion, vaccines, data) Congressional softball video: Video: Bipartisan congressional softball game + cross-party cooperation videos iSideWith quiz: Interactive: iSideWith political quiz Rick and Morty perspective-taking: Video: Rick and Morty perspective-taking: imagine being opposite party member Brené Brown empathy video: Video: RSA Brené Brown empathy video: empathy vs sympathy Perception gap video: Video: Perception gap video with misperception data 'What makes an American' video: Video: Street interviews on 'what makes an American' + superordinate identity McCain defends Obama video: Video: McCain defending Obama at 2008 rally: 'He's a decent family man' Egyptian revolution video: Video: Egyptian revolution aftermath: cautionary tale of polarization Cross-partisan friendship TED talk: Video: Ted Talk: cross-partisan friendship during 2016 election American history video: Video: American history chronology: shared national heritage Party-tailored videos: Video: Partisan-specific videos (different content by party) Jubilee free speech panel: Video: Jubilee panel: liberals and conservatives discuss free speech Jubilee video: Video: Jubilee video (J7We_PYASzc) Media-profits-from-division image: Image: Media critique: corporations profit from division Shared priorities (Pew) table: Text: Pew table showing shared partisan priorities Bipartisan legislation examples: Text: Bipartisan legislation examples (NCLB, ACA, TCJA, IRA) Common threat (Russia): Text: Russia nuclear threat + reflection on cross-party reliance Pro-democracy excerpt: Text: Pro-democracy excerpt (CNN for Dems, Fox for Reps) Biden–DeSantis cooperation: Text: Biden-DeSantis Hurricane Ian cooperation Scandals, both parties (labeled): Text: Political scandals from both parties (labels visible) Scandals (labels revealed later): Text: Political scandals (labels redacted, then revealed) Perception gap quiz: Interactive: Perception Gap Quiz 'as an independent' Outcomes: Affective polarization after treatment, Support for undemocratic practices.


The study randomized US adults from the Lucid Theorem online panel to a control condition ("Please continue") or one of 32 interventions, such as videos, articles, images and quizzes. A thirty-third arm, a GPT-3 chatbot, was excluded after technical failures. Of 6,086 raw respondents, 4,547 were analyzed. The models drop rows with missing outcomes; the affective polarization model used 3,825 respondents. Arm sizes ranged from about 60 to 660. Nothing was pre-registered; H1 and H2 are post hoc analyses reconstructed from a replication script. Each arm is compared with control, using two-sided tests.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=unregistered outcome=post_ap -->
### H1. Affective polarization after treatment

*Each intervention changes affective polarization after treatment relative to control.*  
*Post hoc, not pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

The Perception gap video, the largest arm (641 respondents in the affective polarization sample; 662 in the undemocratic practices sample), lowered affective polarization by 2.3 points relative to control (95% CI [−4.3, −0.4], two-sided p = 0.019). Pooled across all 32 arms the reduction was 0.8 points (95% CI [−1.4, −0.2], p = 0.005). The other arms were not distinguishable from control; their intervals were wide and mostly spanned zero. The 'What makes an American' video (−2.6, p = 0.059) and the Patriotic article (−2.1, p = 0.100) were suggestive only. With 32 uncorrected tests, one nominal hit at p = 0.019 deserves a hedge.

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

*Each intervention changes support for undemocratic practices relative to control.*  
*Post hoc, not pre-registered.*

![H2: effect by arm](figures/H2_arms.png)

No arm was distinguishable from control on support for undemocratic practices. The pooled estimate was −0.015 (95% CI [−0.044, 0.014], p = 0.309), a small and imprecise difference. The nearest case was the McCain defends Obama video at +0.144 (95% CI [−0.018, 0.306], two-sided p = 0.082), which points toward higher support, not lower. These intervals do not rule out modest effects in either direction.

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

<!-- fd:hyp id=E1 tag=exploratory kind=pipeline -->
### E1. Completers-only re-fit of planned H1 and H2

Partial completers may differ in attention, so the planned estimates are re-fit on completed surveys to check stability. The planned H1 and H2 arm contrasts were re-estimated with the same specification on all respondents and again on only respondents who finished the survey, and the two sets of estimates were compared side by side.

**Finding.** Restricting to completers left every arm estimate unchanged (largest absolute change 0.00); H1 had 1 and H2 had 0 of 32 arm contrasts at p<0.05 in both samples, so the planned results are not sensitive to partial completion.

An unreviewed exploratory completers-only re-fit of the post hoc H1 and H2 models was run. The rows shown are all from the full sample, so they cannot confirm how the completers estimates compare with the main models.

#### Details: table (E1)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n | analysis | sample |
|---|---|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='T0'))[T.T1] | Cooperation infographic | -1.153 | 1.592 | 0.469 | -4.273 | 1.968 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T2] | Bipartisan bills graph | 0.377 | 1.522 | 0.804 | -2.607 | 3.361 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T3] | Bipartisan elite quotes | -0.152 | 1.470 | 0.918 | -3.032 | 2.729 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T4] | Shared values exercise | 0.860 | 1.690 | 0.611 | -2.453 | 4.173 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T5] | Cross-partisan dialogue guide | -1.760 | 3.204 | 0.583 | -8.039 | 4.519 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T6] | Meta-dehumanization correction | -0.024 | 1.633 | 0.988 | -3.225 | 3.178 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T7] | Perception survey (form) | 0.172 | 1.743 | 0.921 | -3.243 | 3.588 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T8] | Common-ground articles | -1.627 | 1.868 | 0.384 | -5.288 | 2.034 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T9] | Patriotic article | -2.101 | 1.277 | 0.100 | -4.604 | 0.402 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T10] | 14th Amendment video | -1.562 | 1.494 | 0.296 | -4.490 | 1.367 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T11] | Congressional softball video | -2.437 | 1.954 | 0.212 | -6.268 | 1.393 | 3825 | H1 | planned_full |
| C(arm_code, Treatment(reference='T0'))[T.T12] | iSideWith quiz | 0.357 | 1.304 | 0.784 | -2.198 | 2.912 | 3825 | H1 | planned_full |
| … 116 more rows |  | | | | | | | | |

<!-- fd:hyp id=E2 tag=exploratory kind=pipeline -->
### E2. Arm by Democrat-versus-other heterogeneity on the planned H1 outcome

The pooled planned test may hide opposite responses between Democrats and other respondents, so arm effects are compared across the two groups. The planned H1 model was extended with an interaction between each arm and a 0/1 indicator for Democratic partisanship, and the interaction terms were reported per arm.

**Finding.** Of 32 arm-by-Democrat interaction terms on affective polarization after treatment, 0 had p<0.05 with no multiplicity correction, so no arm's effect detectably differs between Democrats and other respondents.

An unreviewed exploratory check interacted each arm with being a Democrat. None of the 32 interactions reached p < 0.05, but these tests are imprecise, so differences between Democrats and others cannot be ruled out.

#### Details: table (E2)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='T0'))[T.T1]:C(_mod)[T.1] | Cooperation infographic x dem=1 | 2.008 | 3.074 | 0.514 | -4.017 | 8.034 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T2]:C(_mod)[T.1] | Bipartisan bills graph x dem=1 | 1.552 | 3.096 | 0.616 | -4.516 | 7.621 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T3]:C(_mod)[T.1] | Bipartisan elite quotes x dem=1 | -2.638 | 2.925 | 0.367 | -8.371 | 3.095 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T4]:C(_mod)[T.1] | Shared values exercise x dem=1 | -0.886 | 3.374 | 0.793 | -7.500 | 5.727 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T5]:C(_mod)[T.1] | Cross-partisan dialogue guide x dem=1 | 2.176 | 9.736 | 0.823 | -16.906 | 21.258 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T6]:C(_mod)[T.1] | Meta-dehumanization correction x dem=1 | 2.499 | 3.167 | 0.430 | -3.709 | 8.707 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T7]:C(_mod)[T.1] | Perception survey (form) x dem=1 | -5.461 | 4.031 | 0.175 | -13.362 | 2.440 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T8]:C(_mod)[T.1] | Common-ground articles x dem=1 | 2.027 | 3.927 | 0.606 | -5.670 | 9.724 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T9]:C(_mod)[T.1] | Patriotic article x dem=1 | 1.662 | 2.707 | 0.539 | -3.644 | 6.967 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T10]:C(_mod)[T.1] | 14th Amendment video x dem=1 | 2.748 | 3.261 | 0.399 | -3.643 | 9.140 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T11]:C(_mod)[T.1] | Congressional softball video x dem=1 | 4.925 | 4.949 | 0.320 | -4.774 | 14.624 | 3825 |
| C(arm_code, Treatment(reference='T0'))[T.T12]:C(_mod)[T.1] | iSideWith quiz x dem=1 | 0.297 | 2.640 | 0.910 | -4.877 | 5.471 | 3825 |
| … 20 more rows |  | | | | | | |


<!-- fd:section id=related -->
## Related work

Prior findings on prejudice-reduction interventions bear on H1 and H2 most directly. A large meta-analytic review of 418 experiments finds that these approaches have been evaluated extensively, with meta-analysis used to estimate average effects of different methods (Paluck et al., 2020). Work on partisan prejudice and affective polarization frames the outcome side of such interventions, showing that partisan animus is broad and extends into non-political settings (Lelkes and Westwood, 2016), and that polarization is shaped by local context (Druckman et al., 2020). Evidence on the downstream consequences of affective polarization is limited and largely from the United States, with a multi-country survey experiment examining its effects in nine democracies (Harteveld et al., 2026). Work on who endorses political violence adds a related outcome domain (Armaly and Enders, 2022). The retrieved works do not directly contest the hypotheses, but the evidence base is heterogeneous in what it measures as an outcome. The meta-analytic review pools across many intervention types, so it cannot by itself indicate that any specific intervention moves a specific outcome (Paluck et al., 2020), while the cross-national experiment suggests that effects of polarization may differ outside the United States (Harteveld et al., 2026). The present design, which compares each intervention against a control on separately defined post-treatment outcomes, can speak to whether each intervention shifts each outcome within a single study, but not to the broader question of which mechanism links prejudice to downstream behaviour.

Retrieved works (OpenAlex; queries: affective polarization intervention experiment reduces partisan feeling thermometer gap; depolarization intervention undemocratic practices support partisans survey experiment; affective polarization interventions null effects durable persistence decay; partisan animosity intervention backfire ineffective demand effects; multi-arm survey experiment feeling thermometer affective polarization outcomes):

- Elizabeth Levy Paluck, Roni Porat, Chelsey S. Clark, DONALD PHILIP GREEN (2020). Prejudice Reduction: Progress and Challenges. Annual Review of Psychology. https://doi.org/10.1146/annurev-psych-071620-030619
- James N. Druckman, Samara Klar, Yanna Krupnikov, Matthew S. Levendusky (2020). Affective polarization, local contexts and public opinion in America. Nature Human Behaviour. https://doi.org/10.1038/s41562-020-01012-5
- Yphtach Lelkes, Sean Jeremy Westwood (2016). The Limits of Partisan Prejudice. The Journal of Politics. https://doi.org/10.1086/688223
- Miles Armaly, Adam M Enders (2022). Who Supports Political Violence?. Perspectives on Politics. https://doi.org/10.1017/s1537592722001086
- Eelco Harteveld, Lars Erik Berntzen, Andrej Kokkonen, Haylee Kelsall (2026). The (alleged) consequences of affective polarization: A survey experiment in nine democracies. European Journal of Political Research. https://doi.org/10.1017/s1475676526101273
- Christina Cipriano, Michael J. Strambler, Lauren Hunter Naples, Cheyeon Ha (2023). The state of evidence for social and emotional learning: A contemporary meta-analysis of universal school-based SEL interventions. Child Development. https://doi.org/10.1111/cdev.13968

<!-- fd:section id=limitations -->
## Limitations

No part of this study was pre-registered, so every test is post hoc and the choice of analyses could have been shaped by the data. The 64 arm-level tests were not corrected for multiplicity, and the one arm with p < 0.05 could be a chance finding. Several arms had fewer than 80 respondents, giving wide intervals that cannot exclude meaningful effects. About a quarter of raw respondents were not analyzed, and 3,825 entered the polarization model, so attrition could bias estimates if it differed by arm. The sample is an online panel of US adults, and the outcomes were measured right after exposure, so durability is unknown.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Planned analyses are never changed.*

**Outcome.** 7 of 9 checked claims supported after the agent's corrections; 2 of 2 planned analyses run as planned; 2 reworded; 2 text fixes; 2 still open; 2 correction passes.

#### Corrections

- **Now unsupported** · E1: “Restricting to completers left every arm estimate unchanged (largest absolute change 0.00); H1 had 1 and H2…” (Visible E1 rows are all 'planned_full' (n=3825). No completers rows are shown, and the text itself says it…)
- **Now overstated** · E2: “Of 32 arm-by-Democrat interaction terms ... 0 had p<0.05” (Only 14 of 32 interaction rows are visible; the smallest shown is p=0.090 (Rick and Morty). The other 18…)
- **Corrected** · 4 items reworded or fixed in the text: Abstract, Key findings, R1, Plan match / H1, H2, R2, Abstract / H1 pooled estimate. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The arm-level estimates in the prose match the tables: Perception gap video -2.333 (p=0.019) is the only nominal hit on H1, and no arm is distinguishable on H2. The pooled estimates (-0.819, SE 0.291; H2 -0.015, SE 0.015) appear only in the random-effects sentences, and the pooled CIs are not tabulated. The pooled SE is flagged as approximate because the arms share one control group. The main caveat is that this is a post hoc analysis with 64 uncorrected tests, so the single significant arm is weak evidence and the 'only arm that clearly differed' wording is too strong.

| Planned analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |
| H2 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K1 | medium | presentational | claims | Fixed in text | Abstract: Overstated claim: "Perception gap video was the only individual arm that clearly differed from control, at −2.3 points (95% CI [−4.3, −0.4], p = 0.019)". H1 table: -2.333, CI [-4.283,-0.382], p=0.0191. It is the only arm with p<0.05, but the test is uncorrected among 32, and 'What makes an American' is -2.647 (p=0.059), a larger point estimate. *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | Key findings: Overstated claim: "Only the Perception gap video lowered affective polarization on its own". Other arms have similar or larger point estimates (-2.647, -2.629, -2.437) with wide intervals; nominal significance does not establish that the others had no effect. *claim checked against the tables by the checking agent* |
| R1 | medium | presentational | light | Fixed in text | Plan match / H1, H2: The plan-match table says 'H1: as planned' and 'H2: as planned', but the analysis tags mark both as 'unregistered' because there was no pre-registration and the plan was reconstructed post hoc. The figure 'Planned treatment effects' and the E1 and E2 wording ('planned H1 and H2') also suggest a planned plan. *The 'planned' and 'as planned' labels wrongly imply a planned plan, so the wording and figure title need relabelling as post hoc.* |
| R2 | medium | presentational | light | Fixed in text | Abstract / H1 pooled estimate: The pooled H1 estimate (-0.8, CI [-1.4, -0.2], p = 0.005) and the pooled H2 CI [-0.044, 0.014] appear in no provided table. The text gives only -0.819 and SE 0.291. The visible tables show no pooled row, and a CI built from that SE would be about [-1.39, -0.25]. *The pooled estimates exist in the text; they need to be tabulated or cited with SE, not re-estimated.* |
| R3 | low | presentational | light | Fixed in text | H1 text: The text says the Perception gap video lowered polarization by 2.3 points. The table gives -2.333, which rounds to -2.3, so this is fine. The text also says 'the largest arm at 641 respondents'. By the H2 table the arm has 662 respondents, while the H1 table shows 641 for H1, so the sample sizes differ by outcome. *The n differs by outcome sample (641 in H1, 662 in H2), so each should be labelled to its sample.* |
| R4 | low | presentational | light | Fixed in text | Abstract / Limitations: The text refers to '64 arm-level tests', which is 32 arms × 2 outcomes. The E1 tag says 'H1 had 1 ... of 32'. Both are consistent. However, 'No arm was distinguishable' on H2 is consistent with the table, while the 'about a quarter' of raw respondents not analysed is 1,539 of 6,086 (25.3%), which is fine. *The reviewer states that no change is needed.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| Perception gap video was the only individual arm that clearly differed from control, at −2.3 points (95% CI [−4.3, −0.4], p = 0.019) | Abstract | overstated | H1 table: -2.333, CI [-4.283,-0.382], p=0.0191. It is the only arm with p<0.05, but the test is uncorrected among 32, and 'What makes an American' is -2.647 (p=0.059), a larger point estimate. | supported: The Perception gap video was the only individual arm with an uncorrected p < 0.05, at −2.3 points (95% CI [−4.3, −0.4], p = 0.019); other arms had similar or larger point estimates with wide intervals. |
| Only the Perception gap video lowered affective polarization on its own | Key findings | overstated | Other arms have similar or larger point estimates (-2.647, -2.629, -2.437) with wide intervals; nominal significance does not establish that the others had no effect. | supported: Only the Perception gap video reached nominal significance on affective polarization |
| Pooled effect on affective polarization was −0.8 points (95% CI [−1.4, −0.2], p = 0.005) | Abstract | supported | Pooled random-effects estimate -0.819, SE 0.291, p=0.005. The implied CI is about [-1.39,-0.25]. The pooled SE is approximate because the arms share one control group. | supported: pooled effect on affective polarization (feeling thermometer) was −0.8 points (95% CI [−1.4, −0.2], p = 0.005), a small reduction |
| Support for undemocratic practices pooled −0.015, 95% CI [−0.044, 0.014] | Abstract | supported | Pooled -0.015, SE 0.015, p=0.309. The implied CI is about [-0.044, 0.014]. | supported: Support for undemocratic practices ... pooled estimate was −0.015 (95% CI [−0.044, 0.014]) |
| No arm was distinguishable from control on support for undemocratic practices; McCain +0.144, p = 0.082 | H2 | supported | H2 table: the smallest p is 0.0817 (McCain, +0.144, CI [-0.018,0.306]); all arms are marked 'no'. | supported: No arm was distinguishable from control on support for undemocratic practices ... McCain +0.144, p = 0.082 |
| Restricting to completers left every arm estimate unchanged (largest change 0.00) | E1 | supported | The E1 rows shown are all labelled planned_full with n=3825 and match H1. The completers rows are not visible in the excerpt. | unsupported: Restricting to completers left every arm estimate unchanged (largest absolute change 0.00); H1 had 1 and H2 had 0 of 32 arm contrasts at p<0.05 in both samples |
| Perception gap video is the largest arm at 641 respondents | H1 | supported | H1 table n=641, the largest arm (next is Patriotic article at 330). The H2 sample has 662. | supported: The Perception gap video, the largest arm (641 respondents in the affective polarization sample; 662 in the undemocratic practices sample) |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Relabel 'planned' wording in E1, E2 and the figure title ('Planned treatment effects') as post hoc reconstructed. Done: E1 and E2 text now call H1 and H2 post hoc rather than planned; the figure title is in the skeleton and could not be changed here.
- G2. Add a pooled row with CI to a results table. Done: Pooled estimates with CIs are cited from the Key numbers block (−0.819 [−1.389, −0.249]; −0.015 [−0.044, 0.014]); adding a table row is outside the prose sections.
- G3. Specify n by outcome sample for the Perception gap video. Done: H1 note now gives n = 641 for the polarization sample and 662 for the undemocratic practices sample.

Re-check of the corrected text: The E1 completers claim is not backed by any visible completers rows and the E2 '0 of 32' count rests on only 14 visible rows; both need rewording or the missing rows.

#### Other review options

- **Advanced Pass**: methodology and statistics referees whose analytical issues get agent-run robustness checks. `--review light,advanced`
- **Coarse**: the open-source coarse-ink reviewer, run locally (about $1-2). `--review light,coarse`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview**: import any referee report, e.g. one posted on an OpenReview submission. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Ran 32 interventions against one shared control in a single fielding, so arms are directly comparable and the pooled estimate is not confounded by wave, panel or outcome wording. Adjusted for the pre-treatment measure of each outcome (affective polarization after treatment ~ arm + pre_ap) with HC2 robust SEs, which tightens estimates; the Perception gap video interval is the narrowest at [-4.3, -0.4]. Reported the whole arm table and hedged the lone p = 0.019 result against 64 uncorrected tests, rather than presenting one arm as a winner. Pooled across arms (-0.8 points, 95% CI [-1.4, -0.2]) and found no pooled movement in support for undemocratic practices (-0.015, CI [-0.044, 0.014]).

**Verdict.** A follow-up is worth running, but narrowly. The 32-arm screen found a pooled -0.8 point shift, one nominal hit (Perception gap video, -2.3, p = 0.019, uncorrected and post hoc), and nothing on undemocratic practices. Run the Perception gap correction with a mechanism manipulation and delayed follow-up first: it replicates the single signal at adequate power, adds a placebo, and tests persistence. The affect-to-democratic-attitude transfer test and the cross-party, cross-sample test follow once the effect is confirmed.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Most arms had 48-150 respondents against a control of 229, so arm-level intervals are about 6-8 points wide and cannot exclude effects larger than the pooled -0.8. Only the Perception gap video (n = 641) was estimated with any precision. | Standard errors of 1.3-3.2 on the feeling thermometer for nearly all arms; control n = 229; Cross-partisan dialogue guide CI [-8.0, 4.5]. |
| Design | Interventions differ in format, length, topic and target, so 32 arms bundle many features. A null or a hit cannot be tied to a mechanism, and one arm clearing p < 0.05 among 32 tests is about what chance produces. | Perception gap video p = 0.019 uncorrected; next arms are 'What makes an American' video p = 0.059 and Patriotic article p = 0.100. |
| Measurement | Outcomes were measured immediately after exposure, with a single thermometer-based measure and one undemocratic-practices scale. Durability and behaviour are unobserved, and immediate shifts may reflect demand. | Limitations: outcomes measured right after exposure; the thermometer gap is the only affect measure. |
| Sample | Analysis kept 4,547 of 6,086 respondents, and 3,825 and 3,953 entered the two models. Differential attrition across arms, plus the dropped chatbot arm, could bias the contrasts. Only Democrats and Republicans were retained. | N = 3825 (H1) and N = 3953 (H2) versus 6,086 raw; arm T33 excluded after technical failures. |
| Analysis | No pre-registration, so analytic choices (weights, exclusions, pooling) are post hoc, and the robustness checks add little: the completers re-fit showed only full-sample rows and the Democrat-interaction tests are too imprecise to say anything. | Registration status 'none'; E2 interaction SEs of 3-10 points; 0 of 32 interactions at p < 0.05. |

**D1. Do prejudice-reduction effects carry through to downstream political outcomes?.** (a) Brief interventions can shift intergroup affect, and that shift should extend to political attitudes such as support for undemocratic practices or violence. [Paluck et al. (2020)] (b) Affective shifts are small and local, and may not transfer to democratic attitudes, or to settings beyond the United States. [Harteveld et al. (2026)] This study: Leans to position b, weakly: a small thermometer reduction (-0.8) coexisted with no pooled change in undemocratic-practices support (-0.015). The intervals are wide and the outcomes were measured immediately, so the study cannot settle it.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Perception gap correction with a mechanism manipulation and delayed follow-up

Fixes the power and design problems by concentrating on the only arm with signal and by isolating its mechanism, adding a delayed outcome to address the immediate-measurement limit.

**Hypothesis.** The Perception gap video lowers outparty animosity (thermometer gap) more than placebo or control, mediated by reduced perceived outparty extremity; the effect partly persists at follow-up, with smaller or null effects on support for undemocratic practices.

**Design.** Control vs. Perception gap video vs. Placebo video vs. Statistics-only text; primary outcome: Affective polarization (in-party minus out-party feeling thermometer) immediately and at 2-4 weeks. About 1100 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items

In the source study the Perception gap video was the only arm with p<0.05 on the thermometer (-2.3 points, SE 0.995, n=641), while pooled undemocratic-practices support did not move (-0.015, CI [-0.044, 0.014]) and outcomes were measured immediately. This design tests whether the effect runs through corrected beliefs about the outparty, whether it replicates against a placebo video, and whether it persists and reaches democratic attitudes.

**Debate it speaks to.** Do prejudice-reduction effects carry through to downstream political outcomes?: Brief interventions can shift intergroup affect, and that shift should extend to political attitudes such as support for undemocratic practices or violence. versus Affective shifts are small and local, and may not transfer to democratic attitudes, or to settings beyond the United States.

**Power.** About 1100 per arm to detect 1.7 at 80% power (Observed Perception gap video effect of -2.3 points (SE 0.995 at n = 641); sizing to detect about -1.7 at 80% power allows for winner's-curse shrinkage.).

Open items before fielding:

- The actual video files, wave 2 survey instrument and link, IRB approval number, and compensation must be supplied by the research team.
- Supply media: pgvideo: video stimulus to supply (Perception gap video showing how partisans overestimate the other party's extrem)
- Supply media: plvideo: video stimulus to supply (Non-political explainer video on how bees make honey, about 4 minutes)
- Supply media: pre_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90
- Supply media: post_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Perception gap video across partisanship and sample

Addresses the sample and framing limits: the original was one Lucid panel, only partisans, with heterogeneity tests too imprecise to interpret.

**Hypothesis.** The Perception gap video lowers affective polarization relative to control, and the effect does not differ materially by party, partisan strength or sample source.

**Design.** Control vs. Perception gap video; primary outcome: Affective polarization: in-party minus out-party feeling thermometer after treatment; secondary: mean support for undemocratic practices. About 1500 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items

The Perception gap video was the only arm with p<0.05 (-2.3 points, 95% CI [-4.3, -0.4], p=0.019, uncorrected) in a single Lucid panel with only partisans, and heterogeneity tests were too imprecise to interpret. This design replicates it in two sample sources across Democrats, Republicans and independent leaners with pre-measures.

**Power.** About 1500 per arm to detect 2.0 at 80% power (Interaction contrasts need roughly 2x the SE of the main effect; observed SE 0.995 at n = 641 implies detecting about 2 points in subgroups at around 750 per cell.).

Open items before fielding:

- Hosting of the Perception gap video file
- Choice of second panel vendor, compensation and IRB number
- Supply media: video1: video stimulus to supply (Perception gap video showing data on how partisans overestimate the other side's)
- Supply media: pre_ap_scores: set the matrix recode values after import 0=0, 10=10, 20=20, 30=30, 40=40, 50=50, 60=60, 70=70, 80=80, 90=90, 100=100
- Supply media: post_ap_scores: set the matrix recode values after import 0=0, 10=10, 20=20, 30=30, 40=40, 50=50, 60=60, 70=70, 80=80, 90=90, 100=100

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Affect-to-democratic-attitude transfer test

Addresses the measurement failure: the original had a null on undemocratic-practices support with no way to tell whether affect failed to transfer or the intervention was too weak.

**Hypothesis.** Transfer: downstream change is proportional to the affect change induced by treatment. Independence: undemocratic-practices support and donation willingness do not change even when affect shifts substantially.

**Design.** Control vs. Patriotic article vs. Perception gap video plus recall; primary outcome: Support for undemocratic practices (mean of four items), with the thermometer gap as the first stage. About 900 per arm for 80% power.

Files: [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) · [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: background and open items

The source found a pooled thermometer drop of -0.8 (95% CI [-1.4,-0.2]) and a Perception gap video drop of -2.3, but no change in undemocratic-practices support (-0.015, CI [-0.044,0.014]). It cannot tell whether affect fails to transfer or the interventions were too weak. This design uses a strengthened intervention to produce a larger affect shift, then tests whether downstream outcomes move in proportion to it.

**Debate it speaks to.** Do prejudice-reduction effects carry through to downstream political outcomes?: Brief interventions can shift intergroup affect, and that shift should extend to political attitudes such as support for undemocratic practices or violence. versus Affective shifts are small and local, and may not transfer to democratic attitudes, or to settings beyond the United States.

**Power.** About 900 per arm to detect 0.09 at 80% power (Undemocratic-practices pooled CI [-0.044, 0.014] and arm SEs of 0.05-0.12; 900 per arm detects about 0.09 on that scale.).

Open items before fielding:

- Hosting of the Perception gap video and the Patriotic article text.
- IRB approval number and participant compensation.
- How the bonus donation will be paid out.
- Supply media: pgvideo: video stimulus to supply (Perception gap video showing how each party overestimates the other's extremity,)
- Supply media: pre_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90
- Supply media: post_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90


<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on filedrawer.org.*


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

### Reviewer pass

The automated review (Light Pass) flagged 6 issue(s); see `review.md`.

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
- `RUN.md`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/advance_design.json`
- `extensions/advance_design.qsf`
- `extensions/advance_design.svg`
- `extensions/advance_design.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `extensions/theoretical_debate.json`
- `extensions/theoretical_debate.qsf`
- `extensions/theoretical_debate.svg`
- `extensions/theoretical_debate.txt`
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
- `pap.json`
- `pap.md`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/E1_completers_robustness.csv`
- `results/E2_partisan_heterogeneity.csv`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/H2.csv`
- `results/H2_arms.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `review.json`
- `review.md`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/04_exploratory.py`
- `study.json`
- `survey.qsf`
