import requests
import json
import re

switchuser = "admin"
switchpassword = "Admin_1234!"

url = "https://sbx-nxos-mgmt.cisco.com/ins"
myheader = {"Content-Type": "application/json"}

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp neighbors",
        "output_format": "json"
    }
}

# Make the request
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheader,  # <- corrected here
    auth=(switchuser, switchpassword),
    verify=False
)

# Print the parsed JSON response
print(json.dumps(response.json(), indent=2))

##################### LOGIN WITH NX-API REST ########################

# auth_url = "https://sbx-nxos-mgmt.cisco.com/mo/api/aaaLogin.json"
# auth_body = {
#     "aaaUser": {
#         "attributes": {
#             "name": switchuser,
#             "pwd": switchpassword
#         }
#     }     
# }

# auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
# token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]
# cookies = {}
# cookies['APIC-cookie'] = token
# print("cookies")

# NX-API REST Authentication
auth_url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

auth_payload = {
    "aaaUser": {
        "attributes": {
            "name": switchuser,
            "pwd": switchpassword
        }
    }
}

try:
    auth_response = requests.post(auth_url, json=auth_payload, verify=False, timeout=5)
    auth_response.raise_for_status()

    auth_data = auth_response.json()
    token = auth_data["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookies = {'APIC-cookie': token}

    print("\nAuthentication token received.")
    print(f"APIC-cookie: {token}")
    print(cookies)
    print(cookies['APIC-cookie'])

except requests.exceptions.RequestException as e:
    print(f"Authentication failed: {e}")

counter = 0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']
print(nei_count)

while counter < nei_count:
    hostname = response['ins_api']['outputs']['output']['body']['neigh_count'][
        ['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device-id']]
    local_int = response['ins_api']['outputs']['output']['body']['neigh_count'][
        ['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf-id']]
    remote_int = response['ins_api']['outputs']['output']['body']['neigh_count'][
        ['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port-id']]

    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": "Connected to "+ hostname +"Remote if is "+ remote_int
            }
        }

    }
    counter += 1

    if local_int != 'mgmt0': 
        int_name = str.lower(str(local_int[:3]))
        int_num = re.search(r'[1-9]/[1-9]*', local_int)
        int_url = '"https://sbx-nxos-mgmt.cisco.com/api/mo/sys/intf/phys-['+int_name+str(int_num.group(0))+'].json'
        post_response = requests.post(int_url, 
                                        data=json.dump(body), 
                                        headers=myheader, 
                                        cookies=cookies, 
                                        verify=False).json()
        print(post_response)
    
