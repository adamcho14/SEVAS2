#!/usr/bin/env python
# coding: utf-8

import cgi
import sqlite3


def select_voters(login):
    connection = sqlite3.connect("/Users/Adam/PycharmProjects/SEVAS/db/persons.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM voters WHERE login=?", (login,))
    result = cursor.fetchall()

    connection.close()

    return result

form = cgi.FieldStorage()
login = form.getvalue('login')

result = select_voters(login)

print """Content-type: text/html

<html>
<head>

<meta charset="UTF-8">

</head>

<body>"""

if len(result) == 0:

    print """

<p>Chyba! Taký volič v databáze nie je</p>"""

else:
    connection = sqlite3.connect("/Users/Adam/PycharmProjects/SEVAS/db/votes.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM votes WHERE login=?", (login,))
    result2 = cursor.fetchall()
    if result2 == [(0,)]:
        cursor.execute("INSERT INTO votes (login, vote) VALUES(?, 0)", (login,))
    else:
        cursor.execute("UPDATE votes SET vote = 0 WHERE login = ?", (login,))
    connection.commit()
    connection.close()
    print
    """<p>Úspešne ste zaregistrovali voliča.</p>"""

print """
</body>
</html>"""
