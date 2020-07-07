import unittest
import Viikko2.testaus.calculator.calculator as laskin

#  Testing plus

class TestCalculator(unittest.TestCase):

    def test_int_numbers_plus(self):
        result = laskin.plus(2, 3)
        self.assertEqual(result, 5)

    def test_negative_int_numbers_plus(self):
        result = laskin.plus(-2, -3)
        self.assertEqual(result, -5)

    def test_if_returns_floats_plus(self):
        result = laskin.plus(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_if_returns_integer_and_float_plus(self):
        result = laskin.plus(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_error_if_not_numbers_plus(self):
        with self.assertRaises(TypeError):
            laskin.plus(1, "a")

#  Testing minus

    def test_int_numbers_minus(self):
        result = laskin.minus(2, 3)
        self.assertEqual(result, -1)

    def test_negative_int_numbers_minus(self):
        result = laskin.minus(-2, -3)
        self.assertEqual(result, 1)

    def test_if_returns_floats_minus(self):
        result = laskin.minus(3.2, 2.4)
        self.assertAlmostEqual(result, 0.8)

    def test_if_returns_integer_and_float_minus(self):
        result = laskin.minus(3.2, 2)
        self.assertAlmostEqual(result, 1.2)

    def test_error_if_not_numbers_minus(self):
        with self.assertRaises(TypeError):
            laskin.minus(1, "a")

#  Testing multiplication

    def test_int_numbers_multi(self):
        result = laskin.multiplication(2, 3)
        self.assertEqual(result, 6)

    def test_negative_int_numbers_multi(self):
        result = laskin.multiplication(-2, -3)
        self.assertEqual(result, 6)

    def test_if_returns_floats_multi(self):
        result = laskin.multiplication(3.2, 2.4)
        self.assertAlmostEqual(result, 7.68)

    def test_if_returns_integer_and_float_multi(self):
        result = laskin.multiplication(3.2, 2)
        self.assertAlmostEqual(result, 6.4)

    def test_error_if_not_numbers_multi(self):
        with self.assertRaises(ValueError):
            laskin.multiplication(1, "a")

#  Testing division

    def test_int_numbers_divi(self):
        result = laskin.division(4, 2)
        self.assertEqual(result, 2)

    def test_negative_int_numbers_divi(self):
        result = laskin.division(-4, -2)
        self.assertEqual(result, 2)

    def test_if_returns_floats_divi(self):
        result = laskin.division(3.5, 2.5)
        self.assertAlmostEqual(result, 1.4)

    def test_if_returns_integer_and_float_divi(self):
        result = laskin.division(3.2, 2)
        self.assertAlmostEqual(result, 1.6)

    def test_error_if_not_numbers_divi(self):
        with self.assertRaises(TypeError):
            laskin.division(1, "a")

if __name__ == '__main__':
        unittest.main()
