#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1(f):
    def f2():
        print('this is function f2')
        f()
    return f2

def f3():
    print('this is f3')

x = f1(f3)
x()


