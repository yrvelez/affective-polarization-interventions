import importlib.util, pathlib
import pandas as pd

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
RES.mkdir(exist_ok=True)

d = pd.read_csv(ROOT / 'data' / 'clean.csv')
for c in ['pre_ap', 'post_ap', 'pre_udp', 'post_udp', 'Finished', 'ipw_weight']:
    if c in d.columns:
        d[c] = pd.to_numeric(d[c], errors='coerce')

H1 = reg.HYPOTHESES[0]
H2 = reg.HYPOTHESES[1]

# E1: completers-only re-fit of planned H1 and H2.
# Rationale: partial completers may differ in attention, so the planned estimates are re-fit on completed surveys to check stability.
rows = []
for hid, h in [('H1', H1), ('H2', H2)]:
    orig = reg.reestimate(h, d).assign(analysis=hid, sample='planned_full')
    sub = d[d['Finished'] == 1]
    re = reg.reestimate(h, sub).assign(analysis=hid, sample='completers_only')
    rows.append(orig)
    rows.append(re)
e1 = pd.concat(rows, ignore_index=True)
e1.to_csv(RES / 'E1_completers_robustness.csv', index=False)
p = e1.pivot_table(index=['analysis', 'arm'], columns='sample',
                   values=['estimate', 'std_error', 'n'], aggfunc='first')
p.columns = [f'{a}_{b}' for a, b in p.columns]
p = p.reset_index()
dev = (p['estimate_completers_only'] - p['estimate_planned_full']).abs().max()
ncount = {k: int((v < 0.05).sum()) for k, v in e1.groupby(['analysis', 'sample'])['p_value']}
print(f"E1 Completers-only re-fit of planned tests: largest absolute change in an arm estimate is {dev:.2f}; "
      f"arm contrasts with p<0.05 (of 32 per hypothesis) planned vs completers-only: "
      f"H1 {ncount.get(('H1','planned_full'),0)} vs {ncount.get(('H1','completers_only'),0)}, "
      f"H2 {ncount.get(('H2','planned_full'),0)} vs {ncount.get(('H2','completers_only'),0)}")

# E2: arm x partisan (Democrat vs other) interaction on the planned H1 outcome.
# Rationale: the pooled planned test may hide opposite responses between Democrats and Republicans, so arm effects are compared across the two groups.
d['dem'] = (d['partisan'].astype(str).str.strip() == 'Democrat').astype(int)
m = reg.reestimate(H1, d, moderator='dem')
m.to_csv(RES / 'E2_partisan_heterogeneity.csv', index=False)
print(f"E2 Arm x Democrat interaction on post_ap: {int((m['p_value'] < 0.05).sum())} of {len(m)} "
      f"interaction rows have p<0.05 (planned-style test, 32 arms; no multiplicity correction applied)")
