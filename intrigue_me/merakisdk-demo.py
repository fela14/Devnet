from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from pprint import pprint
import json

token = ''
meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()
pprint(orgs)

for org in orgs:
    if orgs['name'] == "Devnet sandbox":
        orgId = org['id']

params = {}
params['organization_id'] = orgId

#search for get_organization_networks on pip3 sdk
# the parameter to be passed into this method should be a dictionary
networks = meraki.networks.get_organization_networks(params) 
pprint(networks)

for network in networks:
    if network['name'] == 'Devnet Always On Read Only':
        netId = network['id']

#search for get_network_vlans on pip3 sdk
# the parameter to be passed into this method isn't a dictionary
vlans = meraki.vlans.get_network_vlans(netId)
pprint(vlans)

# search for update_network_vlan
# the parameter to be passed into this method should be a dictionary
# dictionary should contain 2 required parameters and 1 optional parameter

vlan = vlans[0]
vlan['name'] = 'Developer'

updated_vlan = {}
updated_vlan['network_id'] = netId
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan # optional

result = meraki.get_network_vlan(updated_vlan)
result_vlan = meraki.network.get_network_vlans(netId)
 
pprint(result_vlan)


