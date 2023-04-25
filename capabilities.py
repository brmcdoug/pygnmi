from pygnmi.client import gNMIclient
import json

host = ("10.200.99.51",57400)

if __name__ == '__main__':

	with gNMIclient(target=host,username="admin",password="IELab123!",insecure=True) as gc:
		
		capability_result = gc.capabilities()
	
	print(json.dumps(capability_result, indent=4))