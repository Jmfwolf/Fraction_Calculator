import unittest

from fractions import Fraction

import calculator


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1, 0), 0, "Multiply 1 * 0 = 0")
        self.assertEqual(calculator.multiply(-5, 5), -25, "Multiply -5 * 5 = -25")

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2, "Divide 10 / 5 = 2")
        self.assertEqual(calculator.divide(-5, 5), -1, "Divide -5 / 5 = -1")

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15, "Add 10 + 5 = 15")
        self.assertEqual(calculator.add(-5, 5), 0, "Add -5 + 5 = 0")

    def test_subs(self):
        self.assertEqual(calculator.subs(10, 5), 5, "Subtract 10 - 5 = 5")
        self.assertEqual(calculator.subs(-5, 5), -10, "Subtract -5 - 5 = -10")

    def test_frac(self):
        self.assertEqual(calculator.frac('1/2'), Fraction(1, 2), "String to Fraction '1/2' to Fraction(1, 2)")
        self.assertEqual(calculator.frac('10/3'), Fraction(10, 3), "String to Fraction '10/3' to Fraction(10, 3)")

    def test_parsenum(self):
        self.assertEqual(calculator.parsenum('3_1/2'), Fraction(7, 2), "Mixed Number '3_1/2' to Fraction(7, 2)")
        self.assertEqual(calculator.parsenum('5_1/3'), Fraction(16, 3), "Mixed Number '5_1/3' to Fraction(16, 3)")

    def test_calculate(self):
        self.assertEqual(calculator.calculate('3_1/2', '+', '1/3'), Fraction(23, 6))
        self.assertEqual(calculator.calculate('5_1/3', '*', '2'), Fraction(32, 3))

    def test_error_handling(self):
        self.assertRaises(Exception, calculator.calculate('abhdi_1/2', '+', '1'), "Error Condition Letters Caught")
        self.assertRaises(Exception, calculator.calculate('2_3_1/2', '*', '2'), "Error Condition Improper Format Caught")
        self.assertRaises(Exception, calculator.calculate('1', 'T', '1'), "Error Condition Improper Operand Caught")


if __name__ == "__main__":
    main()
