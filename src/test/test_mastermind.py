# encoding: utf-8
import unittest 
import main.mastermind

class MastermindTestCase(unittest.TestCase):    
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]
    number=3
    guess = ["gulur", "svartur"]
    expected = ['Gulur', 'Bl\xc3\xa1r', 'Svartur']
     
    def testColorsToPlay(self):
        result = main.mastermind.Mastermind(self.colors)
        result = result.colorsToPlay(self.number)
        self.assertEqual(result, self.expected)

    def testGradePlayerChoice(self):
        result = main.mastermind.Mastermind(self.colors)
        result = result.gradePlayerChoice()
        self.assertEqual(result,None)

if __name__ == '__main__': unittest.main()