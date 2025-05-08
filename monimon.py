#!/usr/bin/env python
import yaml
import pprint
import json
import sys
sys.path.append('plugins/plugins')
import pkgutil
import importlib
plugins = {}
for finder, name, ispkg in pkgutil.iter_modules(path=['plugins/plugins']):
    plugins[name] = importlib.import_module(name)
row_format = "{:<30}{:<10}{:<6}{:<20}"

with open('hosts.yaml', 'r') as file:
    hosts = yaml.safe_load(file)

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
        print(row_format.format(host, action_name, result[0], result[1]))
