#!/usr/bin/env bash
#
# Checks if the pools.json file is up-to-date.

tmp_GENERATED=$(mktemp)

python3 contrib/generate-old-pools-json.py $tmp_GENERATED

diff_output=$(diff generated/pools.json $tmp_GENERATED --color=always --minimal)

rm $tmp_GENERATED

if [[ -z $diff_output ]]; then
    echo "The generated pools.json file is up-to-date."
else
    echo "The generated pools.json file is NOT up-to-date. Diff does not match:"
    echo $diff_output
    exit 1
fi
