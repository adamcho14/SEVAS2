#!/usr/bin/env python

import rsa
import base64

(pubkey, privkey) = rsa.newkeys(512)

with open('private.pem', 'w') as private:
    private.write(str(base64.b64encode(privkey.save_pkcs1())))
    print(base64.b64encode(privkey.save_pkcs1()))

with open('public.pem', 'w') as public:
    public.write(str(base64.b64encode(pubkey.save_pkcs1())))
    print(base64.b64encode(pubkey.save_pkcs1()))
