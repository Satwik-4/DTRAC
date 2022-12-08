from scripts.helpful_scripts import get_account

from brownie import Issue, Opening, Params, Request, Verify, G, BN256G2, network, config


def deploy():

    account = get_account()
    #G_deploy = G.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    #BN256G2_deploy = BN256G2.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    
    #Params_deploy = Params.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"])'''
    #print(Params_deploy)
    #Issue_deploy = Issue.deploy("0x8aE516da91de4A38C00e5309089A70Cd45CD916b", {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    #Opening_deploy = Opening.deploy("0x8aE516da91de4A38C00e5309089A70Cd45CD916b", {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    #Request_deploy = Request.deploy("0x8aE516da91de4A38C00e5309089A70Cd45CD916b", {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    #Verify_deploy = Verify.deploy("0x8aE516da91de4A38C00e5309089A70Cd45CD916b", {"from": get_account(1)})#""", publish_source = config["networks"][network.show_active()]["verify"]"""

def main():
    deploy()