#!/usr/bin/env python3

import json
import glob
import sys

output_file_name = "generated/pool-list.json"

if len(sys.argv) == 2:
    print(f"Using {sys.argv[1]} as output file name.")
    output_file_name = sys.argv[1]

entity_files = glob.glob("pools/*.json")

pools = list()

for file_path in entity_files:
    with open(file_path, "r") as f:
        e = json.load(f)
        pools.append(e)

pools.sort(key = lambda p: p["id"])

with open(output_file_name, "w") as out:
    json.dump(pools, out, indent = 2, ensure_ascii=False)

