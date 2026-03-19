#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

function info() { echo "[toolcheck] $*"; }

info "Checking arXiv helper"
python3 tools/arxiv_search.py --query "test" --max-results 1 --json >/dev/null

info "Checking QMD availability"
qmd status >/dev/null

info "Checking Hugging Face token"
if [[ ! -f "$HOME/.huggingface/token" ]]; then
  echo "Hugging Face token file missing at ~/.huggingface/token" >&2
  exit 1
fi

info "All checks passed"
