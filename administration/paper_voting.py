#!/usr/bin/env python
# coding: utf-8

import cgi, cgitb

form = cgi.FieldStorage()
login = form.getvalue('login')
password = form.getvalue('password')

if login == "admin" and password == "matfyzjein":
    print """Content-type: text/html

<head>

<meta charset="UTF-8">

</head>
<body>

<p>Zadajte login voliča, ktorého práve chcete zaregistrovať na podanie papierového hlasu:</p><br>

<form method="post" action="process_pv.py">
<input type="text" name="login" placeholder="Login" required>
<br/>
<input type="submit" value="Submit">
</form>

</body>"""

else:
    print """Chyba!"""
