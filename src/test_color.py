# encoding: utf-8
import unittest, py.main.color, os

class colorTestCase(unittest.TestCase):    
     
    def testInitColor(self):
        yellow = Color("Gulur","blah.gif")
        c = Color("Gulur","blah.gif")
        self.assertEqual(yellow, c, 'Test féll')

if __name__ == '__main__': unittest.main()