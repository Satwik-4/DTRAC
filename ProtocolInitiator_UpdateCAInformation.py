import jsonpickle
from TTP import *
from py_ecc_tester import *

from datetime import datetime
import time

import argparse
import os
import pickle
import socket
import threading
import json
from web3 import Web3

from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware

# python3 ProtocolInitiator_UpdateCAInformation.py --titles "Identity Certificate" "Income Certificate" --address 0x5CB76baeE21095597486690A0AD3322C7A2d0Cb2 --rpc-endpoint "http://127.0.0.1:7545"

parser = argparse.ArgumentParser(description="Update Attribute Certifiers information to smart contracts")
parser.add_argument('--titles', nargs='+', help='The attribute certifiers in the system', required=True)
parser.add_argument("--address", type=str, default = None, required = True,  help= "The blockchain address on which Protocol Initiator is running")
parser.add_argument("--rpc-endpoint", type=str, default = None, required = True,  help= "The node rpc endpoint through which a client is connected to blockchain network")
args = parser.parse_args()

mode = 0o777
root_dir = "/home/satwik/Documents/Modifier Version Ganache_Exp-1/ROOT"

try:
	os.mkdir(root_dir, mode = mode)
except FileExistsError as e:
	pass 

def downloadCAParams(title):
	ca_path = os.path.join(root_dir, title)
	ca_file_path = os.path.join(ca_path, "params.pickle")
	f = open(ca_file_path,'rb')
	json_params = pickle.load(f)
	params = jsonpickle.decode(json_params)
	f.close()
	return params

def downloadCAPk(title):
	ca_path = os.path.join(root_dir, title)
	ca_file_path = os.path.join(ca_path, "pk.pickle")
	f = open(ca_file_path,'rb')
	json_pk = pickle.load(f)
	pk = jsonpickle.decode(json_pk)
	f.close()
	return pk

def getParamsAddress():
	file_path = os.path.join(root_dir, "params_address.pickle")
	f = open(file_path,'rb')
	params_address = pickle.load(f)
	f.close()
	return params_address

params_address = getParamsAddress()
private_key = args.address

for title in args.titles:
	_, _, _, hs = downloadCAParams(title)
	pk = downloadCAPk(title)
	encoded_hs = [(x[0].n, x[1].n) for x in hs]
	encoded_pk = (pk[0].n, pk[1].n)
		
	# w3 = Web3(Web3.WebsocketProvider(args.rpc_endpoint, websocket_timeout = 100))
	w3 = Web3(Web3.HTTPProvider(args.rpc_endpoint))
		
	tf = json.load(open('./build/contracts/Params.json'))
	params_address = Web3.toChecksumAddress(params_address)
	params_contract = w3.eth.contract(address = params_address, abi = tf['abi'])
		
	#tx_hash = params_contract.functions.set_ttp_params(title, encoded_pk, encoded_hs).transact({'from': args.address})
	#w3.eth.waitForTransactionReceipt(tx_hash)

	
	assert private_key is not None, "You must set PRIVATE_KEY environment variable"
	assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

	account: LocalAccount = Account.from_key(private_key)
	w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

	tx_hash = params_contract.functions.set_ttp_params(title, encoded_pk, encoded_hs).transact({'from': account.address})
	w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120, poll_latency=0.1)

	print(f"Your hot wallet address is {account.address}")