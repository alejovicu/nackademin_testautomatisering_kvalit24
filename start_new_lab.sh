#!/usr/bin/env bash
set -euo pipefail
LAB_NUM="${1:-}"  # e.g. 03
YOUR_NAME="daniel_bostrom"

if [[ -z "$LAB_NUM" ]]; then
  echo "Usage: ./start-new-lab.sh <LAB_NUM>"; exit 1
fi

git checkout main
git fetch upstream
git pull --ff-only upstream main
git push origin main
git switch -c "lab_${LAB_NUM}_${YOUR_NAME}"
echo "Ready on branch: lab_${LAB_NUM}_${YOUR_NAME}"



# RUN EVERY LAB WITH THE NUMBER AT THE END, FOR EXAMPLE 
# ./start-new-lab.sh 04
# ./start-new-lab.sh 05