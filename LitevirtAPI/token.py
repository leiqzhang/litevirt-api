#/usr/bin/python

import time
import socket
import os
import base64

from OpenSSL.crypto import load_certificate, load_privatekey
from OpenSSL.crypto import sign, verify
from OpenSSL.crypto import FILETYPE_PEM, FILETYPE_ASN1, FILETYPE_TEXT

PRIV_KEY_FILE = '/etc/ssl/private/litevirt.pem'
CERT_FILE = '/etc/ssl/private/litevirt.cert'

def populate():
    timestamp = int(time.time())
    hostname = socket.gethostname()
    uid = os.getuid()

    content = '%s:%s:%s' % (timestamp, hostname, uid)
    priv_key = load_privatekey(FILETYPE_PEM, open(PRIV_KEY_FILE).read())
    sig = base64.b64encode(sign(priv_key, content, "sha1"))
    return '%s:%s' % (content, sig)

def validate(token):
    try:
        # This will probably populate ValueError, 
        # if token is not correctly formatted.
        ts, hostname, uid, sig = token.split(':')
        content = '%s:%s:%s' % (ts, hostname, uid)
        sig = base64.b64decode(sig)
        cert = load_certificate(FILETYPE_PEM, open(CERT_FILE).read())

        # Openssl populates Error if verfication fails.
        verify(cert, sig, content, "sha1")
        return (ts, hostname, uid)
    except:
        return None

if __name__ == '__main__':
    token = populate()
    print "token=%s" % token

    res = validate(token)
    if res:
        print "ts=%s, hostname=%s, uid=%s" % (res[0], res[1], res[2])
