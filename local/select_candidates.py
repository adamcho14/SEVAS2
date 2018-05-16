import sqlite3
import json

connection = sqlite3.connect("../db/persons.sqlite")
cursor = connection.cursor()
cursor.execute("SELECT * FROM candidates")
result = cursor.fetchall()

connection.close()

with open("candidates.txt", 'w') as file:
    json.dump(result, file)
