from ncclient import manager

router = {"host": "devnetsandboxiosxe.cisco.com",
          "port": "22", 
          "username": "admin", 
          "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()

