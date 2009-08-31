# encoding: utf-8
import random

colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]

def shuffleColors():
    random.shuffle(colors)

def main():
    shuffleColors()
    print colors

if __name__== "__main__": main()