#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        x = int('Hello, World.')
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('don\'t divide by 0!')
    else:
        print(x)

if __name__ == '__main__': main()
