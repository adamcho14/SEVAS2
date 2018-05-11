#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi
from os import environ
#import rsa
#import base64

#form = cgi.FieldStorage()
#login = form.getvalue('login')

#  variable sent from the server
#if environ.has_key('REMOTE_USER'):
    #login = environ['REMOTE_USER']

#these two lines must be deleted before release
#else:
    #login = "skuska"

#if f.select_voters(login) == [(0,)]:
    #print """Content-type: text/html

#You are not allowed to vote. Please, log in again.

#<form method="post" action="login.py">
#<input type="submit" name ="return" value="Return">
#</form>
#"""

# variable sent from the server

if True:
#if environ.has_key('REMOTE_USER'):
    #login = environ['REMOTE_USER']

    #with open('administration/public.pem', 'r') as public:
        #data = public.read()
    #pubkey = rsa.PublicKey.load_pkcs1(base64.b64decode(data))
    #encryptedLogin = rsa.encrypt(login.encode('utf8'), pubkey)

    encryptedLogin = "skuska"

    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<script type="text/javascript" src="static/conf.js">
<script type="text/javascript" src="static/pkijs/addressparser.js"></script>
<script type="text/javascript" src="static/pkijs/mimeparser-tzabbr.js"></script>
<script type="text/javascript" src="static/pkijs/mimeparser.js"></script>
<script type="text/javascript" src="static/pkijs/emailjs-mime-codec.js"></script>
<script type="text/javascript" src="static/pkijs/emailjs-mime-types.js"></script>
<script type="text/javascript" src="static/pkijs/emailjs-addressparser.js"></script>
<script type="text/javascript" src="static/pkijs/punycode.js"></script>
<script type="text/javascript" src="static/pkijs/emailjs-mime-builder.js"></script>
<script type="text/javascript" src="static/pkijs/SMIMEEncryptionExample.js"></script>
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
<input type="hidden" name ="submit" value="">
</form>
<button type="button" onclick="processForm(%s);">Vytvor hlas</button><br>
<textarea rows="10" cols="50" id="display_vote">Tvoj zašifrovaný hlas</textarea>
</body>
</html>""" % (encryptedLogin, str(c.CAND_NUM))

else:
    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">

</head>
<body>
<p>Nie ste platne prihlásení. Skúste to znova.</p>

<form method="post" action="https://login.uniba.sk">
<input type="submit" name ="return" value="Prihlásiť sa">
</form>
</body>
</html>"""


