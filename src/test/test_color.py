# encoding: utf-8
import unittest, os
from main.color import Color

class colorTestCase(unittest.TestCase):    
     
    def testInitColor(self):
        raudur = Color("raudur","test")
        yellow = Color("Gulur","blah.gif")
        c = Color("Gulur","blah.gif")
        self.assertEqual(yellow.name, c.name, 'Test féll')

if __name__ == '__main__': unittest.main()