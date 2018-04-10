#!/usr/bin/env python

import functions as f
import config as c

print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">
<script type="text/javascript" src="/static/form_processing.js">
</script>
</head>
<body>

<form name="voting" method="post" action="collection.py" onsubmit="return processForm()">"""
print(f.print_form_field(f.select_candidates()))

print """
<input type="hidden" name="login" value="%s">
<input type="hidden" name="vote" value="0">
<input type="submit" name ="submit" value="Submit">
</form>

</body>
</html>""" % (c.LOGIN)


