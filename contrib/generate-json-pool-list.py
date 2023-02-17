#!/usr/bin/env python3

import argparse
import json
import glob
import sys

DEFAULT_ENTITIES_DIR = "pools/"
DEFAULT_OUTPUT = "pool-list.json"

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("output", default=DEFAULT_OUTPUT, type=str, help="output file name", nargs="?")
    parser.add_argument("entities", default=DEFAULT_ENTITIES_DIR, type=str, help="entities directory", nargs="?")

    args = parser.parse_args(args)

    if args.output != DEFAULT_OUTPUT:
        print(f"Using {args.output} as output file name.")

    entity_files = glob.glob(args.entities + "/*.json")
    pools = list()

    for file_path in entity_files:
        with open(file_path, "r") as f:
            e = json.load(f)
            pools.append(e)

    pools.sort(key = lambda p: p["id"])

    with open(args.output, "w") as out:
        json.dump(pools, out, indent = 2, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1:])
