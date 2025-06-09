# import requests
# import json

# target = "https://sbx-nxos-mgmt.cisco.com"
# username = "admin"
# password = "admin"

# requestheaders = {"content-type": "application/json"}
# showcmd = {
#     "ins_api": {
#         "version": "1.0",
#         "type": "cli-show", # cli-config to make configuration changes
#         "chunk": "0",
#         "sid": "1",
#         "input": "show ip int b",
#         "output_format": "json",
#     }
# }

# response = requests.post(
#     target,
#     data=json.dumps(showcmd),
#     headers=requestheaders,
#     auth=(username, password),
#     verify=False,
# ).json()

#print(json.dumps(response, indent=2, sort_keys=True))


import requests
import json
import urllib3

# Suppress SSL warnings (only for sandbox/testing)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Correct URL
target = "https://sbx-nxos-mgmt.cisco.com/ins"
username = "admin"
password = "Admin_1234!"

headers = {"Content-Type": "application/json"}

showcmd = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",  # underscore is required here
        "chunk": "0",
        "sid": "1",
        "input": "show ip interface brief",
        "output_format": "json"
    }
}

try:
    response = requests.post(
        target,
        data=json.dumps(showcmd),
        headers=headers,
        auth=(username, password),
        verify=False
    )

    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, indent=2))
    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
