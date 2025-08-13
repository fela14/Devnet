import yaml

with open('router.yaml') as data:
    yaml_data = data.read()
yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)
print(yaml_dict)

yaml_dict['interfaces'][0]['name'] = 'my_eth'
yaml_dict['interfaces'][0]['description'] = 'MainOne link'
yaml_dict['interfaces'][1]['name'] = 'your_eth'
yaml_dict['interfaces'][1]['description'] = 'Airtel link'

print(yaml.dump(yaml_dict, default_flow_style=False))

with open('router.yaml', 'w') as data:
    yaml.dump(yaml_dict, data, default_flow_style=False)
