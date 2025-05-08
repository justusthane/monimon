import os
import subprocess

def ping(host):
    response = subprocess.run(["ping","-c","1",host], 
                              stdout = subprocess.DEVNULL, stderr = subprocess.PIPE)
    if response.returncode == 0:
        return [True, ""]
    elif response.stderr:
        return [False, response.stderr]
    else:
        return [False, ""]
    
