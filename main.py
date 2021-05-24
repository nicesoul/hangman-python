#! python3
# -*- coding: utf-8 -*-
""" This is a main module for hangman game.
We define a logic of starting, breaking
and ending of the game here. or not??? :)
"""
# enjoy ))))

# below is the initial way of how I started the game
# if I run the file, it worked with only 1 line here - import...

# import utils.game as game
# game.Hangman().start_game() #this line originally was in game.py

# but is the below version better somehow?
# maybe yes, because we can import, alter methods and
# then decide how we want to run it

import utils.game as hangman

game = hangman.Hangman()
game.start_game()