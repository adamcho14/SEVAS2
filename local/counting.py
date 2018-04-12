#!/usr/bin/env python

import json
import config as c

def decrypt(s):
    return s

# this function creates a list out of given string
def parse(s):
    return list(s)


# this function validates given list
def validate(l):
 return True


#this function gets values in given list. List must be validated beforehand
def get_values(l):
    #print(len(l))
    values = {}
    j = 1 #prve cislo v stringu
    while j < len(l):
        key = 0
        val = 0
        while l[j] != '#':
            key = 10*key + int(l[j])
            j += 1
        j += 1 #prve cislo po #
        while l[j] != '>':
            val = 10*val + int(l[j])
            j += 1
        values[key] = val
        j += 2 #prve cislo po <... preskakujem ><
    return values

with open('votes.txt', 'r') as file:
    votes = json.load(file)

for i in votes:
    print(get_values(parse(decrypt(i[0]))))
