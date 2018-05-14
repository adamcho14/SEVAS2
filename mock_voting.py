#!/usr/bin/env python
# coding: utf-8

#This is to be provided by Cosign, but for now...

import os
import cgi, cgitb

form = cgi.FieldStorage()
login = form.getvalue('login')

os.environ['REMOTE_USER'] = str(login)

print """Content-type: text/html
<html>

<head>

<meta charset="UTF-8">

</head>

<body>
<p>%s, vitajte!</p>
<form method="post" action="voting.py">
<input type="submit" value="Začať hlasovať">
</form>
</body>
</html>""" % login
