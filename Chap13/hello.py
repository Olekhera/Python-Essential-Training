#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'Hello, World.'
print(repr(s)) # best string representation of a value

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

y = bunny(45)
print(y)
print(ascii(y))



q = (0, 1, 2, 3, 4, 5)
print(len(q))
f = list(reversed(q))
print(f)
for i in f: print(i)
print(sum(q)) # max / min
print(any(q)) # true if at least one <> 0
print(all(q)) # true if all <> 0

u = ('cat', 'dog', 'pet', 'rabbit')
for i, v in enumerate(u): print(f'{i}: {v}')


o = 43.0
p = isinstance(o, int)  # check if an object is of certain type or class
                        # false because float