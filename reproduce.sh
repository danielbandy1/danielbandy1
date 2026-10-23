#!/usr/bin/env bash
# AUTHORED BY ORION. Standard-library static content checks only.
set -euo pipefail
cd "$(dirname "$0")"
python3 portfolio_check.py
