# encoding: utf-8
import random
import copy
from main.row import Row

""" 
    Mastermind game class, this class provides the most methods which are
    required for the gameplay. It has colors list for the random generated
    guess colors. It has rows which provides list of guessed colors and hints.
    Number of color is just for how many colors are used in the game. Same color
    is for allowing the same color twice or often. Total guesses holds the tries
"""

class Mastermind:  
    def __init__(self,colors,numberOfGuesses,numbersOfColors,sameColor=False):
        self.colors = colors
        self.rows = range(numberOfGuesses)
        self.numbersOfColors = numbersOfColors
        self.sameColor = sameColor
        self.totalGuesses = 0
        self.numberOfGuesses = numberOfGuesses
        # Shufling the colors
        self.colorsToPlay()
    
    # leikja lógík til þess að setja hvítu og svörtu pinna í röð
    # True, False = Unnið eða False,True = Tapað
    def gradePlayerChoice(self,guessColors):
        black = 0
        white = 0
        common = 0
        secretColorsUnused = copy.copy(self.colors)
        
        #print "finna svarta"
        for color in guessColors:
            i = guessColors.index(color)
            secretColor = self.colors[i]
            #print color.name
            #print secretColor.name
            if color.name == secretColor.name:
                black = black+1
                #print black
        #print "finna hvíta"
        for color in guessColors:
            for secretColor in secretColorsUnused:
                #print color.name
                #print secretColor.name
                if secretColor.name == color.name:
                    common = common+1
                    secretColorsUnused.remove(secretColor)
                    #print "common", common
        white = common - black
            
        row1 = Row(guessColors, black, white)
        self.addToRows(row1)  
        # ef jafnt tapar player
        if (self.totalGuesses == self.numberOfGuesses) and not (self.colors == guessColors):
            return False,True
        # ef eins player vinnur
        if self.numbersOfColors == black:
            return True,False
        # leikur heldur áfram    
        return False,False
      
    def colorsToPlay(self):
        random.shuffle(self.colors)
        if (self.sameColor):
            tmp = self.colors
            self.colors = []
            idx = 0
            while (idx != self.numbersOfColors):
                self.colors.insert(idx, tmp.__getitem__(random.randint(0, self.numbersOfColors-1)))
                idx+=1
        else:
            self.colors = self.colors[0:self.numbersOfColors]

# ATH. Secret Code sést ef þetta er uncommentað   
#        for color in self.colors:
#            print color.name
    
    def addToRows(self,row):
        self.rows.remove(self.totalGuesses)
        if self.totalGuesses == len(self.rows):
            self.rows.append(row)
        else:
            self.rows.insert(self.totalGuesses,row)
        self.totalGuesses += 1
        
    def guessesLeft(self):
        return self.numberOfGuesses - self.totalGuesses 
       
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    master = Mastermind(colors,1,4,True)
    for color in master.colors:
        print color.encode("utf-8")       
    
if __name__== "__main__": main()