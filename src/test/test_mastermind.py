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
    gameSecretColors = [blar,svartur,gulur,fjolublar]
    numberOfColors=7
    numberOfGuesses=8
    sameColor=True
    guess1 = [gulur,graenn]
    guess2 = [graenn,blar]
    expected = [blar,graenn]
     
    def testColorsToPlay(self):
        mastermind = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors,self.sameColor)
        self.assertEqual(len(mastermind.colors),7, 'Test féll')

    def testGradePlayerChoice(self):
        mastermind = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors)
        result = mastermind.gradePlayerChoice(self.guess1)
        tuple = False,False
        self.assertEqual(result,tuple, 'Test féll')    
        
    def testRows(self):
        mastermind = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors)
        row1 = Row(self.guess1)
        mastermind.addToRows(row1)
        row2 = Row(self.guess2)
        mastermind.addToRows(row2)
        self.assertEqual(len(mastermind.rows),8, 'Test féll')
        
    def testGuessesLeft(self):
        mastermind = Mastermind(self.colors,self.numberOfGuesses,self.numberOfColors)
        mastermind.gradePlayerChoice(self.guess1)
        result = mastermind.guessesLeft()
        self.assertEqual(result,7,  'Test féll')
        
if __name__ == '__main__': unittest.main()