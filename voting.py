#!/usr/bin/env python
# coding: utf-8

import functions as f
import config as c
import cgi

form = cgi.FieldStorage()
login = form.getvalue('login')

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
<script type="text/javascript" src="/static/form_processing.js">
</script>
</head>
<body>

<p>Zvoľte maximálne %s kandidátov</p>
<form name="voting" method="post" action="collection.py" onsubmit="return processForm(%s)">""" % (str(c.CAND_NUM), str(c.CAND_NUM))
    print(f.print_form_field(f.select_candidates()))

    print """
<input type="hidden" name="login" value="%s">
<input type="hidden" name="vote" value="0">
<input type="submit" name ="submit" value="Submit">
</form>

</body>
</html>""" % (login)


