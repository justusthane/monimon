import os
import subprocess
from plugins import plugin

def ping(arguments):
    print(plugin.Plugin.i)
    response = subprocess.run(["ping","-c","1",arguments['hostname']], 
                              stdout = subprocess.DEVNULL, stderr = subprocess.PIPE)
    if response.returncode == 0:
        return [True, ""]
    elif response.stderr:
        return [False, response.stderr.decode("UTF-8")]
    else:
        return [False, ""]
    
