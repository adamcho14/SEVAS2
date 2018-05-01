#!/usr/bin/env python
# coding: utf-8

#This is to be provided by Cosign, but for now...

from os import environ
import cgi, cgitb

print """Content-type: text/html
<html>

<head>

<meta charset="UTF-8">

</head>

<body>

<p>Vitajte na stránkach volebného systému FMFI</p>
<form method="post" action="https://login.uniba.sk">
<input type="submit" value="Prihlásiť sa">
</form>
</body>
</html>"""
