#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper()) # a string is immutable
print('Hello, World.'.lower()) # create a new object
print('Hello, World.'.casefold())
print('Hello, World.'.title())
print('Hello, World.'.capitalize())
print('Hello, World.'.swapcase())

s = 'Hello, World. {} {}' # {} -> placeholder
y = 'second string'
z = 'BCG'
print(s.format(4 * 3, z))
print(s + ' ' + y) # concatenate
print('the number is {0:<5} {1:>05}'.format(75, 89))

h = 23
print('{:+07}'.format(h))