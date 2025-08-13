# import requests
# import json
# from pprint import pprint

# # set up connection parameters in a dictionary
# router = {"ip": "10.10.20.48", 
#           "port":"830", 
#           "username": "developer", 
#           "password": "C1sco12345"}

# # set REST API headers
# headers = {"Accept": "application/yang-data+json",
#            "Content-Type": "application/yang-data+json"}

# url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interfaces=GigabitEthernet1"
# # print(url)

# response = requests.get(url, headers=headers, auth=(
#     router['username'], router['password']), verify=False)

# api_data = response.json()
# print("/" * 50)
# pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
# print("/" * 30)
# if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
#     print('Interface is up')

import requests
import json
from pprint import pprint
import urllib.parse

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Router connection parameters
router = {
    "ip": "10.10.20.48",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

# RESTCONF headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# Interface name with URL encoding
interface_name = "GigabitEthernet1"
encoded_interface = urllib.parse.quote(interface_name, safe='')

# RESTCONF URL
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface={encoded_interface}"

try:
    response = requests.get(url, headers=headers,
                            auth=(router['username'], router['password']),
                            verify=False)

    response.raise_for_status()

    api_data = response.json()

    print("/" * 50)

    # The response contains a dictionary with a list of interfaces
    interfaces_list = api_data.get("Cisco-IOS-XE-interfaces-oper:interface", [])

    if interfaces_list:
        interface = interfaces_list[0]  # Access the first matching interface

        print("Description:", interface.get("description", "No description"))
        print("Interface:", interface.get("name", "N/A"))
        print("Admin Status:", interface.get("admin-status", "unknown"))

        print("/" * 30)

        if interface.get("admin-status") == 'if-state-up':
            print('Interface is up')
        else:
            print('Interface is down or status unknown')
    else:
        print("No interface data returned.")

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
except json.JSONDecodeError:
    print("Failed to parse JSON response")
except KeyError as e:
    print(f"Missing expected key in response: {e}")
