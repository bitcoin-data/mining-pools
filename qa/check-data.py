#!/usr/bin/env python3

import argparse
import json
import glob
import sys


DEFAULT_ENTITIES_DIR = "pools/"


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("entities", default=DEFAULT_ENTITIES_DIR,
                        type=str, help="entities directory", nargs="?")
    args = parser.parse_args(args)

    entity_files = glob.glob(args.entities + "/*.json")

    ids = set()
    max_id = -1

    for file_path in entity_files:
        with open(file_path, "r") as f:
            e = json.load(f)

            id = e["id"]
            name = e["name"]
            addresses = e["addresses"]
            tags = e["tags"]
            link = e["link"]

            try:
                id_already_used = id in ids
                assert type(id) == int, "ID is not of type int"
                assert not id_already_used, f"ID {id} is already used"
                assert id != 0, f"ID should not be zero"
                ids.add(id)
                max_id = max(id, max_id)

                assert type(name) == str, "mame is not of type string"

                assert type(addresses) == list, "addresses is not of type list"
                assert type(tags) == list, "tags is not of type list"

                # we should have at least one tag or address
                assert len(addresses) + \
                    len(tags) > 0, "addresses and tags both are empty"

                assert type(link) == str, "link is not of type string"

            except Exception as ex:
                print(f"Invalid pool in file {file_path}.")
                print(f"Pool: {json.dumps(e, indent=2, ensure_ascii=False)}")
                raise ex

    print("No problems found.")
    print(f"The maximum ID is {max_id}.")
    print(f"Use ID {max_id + 1} when creating a new pool JSON file.")


if __name__ == "__main__":
    main(sys.argv[1:])
