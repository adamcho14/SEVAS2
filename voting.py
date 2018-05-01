#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi
from os import environ
#import rsa
#import base64

form = cgi.FieldStorage()
login = form.getvalue('login')

#with open('administration/public.pem', 'r') as public:
#    data = public.read()
#pubkey = rsa.PublicKey.load_pkcs1(base64.b64decode(data))
#encryptedLogin = rsa.encrypt(login.encode('utf8'), pubkey)

#if environ.has_key('REMOTE_USER'):
    #login = environ['REMOTE_USER']

if f.select_voters(login) == [(0,)]:
    print """Content-type: text/html

You are not allowed to vote. Please, log in again.

<form method="post" action="login.py">
<input type="submit" name ="return" value="Return">
</form>
"""

else:

    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<script type="text/javascript" src="static/conf.js">
<script type="text/javascript" src="static/addressparser.js"></script>
<script type="text/javascript" src="static/mimeparser-tzabbr.js"></script>
<script type="text/javascript" src="static/mimeparser.js"></script>
<script type="text/javascript" src="static/emailjs-mime-codec.js"></script>
<script type="text/javascript" src="static/emailjs-mime-types.js"></script>
<script type="text/javascript" src="static/emailjs-addressparser.js"></script>
<script type="text/javascript" src="static/punycode.js"></script>
<script type="text/javascript" src="static/emailjs-mime-builder.js"></script>
<script type="text/javascript" src="static/SMIMEEncryptionExample.js"></script>
<script type="text/javascript" src="static/form_processing.js">
</script>
</head>
<body>

<p>Zvoľte maximálne %s kandidátov</p>
<form name="voting" method="post" action="collection.py">""" % str(c.CAND_NUM)
    print(f.print_form_field(f.select_candidates()))

    print """
<input type="hidden" name="login" value="%s">
<input type="hidden" name="vote" value="0">
<input type="submit" name ="submit" value="Pošli hlas">
</form>
<a onclick="processForm();">Vytvor hlas</a>
<p id="display_vote">Tvoj zašifrovaný hlas</p>
</body>
</html>""" % (login)


