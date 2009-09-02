# encoding: utf-8
import unittest, os
import main.color

class colorTestCase(unittest.TestCase):    
     
    def testInitColor(self):
        yellow = main.color.Color("Gulur","blah.gif")
        c = main.color.Color("Gulur","blah.gif")
        self.assertEqual(yellow.name, c.name, 'Test féll')

if __name__ == '__main__': unittest.main()