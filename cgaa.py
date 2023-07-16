import json, sys
genesis = json.loads(open(sys.argv[1], "r").read())
all_balances = [int(x["balance"], 16) for x in genesis["alloc"].values()]
total_alloc = sum(all_balances)
print("Total allocated ETH to {} addresses: {} wei ({} ETH)".format(len(all_balances), total_alloc, total_alloc/10**18))