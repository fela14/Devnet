import xmltodict

with open('router.xml') as data:
    xml_data = data.read()
xml_dict = xmltodict.parse(xml_data)
print(xml_dict)

xml_dict['interfaces']['interface'][0]['name'] = 'my_eth'
xml_dict['interfaces']['interface'][0]['description'] = 'MainOne link'
xml_dict['interfaces']['interface'][1]['name'] = 'your_eth'
xml_dict['interfaces']['interface'][1]['description'] = 'Airtel link'

print(xmltodict.unparse(xml_dict, pretty=True))

with open('router.xml', 'w') as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))