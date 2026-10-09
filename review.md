# Automated review: Light Pass

Models: light `anthropic/claude-sonnet-5.5`, orchestrator `anthropic/claude-sonnet-5.5`. The two headline estimates match the tables: the Perception gap video at −2.31 (p = 0.021) on affective polarization and the McCain video at +0.174 (p = 0.032) on support for undemocratic practices. Both are single significant arms out of 32 per outcome, are uncorrected, and rest on small arms, so they are fragile. The 'only arm' wording is fine as a description of significance, but the report's claims about the null arms and the E1 robustness check are weaker than stated. The most important caveat is that E1 is not a real robustness check, because the completers table is identical to the planned model (n = 3,772 in every row).

**Review outcome (round 1): 12 of 12 claims supported by the results after the agent's corrections (2 flagged claims corrected).**

- **high** R1 (presentational) [editorial] — E1: Text says 3,900 completers (87% of the sample) were used and calls this a robustness check. The E1 table shows n_completers = 3772 for every arm, identical to the planned n, with estimates and SEs identical to the planned ones. 3,900 appears in no table, and 3,900/4,485 is 87% only of the analysed 4,485, not the 3,772 used.
  - Suggested fix: Report that the completers table shows n = 3,772 and results identical to the planned ones, so it does not actually test sensitivity to dropping partial responses. Remove the 3,900 / 87% figures.
  - Disposition: The E1 prose misreports the completers n and the 3,900 / 87% figures; the table shows an identical sample, so the text must be corrected.
- **medium** R2 (presentational) [editorial] — H1: Text says the remaining arms' point estimates range 'between about −2.4 and +1.4'. The table shows −2.382 for 'What makes an American' and +1.355 for American history, so the range holds, but the sentence also says 'the remaining arms for which results are shown', while the other arms are not all shown. The Brené Brown (−2.137) and Patriotic (−1.959) arms are not mentioned.
  - Suggested fix: State that all 31 other arms had CIs including zero, with estimates from −2.38 to +1.36.
  - Disposition: The prose should state that all 31 other arms had CIs including zero, with estimates from −2.38 to +1.36.
- **medium** R3 (presentational) [editorial] — H2: Text says the other arms were 'within about ±0.15 points of control'. The table shows Media-profits-from-division at +0.162 (p = 0.097) and Pro-democracy excerpt at −0.145. The Media-profits arm exceeds ±0.15.
  - Suggested fix: Say the other arms ranged from about −0.15 to +0.16 points, none significant.
  - Disposition: The ±0.15 range is slightly wrong; Media-profits is +0.162.
- **low** R4 (presentational) [editorial] — Limitations: Text says arms are 'mostly under 200 respondents', while the design section says 'mostly 56 to 330'. Control n = 229 is not stated in the prose, although the report says control sizes are not shown.
  - Suggested fix: Use consistent arm-size wording. Control n = 229 appears in the summary table.
  - Disposition: Arm-size wording is inconsistent between the Design and Limitations sections.
- **low** R5 (presentational) [editorial] — Abstract: The 'Perception gap video' arm is described as about 640 people, while the table shows 641 for H1 and 646 for H2.
  - Suggested fix: Say 641 (H1) and 646 (H2).
  - Disposition: The arm n should be given as 641 (H1) and 646 (H2) instead of 'about 640'.
- **high** K1 (presentational, claims) [editorial] — E1: Unsupported claim: "Re-fitting on 3,900 completers (87% of the sample) ... planned H1 estimates are not sensitive to dropping partial responses". E1 table: n_completers = 3772 in every row, with estimates and SEs identical to the planned ones. 3,900 appears in no table.
  - Suggested fix: State that the completers fit used the same 3,772 respondents and gave identical results, so it does not test sensitivity to partial responses. Remove the 3,900 / 87% figures.
  - Disposition: claim checked against the tables by the checking agent
- **medium** K2 (presentational, claims) [editorial] — H2: Overstated claim: "The other arms shown were within about ±0.15 points of control". H2_arms T24 Media-profits-from-division: +0.162, outside ±0.15.
  - Suggested fix: Say the other arms ranged from about −0.15 to +0.16.
  - Disposition: claim checked against the tables by the checking agent

## Claim checks (checking agent)

- **supported** (Abstract): "The Perception gap video lowered affective polarization by 2.3 points (95% CI [−4.3, −0.4], p = 0.021)" — H1_arms T15: −2.307, CI [−4.262, −0.353], p = 0.021.
- **supported** (Abstract): "McCain defends Obama video raised support for undemocratic practices by 0.17 (CI [0.02, 0.33], p = 0.032)" — H2_arms T17: 0.174, CI [0.015, 0.332], p = 0.032.
- **supported** (Key findings): "only one of 32 interventions lowered affective polarization" — H1_arms summary: 1 of 32 with p < 0.05 (T15). The wording should say 'only one was distinguishable from control'.
- **supported** (Key findings): "the only registered arm with a detectable shift on that outcome" — H2_arms summary: 1 of 32 with p < 0.05, smallest p 0.032.
- **unsupported** (E1): "Re-fitting on 3,900 completers (87% of the sample) ... planned H1 estimates are not sensitive to dropping partial responses" — E1 table: n_completers = 3772 in every row, with estimates and SEs identical to the planned ones. 3,900 appears in no table.
- **overstated** (H2): "The other arms shown were within about ±0.15 points of control" — H2_arms T24 Media-profits-from-division: +0.162, outside ±0.15.
- **supported** (H1): "point estimates between about −2.4 and +1.4 points" — H1_arms: minimum −2.382 (T16), maximum +1.355 (T20).
- **supported** (E2/E3): "0 of 32 arm-by-group interactions significant (E2, E3)" — E2 summary: 0 of 32, smallest p 0.102. E3 summary: 0 of 32, smallest p 0.056.
- **supported** (H1): "Control respondents averaged 41.5 and the video group 39.6" — H1_arms T15: mean_control 41.459, mean_arm 39.587. These are raw means; the estimate is covariate-adjusted.
- **supported** (Abstract): "64 tests were run without correction" — registered_summary has 64 rows. The plan specifies no correction.

## Corrections requested by the checking agent

- Rewrite the E1 text and finding so they match the table: same 3,772 respondents, identical estimates, no sensitivity test.
- Fix the H2 range to −0.15 to +0.16.
- Make arm-size wording consistent and state the control n of 229 (H1) and 234 (H2).
- Fix the Perception gap n to 641 (H1) and 646 (H2).

## Corrections made by the writing agent

- K1: E1 text now says the completers fit used the same 3,772 respondents with identical results, so it tests no sensitivity; removed 3,900/87%.
- K2: H2 now says other arms ranged from about −0.15 to +0.16.
- G1: E1 rewritten to match the table (same respondents, identical estimates, no sensitivity test); the takeaway was adjusted too.
- G2: H2 range fixed to −0.15 to +0.16.
- G3: Arm sizes are now consistently 56 to 330 in the design notes and limitations; control n of 229 (H1) and 234 (H2) stated.
- G4: Perception gap n stated as 641 (H1) and 646 (H2) in the abstract and design notes.
- R1: Same fix as K1/G1 for E1.
- R2: H1 now says all 31 other arms had CIs including zero, with estimates from −2.38 to +1.36.
- R3: Same fix as K2 for H2.
- R4: Arm-size wording made consistent; control n stated.
- R5: Abstract now gives 641 and 646.
- F1: Removed the 3,900 / 87% / 'not sensitive' claim; the E1 finding and note now say only that the completers fit used the same 3,772 respondents with identical results and tests nothing new.

## Claim re-check on the corrected text

No further rewording needed; the previously flagged issues are resolved.

- **supported** (Abstract, re-check of C1): "The Perception gap video ... lowered affective polarization by 2.3 points relative to control (95% CI [−4.3, −0.4], p = 0.021)" — H1_arms T15: −2.307, CI [−4.262, −0.353], p = 0.021.
- **supported** (Abstract, re-check of C2): "McCain defends Obama video raised support for undemocratic practices by 0.17 scale points (95% CI [0.02, 0.33], p = 0.032)" — H2_arms T17: 0.174, CI [0.015, 0.332], p = 0.032.
- **supported** (Key findings, re-check of C3): "only one of 32 interventions, the Perception gap video, lowered affective polarization relative to control" — H1_arms summary: 1 of 32 with p < 0.05 (T15). The wording stays within the one significant result.
- **supported** (Key findings, re-check of C4): "the only registered arm with a detectable shift on that outcome" — H2_arms summary: 1 of 32 with p < 0.05, smallest p 0.032.
- **supported** (E1, re-check of C5): "Re-fitting on 3,900 completers (87% of the sample)... not sensitive to dropping partial responses" — Removed in revision. E1 now says the completers fit used the same 3,772 respondents with identical estimates and tests nothing new, which matches the E1 table.
- **supported** (H2, re-check of C6): "The other arms ranged from about −0.15 to +0.16 points relative to control, and none was distinguishable from it" — H2_arms: other arms run from −0.145 (T28) to +0.162 (T24). Only T17 has p < 0.05.
- **supported** (H1, re-check of C7): "All 31 other arms had intervals that included zero, with estimates from −2.38 to +1.36 points" — H1_arms: minimum −2.382 (T16), maximum +1.355 (T20). All other CIs include 0.
- **supported** (E2/E3, re-check of C8): "none of the 32 arm-by-Democratic-identification interactions was significant ... none of the 32 arm-by-political-interest interactions" — E2 summary: 0 of 32, smallest p 0.102. E3 summary: 0 of 32, smallest p 0.056.
- **supported** (H1, re-check of C9): "Control respondents averaged 41.5 and the video group 39.6" — H1_arms T15: mean_control 41.459, mean_arm 39.587. These are raw means, while the estimate is covariate-adjusted.
- **supported** (Abstract, re-check of C10): "64 tests were run without correction for multiple comparisons" — registered_summary has 64 rows. No correction is reported.
- **supported** (E3): "The closest, for Shared values exercise, was −6.9 points (95% CI [−14.0, 0.2])" — E3 row T4: −6.934, CI [−14.044, 0.177], p = 0.056, the smallest p in the table.
- **supported** (H1): "The 'What makes an American' video came closest (−2.4 points, 95% CI [−5.1, 0.4])" — H1_arms T16: −2.382, CI [−5.130, 0.366], p = 0.089, the smallest p among non-significant arms.
