#!/usr/bin/python 

#https://pyfortiapi.readthedocs.io/en/latest/user/operations.html

import pyfortiapi

device = pyfortiapi.FortiGate(ipaddr="10.1.1.1",port=8443,username="admin", password="senha", vdom="BGP-AS")

addresses = device.get_firewall_address()
for i in addresses:
	print(i['q_origin_key'],'-',i['wildcard'])
