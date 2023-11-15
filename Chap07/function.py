#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    h = [10, 11] # lists are mutable objects
    print(h)
    kitten(4, 6, h)
    g = h
    g[1] = 1
    print(g)
    print(h)

def kitten(n, a, b, x = 0):
    b[0] = 18
    print(f'{n} Meow.')
    print(a, b, x)

if __name__ == '__main__': main()
