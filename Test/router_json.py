import json

with open('router.json') as data:
    json_data = data.read()

json_dict = json.loads(json_data)

print(type(json_dict))
print(json_dict)
print('*'*25)
json_dict['interfaces'][0]['name'] = 'my_eth'
json_dict['interfaces'][0]['description'] = 'MainOne link'
json_dict['interfaces'][1]['name'] = 'your_eth'
json_dict['interfaces'][1]['description'] = 'Airtel link'
print(json.dumps(json_dict, indent=4))

with open('router.json', 'w') as data:
    json.dump(json_dict, data, indent=4)