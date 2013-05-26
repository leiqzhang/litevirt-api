#!/usr/bin/python

import subprocess

def runcmd(cmd):
    proc = subprocess.Popen(cmd, 
                     shell=True, 
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.STDOUT)
    stdout = proc.stdout.read()
    retval = proc.wait()
    return (retval, stdout)

def uuidgen():
    import uuid
    return str(uuid.uuid4())

def hashgen(s):
    import hashlib
    return hashlib.sha224(s).hexdigest()

if __name__ == "__main__":
    ret, out = runcmd("ls")
    print (ret, out)

    uuid = uuidgen()
    print uuid
