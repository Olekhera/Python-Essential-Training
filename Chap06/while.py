#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
c = 0
max_attempt = 5
auth = 0

while pw != secret:
    c += 1
    if c > max_attempt: break
    if c == 3: continue
    pw = input(f"{c}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else 'Calling the FBI ...')
