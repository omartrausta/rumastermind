# encoding: utf-8
import random

colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]

def shuffleColors():
    random.shuffle(colors)
    
def gradePlayerChoice():
    return

def colorsToPlay(numberOfColors):
    return colors[numberOfColors:]

def main():
    shuffleColors()
    print colorsToPlay(3)


if __name__== "__main__": main()