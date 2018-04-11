#!/usr/bin/env python

import json


# this function creates a list out of given string
def parse(s):
    return list(s)

# this function validates given list
def validate(l):
 return True

#this function gets values in given list
def get_values():
    return 0

with open('votes.txt', 'r') as file:
    votes = json.load(file)

for i in votes:
    print(parse(i[0]))
