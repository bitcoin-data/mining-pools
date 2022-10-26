import json
import glob

entity_files = glob.glob("entities/*.json")

addresses = dict()
tags = dict()

for file_path in entity_files:
    with open(file_path, "r") as f:
        e = json.load(f)
        name = e["name"]
        link = ""
        if len(e["links"]) > 0:
            link = e["links"][0]
        for addr in e["addresses"]:
            addresses[addr] = { "name": name, "link": link }
        for tag in e["tags"]:
            tags[tag] = { "name": name, "link": link }

# sort dicts to be at least somewhat deterministic
addresses = dict(sorted(addresses.items()))
tags = dict(sorted(tags.items()))

with open("pools-generated.json", "w") as out:
    content = {
        "payout_addresses": addresses,
        "coinbase_tags": tags
    }
    json.dump(content, out, indent = 2, ensure_ascii=False)

