import json
import requests
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com"
login_url = "/api/fmc_platform/v1/auth/generatetoken"
user = "kfakeye"
pw = "mxblB7FLF2*!6w$*"

# Step 1: Authenticate and get token
login_response = requests.post(f'{url}{login_url}',
                               auth=(user, pw), verify=False)

if login_response.status_code != 204:
    print("Login failed:", login_response.text)
    exit()

# Step 2: Get token from response headers
token = login_response.headers.get('X-auth-access-token')
if not token:
    print("No token found in login response.")
    exit()

headers = {'X-auth-access-token': token}

# Step 3: Call the Applications endpoint
apps_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications"

apps_response = requests.get(f'{url}{apps_url}',
                             headers=headers, verify=False)

# Step 4: Print JSON response nicely
print(json.dumps(apps_response.json(), indent=2, sort_keys=True))
