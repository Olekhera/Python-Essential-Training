#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    def __init__(self, type, name, sound): # special class method -> constructor or initializer
        self._type = type
        self._name = name
        self._sound = sound

    def type(self): # getters
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o): # function
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar') # object -> an instance of a class
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
