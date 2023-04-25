from pygnmi.client import gNMIclient
import json

if __name__ == '__main__':
	
	## update
	
	conf = [
				("openconfig-interfaces:interfaces/interface[name=Loopback3]/config",

						{
							"name":"Loopback3",
							#"enabled": False,
							"type": "iana-if-type:softwareLoopback",     ## mandatory field as per YANG module
							"description":"testing pygnmi to create an interface"
						}

				)

			] 
	with gNMIclient(target=("10.251.254.106",57400),username="cisco",password="cisco123",insecure=True) as gc:
		update_result = gc.set(update=conf,encoding='json_ietf')
	
	print(json.dumps(update_result, indent=4))
	
	## get
	
	path = ['openconfig-interfaces:interfaces/interface[name=Loopback3]']

	with gNMIclient(target=("10.251.254.106",57400),username="cisco",password="cisco123",insecure=True) as gc:	
		get_result = gc.get(path=path,encoding='json_ietf',datatype='all',) 

	print(json.dumps(get_result, indent=4))	

