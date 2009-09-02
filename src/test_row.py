import unittest,row
 
class rowTest(unittest.TestCase):
    
    colorList = []
    
    def testRow(self):
        result = row.Row(self.colorList)
        self.assertEqual(len(result.colorList),0)

if __name__ == '__main__': unittest.main()