# encoding: utf-8
import random

class Mastermind:  
    def __init__(self,colors):
        self.colors = colors
        self.shuffleColors()
        
    def shuffleColors(self):
        random.shuffle(self.colors)
    
    def gradePlayerChoice(self):
         return None

    def colorsToPlay(self,numberOfColors):
        return self.colors[0:numberOfColors]
    
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    mm = Mastermind(colors)
    print mm.colorsToPlay(3)
    
if __name__== "__main__": main()