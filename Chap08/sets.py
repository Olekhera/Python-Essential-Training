#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.") # not ordered list
    b = set("I'm sorry, Dave. I'm afraid I can't do that.") #not duplicate values
    print_set(a)
    print_set(sorted(b))
    print_set(a - b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
