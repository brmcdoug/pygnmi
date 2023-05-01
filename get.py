from pygnmi.client import gNMIclient
import json


host = ("10.251.254.106",57400)

if __name__ == '__main__':

	path = ['openconfig-interfaces:interfaces/interface[name=Loopback0]']#,'Cisco-IOS-XR-ipv4-bgp-oper:bgp/bpm-instances-table/bpm-instances']
	

	with gNMIclient(target=host,username="cisco",password="cisco123",insecure=True, gnmi_timeout=30) as gc:	
		get_result = gc.get(path=path,encoding='json_ietf',datatype='all',) 

	print(json.dumps(get_result, indent=4))
	
	path = ['openconfig-interfaces:interfaces/interface/config']

	with gNMIclient(target=host,username="cisco",password="cisco123",insecure=True, gnmi_timeout=30) as gc:	
		get_result = gc.get(path=path,encoding='json_ietf',datatype='all',) 

	print(json.dumps(get_result, indent=4))