#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') # dictionary
    y = kitten(**x)
    print(type(y), y)


def kitten(**kwargs): # key word arguments
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')
    return kwargs

if __name__ == '__main__': main()
