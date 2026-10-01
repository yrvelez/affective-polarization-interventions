"""
Exploratory analyses for the Affective Polarization survey experiment.
Three analyses:
  E1: Heterogeneity by partisan identity (Democrat vs Republican)
  E2: Robustness to attention-check failures
  E3: Effects on component feeling-thermometer items
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

INK = '#222222'
ACCENT = '#1a6fb5'
plt.rcParams.update({
    'font.size': 9,
    'axes.edgecolor': INK,
    'text.color': INK,
    'axes.labelcolor': INK,
    'xtick.color': INK,
    'ytick.color': INK,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

def style_ax(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(False)
    ax.tick_params(left=False)

def extract_arm_effects(model, prefix='C(arm_code'):
    """Extract per-arm coefficients from a statsmodels result."""
    rows = []
    ci = model.conf_int()
    for term in model.params.index:
        if term.startswith(prefix):
            arm = term.split('[')[1].split(']')[0].replace('T.', '')
            rows.append({
                'arm': arm,
                'estimate': model.params[term],
                'std_error': model.bse[term],
                'p_value': model.pvalues[term],
                'conf_low': ci.loc[term, 0],
                'conf_high': ci.loc[term, 1],
                'n': int(model.nobs),
            })
    return pd.DataFrame(rows)

def arm_sort_key(x):
    return int(x[1:])

# ── Load data ──────────────────────────────────────────────────────────────────
df = pd.read_csv('data/clean.csv')

# ============================================================
# E1: Heterogeneity by partisan identity
# Rationale: Interventions targeting affective polarization may have
# asymmetric effects by party, and pooling could mask significant
# effects in one subgroup.
# ============================================================
print("=" * 60)
print("E1: Heterogeneity by partisan identity")
print("=" * 60)

e1_rows = []
for party in ['Democrat', 'Republican']:
    sub = df.dropna(subset=['post_ap', 'pre_ap'])
    sub = sub[sub['partisan'] == party].copy()
    if len(sub) < 100:
        print(f"  Skipping {party}: n={len(sub)}")
        continue
    formula = 'post_ap ~ C(arm_code, Treatment(reference="T0")) + pre_ap'
    model = smf.wls(formula, data=sub, weights=sub['ipw_weight']).fit(cov_type='HC2')
    eff = extract_arm_effects(model)
    eff['party'] = party
    e1_rows.append(eff)

e1_df = pd.concat(e1_rows, ignore_index=True)
e1_df.to_csv('results/E1_heterogeneity_party.csv', index=False)

# Summary
for party in ['Democrat', 'Republican']:
    sub = e1_df[e1_df['party'] == party].sort_values('p_value')
    if len(sub) > 0:
        best = sub.iloc[0]
        n_sig = (sub['p_value'] < 0.05).sum()
        print(f"  {party}: n={sub['n'].iloc[0]}, {n_sig} arms sig at p<.05, "
              f"best={best['arm']} (b={best['estimate']:.2f}, p={best['p_value']:.3f})")

# Figure E1
fig, ax = plt.subplots(figsize=(9, 10))

dem_arms = sorted(e1_df[e1_df['party'] == 'Democrat']['arm'].unique(), key=arm_sort_key)
rep_arms = sorted(e1_df[e1_df['party'] == 'Republican']['arm'].unique(), key=arm_sort_key)

y_dem = np.arange(len(dem_arms))
y_rep = np.arange(len(rep_arms)) + len(dem_arms) + 2

sub_dem = e1_df[e1_df['party'] == 'Democrat'].set_index('arm').loc[dem_arms].reset_index()
sub_rep = e1_df[e1_df['party'] == 'Republican'].set_index('arm').loc[rep_arms].reset_index()

ax.hlines(y_dem, sub_dem['conf_low'], sub_dem['conf_high'],
          color=ACCENT, alpha=0.4, linewidth=1.2)
ax.scatter(sub_dem['estimate'], y_dem, color=ACCENT, s=28, zorder=3,
           edgecolors='white', linewidths=0.5)

ax.hlines(y_rep, sub_rep['conf_low'], sub_rep['conf_high'],
          color=ACCENT, alpha=0.4, linewidth=1.2)
ax.scatter(sub_rep['estimate'], y_rep, color=ACCENT, s=28, zorder=3,
           edgecolors='white', linewidths=0.5)

ax.axvline(0, color=INK, linewidth=0.6, linestyle='--', alpha=0.6)

all_yticks = np.concatenate([y_dem, y_rep])
all_labels = dem_arms + rep_arms
ax.set_yticks(all_yticks)
ax.set_yticklabels(all_labels, fontsize=7)
ax.set_xlabel('Treatment effect on post_ap (HC2 robust SE)')
ax.set_title('E1: Treatment effects by partisan identity', fontsize=11, fontweight='bold')
style_ax(ax)

# Group labels
ax.text(0.98, 0.52, 'Democrats', transform=ax.transAxes, fontsize=10,
        color=INK, va='center', ha='right', fontweight='bold')
ax.text(0.98, 0.02, 'Republicans', transform=ax.transAxes, fontsize=10,
        color=INK, va='center', ha='right', fontweight='bold')

plt.tight_layout()
plt.savefig('figures/E1_heterogeneity_party.png', dpi=200, bbox_inches='tight')
plt.close()
print("  Figure saved: figures/E1_heterogeneity_party.png")

# ============================================================
# E2: Robustness to attention-check failures
# Rationale: Inattentive respondents may add noise that obscures
# true treatment effects; excluding them tests whether null results
# are driven by low-quality data.
# ============================================================
print("\n" + "=" * 60)
print("E2: Robustness to attention-check failures")
print("=" * 60)

# Correct answers: pk1=3 (Six years), pk2=2 (Twice), pk3=1 (Richi Sunak)
df['ac_wrong'] = (
    (df['pk1'] != 3).astype(float) +
    (df['pk2'] != 2).astype(float) +
    (df['pk3'] != 1).astype(float)
)
df.loc[df[['pk1', 'pk2', 'pk3']].isna().all(axis=1), 'ac_wrong'] = np.nan
df['ac_pass'] = (df['ac_wrong'] <= 1).astype(int)
df.loc[df['ac_wrong'].isna(), 'ac_pass'] = 1  # keep those who skipped AC

df_ap_full = df.dropna(subset=['post_ap', 'pre_ap']).copy()
df_ap_clean = df_ap_full[df_ap_full['ac_pass'] == 1].copy()

n_full = len(df_ap_full)
n_clean = len(df_ap_clean)
n_excl = n_full - n_clean
print(f"  Full sample: N={n_full} | AC-pass: N={n_clean} | Excluded: {n_excl} ({100*n_excl/n_full:.1f}%)")

e2_rows = []
for label, sub in [('full', df_ap_full), ('ac_pass', df_ap_clean)]:
    formula = 'post_ap ~ C(arm_code, Treatment(reference="T0")) + pre_ap'
    model = smf.wls(formula, data=sub, weights=sub['ipw_weight']).fit(cov_type='HC2')
    eff = extract_arm_effects(model)
    eff['sample'] = label
    e2_rows.append(eff)

e2_df = pd.concat(e2_rows, ignore_index=True)
e2_df.to_csv('results/E2_attention_check_robustness.csv', index=False)

sig_full = (e2_df[e2_df['sample'] == 'full']['p_value'] < 0.05).sum()
sig_clean = (e2_df[e2_df['sample'] == 'ac_pass']['p_value'] < 0.05).sum()
print(f"  Significant arms (p<.05): full={sig_full}, AC-pass={sig_clean}")
print(f"  Pattern unchanged: {sig_full == sig_clean}")

# ============================================================
# E3: Effects on component feeling-thermometer items
# Rationale: The composite post_ap (difference score) may mask
# differential effects on in-party vs out-party ratings; examining
# components reveals the mechanism.
# ============================================================
print("\n" + "=" * 60)
print("E3: Effects on component feeling-thermometer items")
print("=" * 60)

e3_rows = []

# Component 1: rating of group1
df_c1 = df.dropna(subset=['post_ap_scores_1', 'pre_ap_scores_1']).copy()
formula_c1 = 'post_ap_scores_1 ~ C(arm_code, Treatment(reference="T0")) + pre_ap_scores_1'
model_c1 = smf.wls(formula_c1, data=df_c1, weights=df_c1['ipw_weight']).fit(cov_type='HC2')
eff_c1 = extract_arm_effects(model_c1)
eff_c1['component'] = 'group1_rating'
e3_rows.append(eff_c1)

# Component 2: rating of group2
df_c2 = df.dropna(subset=['post_ap_scores_2', 'pre_ap_scores_2']).copy()
formula_c2 = 'post_ap_scores_2 ~ C(arm_code, Treatment(reference="T0")) + pre_ap_scores_2'
model_c2 = smf.wls(formula_c2, data=df_c2, weights=df_c2['ipw_weight']).fit(cov_type='HC2')
eff_c2 = extract_arm_effects(model_c2)
eff_c2['component'] = 'group2_rating'
e3_rows.append(eff_c2)

e3_df = pd.concat(e3_rows, ignore_index=True)
e3_df.to_csv('results/E3_component_items.csv', index=False)

sig_c1 = (e3_df[(e3_df['component'] == 'group1_rating') & (e3_df['p_value'] < 0.05)]).shape[0]
sig_c2 = (e3_df[(e3_df['component'] == 'group2_rating') & (e3_df['p_value'] < 0.05)]).shape[0]
print(f"  N group1: {df_c1.shape[0]}, N group2: {df_c2.shape[0]}")
print(f"  Significant arms: group1={sig_c1}, group2={sig_c2}")

# Show largest effects
for comp in ['group1_rating', 'group2_rating']:
    sub = e3_df[e3_df['component'] == comp].copy()
    sub['abs_b'] = sub['estimate'].abs()
    top = sub.nlargest(3, 'abs_b')[['arm', 'estimate', 'p_value']]
    print(f"  {comp} top-3 by |b|: " +
          ", ".join([f"{r['arm']} (b={r['estimate']:.2f}, p={r['p_value']:.3f})" for _, r in top.iterrows()]))

# Figure E3
fig, ax = plt.subplots(figsize=(9, 10))

c1_arms = sorted(e3_df[e3_df['component'] == 'group1_rating']['arm'].unique(), key=arm_sort_key)
c2_arms = sorted(e3_df[e3_df['component'] == 'group2_rating']['arm'].unique(), key=arm_sort_key)

y_c1 = np.arange(len(c1_arms))
y_c2 = np.arange(len(c2_arms)) + len(c1_arms) + 2

sub_c1 = e3_df[e3_df['component'] == 'group1_rating'].set_index('arm').loc[c1_arms].reset_index()
sub_c2 = e3_df[e3_df['component'] == 'group2_rating'].set_index('arm').loc[c2_arms].reset_index()

ax.hlines(y_c1, sub_c1['conf_low'], sub_c1['conf_high'],
          color=ACCENT, alpha=0.4, linewidth=1.2)
ax.scatter(sub_c1['estimate'], y_c1, color=ACCENT, s=28, zorder=3,
           edgecolors='white', linewidths=0.5)

ax.hlines(y_c2, sub_c2['conf_low'], sub_c2['conf_high'],
          color=ACCENT, alpha=0.4, linewidth=1.2)
ax.scatter(sub_c2['estimate'], y_c2, color=ACCENT, s=28, zorder=3,
           edgecolors='white', linewidths=0.5)

ax.axvline(0, color=INK, linewidth=0.6, linestyle='--', alpha=0.6)

all_yticks_e3 = np.concatenate([y_c1, y_c2])
all_labels_e3 = c1_arms + c2_arms
ax.set_yticks(all_yticks_e3)
ax.set_yticklabels(all_labels_e3, fontsize=7)
ax.set_xlabel('Treatment effect on feeling thermometer (HC2 robust SE)')
ax.set_title('E3: Effects on component feeling-thermometer items', fontsize=11, fontweight='bold')
style_ax(ax)

ax.text(0.98, 0.52, 'Group 1 rating', transform=ax.transAxes, fontsize=10,
        color=INK, va='center', ha='right', fontweight='bold')
ax.text(0.98, 0.02, 'Group 2 rating', transform=ax.transAxes, fontsize=10,
        color=INK, va='center', ha='right', fontweight='bold')

plt.tight_layout()
plt.savefig('figures/E3_component_items.png', dpi=200, bbox_inches='tight')
plt.close()
print("  Figure saved: figures/E3_component_items.png")

print("\nAll exploratory analyses complete.")
