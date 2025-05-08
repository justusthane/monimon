import ssl
import OpenSSL
from datetime import datetime,timedelta

def cert_expiration(args):
    hostname = args['endpoint'].split(":")[0]
    
    try:
        port = args['endpoint'].split(":")[1]
    except IndexError:
        port = 443

    cert = ssl.get_server_certificate((hostname, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiration_date = datetime.strptime(f"{x509.get_notAfter().decode("UTF-8")[0:-1]}UTC", "%Y%m%d%H%M%S%Z") 

    status = "Success"
    if (expiration_date - timedelta(days = args['expiration_warning_days'])) < datetime.now():
        status = "Warning"
    else:
        status = "Success"
          

    return [status, f"Expiration: {expiration_date}"]


