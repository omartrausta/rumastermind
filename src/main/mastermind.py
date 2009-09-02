# encoding: utf-8
import random

class Mastermind:  
    def __init__(self,colors,guessColors,sameColor=False):
        self.colors = colors
        self.shuffleColors()
        self.rows = range(guessColors)
        self.sameColor = sameColor
        self.totalGuesses = 0
        
    def shuffleColors(self):
        random.shuffle(self.colors)
    
    def gradePlayerChoice(self):
         return None

    def colorsToPlay(self,numberOfColors):
        return self.colors[0:numberOfColors]
    
    def addToRows(self,row):
        self.rows.remove(self.totalGuesses)
        self.rows.insert(self.totalGuesses,row)
        self.totalGuesses =+ 1
    
    def populateRows(self):
        for row in self.rows:
            print row
    
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    mm = Mastermind(colors)
    print mm.colorsToPlay(3)
    
if __name__== "__main__": main()