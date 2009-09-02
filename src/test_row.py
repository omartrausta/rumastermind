import unittest,row
 
class rowTest(unittest.TestCase):
    
    colorList = []
    
    def testRow(self):
        result = row.Row(self.colorList)
        print result.hintBlack
        print result.hintWhite 
        self.assertEqual(len(result.colorList),0)
        
if __name__ == '__main__': unittest.main()