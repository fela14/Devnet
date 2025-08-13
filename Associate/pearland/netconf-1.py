from ncclient import manager

router = {"host": "10.10.20.48",
          "port": "830", 
          "username": "admin", 
          "password": "C1sco12345"}

with manager.connect(host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False) as m:
    print("NETCONF session established")
   

