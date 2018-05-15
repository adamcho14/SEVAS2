#!/usr/bin/env python
# coding: utf-8

import sqlite3

cont = True
connection = sqlite3.connect("../db/persons.sqlite")

while cont:
    login = input("Login voliča: ")

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM voters WHERE UKLogin=?", (login,))
    result = cursor.fetchall()

    if result == [(0,)]:
        cursor.execute("INSERT INTO voters VALUES(?)", (login,))
        print("Volič pridaný.")
        connection.commit()
    else:
        print("Volič už existuje v db.")

    inp = input("Pridať ďalšieho voliča (y/n)?")

    if inp == "n":
        cont = False

connection.close()
