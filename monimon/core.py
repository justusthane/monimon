import yaml
import pprint
import json
import sys
sys.path.append('monimon/plugins')
import pkgutil
import importlib
plugins = {}
for finder, name, ispkg in pkgutil.iter_modules(path=['monimon/plugins']):
    plugins[name] = importlib.import_module(name)

def monitor():
    with open('monimon/hosts.yaml', 'r') as file:
        hosts = yaml.safe_load(file)

    return_list = []
    for host, details in hosts['hosts'].items():
        for action in details['actions']:
            # Start building the arguments dict that will get passed to the plugin.
            # By default, the only item is the hostname.
            arguments = {'hostname': details['hostname']}

            # Check if the action has any parameters defined in the YAML file, by
            # checking if it's a string or a dict
            if type(action) is str:
                action_name = action
            # If it's a dict, add each parameter to the arguments dict
            elif type(action) is dict:
                action_name = list(action)[0]
                for argument, value in action[action_name].items():
                    arguments[argument] = value

            #print(arguments)
            result = getattr(plugins[action_name], action_name)(arguments)
            #print(f"{host}\t{action_name}\t{result[0]}\t{result[1]}")
            
            return_dict = {'host': host, 'action_name': action_name}
            if type(result) is list:
                return_dict['result'] = result[0]
                if len(result) > 1:
                    return_dict['details'] = result[1]
            else:
                return_dict['result'] = result

            return_list.append(return_dict)
    return return_list
