import requests

def httpcheck(arguments):
    try:
        r = requests.head(f"{arguments['endpoint']}")
        return [True, r.status_code]
    except requests.ConnectionError:
        return [False, r.status_code]
