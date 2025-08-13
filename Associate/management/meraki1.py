import requests
import json

url = "https://api.meraki.com/api/v0/organizations"  

headers = {
    'X-Cisco-Meraki-API-Key': "YOUR_API_KEY_HERE"  
}

response = requests.get(url, headers=headers)

# Check response status
if response.status_code != 200:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
    exit()

response_data = response.json()

print(json.dumps(response_data, indent=2, sort_keys=True))

orgId = None
for response_org in response_data:
    if response_org['name'] == 'Devnet Sandbox':  # Corrected typo in organization name
        orgId = response_org['id']
        break

if orgId:
    print(f"Organization ID: {orgId}")
else:
    print("Organization 'Devnet Sandbox' not found.")
