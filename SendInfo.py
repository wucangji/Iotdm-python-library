#!/usr/bin/python

import criotdm
import ciotdm

# Set varibles
httphost = "localhost"
httpuser = "admin"
httppass = "admin"
rt_ae              = 2
rt_container       = 3
rt_contentInstance = 4

connect = criotdm.connect_to_iotdm(httphost, httpuser, httppass, "http")
attr = '"mni":6'
container_resp = connect.create("InCSE1", rt_container, attr, "TemContaienr")
print(container_resp.text)

