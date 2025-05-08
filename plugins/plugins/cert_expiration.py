import socket
import ssl

def cert_expiration(args):
    hostname = args['endpoint'].split(":")[0]
    
    try:
        port = args['endpoint'].split(":")[1]
    except IndexError:
        port = 443

    context = ssl.create_default_context()

    with context.wrap_socket(socket.socket(socket.AF_INET),
                                           server_hostname = hostname) as conn:
        conn.connect((hostname, int(port)))

        cert = conn.getpeercert()

        return [True, f"Expiration: {cert['notAfter']}"]


          
