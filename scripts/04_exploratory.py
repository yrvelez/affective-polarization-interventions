"""Exploratory analyses for the Affective Polarization survey experiment."""
import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load data ──────────────────────────────────────────────────────────────────
df = pd.read_csv('data/clean.csv')
for c in ['post_ap', 'post_udp', 'pre_ap', 'pre_udp', 'ipw_weight', 'interest']:
    df[c] = pd.to_numeric(df[c], errors='coerce')

if 'arm_code' not in df.columns:
    df['arm_code'] = df['arm']

pathlib.Path('results').mkdir(exist_ok=True)
pathlib.Path('figures').mkdir(exist_ok=True)

def style_ax(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.grid(False)
    ax.tick_params(left=False)

INK = '#1a1a1a'
ACCENT = '#2171b5'

# ── Helper: fit registered model on a subset, return treat coefficient ─────────
def fit_subset(df_sub, outcome, h):
    """Fit the registered model on a subset; return (estimate, se, p, n)."""
    est = h['estimator']
    covs = est['covariates']
    d = df_sub.dropna(subset=[outcome] + covs + ['ipw_weight']).copy()
    formula, d2 = reg.build_formula(outcome, est, covs, d)
    res = reg.fit(d2, formula, est)
    if 'treat' in res.params.index:
        return res.params['treat'], res.bse['treat'], res.pvalues['treat'], int(d2.shape[0])
    return np.nan, np.nan, np.nan, int(d2.shape[0])

# ═══════════════════════════════════════════════════════════════════════════════
# E1: Heterogeneity by respondent party (Democrat vs Republican)
# Rationale: The interventions target cross-partisan attitudes; effects may
#       differ for Democrats vs Republicans, which the pooled estimate masks.
# ═══════════════════════════════════════════════════════════════════════════════
h1 = reg.HYPOTHESES[0]  # post_ap
h2 = reg.HYPOTHESES[1]  # post_udp

df['is_dem'] = (df['pid3'] == 2).astype(int)
df['is_rep'] = (df['pid3'] == 1).astype(int)

rows_e1 = []
for outcome, h in [('post_ap', h1), ('post_udp', h2)]:
    for label, mask in [('Democrat', df['is_dem'] == 1), ('Republican', df['is_rep'] == 1)]:
        est_v, se_v, p_v, n_v = fit_subset(df[mask], outcome, h)
        rows_e1.append({
            'outcome': outcome,
            'group': label,
            'estimate': est_v,
            'std_error': se_v,
            'p_value': p_v,
            'n': n_v,
        })

e1 = pd.DataFrame(rows_e1)
e1.to_csv('results/E1_heterogeneity_party.csv', index=False)

# Figure: forest plot for post_ap, Democrats vs Republicans
fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
for ax, grp in zip(axes, ['Democrat', 'Republican']):
    sub = e1[(e1['outcome'] == 'post_ap') & (e1['group'] == grp)]
    y = np.arange(len(sub))
    ax.errorbar(sub['estimate'], y,
                xerr=1.96 * sub['std_error'],
                fmt='o', color=INK, ms=5, capsize=4, lw=1.2)
    ax.axvline(0, color='grey', lw=0.5, ls='--')
    ax.set_yticks(y)
    ax.set_yticklabels(sub['outcome'], fontsize=9)
    ax.set_xlabel('ATE', fontsize=10)
    ax.set_title(grp, fontsize=11, color=INK)
    style_ax(ax)
fig.tight_layout()
fig.savefig('figures/E1_heterogeneity_party.png', dpi=200, bbox_inches='tight')
plt.close(fig)

sig_dem_ap = e1[(e1['outcome'] == 'post_ap') & (e1['group'] == 'Democrat') & (e1['p_value'] < 0.05)]['estimate'].values
sig_rep_ap = e1[(e1['outcome'] == 'post_ap') & (e1['group'] == 'Republican') & (e1['p_value'] < 0.05)]['estimate'].values
print(f"E1: Party heterogeneity (post_ap) — Democrat ATE={e1[(e1['outcome']=='post_ap')&(e1['group']=='Democrat')]['estimate'].values[0]:.3f} (p={e1[(e1['outcome']=='post_ap')&(e1['group']=='Democrat')]['p_value'].values[0]:.3f}), Republican ATE={e1[(e1['outcome']=='post_ap')&(e1['group']=='Republican')]['estimate'].values[0]:.3f} (p={e1[(e1['outcome']=='post_ap')&(e1['group']=='Republican')]['p_value'].values[0]:.3f}).")

# ═══════════════════════════════════════════════════════════════════════════════
# E2: Robustness — exclude respondents who failed all 3 knowledge checks
# Rationale: Respondents who failed all knowledge checks may not have
#       engaged with the survey; excluding them tests whether results are
#       driven by inattentive respondents.
# ═══════════════════════════════════════════════════════════════════════════════
df['pk1_correct'] = (df['pk1'] == 3).astype(int)
df['pk2_correct'] = (df['pk2'] == 2).astype(int)
df['pk3_correct'] = (df['pk3'] == 1).astype(int)
df['failed_all_kc'] = ((df['pk1_correct'] == 0) &
                       (df['pk2_correct'] == 0) &
                       (df['pk3_correct'] == 0)).astype(int)

n_failed = int(df['failed_all_kc'].sum())
n_total = len(df)
pct_failed = 100 * n_failed / n_total

rows_e2 = []
for outcome, h in [('post_ap', h1), ('post_udp', h2)]:
    # Full sample
    est_f, se_f, p_f, n_f = fit_subset(df, outcome, h)
    # Excluding all-KC-failures
    est_e, se_e, p_e, n_e = fit_subset(df[df['failed_all_kc'] == 0], outcome, h)
    rows_e2.append({
        'outcome': outcome,
        'est_full': est_f, 'se_full': se_f, 'p_full': p_f, 'n_full': n_f,
        'est_excl': est_e, 'se_excl': se_e, 'p_excl': p_e, 'n_excl': n_e,
        'se_ratio': se_e / se_f if se_f > 0 else np.nan,
    })

e2 = pd.DataFrame(rows_e2)
e2.to_csv('results/E2_robustness_kc.csv', index=False)

max_se_ratio = e2['se_ratio'].max()
n_change = 100 * (1 - e2['n_excl'].iloc[0] / e2['n_full'].iloc[0])
print(f"E2: KC robustness — excluded {n_failed} respondents ({pct_failed:.1f}%), max SE ratio = {max_se_ratio:.2f}, sample change = {n_change:.1f}%.")

# ═══════════════════════════════════════════════════════════════════════════════
# E3: Heterogeneity by political interest (high vs low)
# Rationale: Politically interested respondents may be more responsive to
#       cross-partisan interventions; this tests whether null pooled results
#       mask a subgroup effect among the highly interested.
# ═══════════════════════════════════════════════════════════════════════════════
df['hi_interest'] = (df['interest'] >= 4).astype(int)
df['lo_interest'] = (df['interest'] <= 2).astype(int)

rows_e3 = []
for outcome, h in [('post_ap', h1), ('post_udp', h2)]:
    for label, mask in [('High interest', df['hi_interest'] == 1),
                        ('Low interest', df['lo_interest'] == 1)]:
        est_v, se_v, p_v, n_v = fit_subset(df[mask], outcome, h)
        rows_e3.append({
            'outcome': outcome,
            'group': label,
            'estimate': est_v,
            'std_error': se_v,
            'p_value': p_v,
            'n': n_v,
        })

e3 = pd.DataFrame(rows_e3)
e3.to_csv('results/E3_heterogeneity_interest.csv', index=False)

# Figure: forest plot for post_ap, high vs low interest
fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
for ax, grp in zip(axes, ['High interest', 'Low interest']):
    sub = e3[(e3['outcome'] == 'post_ap') & (e3['group'] == grp)]
    y = np.arange(len(sub))
    ax.errorbar(sub['estimate'], y,
                xerr=1.96 * sub['std_error'],
                fmt='o', color=INK, ms=5, capsize=4, lw=1.2)
    ax.axvline(0, color='grey', lw=0.5, ls='--')
    ax.set_yticks(y)
    ax.set_yticklabels(sub['outcome'], fontsize=9)
    ax.set_xlabel('ATE', fontsize=10)
    ax.set_title(grp, fontsize=11, color=INK)
    style_ax(ax)
fig.tight_layout()
fig.savefig('figures/E3_heterogeneity_interest.png', dpi=200, bbox_inches='tight')
plt.close(fig)

hi_ap = e3[(e3['outcome'] == 'post_ap') & (e3['group'] == 'High interest')].iloc[0]
lo_ap = e3[(e3['outcome'] == 'post_ap') & (e3['group'] == 'Low interest')].iloc[0]
print(f"E3: Interest heterogeneity (post_ap) — High ATE={hi_ap['estimate']:.3f} (p={hi_ap['p_value']:.3f}, n={hi_ap['n']}), Low ATE={lo_ap['estimate']:.3f} (p={lo_ap['p_value']:.3f}, n={lo_ap['n']}).")
