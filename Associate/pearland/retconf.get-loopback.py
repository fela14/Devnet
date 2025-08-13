import requests
import json
from pprint import pprint

# Suppress SSL warnings (for self-signed certs in labs)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Router connection details
router = {
    "ip": "10.10.20.48",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

# RESTCONF headers
headers = {
    "Accept": "application/yang-data+json"
}

# Loopback ID
loopback_id = 123

# RESTCONF URL to retrieve Loopback interface
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={loopback_id}"

try:
    response = requests.get(url, headers=headers,
                            auth=(router["username"], router["password"]),
                            verify=False)

    if response.status_code == 200:
        data = response.json()
        print(f"Loopback{loopback_id} retrieved successfully:")
        pprint(data)
    else:
        print(f"Failed to retrieve Loopback. Status Code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"HTTP Request failed: {e}")
