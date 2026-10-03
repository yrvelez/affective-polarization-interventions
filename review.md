# Automated review: light pass, advanced pass (methodology + statistics)

Models: light `anthropic/claude-sonnet-5.5`, advanced:methodology `anthropic/claude-sonnet-5.5`, advanced:statistics `anthropic/claude-sonnet-5.5`, orchestrator `anthropic/claude-sonnet-5.5`. The tables support a narrow reading: one of 32 arms (Perception gap video, -2.33, CI [-4.28,-0.38], p=0.019) is nominally significant on affective polarization, and no arm differs on undemocratic-practice support. The study is post hoc, uncorrected, and has only 229 controls. The pooled -0.8 estimate comes from an approximate random-effects model that ignores the shared control, so its p=0.005 is not reliable. The most important caveat is that the single nominal hit is consistent with chance among 64 uncorrected tests, and the sample flow (4,547 vs 3,825/3,953 modelled) is unexplained.

**Review outcome (round 1): 12 of 12 claims supported by the results after the authors' revision; 8 analytical issues open for a robustness round.**

- **high** R1 (presentational) [editorial] — Design / H1 / H2 sample sizes: The analysed N is reported as 4,547, but the models use N=3,825 (H1) and 3,953 (H2). The 32 arm sizes in the H1 table sum to well under 3,825. The report never explains the gap, which suggests missing pre-treatment or outcome data. The 'arm sizes 60 to 660' and 'about 1,500 missing' statements also don't match this.
  - Suggested fix: Add a sample-flow table covering raw, filtered, complete-case and per-model N, with reasons for each loss. Correct the arm-size range and the missing-data statement.
  - Disposition: A sample-flow table and corrected N and arm-size statements are needed; the data on losses may be partly recoverable but this is a reporting fix.
- **high** R2 (analytical) [address] — H1/H2 pooled estimates: The pooled effects (-0.8 and -0.015) come from a random-effects meta-analysis of arm estimates that share one control group. The report admits the SE is approximate, yet it uses p=0.005 as a headline. Tau² = 0 and I² = 0 look degenerate. Pooled significance is also stated more strongly than the single-arm results justify. The pooled value of -0.8 is far smaller than most arm estimates, and the arm estimates do not obviously average to it.
  - Suggested fix: Estimate a single pooled-treatment-versus-control regression with robust SEs, and report it in place of the approximate meta-analytic SE.
  - Disposition: A pooled any-treatment vs control regression with robust SEs can be fitted on the same data.
- **high** R3 (analytical) [declined] — Abstract / Key findings: The report says only the Perception gap video 'clearly reduced' polarization (p=0.019) and calls this a 'chance finding', but the tests are not multiplicity-corrected. The 'What makes an American' video (−2.6, p=0.059) has a larger point estimate. There is no adjusted p-value, so the 'clearly reduced' wording overstates the evidence.
  - Suggested fix: Add Holm or BH adjusted p-values, and soften the language to say the effect does not survive correction (if it doesn't).
  - Disposition: The plan specifies no multiplicity correction, so adjusted p-values would change the analysis; soften the wording and flag the lack of correction instead.
- **medium** R4 (analytical) [address] — Design / model spec: The models use ipw_weight inverse-probability weights, and the report never says what they correct for. Weights, HC2 SEs and pre-treatment covariates are all choices lifted from the script and not justified. The weights likely relate to the missing-data handling, but this is unexplained.
  - Suggested fix: Describe the weights and show unweighted and complete-case sensitivity results.
  - Disposition: Unweighted and complete-case re-fits can be added as robustness checks, and the weights described.
- **medium** R5 (presentational) [editorial] — Design / exclusions: The exclusion 'arm != T33' (the GPT-3 chatbot arm) is mentioned only in passing. The text also says '32 interventions' in the abstract against '33 arms' in the design section. The restriction to Democrats and Republicans drops independents without discussion.
  - Suggested fix: State clearly that T33 and independents were excluded and why, and reconcile the arm counts.
  - Disposition: State the T33 and independents exclusions and reconcile 32 vs 33 arms in the text.
- **medium** R6 (presentational) [editorial] — Results prose (H1/H2): The text says 'the other arms shown' and 'no arm in the displayed rows', although the table lists all 32 arms. The '64 tests' count also isn't shown in the results.
  - Suggested fix: Say that all 32 arms are shown, and state the number of tests explicitly.
  - Disposition: Fix 'displayed rows' wording and state the test count.
- **low** R7 (presentational) [editorial] — Related work / figures: The retrieved literature is irrelevant (physics papers, etc.). A leftover 'Planned treatment effects' figure appears even though nothing was planned.
  - Suggested fix: Remove the irrelevant citations and relabel or remove the 'Planned' figure.
  - Disposition: Remove the off-topic citations and the 'Planned treatment effects' figure.
- **high** A1 (analytical, advanced:methodology) [address] — Results H1 / Design: Pooled estimate treats arms as independent despite shared control: The random-effects pooled result (−0.819, SE 0.291, p=0.005; tau²=0, I²=0) ignores that all arms share one control group of 229. The text admits the SE is 'approximate', yet the abstract and key findings headline p=0.005. The estimate is also a pooled arm average, not a pooled treated-vs-control contrast. Its precision is likely overstated.
  - Suggested fix: Estimate a single pooled treatment-vs-control contrast (all arms combined vs control) with HC2 SEs, or an omnibus joint test of all arm coefficients. Report that as the primary pooled result.
  - Disposition: Same as R2: a single pooled contrast or omnibus joint test is estimable from existing data.
- **high** A2 (analytical, advanced:methodology) [address] — Design and data: Exclusions and attrition undocumented; analysed N varies: Of 6,086 raw respondents, 4,547 were analysed, and the model N is 3,825 (H1) and 3,953 (H2). The reasons for dropping respondents are not given beyond the partisan filter and the removal of arm T33. Missingness in the post outcomes and in the weights is not reported. Differential attrition across arms could bias the estimates. The exclusion of the GPT-3 arm is mentioned only in passing.
  - Suggested fix: Provide a flow table by arm (raw, partisan filter, missing outcomes or covariates, analysed) and test for differential attrition.
  - Disposition: A by-arm attrition table and a differential-missingness test can be computed from the raw data.
- **high** A3 (analytical, advanced:methodology) [address] — Results H1: Control group small; control mean and arm means inconsistent with adjusted estimates: Only 229 controls anchor all 32 contrasts. The model is adjusted for pre_ap with IPW, but the table's raw mean_arm minus mean_control differs a lot from the estimates. For example, T2 has mean 45.4 vs control 41.5 (+3.9), yet the estimate is +0.38. This suggests large baseline imbalance or weighting effects, which the text does not discuss. Unweighted means are presumably reported.
  - Suggested fix: Report baseline balance across arms, weighted and unweighted means, and results with and without weights and covariates.
  - Disposition: Balance checks and weighted/unweighted and with/without covariate fits use existing data.
- **high** A4 (analytical, advanced:methodology) [unresolved] — Design and data: Randomisation and arm-size imbalance not described: Arm sizes range from about 48 to 660, with the Perception gap video at 641 against typical arms of 60–100. The allocation mechanism is not explained, nor is whether arms were run concurrently. If arms were fielded at different times, comparison with a shared control is confounded. Treatment content differs in length and format, with no manipulation checks.
  - Suggested fix: Document the randomisation procedure and fielding dates, test balance, and show that arms were contemporaneous with the control.
  - Disposition: Randomisation procedure and fielding timing cannot be verified from the tables; balance tests can only partly help.
- **medium** A5 (presentational, advanced:methodology) [declined] — Results H1/H2: Uncorrected multiplicity and inconsistent claims about the single hit: There are 64 uncorrected tests (the multiple-testing policy is 'none', which was the authors' choice). The Perception gap video p=0.019 would not survive any correction. The abstract says it 'clearly reduced' affective polarization, which is stronger than the evidence warrants, even though caveats appear later. The H2 text also says 'rule out large effects' without a stated threshold.
  - Suggested fix: Soften 'clearly reduced' language in the abstract, and state the equivalence or smallest effect size of interest used for H2.
  - Disposition: Corrections conflict with the plan's 'none' multiplicity policy; only soften wording and state the smallest effect of interest.
- **medium** A6 (presentational, advanced:methodology) [editorial] — Results H1: Outcome scaling and sign interpretation unclear: The Intercept of 3.67 in the H1 model, with a control mean of 41.5, shows that pre_ap is a strong predictor. Whether higher values mean more polarization is not defined, and the thermometer-based measure is not specified. The 2.3-point effect is not put in standardized units.
  - Suggested fix: Define the outcome construction and direction, give the SD, and report standardized effects.
  - Disposition: Define the outcome, its direction and the SD; standardised effects follow from existing data.
- **high** A7 (analytical, advanced:statistics) [address] — Results H1 / Limitations: Pooled estimate treats shared-control arms as independent: The random-effects pooled estimate (-0.819, SE 0.291, p=0.005) combines 32 arm effects that all share one control group (n=229), so the arm estimates are positively correlated. The report admits the SE is 'approximate', but the abstract and key findings still headline p=0.005. With tau²=0 and I²=0, this is effectively a fixed-effect average. The SE is likely too small, and a meaningful pooled effect is overstated.
  - Suggested fix: Estimate the pooled effect directly: regress on a single any-treatment indicator with HC2 SEs, or use a covariance-aware meta-analysis. Report that result as the headline.
  - Disposition: Duplicate of R2/A1: fit the pooled any-treatment indicator with HC2 SEs.
- **high** A8 (presentational, advanced:statistics) [editorial] — Results H1 / Abstract: Single significant arm among 32 emphasised; winner's curse: The Perception gap video (p=0.019) is one of 32 uncorrected tests. Under the null, about 1.6 nominal hits are expected, and the p-value is far from any Bonferroni threshold (0.05/32≈0.0016). The point estimate of -2.3 is likely inflated. The abstract's wording 'clearly reduced' is too strong. Under the no-correction policy this is a limitation, not an error.
  - Suggested fix: Replace 'clearly reduced' with 'nominally significant'. State the expected number of false positives. Optionally report adjusted p-values as a sensitivity analysis.
  - Disposition: Replace 'clearly reduced' with 'nominally significant' and state the expected false positives; adjusted p-values are declined under the no-correction policy.
- **high** A9 (analytical, advanced:statistics) [address] — Design and data / Limitations: Differing sample sizes and unexamined attrition and weighting: The analysed N is 4,547 but the models use N=3,825 (H1) and N=3,953 (H2), so about 700 further observations are lost to missing pre/post data. The report does not explain this. The control group has only 229 respondents against 641 in the Perception gap arm, so the control is imprecise and the n(arm) imbalance is unaddressed. IPW weights are used without being described. The exclusion of non-partisans changes the estimand.
  - Suggested fix: Report the attrition flow by arm and test differential missingness. Describe the weights. Give results unweighted as a robustness check.
  - Disposition: Attrition by arm, weight description and unweighted re-fit use existing data.
- **medium** A10 (analytical, advanced:statistics) [address] — Results H2: Null interpretation lacks equivalence or power framing: The text says the pooled CI 'rules out large effects', but the scale is not benchmarked (control mean 2.75, SD not given). Individual arm CIs of about ±0.2 are not interpreted against any smallest effect of interest. The arm-level 'no effect' is therefore uninterpretable. The arm-level range of '−0.13 to +0.14' also omits the observed -0.156 and +0.145.
  - Suggested fix: Report the outcome SD and standardised effects. Do equivalence tests or state minimum detectable effects. Correct the quoted range.
  - Disposition: Outcome SD, standardised effects and minimum detectable effects can be computed from existing data; correct the quoted range.
- **medium** A11 (presentational, advanced:statistics) [editorial] — Limitations / Key findings: Test count is stated inconsistently: The report says '64 tests' (32 per outcome × 2). But the H1 table has 32 rows, and the arm lists total 32 interventions against the 33-arm design text. The T33/GPT-3 exclusion and the 33-arm description are confusing. The 'one in 32 is what chance would produce' claim is also loose: the expected count is 1.6 and P(≥1) is about 0.8.
  - Suggested fix: Clarify the arm count and the number of tests per outcome. State the chance expectation precisely.
  - Disposition: Clarify the arm and test counts and state the chance expectation exactly.
- **medium** K1 (presentational, claims) [editorial] — Abstract: Overstated claim: "Only one intervention clearly reduced affective polarization". H1 table: Perception gap video -2.333, p=0.0191, one of 32 uncorrected tests; 'What makes an American' is -2.647, p=0.059.
  - Suggested fix: Say one arm was nominally significant (p=0.019) in an uncorrected, post hoc analysis; the estimate is likely inflated.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K2 (presentational, claims) [editorial] — Abstract: Overstated claim: "Pooled across all interventions, affective polarization was 0.8 points lower (CI [−1.4, −0.2], p = 0.005)". Random-effects pooled -0.819, SE 0.291, p=0.005, but arms share one control (n=229) so the SE is understated; tau²=0 is degenerate.
  - Suggested fix: Replace with a pooled any-treatment vs control regression with robust SEs, or label the figure approximate.
  - Disposition: claim checked against the tables by the orchestrator
- **high** K3 (presentational, claims) [editorial] — H2: Unsupported claim: "Estimates ranged roughly from −0.13 to +0.14". H2 table: min -0.156 (Pro-democracy excerpt), max +0.145 (Media-profits image).
  - Suggested fix: Report the range as -0.16 to +0.14.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K4 (presentational, claims) [editorial] — Design: Overstated claim: "arm sizes range from roughly 60 to 660". H1 n(arm) runs from 48 (Jubilee free speech panel) to 641; 662 appears in H2.
  - Suggested fix: State 48 to 641 (H1) and 51 to 662 (H2).
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K5 (presentational, claims) [editorial] — H2: Overstated claim: "These intervals ... rule out large effects in the pooled case". Pooled CI [-0.044,0.014] but no outcome SD or smallest effect of interest is given.
  - Suggested fix: Give the outcome SD and standardised bounds, or drop 'large'.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K6 (presentational, claims) [editorial] — Limitations: Overstated claim: "one significant arm out of 32 is about what chance could produce". Expected false positives are 1.6 at alpha .05; P(at least one) is about 0.81.
  - Suggested fix: State the expectation and probability precisely.
  - Disposition: claim checked against the tables by the orchestrator
- **medium** K7 (presentational, claims) [editorial] — Limitations: Overstated claim: "About 1,500 raw respondents are missing from the analysis sample". 6,086-4,547 = 1,539, but models use N=3,825 (H1) and 3,953 (H2), so about 2,100-2,260 are absent from the models.
  - Suggested fix: Report the flow to each model N.
  - Disposition: claim checked against the tables by the orchestrator

## Claim checks (review orchestrator)

- **overstated** (Abstract): "Only one intervention clearly reduced affective polarization" — H1 table: Perception gap video -2.333, p=0.0191, one of 32 uncorrected tests; 'What makes an American' is -2.647, p=0.059.
- **supported** (Abstract): "Perception gap video lowered the measure by 2.3 points (95% CI [−4.3, −0.4], p = 0.019)" — H1 table: -2.333, SE 0.995, CI [-4.283,-0.382], p=0.0191.
- **overstated** (Abstract): "Pooled across all interventions, affective polarization was 0.8 points lower (CI [−1.4, −0.2], p = 0.005)" — Random-effects pooled -0.819, SE 0.291, p=0.005, but arms share one control (n=229) so the SE is understated; tau²=0 is degenerate.
- **supported** (Abstract): "Support for undemocratic practices showed no distinguishable pooled difference (−0.015, CI [−0.044, +0.014])" — H2 pooled -0.015, SE 0.015, p=0.309; same shared-control SE caveat.
- **supported** (Abstract): "no individual arm ... differed clearly from control" — H2 table: smallest p is McCain video 0.082; all supported=no.
- **supported** (H1): "The other arms shown had intervals spanning zero" — All other 31 H1 CIs include 0; 'What makes an American' upper bound 0.102.
- **unsupported** (H2): "Estimates ranged roughly from −0.13 to +0.14" — H2 table: min -0.156 (Pro-democracy excerpt), max +0.145 (Media-profits image).
- **supported** (H1): "The Perception gap video, the largest arm at 641 respondents" — H1 n(arm)=641, the largest.
- **overstated** (Design): "arm sizes range from roughly 60 to 660" — H1 n(arm) runs from 48 (Jubilee free speech panel) to 641; 662 appears in H2.
- **overstated** (H2): "These intervals ... rule out large effects in the pooled case" — Pooled CI [-0.044,0.014] but no outcome SD or smallest effect of interest is given.
- **overstated** (Limitations): "one significant arm out of 32 is about what chance could produce" — Expected false positives are 1.6 at alpha .05; P(at least one) is about 0.81.
- **overstated** (Limitations): "About 1,500 raw respondents are missing from the analysis sample" — 6,086-4,547 = 1,539, but models use N=3,825 (H1) and 3,953 (H2), so about 2,100-2,260 are absent from the models.

## Editorial guidance

- Replace 'clearly reduced' with 'nominally significant (p=0.019), uncorrected, post hoc' everywhere, including the Abstract and Key findings.
- Add a sample-flow table by arm (raw, partisan filter, T33 removal, missing pre/post, per-model N) and fix the '60-660' and '1,500 missing' statements.
- Replace the approximate random-effects pooled result with a pooled any-treatment vs control regression with robust SEs, or label it clearly as approximate.
- Describe the IPW weights and add unweighted and complete-case sensitivity results.
- Define the outcome direction and SD, give standardised effects, and correct the H2 range to -0.16 to +0.14.
- Remove the irrelevant citations and the 'Planned treatment effects' figure; say all 32 arms are shown and reconcile 32 vs 33 arms.

## Author response (the writer's revision notes)

- K1: Abstract now says nominally significant (p=0.019), uncorrected, post hoc, likely inflated; 'clearly' removed.
- K2: Pooled figure labelled approximate in the abstract, takeaways and H1, noting the shared control; no new regression added since no such result is in the tables.
- K3: H2 range corrected to −0.16 to +0.14.
- K4: Arm sizes stated as 48 to 641 (H1) and 51 to 662 (H2).
- K5: Dropped the 'rule out large effects' claim; noted no SD or smallest effect of interest is available.
- K6: Stated expected 1.6 false positives and about 81% chance of at least one.
- K7: Flow reported to model Ns, 3,825 and 3,953, from 6,086 raw and 4,547 filtered.
- R1: Flow described in prose in the design notes; I could not build a per-arm table because the figures are not in the supplied tables.
- R5: Stated T33 and independents are excluded and reconciled 32 analysed arms vs 33 designed.
- R6: Stated that all 32 arms are shown and that there are 64 tests.
- R7: No citations or 'Planned' figure appear in my prose; those belong to the skeleton and are not editable here.
- A6: Noted that the outcome SD is not available, so no standardised effects are given; direction is stated as lower values meaning less polarization only where the tables imply it.
- A8: Replaced 'clearly reduced' with 'nominally significant' and stated the expected false positives.
- A11: Clarified 32 arms × 2 outcomes = 64 tests and the precise chance expectation.
- G1: Applied as in K1, including abstract and takeaways.
- G2: Partly done: the flow is given in prose, and the table cannot be added without data.
- G3: Pooled estimate labelled approximate.
- G4: Not done: no IPW or sensitivity results are in the supplied materials.
- G5: Corrected the H2 range. Outcome SD and standardised effects are not available, and this is stated.
- G6: Stated that all 32 arms are shown and reconciled the arm counts. The figure and citations are outside my sections.
- R3: Declined; no adjusted p-values added.
- A5: Declined; wording softened only.

## Sign-off on the revised text

Fix the Limitations false-positive arithmetic: 1.6 expected and 81% hold for 32 tests, but the text cites 64 tests (3.2 expected, about 96%).

- **supported** (Abstract, re-check of C1): "One intervention was nominally significant for affective polarization: the Perception gap video lowered the post-treatment thermometer-based measure by 2.3 points ... in an uncorrected, post hoc analysis, so the estimate is likely inflated" — H1 table: Perception gap video -2.333, p=0.0191, CI [-4.283,-0.382]; only arm with supported=yes.
- **supported** (Abstract, re-check of C2): "Perception gap video lowered ... by 2.3 points (95% CI [−4.3, −0.4], p = 0.019, two-sided)" — H1 table: -2.333, SE 0.995, p=0.0191.
- **supported** (Abstract, re-check of C3): "An approximate pooled estimate across arms was 0.8 points lower than control (95% CI [−1.4, −0.2])" — Pooled -0.819, SE 0.291, p=0.005; CI roughly [-1.39,-0.25]. Now labelled approximate because of the shared control.
- **supported** (Abstract, re-check of C4): "Support for undemocratic practices showed no distinguishable pooled difference (−0.015, 95% CI [−0.044, +0.014])" — H2 pooled -0.015, SE 0.015, p=0.309.
- **supported** (H2, re-check of C5): "No arm among the 32 shown moved support for undemocratic practices in a way distinguishable from control" — H2 table: smallest p is McCain 0.082; all supported=no.
- **supported** (H1, re-check of C6): "All 32 arms are shown in the table, and the others had intervals spanning zero" — All other 31 H1 CIs include 0; 'What makes an American' CI [-5.397,0.102].
- **supported** (H2, re-check of C7): "Estimates ranged from −0.16 to +0.14 on a scale where the control mean was 2.75" — H2 table: min -0.156, max +0.145, control mean 2.753.
- **supported** (H1, re-check of C8): "The Perception gap video, the largest arm at 641 respondents" — H1 n(arm)=641, the largest.
- **supported** (Design, re-check of C9): "Arm sizes run from 48 to 641 (H1) and 51 to 662 (H2)" — H1 min 48 (Jubilee panel), max 641; H2 min 51, max 662.
- **supported** (H2, re-check of C10): "These intervals are inconclusive. Without an outcome SD ... they cannot be called tight" — The 'rule out large effects' wording was removed; no SD is reported.
- **supported** (Limitations, re-check of C11): "Under the null, about 1.6 false positives are expected at the 5% level, and the chance of at least one is about 81%" — 64×0.05=3.2 expected across all 64 tests; 1.6 applies to 32 tests. 1-0.95^32≈0.81 also fits 32 tests, not 64.
- **supported** (Limitations, re-check of C12): "Of 6,086 raw respondents, 4,547 passed filters and the models use 3,825 (H1) and 3,953 (H2)" — H1 and H2 model N match the tables: 3,825 and 3,953.

## Unresolved questions (candidates for extensions)

- U1: Were arms randomised and fielded concurrently with the control, and is the Perception gap effect robust in a preregistered replication with adequate power? (Allocation and fielding details are not in the tables, and a single uncorrected nominal hit among 32 needs new data to confirm.)
- U2: Does differential attrition between raw and analysed samples bias the arm contrasts? (Reasons for the loss of roughly 2,000 respondents cannot be reconstructed from the tables.)

Analytical issues can be answered with robustness addenda: `filedrawer address <study>` proposes one per issue for approval.
