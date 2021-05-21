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
        self.possible_words = ['becode', 'mamba', 'learning', 'mathematics', 'sessions']
        self.word = str(random.sample(self.possible_words, 1)[0])
        self.word_to_find = [char for char in self.word]
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0
        self.wrongly_guessed_letters = []
        self.correctly_guessed_letters = []
        for i in range(len(self.word_to_find)):
            self.correctly_guessed_letters.append('_')

        # pass

    def play(self):
        print('\n')

        player_input = input('Please, enter a letter: ')
        proper_letter = re.match("[a-zA-Z]", player_input)
        while not player_input or len(player_input) > 1 \
          or proper_letter == None:
            player_input = input('Please, enter only one latin letter: ')
            proper_letter = re.match("[a-zA-Z]", player_input)
        print('your letter is', player_input)
        #print(self.word_to_find)
        #print(self.correctly_guessed_letters)
        if player_input in self.word_to_find:
            print('you guessed correctly')
        #check this
        #elif player_input in self.wrongly_guessed_letters:
        #    self.wrongly_guessed_letters.append(player_input)
        #   print('you have already guess this letter. Try another one')
        #end of check
        else: 
            print('your guess was wrong')
            self.wrongly_guessed_letters.append(player_input)
            self.lives -= 1
            if self.lives == 0:
                print(f'\nThis is so sad. Better luck next time\n\
Your word is {self.word.upper()}')
                return None
            print(f'You are left with {self.lives} lives')
        letter_position = []
        for index, letter in enumerate(self.word_to_find):
            if player_input == letter:
                letter_position.append(index)
        if letter_position:
            print(f'your letter is in positin {letter_position}')
        # next  2 lines should be collapsed in one with list comprehension
        for i in letter_position: 
          self.correctly_guessed_letters[i] = self.word_to_find[i]
        print('\n',self.correctly_guessed_letters)
        #self.word_to_find = correctly_guessed_letters
        #print(self.word_to_find)
        #return self.word_to_find

    def start_game(self):
        print('                                     \n\
                 ###################################\n\
                 ##   Lets play hangman!          ##\n\
                 ##   You have 5 lives, my dear   ##\n\
                 ###################################')
        while self.lives > 0:
            Hangman.play(self)
            if self.correctly_guessed_letters == self.word_to_find:
               print(f"\nAliliya! You are saved\n\
Your word is {self.word.upper()}")
               return None
