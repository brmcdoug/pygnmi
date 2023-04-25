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

				),
				("openconfig-interfaces:interfaces/interface[name=Loopback3]/subinterfaces",
                    {
                            "subinterface": [
                                {
                                    "index": 0,
                                    "openconfig-if-ip:ipv4": {
                                        "addresses": {
                                            "address": [
                                                {
                                                    "ip": "10.0.0.233",
                                                    "config": {
                                                        "ip": "10.0.0.233",
                                                        "prefix-length": 32
                                                    },
                                                    "state": {
                                                        "ip": "10.0.0.233",
                                                        "prefix-length": 32,
                                                        "origin": "STATIC"
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    "openconfig-if-ip:ipv6": {
                                        "addresses": {
                                            "address": [
                                                {
                                                    "ip": "fc00:0:233::1",
                                                    "config": {
                                                        "ip": "fc00:0:233::1",
                                                        "prefix-length": 128
                                                    },
                                                    "state": {
                                                        "ip": "fc00:0:233::1",
                                                        "prefix-length": 128,
                                                        "origin": "STATIC",
                                                        "status": "PREFERRED"
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                }
                            ]
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

