from ncclient import manager
from test_router import router
import xmltodict
import json


netconf_filter = open("test_filter.xml").read()

with manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False,
    look_for_keys=False,
    allow_agent=False
    ) as m:

    for capabilities in m.server_capabilities:
        print("*"*50)
        print(capabilities)
    print("NETCONF CONNECTED")

    interface_netconf = m.get_config(source="running", filter=netconf_filter)
    print("Getting running configuration...")

    xml_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    ind_xml_python = json.dumps(xml_python, indent=4)
    print(ind_xml_python)
    name = xml_python["native"]["interface"]
    name_list = []
    for key in name:
        name_list.append(key)
    print(name_list[0])

    native = xml_python["native"]["interface"]["GigabitEthernet"]
    interfaces = native if isinstance(native, list) else [native]

    for iface in interfaces:
        for key, value in iface.items():
            print(f"{key}: {value}")
        print("**************************")


