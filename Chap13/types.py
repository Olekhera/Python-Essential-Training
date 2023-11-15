#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '-47'
y = int(x)
h = abs(y)
f = divmod(h, 3)
g = h + 45j

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'h is {type(h)}')
print(f'h is {h}')
print(f'f is {type(f)}')
print(f'f is {f}')
print(f'g is {type(g)}')
print(f'g is {g}')