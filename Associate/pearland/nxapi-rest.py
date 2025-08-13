from pprint import pprint
import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'cache-control': 'no cahe'
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()

pprint(response)
token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]
pprint(token)
cookies={}
cookies['APIC-cookie']=token


put_url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/97].json"

put_payload = json.dumps({
  "l1PhysIf": {
    "attributes": {
      "descr": "Knox was here"
    }
  }
})

put_headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive',
  'cache-control': 'no-cache'
}

put_response = requests.put(put_url, headers=put_headers, data=put_payload, cookies=cookies, verify=False)

print(f"Status code: {put_response.status_code}")
try:
    print("Response JSON:")
    pprint(put_response.json())
except Exception as e:
    print("Response Text:")
    print(put_response.text)

