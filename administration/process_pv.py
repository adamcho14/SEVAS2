#!/usr/bin/env python

import cgi
from administration import admin_functions as f

form = cgi.FieldStorage()
first_name = form.getvalue('first')
last_name = form.getvalue('last')

result = f.select_voters(first_name, last_name)

print(result)
