import requests
import json

target = "http://172.16.1.67/ins"
username = "admin"
password = "admin"

requestheaders = {"content-type": "application/json"}
showcmd = {
    "ins_api": {
        "version": "1.0",
        "type": "cli-show", # cli-config to make configuration changes
        "chunk": "0",
        "sid": "1",
        "input": "show ip int b",
        "output_format": "json",
    }
}

response = requests.post(
    target,
    data=json.dumps(showcmd),
    headers=requestheaders,
    auth=(username, password),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))


