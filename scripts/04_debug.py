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
for col in ['post_ap', 'post_udp', 'pre_ap', 'pre_udp', 'ipw_weight']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

h1 = [h for h in reg.HYPOTHESES if h['outcome'] == 'post_ap'][0]
est = h1['estimator']

# Build formula for the full model (same as registered)
formula, d2 = reg.build_formula('post_ap', est, ['pre_ap'], df)

# Debug: print param names from full model
res_full = reg.fit(d2, formula, est)
print("Full model params:", list(res_full.params.index))
print("Formula:", formula)
print("d2 columns:", list(d2.columns))
