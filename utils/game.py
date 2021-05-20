#! python3
# -*- coding: utf-8 -*-
""" This is a game module for hangman game.
We define a logic of word guessing here
"""

# import ... # do we need to import anything for this?
import random
import re


class Hangman():
    """ Here it goes
    """
    # how to properly initiate it =>
    # don't forget play(safe)* instead of just play() :)))
    # *which you should write play(self)
    # let's try without - NO NO NO NO NO! ))))  :*(((
    
    def __init__(self) -> None:
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = str(random.sample(self.possible_words, 1)[0])
        self.word_to_find = [char for char in self.word]
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0

        # pass

    def play(self):
        player_input = input('Please, enter a letter: ')
        proper_letter = re.match("[a-zA-Z]", player_input)
        while not player_input or len(player_input) > 1 \
          or proper_letter == None:
            player_input = input('Please, enter only one latin letter: ')
            proper_letter = re.match("[a-zA-Z]", player_input)
        print('your letter is', player_input)
        print(self.word_to_find)
        correctly_guessed_letters = []
        for i in range(len(self.word_to_find)):
            correctly_guessed_letters.append('_')
        # print(correctly_guessed_letters)
        letter_position = []
        for index, letter in enumerate(self.word_to_find):
            if player_input == letter:
                letter_position.append(index)
        print(letter_position)
        # next  2 lines should be collapsed in one with list comprehension
        for i in letter_position: 
          correctly_guessed_letters[i] = self.word_to_find[i]
        print(correctly_guessed_letters)
        word = correctly_guessed_letters
        return word

            

        
        


Hangman()
Hangman().play()
