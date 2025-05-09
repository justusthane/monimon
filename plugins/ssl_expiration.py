import ssl
import socket

def ssl_expiration(url):
    context = ssl.create_default_context()

    #context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    #context.check_hostname = False
    #context.verify_mode = ssl.CERT_NONE
    #context.options &= ~ssl.OP_NO_TLSv1
    #context.options &= ~ssl.OP_NO_SSLv3
    port = 443 if not "port" in details else details['port']
    with context.wrap_socket(socket.socket(socket.AF_INET),
                             server_hostname=details['hostname']) as conn:
        conn.connect((details['hostname'], port))
        cert = conn.getpeercert()
        print()
        print(host)
        print(cert['serialNumber'])
        print(cert['subject'][4][0][1])
        print(cert['notAfter'])
