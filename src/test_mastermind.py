# encoding: utf-8
import unittest, mastermind, os

class mastermindTestCase(unittest.TestCase):    
    colors = ["Gulur","Rauður","Grænn","Blár","Svartur","Hvítur","Fjólublár"]
    number=3
     
    def testColorsToPlay(self):
        result = mastermind.colorsToPlay(self.number)
        print result
        #self.assertEqual(result, self.expected, 'Test féll')
        
if __name__ == '__main__': unittest.main()