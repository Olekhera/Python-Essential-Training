#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
y = 7.0
print('x is {}'.format(x))
print(f'y is {y}')
print(type(x))
print(type(y))


s = """

s

""".upper()

print(s)
print(type(s))


g = 'string is {1} {0}'.format(8,9)
print(g)

u = 8
k = 9
h = f'string is {u:<06} {k:>06}'
print(h)

q = 7 // 2 # parte intera
l = 7 % 2 # modulo