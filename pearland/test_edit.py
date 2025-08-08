# from ncclient import manager
# from test_router import router
# from jinja2 import Template

# router_config = open("test_edit_filter.xml").read()

# template = Template(router_config)

# router_template = template.render(
#     interface_name="Uplink",
#     interface_description="Management - 'MainOne'",
#     interface_address="20.20.20.20",
#     interface_mask="255.255.255.0"
# )

# with manager.connect(
#     host=router["host"],
#     port=router["port"],
#     username=router["username"],
#     password=router["password"],
#     hostkey_verify=False,
#     look_for_keys=False,
#     allow_agent=False
#     ) as m:

#     m.edit_config(config=router_template, target="running")
#     print("✅ Configuration applied.")
#     print("======= CONFIG TO SEND =======")
#     print(router_template)
#     print("==============================")

from ncclient import manager
from jinja2 import Template
from lxml import etree  # ✅ this is the right one
from test_router import router

# Load and render the XML template
with open("test_edit_filter.xml") as f:
    template_str = f.read()

template = Template(template_str)
router_template = template.render(
    interface_name="1",
    interface_description="Management - MainOne",
    interface_address="20.20.20.20",
    interface_mask="255.255.255.0"
)

# Remove XML declaration if present
if router_template.strip().startswith("<?xml"):
    router_template = router_template.split("?>", 1)[1].strip()

# ✅ Convert string to lxml element
xml_payload = etree.fromstring(router_template.encode())

# Connect and send config
with manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False,
    look_for_keys=False,
    allow_agent=False
) as m:
    m.edit_config(target="running", config=xml_payload)
    print("✅ Configuration applied.")

