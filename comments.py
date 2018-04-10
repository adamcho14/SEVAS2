#!/usr/bin/env python

print """Content-type: text/html

<form method="post" action="collection.py">
<textarea name="login" cols="10" rows="1" placeholder="Enter your name">
</textarea>
<br/>
<textarea name="comments" cols="40" rows="5" placeholder="Enter your comment">
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""
