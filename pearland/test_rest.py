import requests
import urllib
import json

router = {
    "ip": "10.10.20.48",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

interface_name = "GigabitEthernet1"
encoded_name = urllib.parse.quote(interface_name, safe='')

url = f"https://{router["ip"]}:{router["port"]}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface={encoded_name}"

response = requests.get(url, headers=headers,
                        auth=(router["username"], router["password"]),
                        verify=False)
response.raise_for_status
api_data = response.json()
print(json.dumps(api_data, indent=3))


interfaces = api_data["Cisco-IOS-XE-interfaces-oper:interface"]

if interfaces:
    for iface in interfaces:
        print(iface)
        print("*"*25)


        for key, value in iface.items():
            print(f"{key}: {value}")
        print("*"*25)

interfaces_list = api_data.get("Cisco-IOS-XE-interfaces-oper:interface", [])

if interfaces_list:
    interface = interfaces_list[0]
    print(f"Name: {interface.get("name", "No name")}")
    print(f"Description: {interface.get("description", "No description")}")
    if interface["admin-status"] == "if-state-up":
        print(f"Status: {interface.get("admin-status", "No status")}")

####################################################################################################

import requests
import json
import urllib3

# 🔇 Suppress SSL warnings (for self-signed certs in lab)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


router = {
    "ip": "10.10.20.48",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

loopback_name = 33

payload = {
    "Cisco-IOS-XE-native:Loopback": {
        "name": loopback_name,
        "description": "Configured via RESTCONF",
        "ip": {
            "address": {
                "primary": {
                    "address": "102.168.123.14",
                    "mask": "255.255.255.0"
                }
            }
        }
    }
}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={loopback_name}"

response = requests.put(url, headers=headers,
                        auth=(router["username"], router["password"]),
                        data=json.dumps(payload), verify=False)

if response.status_code in [200,201,202,204]:
    print(f"Loopack: {loopback_name} successfully configured")
else:
    print(f"Failed to configure loopback. Status: {response.status_code}")
    
response = requests.get(url, headers=headers,
                        auth=(router["username"], router["password"]),
                        verify=False)

if response.status_code == 200:
    print(f"Loopback {loopback_name} is present")
    data = response.json()
    print(data)

