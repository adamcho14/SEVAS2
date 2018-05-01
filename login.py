#!/usr/bin/env python
# coding: utf-8

#This is to be provided by Cosign, but for now...

from os import environ
import cgi, cgitb

login = ""

#if environ.has_key('HTTP_COOKIE'):
#    cookies = environ['HTTP_COOKIE'].strip()
 #   cookies = cookies.split(';')
 #   for cookie in cookies:
 #       (key, value) = cookie.split('=')
  #      if key == "REMOTE_USER":
  #          login = value

if environ.has_key('REMOTE_USER'):
    login = environ['REMOTE_USER']


print """Content-type: text/html

<form method="post" action="voting.py">
<input type="text" name="login" placeholder="Log in" value ="%s" required>
<br/>
<input type="submit" value="Submit">
</form>""" % login
