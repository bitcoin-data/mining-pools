#!/usr/bin/env python3

import argparse
import json
import glob
import sys

DEFAULT_ENTITIES_DIR = "pools/"
DEFAULT_OUTPUT = "pools.json"

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("output", default=DEFAULT_OUTPUT, type=str, help="output file name", nargs="?")
    parser.add_argument("entities", default=DEFAULT_ENTITIES_DIR, type=str, help="entities directory", nargs="?")
    args = parser.parse_args(args)

    if args.output != DEFAULT_OUTPUT:
        print(f"Using {args.output} as output file name.")

    entity_files = glob.glob(args.entities + "/*.json")

    addresses = dict()
    tags = dict()

    for file_path in entity_files:
        with open(file_path, "r") as f:
            e = json.load(f)
            name = e["name"]
            link = e["link"]
            for addr in e["addresses"]:
                addresses[addr] = { "name": name, "link": link }
            for tag in e["tags"]:
                tags[tag] = { "name": name, "link": link }

    # sort dicts to be at least somewhat deterministic
    addresses = dict(sorted(addresses.items()))
    tags = dict(sorted(tags.items()))

    with open(args.output, "w") as out:
        content = {
            "payout_addresses": addresses,
            "coinbase_tags": tags
        }
        json.dump(content, out, indent = 2, ensure_ascii=False)

if __name__ == "__main__":
    main(sys.argv[1:])
