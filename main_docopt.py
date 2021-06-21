#! python3
# -*- coding: utf-8 -*-
""" This is a main module for hangman game.
Does nothing but calls the game. Enjoy!
Usage:
    main.py [-l | -s] [(-o <path>)]
Options:
    -h, --help  Show this help
    -l, -large  Use large pool of words to guess
    -s, -small  Use small pool of words to guess 
    -o <path>   Open external file as a pool of words: not implemented yet

    Pikabou!
"""
# enjoy ))))

import utils.game_docopt as hangman
from utils.docopt import docopt

doc = '''
Usage:
    my_program tcp <host> <port> [--timeout=<seconds>]
    my_program serial <port> [--baud=<n>] [--timeout=<seconds>]
    my_program (-h | --help | --version)
Options:
    -h, --help  Show this screen and exit.
    --version   Show version.
    --baud=<n>  Baudrate [default: 9600]
'''
#argv = ['tcp', '127.0.0.1', '80', '--timeout', '30']
#docopt(doc, argv)
docopt(__doc__,version='0.2')

game = hangman.Hangman()
game.start_game()