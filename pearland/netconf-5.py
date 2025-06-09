# from ncclient import manager
# from pprint import pprint
# import xmltodict
# import xml.dom.minidom
# from router_info import router
# # import logging
# # logging.basicConfig(level=logging.DEBUG)


# netconf_filter = open("netconf-filter.xml").read()

# with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
#     for capability in m.server_capabilities:
#         print('*' * 50)
#         print(capability)
#     # get the running config on the filtered out interface
#     print('Conneted')
#     interface_netconf = m.get(netconf_filter)
#     print('getting running config')
# # below, xml is a property of interface_conf

# # XMLDOM for formatting output to xml
# # ----UNCOMMENT BELOW
# # xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
# # print(xmlDom.toprettyxml(indent=" "))
# # print('*' * 25 + 'Break' + '*' * 50)
# # ----UNCOMMENT ABOVE

# # XMLTODICT for converting xml output to a python dictionary
# interface_python = xmltodict.parse(interface_netconf.xml)[
#      "rpc-reply"]["data"]
# pprint(interface_python)
# name = interface_python['interfaces']['interface']['name']['#text']
# print(name)

# config = interface_python["interfaces"]["interface"]
# op_state = interface_python["interfaces-state"]["interface"]

# print("start")
# print(f"Name: {config['name']['#text']}")
# print(f"Description: {config['description']}")
# print(f"Packets in {op_state['statistics']['in-unicast-pkts']}")
from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom

router = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

netconf_filter = open("netconf-filter.xml").read()

with manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False
) as m:
    
    print("**Connected**")
    
    for capability in m.server_capabilities:
        print(capability)

    interface_netconf = m.get_config(source="running", filter=netconf_filter)
    print('**Getting running config**')

    xmlDom = xml.dom.minidom.parseString(interface_netconf.xml)
    print(xmlDom.toprettyxml(indent="  "))

    interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    native = interface_python["native"]["interface"]["GigabitEthernet"]
    interfaces = native if isinstance(native, list) else [native]

    for iface in interfaces:
        for key, value in iface.items():
            print(f"{key}: {value}")
        print("*********************")




