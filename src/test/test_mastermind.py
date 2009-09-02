# encoding: utf-8
import unittest 
from main.mastermind import Mastermind
from main.color import Color
from main.row import Row

class MastermindTestCase(unittest.TestCase):    
    gulur = Color("gulur", "path")
    raudur = Color("rauður", "path")
    graenn = Color("grænn", "path")
    blar = Color("blár","path")
    svartur = Color("svartur", "path")
    hvitur = Color("hvítur", "path")
    fjolublar = Color("fjólublár", "path")
    colors = [gulur,raudur,graenn,blar,svartur,hvitur,fjolublar]
    numberOfColors=7
    numberOfGuesses=8
    sameColor=True
    guess1 = [gulur,graenn]
    guess2 = [graenn,blar]
    expected = [blar,graenn]
     
    def testColorsToPlay(self):
        result = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors,self.sameColor)
        for color in result.colors:
            print color.name

    def testGradePlayerChoice(self):
        result = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors)
        result = result.gradePlayerChoice(self.guess1)
        self.assertEqual(result,None)
        
    def testRows(self):
        result = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors)
        row1 = Row(self.guess1)
        result.addToRows(row1)
        row2 = Row(self.guess2)
        result.addToRows(row2)
        result.populateRows()

if __name__ == '__main__': unittest.main()