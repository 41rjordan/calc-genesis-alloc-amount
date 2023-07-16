# calc-genesis-alloc-amount
5-line python script to calculate total allocated ETH from genesis json file

# Purpose
To trustlessly calculate genesis allocated ETH. You can get genesis json file from almost any (*from what i know, geth has params RLP encoded :(* ) ethereum execution client repo. I took mine from [reth](https://raw.githubusercontent.com/paradigmxyz/reth/main/crates/primitives/res/genesis/mainnet.json)

# Usage
`python3 cgaa.py <path-to-genesis-json-file>`

# Returns
For mainnet json file, it should return something like this (at least, this is what was returned in my case):

`Total allocated ETH to 8893 addresses: 72009990499480000000000000 wei (72009990.49948 ETH)`
