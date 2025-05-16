#!/usr/bin/env python
from monimon.colors import Colors
from monimon import core
row_format = "{:<30} {:<10} {:<6}"

def format_status(status):
    if status:
        return f"{Colors.GREEN}Success{Colors.END}"
    else:
        return f"{Colors.RED}Failure{Colors.END}"


if __name__ == 'app':
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def print_monitor():
        return "Hello"

elif __name__ == '__main__':
    for result in core.monitor():
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

