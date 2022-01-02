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

    def test_mediane_int(self):
        self.assertEqual(funcs.mediane_function([1,2,3]),2)
        self.assertEqual(funcs.mediane_function([1,2,3,5,5,6]),4)
        self.assertEqual(funcs.mediane_function([-10,-7,3,6,12]),3)
        self.assertEqual(funcs.mediane_function([0,0,0,0,0,0,0,0,1]),0)

    def test_ecart_type(self):
        self.assertEqual(funcs.ecart_type_function([1,2,3]),0.816496580927726)
        self.assertEqual(funcs.ecart_type_function([1,2,3,5,5,6]),1.7950549357115015)
        self.assertEqual(funcs.ecart_type_function([-10,-7,3,6,12]),8.182909018191515)
        self.assertEqual(funcs.ecart_type_function([0,0,0,0,0,0,0,0,1]),0.31426968052735443)

    def test_suite_arith(self):
        self.assertEqual(funcs.suite_arith_function([1,2,3]), True)
        self.assertEqual(funcs.suite_arith_function([1,2,3,5,5,6]), False)
        self.assertEqual(funcs.suite_arith_function([-10,-7,3,6,12]), False)
        self.assertEqual(funcs.suite_arith_function([-10,3,-6,12]), False)
        self.assertEqual(funcs.suite_arith_function([10,-5,-10,5,0,-15,15]), True)
        self.assertEqual(funcs.suite_arith_function([-4,-1,2,5,8]), True)
        self.assertEqual(funcs.suite_arith_function([7]), False)
        self.assertEqual(funcs.suite_arith_function([8,8,8]), True)

    def test_suite_geo(self):
        self.assertEqual(funcs.suite_geo_function([1,2,3]), False)
        self.assertEqual(funcs.suite_geo_function([0,1,2,3]), False)
        self.assertEqual(funcs.suite_geo_function([8,4,16,2,32]), True)
        self.assertEqual(funcs.suite_geo_function([5,10,40,20]), True)
        self.assertEqual(funcs.suite_geo_function([-5,-10,-40,-20]), True)
        self.assertEqual(funcs.suite_geo_function([-5,5]), True)
        self.assertEqual(funcs.suite_geo_function([7]), False)

if __name__ == '__main__':
    unittest.main()