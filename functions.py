#!/usr/bin/env python
# coding: utf-8
import sqlite3

#this function selects candidates from the database
def select_candidates():
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/candidates.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM candidates")
    result = cursor.fetchall()

    connection.close()

    return result

def select_voters(login):
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM voters WHERE login=?", (login,))
    result = cursor.fetchall()

    connection.close()

    return result


def print_form_field(data):
    for i in data:
        idc = i[0] #candidate ID from the db
        first = i[1] #first name
        last = i[2] #last name

        print '<fieldset>'
        print '<legend>%s %s %s</legend>' % (idc, first, last)
        print '<input type = "radio" name = "%s" id="radios" value = "1"> Áno ' % (idc)
        print '<input type = "radio" name = "%s" id="radios" value = "2"> Nie ' % (idc)
        print '<input type = "radio" name = "%s" id="radios" value = "3" checked> Zdržal som sa' % (idc)
        print '</fieldset>'
