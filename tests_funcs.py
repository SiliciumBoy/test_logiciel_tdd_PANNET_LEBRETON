import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(funcs.min_function(0, 2), 0)
        self.assertEqual(funcs.min_function(8, -5), -5)
        self.assertEqual(funcs.min_function(-1, 2), -1)
        self.assertEqual(funcs.min_function(-1, -10), -10)
        self.assertEqual(funcs.min_function(0, 0), 0)

    def test_mediane_int(self):
        self.assertEqual(funcs.mediane_function([1,2,3]),2)
        self.assertEqual(funcs.mediane_function([1,2,3,5,5,6]),4)
        self.assertEqual(funcs.mediane_function([-10,-7,3,6,12]),3)
        self.assertEqual(funcs.mediane_function([0,0,0,0,0,0,0,0,1]),0)

    def test_ecart_type_f32(self):
        self.assertEqual(funcs.ecart_type_function([1,2,3]),0.8164966)
        self.assertEqual(funcs.ecart_type_function([1,2,3,5,5,6]),1.7078252)
        self.assertEqual(funcs.ecart_type_function([-10,-7,3,6,12]),8.182909)
        self.assertEqual(funcs.ecart_type_function([0,0,0,0,0,0,0,0,1]),0.3142697)

if __name__ == '__main__':
    unittest.main()