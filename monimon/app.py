#!/usr/bin/env python
import yaml
import pprint
import json
import sys
sys.path.append('monimon/plugins')
import pkgutil
import importlib
from monimon.colors import Colors
plugins = {}
for finder, name, ispkg in pkgutil.iter_modules(path=['monimon/plugins']):
    plugins[name] = importlib.import_module(name)
row_format = "{:<30} {:<10} {:<6}"

def format_status(status):
    if status:
        return f"{Colors.GREEN}Success{Colors.END}"
    else:
        return f"{Colors.RED}Failure{Colors.END}"

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

if __name__ == 'app':
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def print_monitor():
        return "Hello"

elif __name__ == '__main__':
    for result in monitor():
        print(row_format.format(f"{Colors.BOLD}{result['host']}{Colors.END}", 
                                result['action_name'], 
                                format_status(result['result'])))
        if 'details' in result:
            print(f"{Colors.YELLOW}{result['details']}{Colors.END}")



#print(monitor())
#if type(result) is list:
#    print(row_format.format(f"{Colors.BOLD}{host}{Colors.END}", action_name, translate_status(result[0])))
#    print(f"{Colors.YELLOW}{result[1]}{Colors.END}")
#else:
#    print(row_format.format(host, action_name, translate_status(result)))

