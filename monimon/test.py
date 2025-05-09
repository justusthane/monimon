#!/usr/bin/env python
import OpenSSL
import ssl
from datetime import datetime,timedelta
now = datetime.now()
cert = ssl.get_server_certificate(('secureassets.confederationcollege.ca', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
expiration_date = datetime.strptime(f"{x509.get_notAfter().decode("UTF-8")[0:-1]}UTC", "%Y%m%d%H%M%S%Z") 
warning_date = expiration_date - timedelta(days = 30)
print(expiration_date)
print(warning_date)

if (expiration_date - timedelta(days = 30)) > now:
    print("WARNING")
else:
    print("All good")
