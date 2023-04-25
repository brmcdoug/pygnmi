from pygnmi.client import gNMIclient
import json

host = ("10.251.254.106",57400)

if __name__ == '__main__':

	with gNMIclient(target=host,username="cisco",password="cisco123",insecure=True) as gc:
		
		capability_result = gc.capabilities()
	
	print(json.dumps(capability_result, indent=4))