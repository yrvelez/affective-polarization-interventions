# Testing 33 Student-Designed Interventions to Reduce Affective Polarization

*Yamil Velez · 2026-10-09 · N = 4,485 analysed of 6,086 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 2 corrected · 12/12 claims supported](figures/badges/review.svg) [![plan: pre-registered](figures/badges/registration.svg)](https://osf.io/k2nwj) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $1.04](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-09; orchestrator `anthropic/claude-sonnet-5.5`, standard `anthropic/claude-haiku-5.5`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $1.04, 354k tokens in and 52k out. Cite as: Velez, Y. (2026). Testing 33 Student-Designed Interventions to Reduce Affective Polarization [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/affective-polarization-interventions

<!-- fd:section id=abstract -->
## Abstract

Can brief, student-designed interventions reduce affective polarization? We tested 32 interventions against a pure control in a registered survey experiment on US adults from the Lucid Theorem online panel (6,086 recruited, 4,485 analysed). The primary outcome was affective polarization, measured with feeling thermometers, and the secondary outcome was support for undemocratic practices. The Perception gap video (641 respondents for the primary outcome, 646 for the secondary) lowered affective polarization by 2.3 points relative to control (95% CI [−4.3, −0.4], p = 0.021). The McCain defends Obama video raised support for undemocratic practices by 0.17 scale points (95% CI [0.02, 0.33], p = 0.032). All other interventions were not distinguishable from control on either outcome, and their wide intervals leave modest effects possible. Because 64 tests were run without correction for multiple comparisons, many arms were small, and both significant results are near the threshold, they should be read cautiously and need replication.

<!-- fd:section id=findings -->
## Key findings

- In this registered experiment, only one of 32 interventions, the Perception gap video, lowered affective polarization relative to control: −2.3 points on the thermometer scale (95% CI [−4.3, −0.4]).
- The McCain defends Obama video raised support for undemocratic practices by 0.17 scale points (95% CI [0.02, 0.33], p = 0.032), the only registered arm with a detectable shift on that outcome.
- The other arms were not distinguishable from control on either affective polarization or support for undemocratic practices; their intervals are wide and do not rule out modest effects.
- Exploratory checks are unreviewed: the completers refit used the same respondents and tests nothing new, and no subgroup interaction by party or political interest was significant.
- Caveat: 64 uncorrected tests with small arms mean the two significant results sit near the threshold and may be chance.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 32 arms and a control group; online panel, US. 6,086 responses were collected and 4,485 are analysed after the exclusions `screener_pass == 1; partisan in ['Democrat','Republican']; arm != 'T33'`. The plan is pre-registered at https://osf.io/k2nwj. Identifier and free-text columns removed before any model saw the data: RecordedDate, dem_intervention, rep_intervention.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 4,485 analysed). Respondents are randomly assigned to 33 arms: Cooperation infographic, Bipartisan bills graph, Bipartisan elite quotes, Shared values exercise, Cross-partisan dialogue guide, Meta-dehumanization correction, Perception survey (form), Common-ground articles, Patriotic article, 14th Amendment video, Congressional softball video, iSideWith quiz, Rick and Morty perspective-taking, Brené Brown empathy video, Perception gap video, 'What makes an American' video, McCain defends Obama video, Egyptian revolution video, Cross-partisan friendship TED talk, American history video, Party-tailored videos, Jubilee free speech panel, Jubilee video, Media-profits-from-division image, Shared priorities (Pew) table, Bipartisan legislation examples, Common threat (Russia), Pro-democracy excerpt, Biden–DeSantis cooperation, Scandals, both parties (labeled), Scandals (labels revealed later), Perception gap quiz, against the control group Control. Cooperation infographic: Image: Infographic on Americans wanting to work together Bipartisan bills graph: Image: Graph showing bipartisan bill passage rates Bipartisan elite quotes: Text: Bipartisan elite quotes (Obama, Reagan, McCain, Sanders, Trump, Clinton) Shared values exercise: Interactive: Values elicitation + policy support statistics by party Cross-partisan dialogue guide: Text: Abortion dialogue guide + docuseries about cross-partisan talks Meta-dehumanization correction: Text: Meta-dehumanization correction (300% overestimate statistic) Perception survey (form): Interactive: Google Forms political perception survey Common-ground articles: Text: Articles on bipartisan common ground (TheHill + PublicConsultation) Patriotic article: Text: 'What Makes America Great' patriotic article 14th Amendment video: Video: 14th Amendment privacy rights: bipartisan implications (abortion, vaccines, data) Congressional softball video: Video: Bipartisan congressional softball game + cross-party cooperation videos iSideWith quiz: Interactive: iSideWith political quiz Rick and Morty perspective-taking: Video: Rick and Morty perspective-taking: imagine being opposite party member Brené Brown empathy video: Video: RSA Brené Brown empathy video: empathy vs sympathy Perception gap video: Video: Perception gap video with misperception data 'What makes an American' video: Video: Street interviews on 'what makes an American' + superordinate identity McCain defends Obama video: Video: McCain defending Obama at 2008 rally: 'He's a decent family man' Egyptian revolution video: Video: Egyptian revolution aftermath: cautionary tale of polarization Cross-partisan friendship TED talk: Video: Ted Talk: cross-partisan friendship during 2016 election American history video: Video: American history chronology: shared national heritage Party-tailored videos: Video: Partisan-specific videos (different content by party) Jubilee free speech panel: Video: Jubilee panel: liberals and conservatives discuss free speech Jubilee video: Video: Jubilee video (J7We_PYASzc) Media-profits-from-division image: Image: Media critique: corporations profit from division Shared priorities (Pew) table: Text: Pew table showing shared partisan priorities Bipartisan legislation examples: Text: Bipartisan legislation examples (NCLB, ACA, TCJA, IRA) Common threat (Russia): Text: Russia nuclear threat + reflection on cross-party reliance Pro-democracy excerpt: Text: Pro-democracy excerpt (CNN for Dems, Fox for Reps) Biden–DeSantis cooperation: Text: Biden-DeSantis Hurricane Ian cooperation Scandals, both parties (labeled): Text: Political scandals from both parties (labels visible) Scandals (labels revealed later): Text: Political scandals (labels redacted, then revealed) Perception gap quiz: Interactive: Perception Gap Quiz 'as an independent' Outcomes: Affective polarization after treatment, Support for undemocratic practices.


The study was registered on OSF (k2nwj) in November 2022, before the adaptive batches were analysed. Respondents were US adults from the Lucid Theorem online panel. Each of 32 interventions was compared with a pure control that simply said 'Please continue'. The GPT-3 chatbot arm was excluded because of technical failures. Of 6,086 raw responses, 4,485 entered the analysis; the models for affective polarization used 3,772 respondents. The control group had 229 respondents for affective polarization and 234 for support for undemocratic practices. Treatment arms ranged from 56 to 330 people, apart from the Perception gap video at 641 and 646.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=registered outcome=post_ap -->
### H1. Affective polarization after treatment

*Primary (registered): the effect of each intervention (1-32) on affective polarization, relative to the pure control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

The Perception gap video was the one intervention that lowered affective polarization, by 2.3 points on the thermometer scale (95% CI [−4.3, −0.4], two-sided p = 0.021). Control respondents averaged 41.5 and the video group 39.6. All 31 other arms had intervals that included zero, with estimates from −2.38 to +1.36 points. The 'What makes an American' video came closest (−2.4 points, 95% CI [−5.1, 0.4]). Given 32 uncorrected comparisons, the single significant result deserves a hedge.

#### Details: model and estimates by arm (H1)

```
post_ap ~ C(arm_code, Treatment(reference='T0')) + pre_ap + pre_udp
OLS | weights = ipw_weight | HC2 robust SEs | N = 3772 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Cooperation infographic | -0.947 | 1.589 | 0.5512 | [-4.061, 2.167] | 89 | no |
| Bipartisan bills graph | 0.377 | 1.537 | 0.8060 | [-2.636, 3.391] | 105 | no |
| Bipartisan elite quotes | -0.789 | 1.340 | 0.5561 | [-3.414, 1.837] | 93 | no |
| Shared values exercise | 0.799 | 1.699 | 0.6383 | [-2.532, 4.129] | 77 | no |
| Cross-partisan dialogue guide | -1.020 | 3.251 | 0.7538 | [-7.392, 5.353] | 65 | no |
| Meta-dehumanization correction | 0.098 | 1.644 | 0.9524 | [-3.123, 3.319] | 220 | no |
| Perception survey (form) | 0.384 | 1.768 | 0.8280 | [-3.081, 3.849] | 83 | no |
| Common-ground articles | -1.586 | 1.865 | 0.3950 | [-5.241, 2.069] | 67 | no |
| Patriotic article | -1.959 | 1.272 | 0.1234 | [-4.452, 0.533] | 328 | no |
| 14th Amendment video | -1.751 | 1.510 | 0.2461 | [-4.710, 1.208] | 60 | no |
| Congressional softball video | -1.215 | 1.496 | 0.4166 | [-4.147, 1.717] | 63 | no |
| iSideWith quiz | 0.383 | 1.333 | 0.7737 | [-2.229, 2.995] | 62 | no |
| Rick and Morty perspective-taking | -0.887 | 1.585 | 0.5757 | [-3.993, 2.219] | 56 | no |
| Brené Brown empathy video | -2.137 | 1.592 | 0.1795 | [-5.259, 0.984] | 163 | no |
| Perception gap video | -2.307 | 0.997 | 0.0207 | [-4.262, -0.353] | 641 | yes |
| 'What makes an American' video | -2.382 | 1.402 | 0.0893 | [-5.130, 0.366] | 148 | no |
| McCain defends Obama video | -0.852 | 2.646 | 0.7476 | [-6.038, 4.335] | 86 | no |
| Egyptian revolution video | 0.342 | 2.468 | 0.8898 | [-4.495, 5.179] | 71 | no |
| Cross-partisan friendship TED talk | 0.952 | 2.040 | 0.6406 | [-3.046, 4.950] | 68 | no |
| American history video | 1.355 | 2.283 | 0.5528 | [-3.120, 5.831] | 66 | no |
| Party-tailored videos | 1.113 | 1.640 | 0.4976 | [-2.103, 4.328] | 68 | no |
| Jubilee free speech panel | -1.747 | 2.119 | 0.4096 | [-5.900, 2.406] | 48 | no |
| Jubilee video | 0.163 | 2.069 | 0.9374 | [-3.893, 4.218] | 121 | no |
| Media-profits-from-division image | -1.464 | 1.909 | 0.4433 | [-5.206, 2.279] | 96 | no |
| Shared priorities (Pew) table | -0.114 | 1.489 | 0.9391 | [-3.031, 2.804] | 63 | no |
| Bipartisan legislation examples | 0.969 | 1.749 | 0.5795 | [-2.459, 4.397] | 66 | no |
| Common threat (Russia) | -0.893 | 1.787 | 0.6175 | [-4.395, 2.610] | 74 | no |
| Pro-democracy excerpt | 0.334 | 1.304 | 0.7977 | [-2.221, 2.889] | 56 | no |
| Biden–DeSantis cooperation | -0.686 | 1.284 | 0.5932 | [-3.203, 1.831] | 76 | no |
| Scandals, both parties (labeled) | -0.480 | 1.799 | 0.7896 | [-4.006, 3.046] | 138 | no |
| Scandals (labels revealed later) | -1.368 | 1.718 | 0.4257 | [-4.735, 1.998] | 71 | no |
| Perception gap quiz | 0.190 | 2.708 | 0.9440 | [-5.117, 5.497] | 55 | no |

<!-- fd:hyp id=H2 tag=registered outcome=post_udp -->
### H2. Support for undemocratic practices

*Secondary (registered): the effect of each intervention (1-32) on support for undemocratic practices, relative to the pure control.*  
*Pre-registered.*

![H2: effect by arm](figures/H2_arms.png)

The McCain defends Obama video raised support for undemocratic practices by 0.17 scale points (95% CI [0.02, 0.33], two-sided p = 0.032), which is a worsening on this outcome. The other arms ranged from about −0.15 to +0.16 points relative to control, and none was distinguishable from it. Intervals were generally wide, so modest effects in either direction cannot be excluded. With 32 uncorrected tests and only 86 people in this arm, the result is fragile.

#### Details: model and estimates by arm (H2)

```
post_udp ~ C(arm_code, Treatment(reference='T0')) + pre_ap + pre_udp
OLS | weights = ipw_weight | HC2 robust SEs | N = 3814 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Cooperation infographic | 0.036 | 0.085 | 0.6734 | [-0.130, 0.201] | 89 | no |
| Bipartisan bills graph | 0.040 | 0.077 | 0.6059 | [-0.111, 0.190] | 107 | no |
| Bipartisan elite quotes | -0.113 | 0.089 | 0.2050 | [-0.288, 0.062] | 95 | no |
| Shared values exercise | -0.040 | 0.086 | 0.6419 | [-0.208, 0.128] | 77 | no |
| Cross-partisan dialogue guide | -0.121 | 0.094 | 0.1952 | [-0.305, 0.062] | 65 | no |
| Meta-dehumanization correction | -0.037 | 0.064 | 0.5644 | [-0.163, 0.089] | 223 | no |
| Perception survey (form) | 0.107 | 0.091 | 0.2426 | [-0.072, 0.286] | 85 | no |
| Common-ground articles | 0.024 | 0.121 | 0.8457 | [-0.214, 0.261] | 67 | no |
| Patriotic article | -0.057 | 0.059 | 0.3335 | [-0.173, 0.059] | 331 | no |
| 14th Amendment video | -0.082 | 0.076 | 0.2788 | [-0.232, 0.067] | 60 | no |
| Congressional softball video | 0.054 | 0.087 | 0.5325 | [-0.116, 0.225] | 63 | no |
| iSideWith quiz | 0.001 | 0.087 | 0.9897 | [-0.169, 0.171] | 62 | no |
| Rick and Morty perspective-taking | -0.061 | 0.095 | 0.5190 | [-0.248, 0.125] | 57 | no |
| Brené Brown empathy video | -0.097 | 0.075 | 0.1954 | [-0.243, 0.050] | 164 | no |
| Perception gap video | -0.006 | 0.055 | 0.9074 | [-0.115, 0.102] | 646 | no |
| 'What makes an American' video | 0.037 | 0.074 | 0.6181 | [-0.108, 0.182] | 150 | no |
| McCain defends Obama video | 0.174 | 0.081 | 0.0324 | [0.015, 0.332] | 86 | yes |
| Egyptian revolution video | -0.005 | 0.081 | 0.9488 | [-0.165, 0.154] | 72 | no |
| Cross-partisan friendship TED talk | 0.048 | 0.109 | 0.6626 | [-0.166, 0.261] | 68 | no |
| American history video | -0.066 | 0.081 | 0.4148 | [-0.225, 0.093] | 66 | no |
| Party-tailored videos | -0.112 | 0.129 | 0.3852 | [-0.364, 0.140] | 68 | no |
| Jubilee free speech panel | -0.076 | 0.099 | 0.4453 | [-0.270, 0.119] | 50 | no |
| Jubilee video | 0.001 | 0.073 | 0.9859 | [-0.143, 0.145] | 123 | no |
| Media-profits-from-division image | 0.162 | 0.097 | 0.0966 | [-0.029, 0.352] | 98 | no |
| Shared priorities (Pew) table | 0.014 | 0.103 | 0.8913 | [-0.188, 0.216] | 65 | no |
| Bipartisan legislation examples | -0.049 | 0.082 | 0.5507 | [-0.210, 0.112] | 67 | no |
| Common threat (Russia) | 0.028 | 0.093 | 0.7616 | [-0.155, 0.211] | 76 | no |
| Pro-democracy excerpt | -0.145 | 0.133 | 0.2741 | [-0.405, 0.115] | 56 | no |
| Biden–DeSantis cooperation | -0.119 | 0.103 | 0.2485 | [-0.321, 0.083] | 77 | no |
| Scandals, both parties (labeled) | -0.010 | 0.084 | 0.9037 | [-0.175, 0.154] | 140 | no |
| Scandals (labels revealed later) | -0.028 | 0.088 | 0.7480 | [-0.202, 0.145] | 72 | no |
| Perception gap quiz | 0.048 | 0.107 | 0.6573 | [-0.163, 0.258] | 55 | no |

<!-- fd:section id=exploratory -->
## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

<!-- fd:hyp id=E1 tag=exploratory kind=pipeline -->
### E1. Completers-only robustness of planned H1

Partial responses are included in the planned sample, so restricting to fully completed surveys checks whether the planned affective polarization estimates depend on who finished. The planned H1 model for each intervention versus the pure control was re-fit on completed responses only and compared side by side with the planned estimates.

**Finding.** The completers-only fit used the same 3,772 respondents as the planned models and gave identical estimates, so it tests nothing new. *(corrected on review)*

Exploratory and unreviewed: the completers-only fit used the same 3,772 respondents as the planned models and gave identical estimates and standard errors, so it tests nothing new.

#### Details: table (E1)

| arm | estimate_planned | std_error_planned | n_planned | estimate_completers | std_error_completers | n_completers |
|---|---|---|---|---|---|---|
| Cooperation infographic | -0.947 | 1.589 | 3772 | -0.947 | 1.589 | 3772 |
| Bipartisan bills graph | 0.377 | 1.537 | 3772 | 0.377 | 1.537 | 3772 |
| Bipartisan elite quotes | -0.789 | 1.340 | 3772 | -0.789 | 1.340 | 3772 |
| Shared values exercise | 0.799 | 1.699 | 3772 | 0.799 | 1.699 | 3772 |
| Cross-partisan dialogue guide | -1.020 | 3.251 | 3772 | -1.020 | 3.251 | 3772 |
| Meta-dehumanization correction | 0.098 | 1.644 | 3772 | 0.098 | 1.644 | 3772 |
| Perception survey (form) | 0.384 | 1.768 | 3772 | 0.384 | 1.768 | 3772 |
| Common-ground articles | -1.586 | 1.865 | 3772 | -1.586 | 1.865 | 3772 |
| Patriotic article | -1.959 | 1.272 | 3772 | -1.959 | 1.272 | 3772 |
| 14th Amendment video | -1.751 | 1.510 | 3772 | -1.751 | 1.510 | 3772 |
| Congressional softball video | -1.215 | 1.496 | 3772 | -1.215 | 1.496 | 3772 |
| iSideWith quiz | 0.383 | 1.333 | 3772 | 0.383 | 1.333 | 3772 |
| … 20 more rows |  | | | | | |

<!-- fd:hyp id=E2 tag=exploratory kind=pipeline -->
### E2. Heterogeneity of planned H1 by Democratic identification

Partisan identity is central to affective polarization, so the planned H1 effects are checked for differences between Democrats and non-Democrats. The planned H1 model was re-fit with an interaction between each intervention and a Democratic-identification indicator, and the interaction terms were tested.

**Finding.** Of 32 arm-by-group interaction tests, 0 were significant at p<0.05.

Exploratory and unreviewed: none of the 32 arm-by-Democratic-identification interactions was significant at p < 0.05. The intervals are wide, so this cannot rule out differences between Democrats and others.

#### Details: table (E2)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='T0'))[T.T1]:C(_mod)[T.1] | Cooperation infographic x is_dem=1 | -1.730 | 3.320 | 0.602 | -8.237 | 4.776 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T2]:C(_mod)[T.1] | Bipartisan bills graph x is_dem=1 | -1.666 | 3.607 | 0.644 | -8.735 | 5.404 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T3]:C(_mod)[T.1] | Bipartisan elite quotes x is_dem=1 | -4.308 | 2.783 | 0.122 | -9.763 | 1.147 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T4]:C(_mod)[T.1] | Shared values exercise x is_dem=1 | -5.675 | 3.474 | 0.102 | -12.483 | 1.134 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T5]:C(_mod)[T.1] | Cross-partisan dialogue guide x is_dem=1 | -2.026 | 5.660 | 0.720 | -13.119 | 9.068 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T6]:C(_mod)[T.1] | Meta-dehumanization correction x is_dem=1 | -2.151 | 3.820 | 0.573 | -9.638 | 5.336 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T7]:C(_mod)[T.1] | Perception survey (form) x is_dem=1 | -4.583 | 3.289 | 0.164 | -11.030 | 1.864 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T8]:C(_mod)[T.1] | Common-ground articles x is_dem=1 | -4.296 | 3.972 | 0.279 | -12.082 | 3.489 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T9]:C(_mod)[T.1] | Patriotic article x is_dem=1 | -0.883 | 2.689 | 0.743 | -6.153 | 4.387 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T10]:C(_mod)[T.1] | 14th Amendment video x is_dem=1 | -2.471 | 3.244 | 0.446 | -8.830 | 3.888 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T11]:C(_mod)[T.1] | Congressional softball video x is_dem=1 | 0.160 | 3.003 | 0.957 | -5.726 | 6.046 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T12]:C(_mod)[T.1] | iSideWith quiz x is_dem=1 | 0.126 | 2.908 | 0.965 | -5.575 | 5.826 | 3772 |
| … 20 more rows |  | | | | | | |

<!-- fd:hyp id=E3 tag=exploratory kind=pipeline -->
### E3. Heterogeneity of planned H1 by political interest

Political interest may moderate how strongly people engage with the interventions, so planned H1 effects are compared between high- and low-interest respondents. The planned H1 model was re-fit with an interaction between each intervention and a high-interest indicator (interest rated 4 or 5), and the interaction terms were tested.

**Finding.** Of 32 arm-by-group interaction tests, 0 were significant at p<0.05.

Exploratory and unreviewed: none of the 32 arm-by-political-interest interactions was significant at p < 0.05. The closest, for Shared values exercise, was −6.9 points (95% CI [−14.0, 0.2]). This does not establish that effects are uniform.

#### Details: table (E3)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='T0'))[T.T1]:C(_mod)[T.1] | Cooperation infographic x high_interest=1 | -3.309 | 3.232 | 0.306 | -9.643 | 3.026 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T2]:C(_mod)[T.1] | Bipartisan bills graph x high_interest=1 | -0.839 | 3.068 | 0.784 | -6.852 | 5.174 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T3]:C(_mod)[T.1] | Bipartisan elite quotes x high_interest=1 | -3.392 | 2.662 | 0.203 | -8.610 | 1.826 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T4]:C(_mod)[T.1] | Shared values exercise x high_interest=1 | -6.934 | 3.628 | 0.056 | -14.044 | 0.177 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T5]:C(_mod)[T.1] | Cross-partisan dialogue guide x high_interest=1 | 0.717 | 6.829 | 0.916 | -12.668 | 14.103 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T6]:C(_mod)[T.1] | Meta-dehumanization correction x high_interest=1 | -4.836 | 3.447 | 0.161 | -11.592 | 1.920 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T7]:C(_mod)[T.1] | Perception survey (form) x high_interest=1 | -2.023 | 3.355 | 0.546 | -8.599 | 4.552 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T8]:C(_mod)[T.1] | Common-ground articles x high_interest=1 | -5.240 | 3.966 | 0.186 | -13.014 | 2.534 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T9]:C(_mod)[T.1] | Patriotic article x high_interest=1 | 0.478 | 2.548 | 0.851 | -4.516 | 5.471 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T10]:C(_mod)[T.1] | 14th Amendment video x high_interest=1 | 2.779 | 2.958 | 0.347 | -3.018 | 8.577 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T11]:C(_mod)[T.1] | Congressional softball video x high_interest=1 | -3.634 | 3.056 | 0.234 | -9.624 | 2.355 | 3772 |
| C(arm_code, Treatment(reference='T0'))[T.T12]:C(_mod)[T.1] | iSideWith quiz x high_interest=1 | -3.428 | 2.697 | 0.204 | -8.713 | 1.858 | 3772 |
| … 20 more rows |  | | | | | | |


<!-- fd:section id=related -->
## Related work

Prior findings on the study's primary hypothesis come from meta-analytic work on prejudice reduction, which reviews hundreds of experiments to estimate average intervention effects and to ask which approaches work best (Paluck et al., 2020). Work on affective polarization treats it as a distinct construct tied to identity rather than policy disagreement, which helps explain why interventions aimed at out-group attitudes may move it (Mason, 2018), and studies of local context suggest that affective polarization varies across environments in ways that bear on whether effects generalise (Druckman et al., 2020). Taken together, the supporting literature gives reason to expect that some interventions may reduce affective polarization, though it offers no direct estimate for the specific 32 interventions under test. The contesting works frame polarization more pessimistically and, in part, locate its causes in political and structural conditions that individual-level interventions may not reach. McCoy and Somer (2018) argue that severe polarization is driven by system-level dynamics and that its consequences for democracy are serious, which implies that modest interventions may have limited leverage. Lorenz-Spreen et al. (2022) and Persily et al. (2020) disagree about the strength of the link between digital media and democratic outcomes, with the systematic review emphasising that causal evidence is mixed and contested. The study's design, which compares each intervention against a pure control and measures both affective polarization (H1) and support for undemocratic practices (H2), can speak to whether individual-level effects exist at all, but it cannot adjudicate the structural claims about pernicious polarization made in the contesting works.

Retrieved works (OpenAlex; queries: interventions reducing affective polarization feeling thermometer; perspective-getting or contact interventions reduce partisan animosity; null effects of depolarization interventions on partisan affect; affective polarization persistent despite interventions and backfire effects of corrective messages; m):

- Elizabeth Levy Paluck, Roni Porat, Chelsey S. Clark, DONALD PHILIP GREEN (2020). Prejudice Reduction: Progress and Challenges. Annual Review of Psychology. https://doi.org/10.1146/annurev-psych-071620-030619
- Lilliana Mason (2018). Ideologues without Issues: The Polarizing Consequences of Ideological Identities. Public Opinion Quarterly. https://doi.org/10.1093/poq/nfy005
- James N. Druckman, Samara Klar, Yanna Krupnikov, Matthew S. Levendusky (2020). Affective polarization, local contexts and public opinion in America. Nature Human Behaviour. https://doi.org/10.1038/s41562-020-01012-5
- Jennifer McCoy, Murat Somer (2018). Toward a Theory of Pernicious Polarization and How It Harms Democracies: Comparative Evidence and Possible Remedies. The Annals of the American Academy of Political and Social Science. https://doi.org/10.1177/0002716218818782
- Philipp Lorenz-Spreen, Lisa Oswald, Stephan Lewandowsky, Ralph Hertwig (2022). A systematic review of worldwide causal and correlational evidence on digital media and democracy. Nature Human Behaviour. https://doi.org/10.1038/s41562-022-01460-1
- Nathaniel Persily, Joshua A. Tucker, Andrew M. Guess, Benjamin A. Lyons (2020). Social Media and Democracy. Cambridge University Press eBooks. https://doi.org/10.1017/9781108890960

<!-- fd:section id=limitations -->
## Limitations

Arms are small, mostly 56 to 330 respondents against a control of about 230, so intervals are wide and most estimates are inconclusive rather than evidence of no effect. The 64 primary and secondary tests were not corrected for multiplicity, and the two significant results have p-values near 0.02 and 0.03, so chance findings are plausible. The sample is a US online panel, and attrition (4,485 analysed of 6,086) may differ across arms. Outcomes were measured immediately after exposure, so durability is unknown. Batches were adaptive, which may complicate comparisons across arms. The design cannot speak to structural causes of polarization raised in the wider literature.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 12 of 12 checked claims supported after the agent's corrections (2 flagged claims corrected); 2 of 2 registered analyses run as planned; 2 reworded; 3 text fixes; 2 correction passes.

#### Corrections

- **Corrected** · 5 items reworded or fixed in the text: E1, H2, R1, E1, R2, H1, R3, H2. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The two headline estimates match the tables: the Perception gap video at −2.31 (p = 0.021) on affective polarization and the McCain video at +0.174 (p = 0.032) on support for undemocratic practices. Both are single significant arms out of 32 per outcome, are uncorrected, and rest on small arms, so they are fragile. The 'only arm' wording is fine as a description of significance, but the report's claims about the null arms and the E1 robustness check are weaker than stated. The most important caveat is that E1 is not a real robustness check, because the completers table is identical to the planned model (n = 3,772 in every row).

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |
| H2 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K1 | high | presentational | claims | Fixed in text | E1: Unsupported claim: "Re-fitting on 3,900 completers (87% of the sample) ... planned H1 estimates are not sensitive to dropping partial responses". E1 table: n_completers = 3772 in every row, with estimates and SEs identical to the planned ones. 3,900 appears in no table. *claim checked against the tables by the checking agent* |
| R1 | high | presentational | light | Fixed in text | E1: Text says 3,900 completers (87% of the sample) were used and calls this a robustness check. The E1 table shows n_completers = 3772 for every arm, identical to the planned n, with estimates and SEs identical to the planned ones. 3,900 appears in no table, and 3,900/4,485 is 87% only of the analysed 4,485, not the 3,772 used. *The E1 prose misreports the completers n and the 3,900 / 87% figures; the table shows an identical sample, so the text must be corrected.* |
| K2 | medium | presentational | claims | Fixed in text | H2: Overstated claim: "The other arms shown were within about ±0.15 points of control". H2_arms T24 Media-profits-from-division: +0.162, outside ±0.15. *claim checked against the tables by the checking agent* |
| R2 | medium | presentational | light | Fixed in text | H1: Text says the remaining arms' point estimates range 'between about −2.4 and +1.4'. The table shows −2.382 for 'What makes an American' and +1.355 for American history, so the range holds, but the sentence also says 'the remaining arms for which results are shown', while the other arms are not all shown. The Brené Brown (−2.137) and Patriotic (−1.959) arms are not mentioned. *The prose should state that all 31 other arms had CIs including zero, with estimates from −2.38 to +1.36.* |
| R3 | medium | presentational | light | Fixed in text | H2: Text says the other arms were 'within about ±0.15 points of control'. The table shows Media-profits-from-division at +0.162 (p = 0.097) and Pro-democracy excerpt at −0.145. The Media-profits arm exceeds ±0.15. *The ±0.15 range is slightly wrong; Media-profits is +0.162.* |
| R4 | low | presentational | light | Fixed in text | Limitations: Text says arms are 'mostly under 200 respondents', while the design section says 'mostly 56 to 330'. Control n = 229 is not stated in the prose, although the report says control sizes are not shown. *Arm-size wording is inconsistent between the Design and Limitations sections.* |
| R5 | low | presentational | light | Fixed in text | Abstract: The 'Perception gap video' arm is described as about 640 people, while the table shows 641 for H1 and 646 for H2. *The arm n should be given as 641 (H1) and 646 (H2) instead of 'about 640'.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| The Perception gap video lowered affective polarization by 2.3 points (95% CI [−4.3, −0.4], p = 0.021) | Abstract | supported | H1_arms T15: −2.307, CI [−4.262, −0.353], p = 0.021. | supported: The Perception gap video ... lowered affective polarization by 2.3 points relative to control (95% CI [−4.3, −0.4], p = 0.021) |
| McCain defends Obama video raised support for undemocratic practices by 0.17 (CI [0.02, 0.33], p = 0.032) | Abstract | supported | H2_arms T17: 0.174, CI [0.015, 0.332], p = 0.032. | supported: McCain defends Obama video raised support for undemocratic practices by 0.17 scale points (95% CI [0.02, 0.33], p = 0.032) |
| only one of 32 interventions lowered affective polarization | Key findings | supported | H1_arms summary: 1 of 32 with p < 0.05 (T15). The wording should say 'only one was distinguishable from control'. | supported: only one of 32 interventions, the Perception gap video, lowered affective polarization relative to control |
| the only registered arm with a detectable shift on that outcome | Key findings | supported | H2_arms summary: 1 of 32 with p < 0.05, smallest p 0.032. | supported: the only registered arm with a detectable shift on that outcome |
| Re-fitting on 3,900 completers (87% of the sample) ... planned H1 estimates are not sensitive to dropping partial responses | E1 | unsupported | E1 table: n_completers = 3772 in every row, with estimates and SEs identical to the planned ones. 3,900 appears in no table. | supported: Re-fitting on 3,900 completers (87% of the sample)... not sensitive to dropping partial responses |
| The other arms shown were within about ±0.15 points of control | H2 | overstated | H2_arms T24 Media-profits-from-division: +0.162, outside ±0.15. | supported: The other arms ranged from about −0.15 to +0.16 points relative to control, and none was distinguishable from it |
| point estimates between about −2.4 and +1.4 points | H1 | supported | H1_arms: minimum −2.382 (T16), maximum +1.355 (T20). | supported: All 31 other arms had intervals that included zero, with estimates from −2.38 to +1.36 points |
| 0 of 32 arm-by-group interactions significant (E2, E3) | E2/E3 | supported | E2 summary: 0 of 32, smallest p 0.102. E3 summary: 0 of 32, smallest p 0.056. | supported: none of the 32 arm-by-Democratic-identification interactions was significant ... none of the 32 arm-by-political-interest interactions |
| Control respondents averaged 41.5 and the video group 39.6 | H1 | supported | H1_arms T15: mean_control 41.459, mean_arm 39.587. These are raw means; the estimate is covariate-adjusted. | supported: Control respondents averaged 41.5 and the video group 39.6 |
| 64 tests were run without correction | Abstract | supported | registered_summary has 64 rows. The plan specifies no correction. | supported: 64 tests were run without correction for multiple comparisons |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Rewrite the E1 text and finding so they match the table: same 3,772 respondents, identical estimates, no sensitivity test. Done: E1 rewritten to match the table (same respondents, identical estimates, no sensitivity test); the takeaway was adjusted too.
- G2. Fix the H2 range to −0.15 to +0.16. Done: H2 range fixed to −0.15 to +0.16.
- G3. Make arm-size wording consistent and state the control n of 229 (H1) and 234 (H2). Done: Arm sizes are now consistently 56 to 330 in the design notes and limitations; control n of 229 (H1) and 234 (H2) stated.
- G4. Fix the Perception gap n to 641 (H1) and 646 (H2). Done: Perception gap n stated as 641 (H1) and 646 (H2) in the abstract and design notes.

Re-check of the corrected text: No further rewording needed; the previously flagged issues are resolved.

#### Other review options

- **Coarse**: the open-source coarse-ink reviewer, run on your machine (about $1-2), then imported. `uvx coarse-ink review report.md, then filedrawer review-import . coarse FILE`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview or any referee report**: import a review posted on OpenReview, or any other referee report. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Pre-registered (OSF k2nwj, before the adaptive batches were analysed), with a pure 'Please continue' control and a common covariate-adjusted model for all 32 arms, so the arms are comparable. Two registered outcomes: affective polarization on the thermometer scale and support for undemocratic practices. This showed that an arm can help on one outcome and not the other (Perception gap video −2.3 on affective polarization, −0.006 on undemocratic practices). The report hedges honestly: 64 uncorrected tests, two results at p≈0.02 and 0.03, and wide intervals described as inconclusive rather than as null. Reports the full arm-by-arm tables with n per arm, so the weakly powered arms are visible.

**Verdict.** A follow-up is worth running, but only a narrow one. Of 64 tests, two were barely significant and 30 of 32 arms were inconclusive, so the broad screening design should not be repeated. Run the Perception gap video replication with a mechanism measure and a delayed follow-up first, since it is the only affective polarization result and also the largest arm. The McCain defends Obama video effect on undemocratic practices rests on 86 people and is probably noise. The structural-cue and moderator briefs can follow if the replication holds.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Most arms have 56-330 respondents against a control of 229 (affective polarization) or 234 (undemocratic practices). Standard errors of 1.3-3.3 points mean only effects above about 3-5 points are detectable. | H1 table: arm SEs 0.997 (Perception gap video, n=641) to 3.251 (dialogue guide, n=65); the 'What makes an American' video estimate of −2.4 had CI [−5.1, 0.4]. |
| Analysis | Thirty-two arms were tested on each of two outcomes with no multiplicity correction. The only two hits are near the threshold and would not survive a correction. | Perception gap video p=0.021 and McCain defends Obama video p=0.032, among 64 tests; about 3 false positives are expected at alpha 0.05. |
| Design | Single-shot exposure with immediate outcomes, and a cross-arm comparison with a shared small control. The batches were adaptive, which complicates comparisons across arms. Durability and behavioural relevance are untested. | Limitations section; arms ranged from 56 to 641 respondents, and the Perception gap video arm was far larger than the others. |
| Sample | Analysis dropped from 6,086 collected to 4,485, and to 3,772 for the affective polarization model. Attrition may differ by arm, and Lucid respondents may be unrepresentative. | N analysed 4,485 of 6,086; H1 model N=3772; H2 model N=3814. |
| Measurement | The exploratory checks add nothing. The completers-only fit reproduced the planned estimates exactly, and the subgroup interactions were underpowered. | E1 estimates identical on the same 3,772 respondents; E2 and E3 had 0 of 32 interactions significant, with CIs such as [−14.0, 0.2]. |

**D1. Can individual-level interventions move polarization, or is it structural?.** (a) Affective polarization is identity-based, so brief interventions that alter perceptions of the out-group can reduce it, and prejudice-reduction experiments show some average effects. [Paluck et al. (2020), Mason (2018)] (b) Severe polarization is driven by system-level and media dynamics, so brief individual-level messages have little leverage and may even backfire on democratic attitudes. [McCoy et al. (2018), Lorenz-Spreen et al. (2022), Persily et al. (2020)] This study: It leans weakly toward the structural side. 30 of 32 arms did nothing detectable on either outcome, and the one affective polarization gain (−2.3) is small and borderline. It cannot rule out modest effects, and it cannot test structural causes directly.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Perception gap video: replication, mechanism and persistence

Addresses power and design: it gives the one borderline effect a large pre-registered replication, adds a mechanism measure, and adds a delayed follow-up.

**Hypothesis.** The full Perception gap video lowers the in-party minus out-party thermometer gap relative to control by about 1.4 points or more. The effect is mediated by reduced misperception of out-party attitudes, so the no-data variant has a smaller effect. Some of the effect remains at about 2 weeks. Undemocratic-practice support does not increase.

**Design.** Perception gap video vs. Video without data vs. Placebo video vs. Control; primary outcome: Affective polarization (in-party minus out-party thermometer) immediately after exposure, full video versus control. About 1000 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items

In the source study the Perception gap video lowered the thermometer gap by 2.3 points (SE 0.997, n=641, p=0.021), one borderline result among 64 uncorrected tests. This follow-up replicates it at scale, tests whether correcting out-party misperceptions is the channel by comparing the full video with a version lacking the misperception data, and re-measures after about 2 weeks because the source only measured outcomes immediately.

**Debate it speaks to.** Can individual-level interventions move polarization, or is it structural?: Affective polarization is identity-based, so brief interventions that alter perceptions of the out-group can reduce it, and prejudice-reduction experiments show some average effects. versus Severe polarization is driven by system-level and media dynamics, so brief individual-level messages have little leverage and may even backfire on democratic attitudes.

**Power.** About 1000 per arm to detect 1.4 at 80% power (Observed −2.3 points with SE 0.997 at n=641; the true effect is probably smaller than the winning estimate, so size for about 1.4 points (SD about 20 implied by the SEs).).

Open items before fielding:

- Video files and the edited no-data version must be produced by the research team.
- IRB approval number and compensation amount.
- Wave 2 invitation mechanics and reminders are handled by the panel.
- Supply media: video_pg: video stimulus to supply (Perception gap video showing how Democrats and Republicans overestimate each oth)
- Supply media: video_nd: video stimulus to supply (Edited version of the Perception gap video with the misperception statistics rem)
- Supply media: video_pl: video stimulus to supply (Neutral nonpolitical explainer video, about 6 minutes)

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Who does the Perception gap video work for?

Addresses sample and measurement: the exploratory interactions were too noisy (CIs of ±7 points), so a dedicated, powered moderator test is needed.

**Hypothesis.** The video effect on affective polarization is larger (more negative) for respondents with larger baseline misperception; effects of party and interest are tested as two-sided preregistered interactions.

**Design.** Control vs. Perception gap video; primary outcome: Affective polarization: in-party minus out-party feeling thermometer after treatment. About 1200 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items

The Perception gap video lowered affective polarization by 2.3 points (95% CI [-4.3, -0.4], n=641 vs control 229), but exploratory party and interest interactions were null with intervals of about ±7 points. A dedicated, stratified, powered test is needed to learn whether the effect depends on partisanship, political interest or baseline misperception.

**Power.** About 1200 per arm to detect 2.5 at 80% power (E2/E3 interaction SEs of 3-3.6 at the arm sizes used; the interaction MDE needs about 4x the n of the main effect.).

Open items before fielding:

- The actual Perception gap video file must be supplied and hosted by the research team.
- IRB approval number and compensation details must be supplied by the research team.
- The panel vendor and quota feasibility for 2400 respondents must be confirmed.
- Supply media: video1: video stimulus to supply (Perception gap video showing how Democrats and Republicans overestimate each oth)
- Supply media: pre_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90
- Supply media: pre_misperception: set the matrix recode values after import 0-20=10, 21-40=30, 41-60=50, 61-80=70, 81-100=90
- Supply media: post_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40=30, 41-60=50, 61-80=70, 81-100 (very warm)=90

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Individual message versus structural cue

Addresses framing: it tests whether individual-level correction is overridden by structural cues, instead of assuming either side.

**Hypothesis.** If individual interventions have leverage, the video lowers affective polarization under both primes. If the structural account holds, the video effect shrinks or vanishes under the hostile prime (video x prime interaction > 0).

**Design.** Neutral feed, control vs. Neutral feed, video vs. Hostile feed, control vs. Hostile feed, video; primary outcome: Affective polarization: in-party minus out-party feeling thermometer. About 800 per arm for 80% power.

Files: [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) · [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: background and open items

Only the Perception gap video lowered affective polarization (-2.3, 95% CI [-4.3, -0.4], n=641) among 32 arms, and the study cannot test structural causes. This 2x2 crosses the video with a hostile elite/media feed prime to see whether the individual-level correction survives a hostile environment.

**Debate it speaks to.** Can individual-level interventions move polarization, or is it structural?: Affective polarization is identity-based, so brief interventions that alter perceptions of the out-group can reduce it, and prejudice-reduction experiments show some average effects. versus Severe polarization is driven by system-level and media dynamics, so brief individual-level messages have little leverage and may even backfire on democratic attitudes.

**Power.** About 800 per arm to detect 2.0 at 80% power (Interaction contrast; the observed main effect of −2.3 with SE 1.0 at n=641 implies an interaction needs roughly 800 per cell.).

Open items before fielding:

- Actual feed screenshots and the Perception gap video file must be supplied by the research team.
- IRB approval number and compensation must be supplied.
- Supply media: feed_neutral: image stimulus to supply (a neutral news feed with weather, library opening, recipe and sports posts)
- Supply media: feed_neutral: image stimulus to supply (a neutral news feed with weather, library opening, recipe and sports posts)
- Supply media: video_pg: video stimulus to supply (Perception gap video presenting data on how each party misperceives the other, a)
- Supply media: feed_hostile: image stimulus to supply (a news feed of elite and media posts attacking the other party and headlines abo)
- Supply media: feed_hostile: image stimulus to supply (a news feed of elite and media posts attacking the other party and headlines abo)
- Supply media: video_pg: video stimulus to supply (Perception gap video presenting data on how each party misperceives the other, a)
- Supply media: post_ap_scores: set the matrix recode values after import 0-20 (very cold)=10, 21-40 (cold)=30, 41-60 (neutral)=50, 61-80 (warm)=70, 81-100 (very warm)=90


<!-- fd:section id=acknowledgments -->
## Acknowledgments

This study was carried out in collaboration with Hayley Cohen.


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
| H1 | **registered** | as registered | as registered |  |
| H2 | **registered** | as registered | as registered |  |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H1, H2 / estimator.weights: "Regression weighted to account for differential probabilities of treatment assignment." -> ipw_weight = 1 / the arm's share among all finished respondents, as in the authors' analysis (the registration does not give the weights, and the per-batch probabilities were not stored with the data (batch is missing for about a third of finished respondents))
- H1, H2 / estimator.covariates: "In the event of significant trends in the control group, will include batch fixed effects." -> batch fixed effects are not in the main specification; they are run as a robustness check (the registration makes them conditional on a control-group trend)
- all / analysis: "The probability of the best-performing arm will be calculated using the simulation approach described in https://osf.io/vdr4g." -> not computed by this pipeline; the arm-level estimates are reported (the pipeline estimates registered regressions only)

### Reviewer pass

The automated review (Light Pass) flagged 7 issue(s); see `review.md`.

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `ACKNOWLEDGMENTS.md`
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
- `pap.json`
- `pap.md`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/E1_completers_only.csv`
- `results/E2_dem_heterogeneity.csv`
- `results/E3_interest_heterogeneity.csv`
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
