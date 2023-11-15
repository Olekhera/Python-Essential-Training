#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = '''
This   is a   long         string 
with a bunch     of 
words in it.
'''
print(s.split()) # create a list of words

l = s.split()
s2 = ' : '.join(l) # separator between words
print(s2)