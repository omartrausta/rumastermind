# encoding: utf-8

""" 
    Mastermind row class holds attributes for guessed colors and hint. White
    is right color at wrong location, black is right color at right location
"""

class Row:
    def __init__(self, colorList, hintBlack=0, hintWhite=0):
        self.colorList = colorList
        self.hintBlack = hintBlack
        self.hintWhite = hintWhite