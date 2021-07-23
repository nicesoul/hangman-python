# 34567891123456789212345678931234567894123456789512345678961234567897123456789
import os
import random
import re
from typing import List

import sys
os.system('')

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

HELP = """
Hangman-python by Lyes
Modded by Vadym
Visit BeCode.org to find your dream :)

USAGE:
    main_ready [-small | -large] [-color]

OPTIONS:
    --help      display this help
    -small      choose a list of  6 words to guess
    -large      choose a list of 12 words to guess
    -color      display guessed letters in color
       """
"""
command_line_arguments   = [arg for arg in sys.argv[1:]]

if '-small' in command_line_arguments:
    words = ['becode', 'mamba', 'learning', 'mathematics', 'sessions']
elif '-large' in command_line_arguments:
    words = ['clouds', 'orange', 'sheep', 'Python', 'program', 'sky', 'ground', "child", "bird", "ocean", "answer", "xylophone"]
elif '--help' in command_line_arguments:
    raise SystemExit(HELP)
elif len(command_line_arguments) == 0:
    pass
else:
    raise SystemExit(HELP)
"""

class Hangman:
    """ Class defining my game 'Hangman', characterized by :
    - a list of possible words
    - the word to find
    - a number of lives
    - the list of correctly guessed letters
    - the list of wrongly guessed letters
    - turn_count : the number of times the player played
    - error_count: the number of errors made by the player player
    """

    def __init__(self):
        """
        :param possible_words_default List: list of default words than can be guessed
        :param possible_words List: complete list of words than can be guessed
        :param word_to_find: List: list of the letters making the word to find. This word is randomly chosen among the possible words
        :param correctly_guessed_letters List: a list showing the number of letters of the secret word
                                        and which completes itself with the correct letters
        :param wrongly_guessed_letters List: list of the letters proposed by the player but not part of the secret word
        :param lives int: number of lives in the game or number of errors allowed
        :param turn_count int: number of turns in a game (each letter proposed, correct or not, counts for a turn)
        :param error_count int: number of errors made by the player during a game

        """

        self.possible_words_default = ['becode', 'learning', 'mathematics', 'sessions']
        self.possible_words = ['test', 'rescue', 'interfere', 'light', 'woozy',
                               'fetch', 'wrong', 'bruise'] + self.possible_words_default
        self.word_to_find = list(random.choice(self.possible_words))

        #######################
        command_line_arguments   = [arg for arg in sys.argv[1:]]

        if '-small' in command_line_arguments:
            words = ['becode', 'mamba', 'learning', 'mathematics', 'sessions']
        elif '-large' in command_line_arguments:
            words = ['clouds', 'orange', 'sheep', 'Python', 'program', 'sky', 'ground', "child", "bird", "ocean",         "answer", "xylophone"]
        elif '--help' in command_line_arguments:
            raise SystemExit(HELP)
        elif len(command_line_arguments) == 0:
            words = self.possible_words
        else:
            raise SystemExit(HELP)

        self.word_to_find = list(random.choice(words))
        #########################

        Hangman.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        Hangman.lives = 5
        Hangman.turn_count = 0
        Hangman.error_count = 0
        Hangman.wrongly_guessed_letters = []

    def game_over(self):
        """Method used to notify the player that the game is over because the number of lives is 0.
        """
        print("Game over. Sorry. You can try a new one if you want.")

    def well_played(self):
        """Method used to notify the player that the game is won and how
        """
        print(f"Well done! You found the word: {self.word_to_find} in \
                {Hangman.turn_count} turns with {Hangman.error_count} errors!")

    def play(self):
        """ Method for playing the game: the player proposes a letter that might
        be in the secret word or not
        If the player inputs something else, he must do it again
        :param letter: a letter from A to Z proposed by the player with the use of "input"
        """

        pattern = "^[a-zA-Z]$"
        Hangman.retry = False
        Hangman.exit = False

        # while Hangman.lives>0:
        self.letter = input("Please choose a letter from A to Z that you believe\n\
                            is in the word to guess... ")
        if (re.match(pattern, self.letter)):
            Hangman.turn_count += 1
            if self.letter.lower() in self.word_to_find:
                pos = []
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == self.letter.lower():
                        pos.append(i)
                for j in pos:
                    Hangman.correctly_guessed_letters[j] = self.letter.lower()
                if '_' not in Hangman.correctly_guessed_letters:
                    Hangman.well_played(self)
                    Hangman.exit = True
            else:
                Hangman.error_count += 1
                Hangman.lives -= 1
                Hangman.wrongly_guessed_letters.append(self.letter)
        else:
            print("Not good, please, choose a letter")
            Hangman.retry = True
            pass

        if Hangman.lives == 0:
            Hangman.game_over(self)

    def start_game(self):
        while Hangman.lives > 0:
            print("##################" + os.linesep)
            Hangman.play(self)
            if Hangman.retry:
                pass
            elif Hangman.exit:
                break
            else:
                print(f"your letter is {self.letter}")
                print(f"The correctly guessed letters are {Hangman.correctly_guessed_letters}")
                print(f"The wrongly guessed letters are {Hangman.wrongly_guessed_letters}")
                print(f"You have {Hangman.lives} attempt(s) remaining")
                print(f"You made {Hangman.error_count} errors until now")
                print(f"You tried {Hangman.turn_count} guesses until now")