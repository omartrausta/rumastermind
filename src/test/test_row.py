import unittest
from main.row import Row
 
class rowTest(unittest.TestCase):
    
    colorList = []
    
    def testRow(self):
        result = Row(self.colorList)
        print result.hintBlack
        print result.hintWhite 
        self.assertEqual(len(result.colorList),0)
        
if __name__ == '__main__': unittest.main()