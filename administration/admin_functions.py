#!/usr/bin/env python

import sqlite3


def select_voters(first, last):
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM voters WHERE first_name=? AND last_name=?", (first,last,))
    result = cursor.fetchall()

    connection.close()

    return result

def make_havin_voted(first, last):
    connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
    cursor = connection.cursor()
    cursor.execute("UPDATE voters SET paper_voted = 1 WHERE first_name = ? AND last_name = ?", (first, last,))

    connection.close()
