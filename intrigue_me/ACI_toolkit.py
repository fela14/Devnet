from acitoolkit.acitoolkit import *

"""
# see capabilities
# dir()

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pw = "!v3G@!4@Y"

# create the session object
session = Session(url, user, pw)

# login to the session
session.login()

# get tenants
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*'*30)
    print(' ')

# create a new tenant
new_tenant = Tenant("Tenant_Name_Here")

# create the application profile and the EPG
apn = AppProfile("My_apn", new_tenant)
epg = EPG("My_epg", apn)

# create the L3 namespace
context = Context("My_vrf", new_tenant)
bridge_domain = BridgeDomain("My_bd", new_tenant)

# associate the BD with the L3 namespace
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

##### Tenant Creation is Completed #####
print(new_tenant.get_url())
print(new_tenant.get_json())
response = session.push_to_apic(
    new_tenant.get_url(), data=new_tenant.get_json()
)
print(response)

tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Tenant_Name_Here':
        print(tenant.name)
    else: 
        print(tenant.name)
        print(tenant.descr)
        print('*'*30)
        print(' ')

# delete created tenant
new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
"""

from acitoolkit.acitoolkit import *
import urllib3

# Disable SSL warnings for sandbox use
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# APIC sandbox credentials
url = "https://sandboxapicdc.cisco.com"
user = "admin"
pw = "!v3G@!4@Y"  

# Create session object and login
session = Session(url, user, pw)
resp = session.login()

if not resp.ok:
    print("❌ Login failed:", resp.text)
    exit()
print("✅ Logged in successfully.")

# List existing tenants
print("\n--- Existing Tenants ---")
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)

# Create a new tenant
new_tenant_name = "Tenant_Name_Here"
new_tenant = Tenant(new_tenant_name)

# Create Application Profile and EPG
apn = AppProfile("My_apn", new_tenant)
epg = EPG("My_epg", apn)

# Create L3 context (VRF) and bridge domain
context = Context("My_vrf", new_tenant)
bridge_domain = BridgeDomain("My_bd", new_tenant)

# Link bridge domain with context and EPG
bridge_domain.add_context(context)
epg.add_bd(bridge_domain)

# Print payload and URL
print("\n--- Tenant JSON Payload ---")
print(new_tenant.get_url())
print(new_tenant.get_json())

# Push configuration to APIC
response = session.push_to_apic(new_tenant.get_url(), data=new_tenant.get_json())

if response.ok:
    print(f"\n✅ Tenant '{new_tenant_name}' created successfully.")
else:
    print(f"\n❌ Failed to create tenant: {response.text}")
    exit()

# Confirm tenant creation
print("\n--- Updated Tenant List ---")
tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)
    print('*' * 30)

# Clean up: Delete the tenant
print(f"\n🗑️  Deleting tenant '{new_tenant_name}'...")
new_tenant.mark_as_deleted()
del_response = session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())

if del_response.ok:
    print(f"✅ Tenant '{new_tenant_name}' deleted successfully.")
else:
    print(f"❌ Failed to delete tenant: {del_response.text}")


# sudo apt-get install graphviz libgraphviz-dev pkg-config
# pip3 install graphviz
# 
