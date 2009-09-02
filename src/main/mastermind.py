# encoding: utf-8
import random

class Mastermind:  
    def __init__(self,colors):
        self.colors = colors

    def shuffleColors():
        random.shuffle(colors)
    
    def gradePlayerChoice():
        return

    def colorsToPlay(numberOfColors):
        return colors[numberOfColors:]

    def main():
        shuffleColors()
        print colorsToPlay(3)
    
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    mm = Mastermind(colors)
    print mm.colors
    
if __name__== "__main__": main()