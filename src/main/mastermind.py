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
        #self.shuffleColors()
        # Taking setting how many colors to play
        self.colorsToPlay()
    
#    # TODO þarf að útfæra meiri shuffle lógík ef sami litur er True    
#    def shuffleColors(self):
#        random.shuffle(self.colors)
    
    # TODO leikja lógík til þess að setja hvítu og svörtu pinna í röð
    # True, False = Unnið eða False,True = Tapað
    def gradePlayerChoice(self,guessColors):
        black = 0
        white = 0
        common = 0
        secretColorsUnused = copy.copy(self.colors)
        
        print "finna svarta"
        for color in guessColors:
            i = guessColors.index(color)
            secretColor = self.colors[i]
            print color.name
            print secretColor.name
            if color.name == secretColor.name:
                black = black+1
                print black
        print "finna hvíta"
        for color in guessColors:
            for secretColor in secretColorsUnused:
                print color.name
                print secretColor.name
                if secretColor.name == color.name:
                    common = common+1
                    secretColorsUnused.remove(secretColor)
                    print "common", common
        white = common - black
        
        
        
        row1 = Row(guessColors, black, white)
        self.addToRows(row1)  
        # ef jafnt tapar player
        if (self.totalGuesses == self.numberOfGuesses) and not (self.colors == guessColors):
            return False,True
        # ef eins player vinnur
        if self.numbersOfColors == black:
            return True,False
   
       
        # fara í gegnum guessColors og bera saman við self.colors
        
        return False,False #Eitthvað rangt
    

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
        for color in self.colors:
            print color.name
    
    def addToRows(self,row):
        self.rows.remove(self.totalGuesses)
        if self.totalGuesses == len(self.rows):
            self.rows.append(row)
        else:
            self.rows.insert(self.totalGuesses,row)
        self.totalGuesses += 1
    
    # Ef number of guess og total guess eru jöfn og current lita röð ekki rétt 
    
    def guessesLeft(self):
        return self.numberOfGuesses - self.totalGuesses 
    
    def populateRows(self):
        for row in self.rows:
            print row

# TODO vantar að útfæra client kóða fyrir skipanalínuútgáfu    
def main():
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár","Brúnn"]
    mm = Mastermind(colors,1,4,True)
#    for color in mm.colors:
#        print color.encode("utf-8")       
    print mm.populateRows()
    
if __name__== "__main__": main()