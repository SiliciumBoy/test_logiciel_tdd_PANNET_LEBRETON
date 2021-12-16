import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(funcs.min_function(0, 2), 0)
        self.assertEqual(funcs.min_function(8, -5), -5)
        self.assertEqual(funcs.min_function(-1, 2), -1)
        self.assertEqual(funcs.min_function(-1, -10), -10)
        self.assertEqual(funcs.min_function(0, 0), 0)

    def test_mean_int(self):
        self.assertEqual(funcs.mean_function([0,1,2,3,4]), 2)
        self.assertEqual(funcs.mean_function([0,0,0,0,0]), 0)
        self.assertEqual(funcs.mean_function([2,2]), 2)
        self.assertEqual(funcs.mean_function([-10,10]), 0)
        self.assertEqual(funcs.mean_function([-4,10,25,-12]), 4)
        self.assertEqual(funcs.mean_function([-5,7,3,-3,2]), 0)

if __name__ == '__main__':
    unittest.main()