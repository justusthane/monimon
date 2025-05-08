#!/usr/bin/env python
import yaml
import pprint
import json
import sys
sys.path.append('plugins')
import pkgutil
import importlib
plugins = {}
for finder, name, ispkg in pkgutil.iter_modules(path=['plugins']):
    plugins[name] = importlib.import_module(name)
row_format = "{:<30}{:<10}{:<6}{:<20}"

with open('hosts.yaml', 'r') as file:
    hosts = yaml.safe_load(file)

for host, details in hosts['hosts'].items():
    for action in details['actions']:
        !!! arguments = {'hostname': }

        result = getattr(plugins[action], action)(details['hostname'])
        #print(f"{host}\t{action}\t{result[0]}\t{result[1]}")
        print(row_format.format(host, action, result[0], result[1]))
