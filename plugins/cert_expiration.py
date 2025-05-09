import ssl
import OpenSSL
from datetime import datetime,timedelta
from socket import gaierror

def cert_expiration(args):
    hostname = args['endpoint'].split(":")[0]
    
    try:
        port = args['endpoint'].split(":")[1]
    except IndexError:
        port = 443

    try:
        cert = ssl.get_server_certificate((hostname, port))
    except gaierror:
        return [False, "Failed to connect to server."]

    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiration_date = datetime.strptime(f"{x509.get_notAfter().decode("UTF-8")[0:-1]}UTC", "%Y%m%d%H%M%S%Z") 

    if (expiration_date - timedelta(days = args['expiration_warning_days'])) < datetime.now():
        status = False
    else:
        status = True
          

    return [status, f"Expiration: {expiration_date}"]


