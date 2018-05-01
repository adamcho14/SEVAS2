#!/usr/bin/env python
# coding: utf-8

import cgi
import sqlite3
#import rsa
#import base64

form = cgi.FieldStorage()
#encryptedLogin = form.getvalue('login')
login = form.getvalue('login')
vote = form.getvalue('vote')

#with open('administration/private.pem', 'r') as private:
#    data = private.read()
#privkey = rsa.PrivateKey.load_pkcs1(base64.b64decode(data))
#login = rsa.encrypt(encryptedLogin, privkey)

connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
result = cursor.fetchall()

print """Content-type: text/html

"""

if result != [(0,)]:
    cursor.execute("SELECT COUNT(*) FROM votes WHERE login=?", (login,))
    result2 = cursor.fetchall()
    if result2 == [(0,)]:
        cursor.execute("INSERT INTO votes VALUES(?, ?)", (login, vote,))
    else:
        cursor.execute("UPDATE votes SET vote = ? WHERE login = ?", (vote, login,))
    connection.commit()
    print """You have successfully casted your vote."""
    print(vote)

else:
    print """Sorry, you are not allowed to vote. If you think this is a mistake, please, ask Lamparen for help"""

connection.close()





