import json
import requests
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fmcrestapisandbox.cisco.com"
login_url = "/api/fmc_platform/v1/auth/generatetoken"
headers = {"Content-Type": "application/json"}
user = "kfakeye"
pw = "mxblB7FLF2*!6w$*"

# Step 1: Authenticate and get token
login_response = requests.post(f'{url}{login_url}',
                               auth=(user, pw), verify=False)
resp_headers = login_response.headers

token = resp_headers.get("X-auth-access-token", default=None)
headers['X-auth-access-token'] = token

apps_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"

apps_response = requests.get(f'{url}{apps_url}',
                             headers=headers, verify=False)

# Step 4: Print JSON response nicely
print(json.dumps(apps_response.json(), indent=2, sort_keys=True))