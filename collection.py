#!/usr/bin/env python
# coding: utf-8

import cgi
import sqlite3
import rsa
import base64

form = cgi.FieldStorage()
encryptedLogin = form.getvalue('login')
#login = form.getvalue('login')
vote = form.getvalue('vote')

with open('administration/private.pem', 'rb') as private:
    data = private.read()
privkey = rsa.PrivateKey.load_pkcs1(data)
encryptedLogin = base64.b64decode(encryptedLogin)
login = rsa.decrypt(encryptedLogin, privkey)

connection = sqlite3.connect("db/persons.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
result = cursor.fetchall()
connection.close()

print """Content-type: text/html
<html>
<head>

<meta charset="UTF-8">

</head>

<body>

"""

sent = False
if result != [(0,)]:
    connection = sqlite3.connect("db/votes.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM votes WHERE login=?", (login,))
    result2 = cursor.fetchall()
    if result2 == [(0,)]:
        cursor.execute("INSERT INTO votes VALUES(?, ?)", (login, vote,))
        sent = True
    else:
        cursor.execute("SELECT CASE WHEN vote=0 THEN 0 ELSE 1 END FROM votes WHERE login=?", (login,))
        result3 = cursor.fetchall()
        if result3 ==[(0,)]:
            print """Už ste hlasovali papierovo. Nemožno už hlasovať elektronicky."""
        else:
            cursor.execute("UPDATE votes SET vote = ? WHERE login = ?", (vote, login,))
            sent = True
    connection.commit()
    if sent:
        print """Úspešne si poslal svoj hlas.
    <textarea rows="10" cols="50" id="display_vote">%s</textarea>""" % vote

else:
    print """Prepáč, ale nemôžeš hlasovať. Ak si myslíš, že to je chyba, prosím, obráť sa na Lampáreň!"""

connection.close()


print """
<a href=cosign/coslogout.php?backurl=/index.py>Odhlásiť sa</a>
</body>

</html>"""





