"""
Exploratory analyses for the Affective Polarization survey experiment.
Three analyses:
  E1: Heterogeneity by party for T15 (only significant registered arm)
  E2: Robustness to attention-check failures
  E3: Component feeling-thermometer items for T15
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

# ── Load & clean ──────────────────────────────────────────────────────────────
df = pd.read_csv('data/clean.csv')
df_elig = df.dropna(subset=['post_ap', 'ipw_weight', 'pre_ap']).copy()

# ═══════════════════════════════════════════════════════════════════════════════
# E1: Heterogeneity by party for T15
# Rationale: T15 (perception-gap video) was the only arm with a significant
# effect on post_ap (p=.019); testing whether the effect differs by party
# identity helps interpret the mechanism.
# ═══════════════════════════════════════════════════════════════════════════════
df_e1 = df_elig[df_elig['arm_code'].isin(['T0', 'T15'])].copy()

results_e1 = []
for party in ['Democrat', 'Republican']:
    sub = df_e1[df_e1['partisan'] == party]
    formula = 'post_ap ~ C(arm_code, Treatment(reference="T0")) + pre_ap'
    model = smf.wls(formula, data=sub, weights=sub['ipw_weight']).fit(cov_type='HC2')
    term = 'C(arm_code, Treatment(reference="T0"))[T.T15]'
    if term in model.params.index:
        ci = model.conf_int().loc[term]
        results_e1.append({
            'party': party,
            'estimate': round(model.params[term], 4),
            'std_error': round(model.bse[term], 4),
            'p_value': round(model.pvalues[term], 4),
            'conf_low': round(ci[0], 4),
            'conf_high': round(ci[1], 4),
            'n': int(model.nobs)
        })

# Interaction model
df_e1['is_t15'] = (df_e1['arm_code'] == 'T15').astype(int)
df_e1['is_rep'] = (df_e1['partisan'] == 'Republican').astype(int)
formula_int = 'post_ap ~ is_t15 * is_rep + pre_ap'
model_int = smf.wls(formula_int, data=df_e1, weights=df_e1['ipw_weight']).fit(cov_type='HC2')
int_term = 'is_t15:is_rep'
ci_int = model_int.conf_int().loc[int_term]
results_e1.append({
    'party': 'Interaction (T15 x Republican)',
    'estimate': round(model_int.params[int_term], 4),
    'std_error': round(model_int.bse[int_term], 4),
    'p_value': round(model_int.pvalues[int_term], 4),
    'conf_low': round(ci_int[0], 4),
    'conf_high': round(ci_int[1], 4),
    'n': int(model_int.nobs)
})

e1_df = pd.DataFrame(results_e1)
e1_df.to_csv('results/E1_party_heterogeneity.csv', index=False)

# Figure E1
fig, ax = plt.subplots(figsize=(7, 3))
colors_e1 = ['#2171b5', '#cb181d', '#666666']
for i, row in e1_df.iterrows():
    ax.hlines(i, row['conf_low'], row['conf_high'], color=colors_e1[i], linewidth=2)
    ax.plot(row['estimate'], i, 'o', color=colors_e1[i], markersize=8)
ax.axvline(0, color='grey', linewidth=0.5, linestyle='--')
ax.set_yticks(range(len(e1_df)))
ax.set_yticklabels(e1_df['party'])
ax.set_xlabel('Effect on post_ap (95% CI)')
ax.set_title('E1: T15 Effect by Party')
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.grid(False)
plt.tight_layout()
plt.savefig('figures/E1_party_heterogeneity.png', dpi=200)
plt.close()

print(f"E1: T15 Dem={e1_df.loc[0,'estimate']:.3f} (p={e1_df.loc[0,'p_value']:.3f}), "
      f"Rep={e1_df.loc[1,'estimate']:.3f} (p={e1_df.loc[1,'p_value']:.3f}), "
      f"interaction p={model_int.pvalues[int_term]:.3f}")

# ═══════════════════════════════════════════════════════════════════════════════
# E2: Robustness to attention-check failures
# Rationale: Excluding respondents who failed 2+ of 3 knowledge questions tests
# whether inattentive respondents add noise that obscures true treatment effects.
# ═══════════════════════════════════════════════════════════════════════════════
df_e2 = df_elig.copy()
# Correct answers: pk1=3 (six years), pk2=2 (twice), pk3=1 (Sunak)
df_e2['n_wrong'] = (
    (df_e2['pk1'] != 3).astype(int) +
    (df_e2['pk2'] != 2).astype(int) +
    (df_e2['pk3'] != 1).astype(int)
)
df_e2['n_wrong'] = df_e2['n_wrong'].fillna(3)  # missing = wrong
df_e2_pass = df_e2[df_e2['n_wrong'] <= 1]
n_excluded = len(df_e2) - len(df_e2_pass)

formula_e2 = 'post_ap ~ C(arm_code, Treatment(reference="T0")) + pre_ap'
model_e2 = smf.wls(formula_e2, data=df_e2_pass, weights=df_e2_pass['ipw_weight']).fit(cov_type='HC2')

arms = [f'T{i}' for i in range(1, 33)]
e2_rows = []
for arm in arms:
    term = f'C(arm_code, Treatment(reference="T0"))[T.{arm}]'
    if term in model_e2.params.index:
        ci = model_e2.conf_int().loc[term]
        e2_rows.append({
            'arm_code': arm,
            'estimate': round(model_e2.params[term], 4),
            'std_error': round(model_e2.bse[term], 4),
            'p_value': round(model_e2.pvalues[term], 4),
            'conf_low': round(ci[0], 4),
            'conf_high': round(ci[1], 4)
        })

e2_df = pd.DataFrame(e2_rows)
e2_df.to_csv('results/E2_attention_check_robustness.csv', index=False)

# Figure E2
fig, ax = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(e2_df))
colors_e2 = ['#cb181d' if p < 0.05 else '#2171b5' for p in e2_df['p_value']]
ax.hlines(y_pos, e2_df['conf_low'], e2_df['conf_high'], color=colors_e2, linewidth=1.5)
ax.scatter(e2_df['estimate'], y_pos, c=colors_e2, s=25, zorder=5)
ax.axvline(0, color='grey', linewidth=0.5, linestyle='--')
ax.set_yticks(list(y_pos))
ax.set_yticklabels(e2_df['arm_code'], fontsize=7)
ax.set_xlabel('Effect on post_ap (95% CI)')
ax.set_title(f'E2: Attention-check passers only (n={len(df_e2_pass)}, excluded {n_excluded})')
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.grid(False)
plt.tight_layout()
plt.savefig('figures/E2_attention_check.png', dpi=200)
plt.close()

sig_arms = e2_df[e2_df['p_value'] < 0.05]['arm_code'].tolist()
print(f"E2: Excluded {n_excluded} inattentive (n={len(df_e2_pass)}), "
      f"significant arms: {sig_arms if sig_arms else 'none'}")

# ═══════════════════════════════════════════════════════════════════════════════
# E3: Component feeling-thermometer items for T15
# Rationale: Decomposing the composite post_ap into its two component items
# reveals whether T15 works by increasing in-party warmth or decreasing
# out-party warmth (or both).
# ═══════════════════════════════════════════════════════════════════════════════
df_e3 = df_elig[df_elig['arm_code'].isin(['T0', 'T15'])].copy()

e3_rows = []
for col in ['post_ap_scores_1', 'post_ap_scores_2']:
    sub = df_e3.dropna(subset=[col])
    formula_e3 = f'{col} ~ C(arm_code, Treatment(reference="T0")) + pre_ap'
    model_e3 = smf.wls(formula_e3, data=sub, weights=sub['ipw_weight']).fit(cov_type='HC2')
    term = 'C(arm_code, Treatment(reference="T0"))[T.T15]'
    if term in model_e3.params.index:
        ci = model_e3.conf_int().loc[term]
        e3_rows.append({
            'component': col,
            'estimate': round(model_e3.params[term], 4),
            'std_error': round(model_e3.bse[term], 4),
            'p_value': round(model_e3.pvalues[term], 4),
            'conf_low': round(ci[0], 4),
            'conf_high': round(ci[1], 4),
            'n': int(model_e3.nobs)
        })

e3_df = pd.DataFrame(e3_rows)
e3_df.to_csv('results/E3_component_items.csv', index=False)

print(f"E3: T15 on post_ap_scores_1={e3_df.loc[0,'estimate']:.3f} (p={e3_df.loc[0,'p_value']:.3f}), "
      f"post_ap_scores_2={e3_df.loc[1,'estimate']:.3f} (p={e3_df.loc[1,'p_value']:.3f})")
