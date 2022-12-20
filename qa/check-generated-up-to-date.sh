#!/usr/bin/env bash
#
# Checks if the (manually) generated files are up-to-date.

set -eux

function check_generated {
  local file=$1
  local script=$2

  echo "checking if $file is up-to-date.."
  tmp_generated=$(mktemp)
  python3 "contrib/$script" "$tmp_generated"
  diff_output="$(diff generated/$file $tmp_generated --color=always --minimal || true)"
  rm $tmp_generated

  if [[ -z $diff_output ]]; then
    echo "The generated $file file is up-to-date."
  else
    echo "The generated $file file is NOT up-to-date. Diff does not match:"
    echo $diff_output
    exit 1
  fi
  echo ""
}

check_generated "pools.json"        "generate-old-pools-json.py"
check_generated "pool-list.json"    "generate-json-pool-list.py"
