#!/usr/bin/env python

#This is to be provided by Cosign, but for now...

print """Content-type: text/html

<form method="post" action="voting.py">
<input type="text" name="login" placeholder="Log in" required>
<br/>
<input type="submit" value="Submit">
</form>"""
