# encoding: utf-8
import random

class Mastermind:  
    def __init__(self,colors,numberOfGuesses,numbersOfColors,sameColor=False):
        self.colors = colors
        self.rows = range(numberOfGuesses)
        self.numbersOfColors = numbersOfColors
        self.sameColor = sameColor
        self.totalGuesses = 0
        # Shufling the colors
        self.shuffleColors()
        # Taking setting how many colors to play
        self.colorsToPlay()
    
    # TODO þarf að útfæra meiri shuffle lógík ef sami litur er True    
    def shuffleColors(self):
        random.shuffle(self.colors)
    
    # TODO leikja lógík til þess að setja hvítu og svörtu pinna í röð
    def gradePlayerChoice(self,guessColors):
         return None

    def colorsToPlay(self):
        self.colors = self.colors[0:self.numbersOfColors]
    
    def addToRows(self,row):
        self.rows.remove(self.totalGuesses)
        self.rows.insert(self.totalGuesses,row)
        self.totalGuesses =+ 1
    
    def populateRows(self):
        for row in self.rows:
            print row
    
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    mm = Mastermind(colors,8,4)
    for color in mm.colors:
        print color.encode("utf-8")
    
if __name__== "__main__": main()