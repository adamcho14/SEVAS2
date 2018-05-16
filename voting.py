#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi, cgitb
import os
import rsa
import base64

#if 'REMOTE_USER' in os.environ:
    #login = os.environ['REMOTE_USER']
if True:
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
<title>Hlasovanie</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script type="text/javascript" src="static/conf.js"></script>
<script type="text/javascript" src="static/dist/openpgp.min.js"></script>
<script type="text/javascript" src="static/form_processing.js">
</script>
</head>
<body>

<h1> %s, vitajte vo volebnej aplikácii</h1>
<h2>Zvoľte maximálne %s kandidátov</h2>
<form name="voting" method="post" action="collection.py">""" % (login, str(c.CAND_NUM))
    print(f.print_form_field(f.select_candidates()))

    print """<input type="hidden" name="vote" value="0">
<input type="hidden" class="btn btn-primary" name ="submit" value="">
</form>
<button type="button" class="btn btn-primary" onclick="processForm(%s);">Vytvor hlas</button><br>
<textarea rows="10" cols="50" id="display_vote">Tvoj zašifrovaný hlas</textarea>
</body>
</html>""" % (str(c.CAND_NUM))

else:
    print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">

</head>
<body>
<p>Nie ste platne prihlásení. Skúste to znova.</p>

<form method="post" action="cosign/coslogin.php?backurl=/voting.py">
<input type="submit" name ="return" class="btn btn-primary" value="Prihlásiť sa">
</form>
</body>
</html>"""


