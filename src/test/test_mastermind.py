# encoding: utf-8
import unittest 
from main.mastermind import Mastermind
from main.color import Color
from main.row import Row

class MastermindTestCase(unittest.TestCase):    
    gulur = Color("gulur", "path")
    raudur = Color("rauður", "path")
    graenn = Color("graenn", "path")
    blar = Color("blaur","path")
    colors = [gulur,raudur,graenn,blar]
    numberOfColors=2
    numberOfGuesses=8
    sameColor=True
    guess1 = [gulur,graenn]
    guess2 = [graenn,blar]
    expected = [blar,graenn]
     
    def testColorsToPlay(self):
        result = Mastermind(self.colors,self.numberOfGuesses)
        result = result.colorsToPlay(self.numberOfColors)
        self.assertEqual(result, self.expected)

    def testGradePlayerChoice(self):
        result = Mastermind(self.colors,self.numberOfGuesses)
        result = result.gradePlayerChoice()
        self.assertEqual(result,None)
        
    def testRows(self):
        result = Mastermind(self.colors,self.numberOfGuesses)
        result.colorsToPlay(self.numberOfColors)
        row1 = Row(self.guess1)
        result.addToRows(row1)
        row2 = Row(self.guess2)
        result.addToRows(row2)
        result.populateRows()

if __name__ == '__main__': unittest.main()