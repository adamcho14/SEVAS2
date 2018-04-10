#!/usr/bin/env python

import cgi
import sqlite3
import functions

form = cgi.FieldStorage()
login = form.getvalue('login')
vote = form.getvalue('vote')
f_val = form.getvalue('1')

connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
result = cursor.fetchall()

print """Content-type: text/html

The form input is below...<br/>"""
print login
print vote
#print f_val
#print result

#if result != [(0,)]:
    #conn = sqlite3.connect("votes.db")
cursor.execute("INSERT INTO votes VALUES(?, ?)", (login, vote,))





