#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi, cgitb
import os
import rsa
import base64

if True:
#if os.environ.has_key('REMOTE_USER'):
    #login = os.environ['REMOTE_USER']
    login = "skuska"

    with open('administration/public.pem', 'rb') as public:
        data = public.read()
    pubkey = rsa.PublicKey.load_pkcs1(data)
    encryptedLogin = rsa.encrypt(login.encode('utf8'), pubkey)
    encryptedLogin = base64.b64encode(encryptedLogin)

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


