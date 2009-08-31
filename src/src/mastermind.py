# encoding: utf-8
import random

colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]
playColors = []


def shuffleColors():
    random.shuffle(colors)
    
def gradePlayerChoice():
    return

def colorsToPlay(numberOfColors):
    playColors = colors[numberOfColors:]

def main():
    shuffleColors()
    print colors
    colorsToPlay(3)
    print playColors

if __name__== "__main__": main()