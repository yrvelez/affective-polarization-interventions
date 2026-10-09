import importlib.util, pathlib
import pandas as pd
import numpy as np

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
RES.mkdir(exist_ok=True)

clean = pd.read_csv(ROOT / 'data' / 'clean.csv', low_memory=False)
for c in ['Finished', 'pid3', 'interest']:
    clean[c] = pd.to_numeric(clean[c], errors='coerce')

H1 = reg.HYPOTHESES[0]


def sig_count(df):
    p = pd.to_numeric(df['p_value'], errors='coerce')
    return int((p < 0.05).sum()), int(p.notna().sum())


# E1: robustness to completers-only exclusion (Finished == 1)
orig = reg.reestimate(H1, clean)
sub = clean[clean['Finished'] == 1]
alt = reg.reestimate(H1, sub)
m = orig[['arm', 'estimate', 'std_error', 'n']].merge(
    alt[['arm', 'estimate', 'std_error', 'n']], on='arm', suffixes=('_planned', '_completers'))
m.to_csv(RES / 'E1_completers_only.csv', index=False)
n_ratio = len(sub) / len(clean)
se_ratio = (m['std_error_completers'] / m['std_error_planned']).abs()
print(f"E1 Completers-only robustness: planned H1 estimates re-fit on {len(sub)} completers ({n_ratio:.0%} of sample); median SE ratio {se_ratio.median():.2f}")

# E2: heterogeneity of planned H1 by Democratic identification
clean['is_dem'] = (clean['pid3'] == 2).astype(int)
het = reg.reestimate(H1, clean, moderator='is_dem')
het.to_csv(RES / 'E2_dem_heterogeneity.csv', index=False)
s, n = sig_count(het)
print(f"E2 Heterogeneity by Democratic identification: {s} of {n} arm-by-group interaction tests significant at p<0.05")

# E3: heterogeneity by political interest
clean['high_interest'] = (clean['interest'] >= 4).astype(int)
het2 = reg.reestimate(H1, clean, moderator='high_interest')
het2.to_csv(RES / 'E3_interest_heterogeneity.csv', index=False)
s2, n2 = sig_count(het2)
print(f"E3 Heterogeneity by high political interest: {s2} of {n2} arm-by-group interaction tests significant at p<0.05")
