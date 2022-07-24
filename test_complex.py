from Qblox_complex import Complex
import math
import unittest


class ComplexTest(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(Complex(2, 2) == Complex(2, 2))

    def test_inequality(self):
        self.assertFalse(Complex(1, 1) == Complex(2, 2))

    def test_negation(self):
        self.assertEqual(-Complex(4, 4), Complex(-4, -4))

    def test_add(self):
        z = Complex(2, 2)
        self.assertEqual(z + z, Complex(4, 4))

    def test_subtract(self):
        z = Complex(4, 4)
        self.assertEqual(z - Complex(2, 2), Complex(2, 2))

    def test_complex_mul(self):
        z1 = Complex(4, 4)
        z2 = Complex(2, 2)
        self.assertEqual(z1 * z2, Complex(0, 16))


    def test_left_mul(self):
        z = Complex(2, 2)
        self.assertEqual(z * 2, Complex(4, 4))

    def test_right_mul(self):
        z = Complex(2, 2)
        self.assertEqual(2 * z, Complex(4, 4))

    def test_complex_division(self):
        z1 = Complex(4, 4)
        z2 = Complex(2, 2)
        self.assertEqual(z1 / z2, Complex(2, 0))

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            z = Complex(2, 2) / 0

    def test_left_division(self):
        z = Complex(4, 4)
        self.assertEqual(z / 2, Complex(2, 2))

    def test_right_division(self):
        z = Complex(2, 2)
        self.assertEqual(2 / z, Complex(0.5, -0.5))

    def test_conjugate(self):
        z = Complex(2, 2)
        self.assertEqual(z.conj(), Complex(2, -2))

    def test_abs(self):
        z = Complex(2, 2)
        self.assertAlmostEqual(abs(z), 2 * math.sqrt(2), delta=10e-16)

    def test_arg(self):
        z = Complex(2, 2)
        self.assertAlmostEqual(z.arg(), math.pi / 4, delta=10e-16)

if __name__ == '__main__':
    unittest.main(verbosity=2)
