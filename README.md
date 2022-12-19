# Known Bitcoin Pools

Known Bitcoin mining pool coinbase tags and coinbase output addresses.

For maintainability, the data is defined as a JSON-file per pool in the `pools/`
folder. For each pool, the following information is included in the JSON file:

```JSON
{
  "name": "Example Pool",
  "addresses": [
    "15kDhRAcpgsugmh6mQsTcCHdvbsuYncEEV",
    "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"
  ],
  "tags": [
    "/example/",
    "Example Pool"
  ],
  "link": "https://example.com"
}
```

The JSON files aren't intended for direct consumption by tools trying to
identify mining pools. The format may change. Rather, the data in the
JSON-files should be used to generate a file suitable for consumption by
down-stream tools. An example is the `contrib/create-old-pools-json.py` script
which generates `generated/pools.json`. This file was previously used to
collect the coinbase tags and addresses and is still used by some tools.

## Origin

This repository was forked from [btccom/Blockchain-Known-Pools](https://github.com/btccom/Blockchain-Known-Pools)
in early 2021 and has received multiple additions and improvements:

- [remove: AntPool false positives](https://github.com/0xB10C/known-mining-pools/commit/282d56844ec8072cf1ae8e793fe60faa96afa658): See this [comment](https://github.com/btccom/Blockchain-Known-Pools/commit/c5e50d99d319065623633342c6711c3db6e9802b#commitcomment-36520323).
- [cleanup: addresses that definitely aren't coinbase output addresses ](https://github.com/0xB10C/known-mining-pools/pull/6)
- [change: all URLs to HTTPS](https://github.com/0xB10C/known-mining-pools/commit/ed4b3f3ac96f28c11bea570ed071dfbafa3cef80)
