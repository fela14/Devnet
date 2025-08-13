import json

with open('custom.json') as data:
    json_data = data.read()
    json_dict = json.loads(json_data)


print(json_dict)
print(type(json_dict))
print(json_dict['Interface'])
print(json_dict['Interface'][0])
print(json_dict['Interface'][1])
print(json_dict['Interface'][1]['name'])
print(json_dict['Interface'][1]['description'])
print(json_dict['Interface'][1]['ipv4'])
print(json_dict['Interface'][1]['ipv4']['address'])
print(json_dict['Interface'][1]['ipv4']['address'][0])


json_dict['Interface'][0]['description'] = 'Backup Link'
json_dict['Interface'][1]['description'] = 'Router Uplink'

with open('custom.json', 'w') as fh:

    json_edit = json.dump(json_dict, fh, indent=4)

print(json_dict['Interface'])

