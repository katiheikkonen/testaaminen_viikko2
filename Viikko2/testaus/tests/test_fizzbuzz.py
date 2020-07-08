import unittest
import Viikko2.testaus.fizzbuzz.fizzbuzz as muuntaja


class TestFizzBuzz(unittest.TestCase):
    def test_division_five_and_three(self):
        exp = 'FizzBuzz'
        result = muuntaja.fizzbuzz(15)
        self.assertEqual(result, exp)

    def test_division_five(self):
        exp = 'Fizz'
        result = muuntaja.fizzbuzz(5)
        self.assertEqual(result, exp)

    def test_division_three(self):
        exp = 'Buzz'
        result = muuntaja.fizzbuzz(3)
        self.assertEqual(result, exp)

    def test_for_negative(self):
        with self.assertRaises(ValueError):
            muuntaja.fizzbuzz(-4)

    def test_for_letter(self):
        with self.assertRaises(TypeError):
            muuntaja.fizzbuzz('b')

    def test_for_float(self):
        with self.assertRaises(ValueError):
            muuntaja.fizzbuzz(1.5)

if __name__ == '__main__':
    unittest.main()
