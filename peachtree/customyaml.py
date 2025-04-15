from yaml import load, dump, FullLoader
import yaml

with open('custom.yaml') as data:
    yaml_sample = data.read()
    yaml_dict = load(yaml_sample, Loader=FullLoader)

print(type (yaml_dict))

yaml_dict["interface"]["name"] = "GigabitEthernet3"
yaml_dict["interface"]["enabled"] = "False"

with open('custom.yaml', 'w'):
    yaml_dic = dump(yaml_dict, default_flow_style=False)

print(yaml_dic)
