#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt') # file object
    b = open('lines.txt', 'r')  # r / w -> read only or write, if not exists then it creates a new file
    b = open('lines.txt', 'rt') # rt / rb -> text (default) or binary mode
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
