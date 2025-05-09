import requests

def httpcheck(arguments):
    try:
        r = requests.head(f"{arguments['endpoint']}")
        return ["Success", f"Status code: {r.status_code}"]
    except requests.ConnectionError:
        return ["Failure", f"Status code: {r.status_code}"]
