
import unittest

class TestStringMethods(unittest.TestCase):

    def test_reverso(self):
        self.assertEqual(reverso("Remi"), 'imeR')
    
    def test_square(self):
        self.assertEqual(square(4), 16)
        with  self.assertRaises(TypeError):
            square('') #must be in a context manager for the test to fail and be accepted as such

    def test_n_letters_is_5(self):
        self.assertEqual(n_letters_is_5('Remi'),False)
        self.assertEqual(n_letters_is_5('Maz'), False)
        self.assertEqual(n_letters_is_5('abcde'), True)
            
if __name__ == '__main__':
    unittest.main()
