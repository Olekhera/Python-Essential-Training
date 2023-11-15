#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys # import modules
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    a = sys.platform
    print(a)
    b = os.name
    print(b)
    c = os.getenv('PATH')
    print(c)
    y = random.randint(1, 5679)
    print(y)
    g = list(range(25))
    random.shuffle(g)
    print(g)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day)

if __name__ == '__main__': main()
