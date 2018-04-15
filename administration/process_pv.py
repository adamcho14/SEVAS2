#!/usr/bin/env python
# coding: utf-8

import cgi
import sqlite3


def select_voters(login):
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM voters WHERE login=?", (login,))
    result = cursor.fetchall()

    connection.close()

    return result


def make_having_voted(login):
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
    cursor = connection.cursor()
    cursor.execute("UPDATE voters SET paper_voted='1' WHERE login=?", (login,))
    connection.commit()

    connection.close()

form = cgi.FieldStorage()
UKlogin = form.getvalue('login')

result = select_voters(UKlogin)

print """Content-type: text/html

    <head>

    <meta charset="UTF-8">

    </head>"""

if len(result) == 0:

    print """<body>

    <p>Chyba! Taký volič v databáze nie je</p>

    </body>"""

else:
    make_having_voted(UKlogin)
    print """<body>

    <p>Zaregistrujte voličov papierový hlas</p>

    <form method="post" action="../collection.py">
    <input type="hidden" name="login" value="%s">
    <input type="hidden" name="vote" value="0">
    <input type="submit" value="Submit">
    </form>

    </body>""" % (UKlogin)
