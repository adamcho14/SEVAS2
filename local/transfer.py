#!/usr/bin/env python

import json
import sqlite3

connection = sqlite3.connect("/Applications/PyCharm.app/Contents/bin/voting.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT vote FROM votes")
result = cursor.fetchall()
connection.close()

# getting rid of paper votes. They are counted somewhere else.
for v in result:
    if v[0] == '0':
        result.remove(v)

with open('votes.txt', 'w') as file:
    json.dump(result, file)

