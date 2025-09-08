#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$SCRIPT_DIR/labs/02_integration/backend-dev"
cd "$APP_DIR"
if [[ "${1:-}" == "--fresh" ]]; then rm -rf .venv; fi
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip >/dev/null
pip install -r requirements.txt
echo "✅ DEV http://127.0.0.1:8080/docs  (admin_dev / pass_1234)"
uvicorn main:app --reload --port 8080
