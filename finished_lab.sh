#!/usr/bin/env bash
set -euo pipefail
MSG="${1:-Lab: work completed}"
BRANCH="$(git branch --show-current)"

git add .
git commit -m "$MSG"
git push -u origin "$BRANCH"
echo "Pushed $BRANCH. Create PR: your fork → teacher main."


# RUN SCRIPT WITH MESSAGE AT THE END, FOR EXAMPLE
# ./finished_lab.sh "Completed selenium scriot for lab 03"