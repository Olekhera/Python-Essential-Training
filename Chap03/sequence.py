#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
x[1] = 567
for i in x:
    print('i is {}'.format(i))

y = ( 1, 2, 3, 4, 5 ) # immutable
z = range(5,10)
k = range(5,50, 5)

g = list(range(8))
g[3] = 45

j = {'one': 1, 'two': 2} #dictionary
for k, v in j.items():
    print(f'{k}: {v}')