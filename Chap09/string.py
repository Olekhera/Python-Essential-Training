#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str): #built-in method
    def __str__(self): # overwriting
        return self[::-1] # step goes backwards

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()
