import argparse
import os
import pickle

# python3 ProtocolInitiator_DeployContracts.py --params-address 0x909bf278dAE91ae352E1Ef5F77B18d85427443a2 --request-address 0x909bf278dAE91ae352E1Ef5F77B18d85427443a2 --issue-address 0x564332ff8f840dD78432051dD49A5F8442E4487F --opening-address 0x7d30975d2e03F4BE59e28790F093538C76A06C5A


parser = argparse.ArgumentParser(description="Smart Contracts Deployment")
# parser.add_argument("--address", type=str, default = None, required = True,  help= "The blockchain address on which Protocol Initiator is running.")
parser.add_argument("--params-address", type=str, default = None, required = True,  help= "The blockchain address at which params contract is deployed.")
parser.add_argument("--request-address", type=str, default = None, required = True,  help= "The blockchain address at which request contract is deployed.")
parser.add_argument("--issue-address", type=str, default = None, required = True,  help= "The blockchain address at which issue contract is deployed.")
parser.add_argument("--opening-address", type=str, default = None, required = True,  help= "The blockchain address at which opening contract is deployed.")
# parser.add_argument("--rpc-endpoint", type=str, default = None, required = True,  help= "The node rpc endpoint through which a client is connected to blockchain network.")
args = parser.parse_args()

mode = 0o777
root_dir = "/home/satwik/Documents/Modifier Version Ganache_Exp-1/ROOT"
try:
	os.mkdir(root_dir, mode = mode)
except FileExistsError as e:
	pass

def uploadAddresses(address, filename):
	file_path = os.path.join(root_dir, filename)
	f = open(file_path,'wb')
	pickle.dump(address, f)
	f.close()

uploadAddresses(args.params_address, "params_address.pickle")
uploadAddresses(args.request_address, "request_address.pickle")
uploadAddresses(args.issue_address, "issue_address.pickle")
uploadAddresses(args.opening_address, "opening_address.pickle")