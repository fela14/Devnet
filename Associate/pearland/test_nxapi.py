import requests
import json
import urllib3
from pprint import pprint

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Login credentials
username = "admin"
password = "Admin_1234!"

# Step 1: Login to get auth token
login_url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

login_headers = {
    "Content-Type": "application/json"
}

login_payload = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}

print("🔐 Logging in...")
login_response = requests.post(login_url, data=json.dumps(login_payload),
                               headers=login_headers, verify=False)

print("Status Code:", login_response.status_code)
print("Raw Response:", login_response.text)

try:
    login_data = login_response.json()
    print("✅ Login JSON Parsed")
except Exception as e:
    print("❌ Failed to parse login JSON:", e)
    exit(1)

# Extract token
try:
    token = login_data["imdata"][0]["aaaLogin"]["attributes"]["token"]
    print("🔑 Token:", token)
except Exception as e:
    print("❌ Token extraction failed:", e)
    exit(1)

# Step 2: Prepare cookies
cookies = {
    "APIC-cookie": token
}

# Step 3: Make the interface update request
intf_dn = "sys/intf/phys-[eth1/97]"  # Ensure this exists on the device!
intf_url = f"https://sbx-nxos-mgmt.cisco.com/api/node/mo/{intf_dn}.json"

intf_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

intf_payload = {
    "l1PhysIf": {
        "attributes": {
            "descr": "UPDATED via API"
        }
    }
}

print("\n📡 Sending interface update request...")
response = requests.put(intf_url, data=json.dumps(intf_payload),
                        headers=intf_headers, cookies=cookies, verify=False)

print("Status Code:", response.status_code)
print("Raw Response Text:")
print(response.text)

# Try to parse the response as JSON
try:
    response_data = response.json()
    print("✅ JSON Response:")
    print(json.dumps(response_data, indent=3))
except ValueError as e:
    print("❌ JSON Decode Error:", e)
