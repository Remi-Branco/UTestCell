
import unittest

class TestStringMethods(unittest.TestCase):

    def test_reverso(self):
        self.assertEqual(reverso("Remi"), 'imeR')
    
    def test_square(self):
        self.assertEqual(square(4), 16)
        with  self.assertRaises(TypeError):
            square('') #need to be in a context manager for the test to fail and be accepted as such
    
            
if __name__ == '__main__':
    unittest.main()