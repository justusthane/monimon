import os
import subprocess
import plugin
x = plugin.Plugin()
def ping(arguments):
    response = subprocess.run(["ping","-c","1",arguments['hostname']], 
                              stdout = subprocess.DEVNULL, stderr = subprocess.PIPE)
    if response.returncode == 0:
        return ["Success", ""]
    elif response.stderr:
        return ["Success", response.stderr.decode("UTF-8")]
    else:
        return ["Failure", ""]
    
