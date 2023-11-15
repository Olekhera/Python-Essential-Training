#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self): # self -> reference to the object
        print(self.sound)

    def move(self): # method
        print(self.movement)

def main():
    donald = Duck() # object -> an instance of a class
    donald.quack() # invoice to the object method
    print(donald.sound) # same but not recommended
    donald.move()

if __name__ == '__main__': main()
