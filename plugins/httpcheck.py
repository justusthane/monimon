import requests

def httpcheck(host):
    try:
        r = requests.head(f"https://{host}")
        return [True, r.status_code]
    except requests.ConnectionError:
        return [False, r.status_code]
