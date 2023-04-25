from pygnmi.client import gNMIclient
import json

if __name__ == '__main__':

	with gNMIclient(target=("10.251.254.106",57400),username="cisco",password="cisco123",insecure=True) as gc:
		
		capability_result = gc.capabilities()
	
	print(json.dumps(capability_result, indent=4))