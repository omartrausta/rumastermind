import unittest
from main.row import Row
from main.color import Color
 
class rowTest(unittest.TestCase):
    
    colorList = []
    
    def testRow(self):
        result = Row(self.colorList)
        gulur = Color("gulur","path")
        result.colorList.append(gulur)
        print result.hintBlack
        print result.hintWhite 
        result.hintBlack =+ 1
        result.hintWhite =+ 1
        print result.hintBlack
        print result.hintWhite
        print result.colorList
        self.assertEqual(len(result.colorList),1, 'Test féll')
        
if __name__ == '__main__': unittest.main()