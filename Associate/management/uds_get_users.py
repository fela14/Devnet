import requests
import xml.dom.minidom
import xmltodict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.10.20.1/cucm-uds"
endpoint = "users"

users_url = f"{url}/{endpoint}"

headers = {
    'Content-Type': 'application/xml',
    'Accept': 'application/xml'
}

username = 'administrator'
password = 'ciscopsdt'

r = requests.get(users_url, auth=(username, password), headers=headers)

tree = xml.dom.minidom.parseString(r.text)
pretty = tree.toprettyxml()

xmldata = xmltodict.parse(pretty)

users = xmldata['users']['user']
for user in users:
    print(f"{user['lastName']} {user['firstName']}")
    print(f"ID: {user['id']}")
    print(" ")