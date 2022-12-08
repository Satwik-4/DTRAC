from brownie import network, accounts, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["ganache-local", "development"]

def get_account(index=None):
#    if index:
#        return accounts[index]
#    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#        return accounts[1]
#    if id:
#        return accounts.load(id)
    if index:
        return accounts.add(config["wallets"]["from_key_1"])
    return accounts.add(config["wallets"]["from_key"])