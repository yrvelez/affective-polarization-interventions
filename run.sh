#!/usr/bin/env bash
# Runs the filedrawer pipeline on this study. Needs: pip install "filedrawer @ git+https://github.com/yrvelez/filedrawer"
# Inputs are NOT in this repository (the export holds respondent rows): point INPUTS at the folder holding
# pipeline_input.csv (built by prepare_pipeline_input.py), affective_polarization.qsf, pap.md and pap_labeled.json.
set -euo pipefail
cd "$(dirname "$0")"
: "${OPENROUTER_API_KEY:?set OPENROUTER_API_KEY (bring your own token)}"
INPUTS="${INPUTS:-$HOME/Projects/filedrawer/affective_polarization}"
filedrawer run \
  --csv "$INPUTS/pipeline_input.csv" --qsf "$INPUTS/affective_polarization.qsf" \
  --pap "$INPUTS/pap.md" --pap-json "$INPUTS/pap_labeled.json" \
  --arm-column arm --config filedrawer.config.yaml \
  --slug affective-polarization-interventions \
  --title "Testing 33 Student-Designed Interventions to Reduce Affective Polarization" \
  --authors "Yamil Velez" --repo-url https://github.com/yrvelez/affective-polarization-interventions \
  --package-dir . --review "${REVIEW:-light,advanced}" "$@"
