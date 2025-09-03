#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$SCRIPT_DIR/labs/02_integration/backend-qa"
cd "$APP_DIR"
if [[ "${1:-}" == "--fresh" ]]; then rm -rf .venv; fi
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip >/dev/null
pip install -r requirements.txt
echo "✅ QA  http://127.0.0.1:9090/docs  (admin_qa / pass_5678)"
uvicorn main:app --reload --port 9090
