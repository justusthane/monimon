import requests

# TODO: Check return status code
def httpcheck(arguments):
    try:
        r = requests.head(f"{arguments['endpoint']}")
        return [True, f"Status code: {r.status_code}"]
    except requests.ConnectionError:
        return [False, f"Status code: {r.status_code}"]
