#!/usr/bin/env python
#codin: utf-8
#https://cryptography.io/en/latest/

from secretsharing import PlaintextToHexSecretSharer

ids = []
shares = []
no_of_chars = []

# get the number of lines of our key
with open("lines.txt", 'r') as lines:
    sh = int(lines.readline()) #  required shares
    n = int(lines.readline())  #  number of lines
    for i in range(n):
        no_of_chars.append(int(lines.readline()))

print("Write " + str(sh) + " IDs used to recover the secret.")
for i in range(sh):
    ids.append(int(input()))

# for each line open shares
for l in range(n):
    new_share = []
    for s in range(sh):
        dir = "shares" + str(ids[s]) + "/"
        fname = "share" + str(ids[s]) + "_" + str(l) + ".txt"
        with open(dir + fname, 'rb') as f:
            new_share.append(f.read())
    shares.append(new_share)

#print(shares)

with open("../local/retrieved_key.pem", 'w') as file:
#with open("../local/private_key.pem", 'w') as file:
    for l in range(n):
        secretLine = PlaintextToHexSecretSharer.recover_secret(shares[l][0:sh])
        if l == 19:
            print(secretLine)
        diff = no_of_chars[l] - len(secretLine)
        if diff > 0:
            secretLine = diff*"0" + secretLine
        file.write(secretLine)

print("The key was successfully recovered")
