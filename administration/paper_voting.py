#!/usr/bin/env python

print """Content-type: text/html

<form method="post" action="process_pv.py">
<input type="text" name="first" placeholder="Meno" required>
<input type="text" name="last" placeholder="Priezvisko" required>
<br/>
<input type="submit" value="Submit">
</form>"""
