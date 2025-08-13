from ncclient import manager
from router_info import router
from pprint import pprint
import xml.dom.minidom
import xmltodict


#reading the netconf-filter.xml file
netconf_filter = open("netconf-filter.xml").read()


with manager.connect(host = router["host"], 
                     port = router["port"],
                     username = router["username"],
                     password = router["password"],
                     hostkey_verify = False) as m:
    for capability in  m.server_capabilities:
        print('*'*50)
        #getting the capabilities of the device
        print(capability)
        print('*'*50)
        print("Connected")


        interface_netconf = m.get(netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent = " "))
        print('*'*50)
        
        # xmltodict for converting xml output to a python dictionary
        interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
        print("Getting running config")
        pprint(interface_python)

        name = interface_python["interfaces"]["interface"]["name"]["#text"]
        config = interface_python["interfaces"]["interface"]["description"]
        op_state = interface_python["interfaces-state"]["interface"]["statistics"]["in-unicast-pkts"]

        print(f"Name = {name}")
        print(f"Description = {config}")
        print(f"Number of packets sent in = {op_state}")


        config_template = open("ios_config.xml").read()
        netconf_edit = config_template.format(interface_name = "GigabitEthernet2", interface_desc = "uplink")

        with manager.connect(host = router["host"], 
                     port = router["port"],
                     username = router["username"],
                     password = router["password"],
                     hostkey_verify = False) as m:
            device_reply = m.edit_config(netconf_edit, target= "running")
            print(device_reply)

    m.close_session()