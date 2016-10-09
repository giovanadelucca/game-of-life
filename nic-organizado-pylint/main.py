#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Módulo Main:
'''
#from collections import OrderedDict
#import pygame, random
#from pygame.locals import *
from Game import Board
from PatternsParser import FromImgToCSV
from Patterns import Patterns
#from PatternsParser import Patterns

if __name__ == '__main__':
    SPEED = 1
    SQUARES = 1
    MAP_SIZE = 8
    START_VALUE = False
    
    NEW_BOARD = Board(SQUARES, MAP_SIZE, START_VALUE)
    NEW_BOARD.set_board(SPEED)
    PATTERNS = ['BARGE', 'BOAT', 'BEACON', 'BEEHIVE', 'BLINKER', 'BLOCK', 'BOAT', 'GLIDER', 'HALF_BAKERY', 'HALF_FLEET', 'LOAF', 'LONG_BARGE', 'LONG_BOAT', 'MANGO', 'POND', 'SHIP', 'TOAD', 'TUB']
    #NEW_PATTERNS = Patterns(START_VALUE)
    #NEW_PATTERNS.patterns_array_to_txt()
    print(NEW_BOARD.parser.mat_video)
    NEW_PARSER = FromImgToCSV(START_VALUE, PATTERNS, NEW_BOARD.parser.mat_video)
    NEW_PARSER.find_patterns()
