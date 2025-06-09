import xmltodict

with open('custom.xml') as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict)
print(type (xml_dict))

print(xml_dict["interface"])
print(xml_dict["interface"]["name"])
print(xml_dict["interface"]["ipv4"])
print(xml_dict["interface"]["ipv4"]["address"])
print(xml_dict["interface"]["ipv4"]["address"]["ip"])

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.6.5"
xml_dict["interface"]["ipv4"]["address"]["netmask"] = "255.255.255.252"

print(xml_dict["interface"]["ipv4"]["address"])
print(xml_dict["interface"]["ipv4"]["address"]["ip"])

with open('custom.xml', 'w')as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))
    