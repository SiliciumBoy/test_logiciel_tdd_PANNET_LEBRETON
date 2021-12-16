import min_function
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(min_function.min_function(0, 2), 0)
        self.assertEqual(min_function.min_function(8, -5), -5)
        self.assertEqual(min_function.min_function(-1, 2), -1)
        self.assertEqual(min_function.min_function(-1, -10), -10)
        self.assertEqual(min_function.min_function(0, 0), 0)

if __name__ == '__main__':
    unittest.main()