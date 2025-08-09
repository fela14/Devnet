import requests
import json

url = "https//172.16.1.131/api/routing/static"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

userpw = ("cisco", "cisco")

get_response = requests.get(url, headers=headers,
                            verify=False)
result = get_response.json()['items']

print(json.dumps(result), indent=2, sort_keys=True)