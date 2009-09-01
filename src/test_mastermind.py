# encoding: utf-8
import unittest, mastermind, os

class mastermindTestCase(unittest.TestCase):    
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]
    number=3
    guess = ["gulur", "svartur", ]
     
    def testColorsToPlay(self):
        result = mastermind.colorsToPlay(self.number)
        print result
        #self.assertEqual(result, self.expected, 'Test féll')

    def testGradePlayerChoice(self):
        result = mastermind.gradePlayerChoice()
        self.assertNotEqual
if __name__ == '__main__': unittest.main()