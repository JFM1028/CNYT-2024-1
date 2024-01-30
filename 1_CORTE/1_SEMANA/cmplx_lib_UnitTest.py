import math
import unittest

import complex_lib as cplxlib


class TestComplexNumbers(unittest.TestCase):
    def test_complex_add(self):
        self.assertAlmostEqual(cplxlib.complex_add([1, 2], [3, 4]), (4, 6))

    def test_complex_subs(self):
        self.assertAlmostEqual(cplxlib.complex_subs([1, 2], [3, 4]), (-2, -2))

    def test_complex_mult(self):
        self.assertAlmostEqual(cplxlib.complex_mult([1, 2], [3, 4]), (-5, 10))

    def test_complex_div(self):
        self.assertAlmostEqual(cplxlib.complex_div([1, 2], [3, 4]), (0.44, 0.08))

    def test_complex_modul(self):
        self.assertAlmostEqual(cplxlib.complex_modul([3, 4]), 5)

    def test_complex_conj(self):
        self.assertAlmostEqual(cplxlib.complex_conj([1, 2]), (1, -2))

    def test_complex_fase(self):
        self.assertAlmostEqual(cplxlib.complex_fase([1, 1]), math.pi/4)

    def test_complex_cartesianoPolar(self):
        self.assertAlmostEqual(cplxlib.complex_cartesianoPolar([3, 4]), (5, 0.9272952180016122))

    def test_complex_polarCartesiano(self):
        self.assertAlmostEqual(cplxlib.complex_polarCartesiano([5, math.pi/4]), (3.5355339059327378, 3.5355339059327378))

if __name__ == '__main__':
    unittest.main(exit=False)
