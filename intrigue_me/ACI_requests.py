import json
import requests
from pprint import pprint

# Disable SSL warnings (only for sandbox testing)
requests.packages.urllib3.disable_warnings()

########## LOGIN ##########

login_url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

login_payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"  
        }
    }
}

headers = {"Content-Type": "application/json"}

response = requests.post(login_url, data=json.dumps(login_payload), headers=headers, verify=False)
response_json = response.json()

pprint(response_json)

# Get token
token = response_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
# Set the cookie for authentication
cookie = {"APIC-cookie": token}

########## GET APN ##########

apn_url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

get_response = requests.get(apn_url, headers={"Content-Type": "application/json"}, cookies=cookie, verify=False)
get_json = get_response.json()

print("\n--- BEFORE UPDATE ---")
pprint(get_json)

########## UPDATE APN ##########

post_payload = {
    "fvAp": {
        "attributes": {
            "dn": "uni/tn-Heroes/ap-Save_The_Planet",
            "descr": "Developer xtra-ordinaire",
            "status": "modified"
        }
    }
}

post_response = requests.post(apn_url, headers={"Content-Type": "application/json"}, cookies=cookie, verify=False, data=json.dumps(post_payload))
post_json = post_response.json()

print("\n--- UPDATE RESPONSE ---")
pprint(post_json)

########## VERIFY UPDATE ##########

verify_response = requests.get(apn_url, headers={"Content-Type": "application/json"}, cookies=cookie, verify=False)
verify_json = verify_response.json()

print("\n--- AFTER UPDATE ---")
pprint(verify_json)

# acitoolkit.readthedocs.io
# github.com/datacenter/acitoolkit

