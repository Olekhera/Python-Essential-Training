#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ] # list mutable
    game_tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock') # tuple immutable
    print(game[1:5:2])
    i = game.index('Rock')
    game.append('o')
    game.remove('Rock')
    print(', '.join(game))
    print_list(game)
    print_list(game_tuple)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
