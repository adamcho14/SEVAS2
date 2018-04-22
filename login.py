#!/usr/bin/env python
# coding: utf-8

#This is to be provided by Cosign, but for now...

from os import environ
import cgi, cgitb

if environ.has_key('HTTP_COOKIE'):
    for cookie in map(environ['HTTP_COOKIE'].strip(), environ['HTTP_COOKIE'].split(';')):
        (key, value) = cookie.split('=')
        if key == "REMOTE_USER":
            login = value

else:
    print """Content-type: text/html

    <form method="post" action="voting.py">
    <input type="text" name="login" placeholder="Log in" required>
    <br/>
    <input type="submit" value="Submit">
    </form>"""
