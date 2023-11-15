#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 'one', [0, 1])
y = (1, 'one', [0, 1])

print(id(x))
print(id(y))

print(id(x[0]))
print(id(y[0]))