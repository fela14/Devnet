import requests
import json

# Router connection details
router = {
    "ip": "10.10.20.48",
    "port": "443",
    "username": "developer",
    "password": "C1sco12345"
}

# RESTCONF headers
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

# Loopback number and RESTCONF URL
loopback_id = 123
url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback={loopback_id}"

# JSON payload
payload = {
    "Cisco-IOS-XE-native:Loopback": {
        "name": loopback_id,
        "description": "Configured via RESTCONF",
        "ip": {
            "address": {
                "primary": {
                    "address": "192.168.123.1",
                    "mask": "255.255.255.0"
                }
            }
        }
    }
}

# Send the PUT request to configure the loopback
try:
    response = requests.put(url, headers=headers, auth=(router["username"], router["password"]),
                            data=json.dumps(payload), verify=False)

    if response.status_code in [200, 201, 204]:
        print(f"Loopback{loopback_id} successfully configured.")
    else:
        print(f"Failed to configure Loopback. Status: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
