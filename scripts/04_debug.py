import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

import pandas as pd
import numpy as np

df = pd.read_csv('data/clean.csv')
for col in ['post_ap', 'pre_ap', 'post_udp', 'pre_udp', 'ipw_weight']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

h1 = [h for h in reg.HYPOTHESES if h['id'] == 'H1'][0]
est = h1['estimator']
outcome = 'post_ap'
covariates = ['pre_ap']

df_elig = df.dropna(subset=['post_ap', 'ipw_weight']).copy()
df_sub = df_elig[df_elig['partisan'] == 'Democrat'].copy()
print(f"df_sub shape: {df_sub.shape}")
print(f"df_sub columns with 'arm': {[c for c in df_sub.columns if 'arm' in c.lower()]}")

formula, d2 = reg.build_formula(outcome, est, covariates, df_sub)
print(f"formula: {formula}")
print(f"d2 shape: {d2.shape}")
print(f"d2 columns with 'arm': {[c for c in d2.columns if 'arm' in c.lower()]}")
print(f"d2 arm_code values: {sorted(d2['arm_code'].unique()) if 'arm_code' in d2.columns else 'NO arm_code col'}")

res = reg.fit(d2, formula, est)
print(f"res.params index (first 10): {list(res.params.index[:10])}")
print(f"res.nobs: {res.nobs}")
