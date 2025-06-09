# a simple python script to configure loopback interfaces and ospf on a router

import getpass
import telnetlib

HOST = "192.168.64.130"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"python\n")
tn.write(b"conf t\n")
tn.write(b"int lo1\n")
tn.write(b"ip add 10.10.10.10 255.255.255.255\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 20.20.20.20 255.255.255.255\n")
tn.write(b"int lo3\n")
tn.write(b"ip add 30.30.30.30 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))


# a simple python script to configure vlans on a switch


import getpass
import telnetlib

HOST = "192.168.64.131"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"enable\n")
tn.write(b"python\n")
tn.write(b"conf t\n")
tn.write(b"vlan 10\n")
tn.write(b"name HR\n")
tn.write(b"vlan 20\n")
tn.write(b"name VOICE\n")
tn.write(b"vlan 30\n")
tn.write(b"name SALES\n")
tn.write(b"vlan 40\n")
tn.write(b"name MGMT\n")
tn.write(b"vlan 50\n")
tn.write(b"name LEISURE\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))


# a simple python script to configure vlans on a switch using a for loop

import getpass
import telnetlib

HOST = "192.168.64.131"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"enable\n")
tn.write(b"python\n")
tn.write(b"conf t\n")

for n in range(2,51):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name PYTHON_VLAN_" + str(n).encode('ascii') + b"\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))

# a simple python script for configuring vlans on multiple switches

import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open('myswitches')
for IP in f:
    IP = IP.strip()
    print("Configuring Swicth " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"enable\n")
    tn.write(b"python\n")
    tn.write(b"conf t\n")

    for n in range(2,51):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name PYTHON_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))


# a simple python script for getting running config from switches



import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open('myswitches')
for IP in f:
    IP = IP.strip()
    print("Get running config from Swicth " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"enable\n")
    tn.write(b"python\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write(b"\n")
    saveoutput.close

    print(tn.read_all().decode('ascii'))


# netmiko

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.130',
    'username': 'david',
    'password': 'cisco'
}

net_connect = ConnectHandler(**iosv_l2)
net_connect.enable()
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,21):
    print ("creating VLAN " + str(n))
    config_command = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)


# connect to multiple switches via ssh, create vlans


from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.131',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.132',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'

}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.133',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    for n in range (2,21):
        print ("creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)


# connect to multiple switches, read a set of commands from a file


from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.134',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.135',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.136',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)


# connect to multiple switches, read a set of commands from a file


from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.131',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.132',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.133',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.134',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.135',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.64.136',
    'username': 'switch',
    'password': 'switch',
    'secret': 'python'
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)

with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)