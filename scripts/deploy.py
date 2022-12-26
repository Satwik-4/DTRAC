from scripts.helpful_scripts import get_account

from brownie import Issue, Opening, Params, Request, Verify, G, BN256G2, network, config

from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware

from web3 import Web3


def deploy():

    account = get_account()
    G_deploy = G.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    BN256G2_deploy = BN256G2.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    
    Params_deploy = Params.deploy({"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"])'''

    Issue_deploy = Issue.deploy(Params_deploy, {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    Opening_deploy = Opening.deploy(Params_deploy, {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    Request_deploy = Request.deploy(Params_deploy, {"from": account})#''', publish_source = config["networks"][network.show_active()]["verify"]'''
    Verify_deploy = Verify.deploy(Params_deploy, {"from": get_account(1)})#""", publish_source = config["networks"][network.show_active()]["verify"]"""
    
def main():
    deploy()