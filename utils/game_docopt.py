#! python3
# -*- coding: utf-8 -*-
""" This is a game module for hangman game.
We define a logic of word guessing here.
"""
import random # generate random number or objects
import re     # Regural expression
import os     # Miscellaneous operating system interfaces
os.system('') # Execute the command(a string) in a subshell


class Terminal_colors(): # ANSI escape sequences
    reset_style = '\033[0m'
    colors = []
    for i in range(30, 38):
        colors.append('\033['+str(i)+'m')
    def color_check(self):
        for i in self.colors:
            print(i + 'color')

[black,red,green,yellow,blue,violet,cyan,grey] = Terminal_colors().colors
# usage of colors should always be returned to grey afterwards
# example below
# print(f'{yellow}I am Yellow{grey}')
        
class Hangman():
    """ Here it goes
    """

    def __init__(self) -> None:
        self.possible_words = ['becode', 'mamba', 'learning', 'mathematics', 'sessions']
        # random.sample() creates a list but I need an uppercase string
        self.word = str(random.sample(self.possible_words, 1)[0].upper())
        # I am just starting to use and understand list comprehension
        self.word_to_find = [char for char in self.word] 
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0 # we will not count errors, c'mon
        self.wrongly_guessed_letters = []
        self.correctly_guessed_letters = ['_' for i in self.word_to_find]
        self.print_guessed_letters = ' '

    def play(self):
        # print('\n') # we definitely need some clearing or we don't?
        # somehow it gives me 2 blank lines so I added \n to turn_count print below
        print(f'\nRound {self.turn_count}')
        player_input = input('Please, enter a letter: ').upper()
        print(f'Your input is {yellow}{player_input}{grey}') # let them see
        # check for proper input
        proper_letter = re.match("[a-zA-Z]", player_input)
        while not player_input or len(player_input) > 1 \
          or proper_letter == None:
            player_input = input('Please, enter only one latin letter: ').upper()
            print(f'Your input is {yellow}{player_input}{grey}')
            proper_letter = re.match("[a-zA-Z]", player_input)
        # check if we tried to guess this letter before   
        if player_input in self.correctly_guessed_letters\
          or player_input in self.wrongly_guessed_letters:
                print('You have already guessed this letter. Try another one')
                self.turn_count -= 1 # are you cheating, baby? :)
                return player_input 
        # we keep both right and wrong guessed letters but display them all together
        if player_input not in self.print_guessed_letters: 
            self.print_guessed_letters += player_input + ' '
        # check if the player was smart or lucky to find a letter
        if player_input in self.word_to_find:
            print('You guessed correctly')
        else: 
            print('Your guess was wrong')
            self.wrongly_guessed_letters.append(player_input)
            self.lives -= 1
            if self.lives == 1:
                print(f"{yellow}Be careful, you've got only 1 life left{grey}")
            else: print(f'You are left with {self.lives} lives')
            if self.lives == 0:
                self.game_over()
                return
        # here we continue if the guess was right or wrong?
        # it is done not inside if check to have less indentation
        # should I change it for a better flow? 
        letter_position = []
        for index, letter in enumerate(self.word_to_find):
            if player_input == letter:
                letter_position.append(index)
        if letter_position:
            print(f'Your letter is in position {letter_position}')
        # next 2 of 4 lines should be collapsed in one with list comprehension
        # let's try - !@#$*&^$ )))
        for i in letter_position: 
          self.correctly_guessed_letters[i] = self.word_to_find[i]
        word_to_print = ''
        for i in self.correctly_guessed_letters:
            word_to_print = word_to_print + i + ' ' 

        print('\n',word_to_print)
        print(f'\nChecked letter are: {cyan}{self.print_guessed_letters}{grey}')

    def start_game(self): # how much is too much?
        print('                                 \n\
            ####################################\n\
            ##       Lets play hangman!       ##\n\
            ##    You have 5 lives, my dear   ##\n\
            ####################################')
        while self.lives > 0:
            self.turn_count += 1
            Hangman.play(self)
            if self.correctly_guessed_letters == self.word_to_find:
                print(f"{yellow}\nHallelujah! {grey}You are saved.\n\
Your word is {green}{self.word}{grey}")
                return
    def game_over(self):
        print(f'\nThis is so {red}SAD{grey}')
        print(f'Better luck next time')
        print(f'Your word is {green}{self.word}{grey}')
