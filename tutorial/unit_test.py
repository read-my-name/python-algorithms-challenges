# test_my_module.py
import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):
    
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.1, -1.1), -2.2)
    
    def test_add_strings(self):
        self.assertEqual(add('hello', ' world'), 'hello world')

if __name__ == '__main__':
    unittest.main()
