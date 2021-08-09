import unittest
from unittest import result
import test2


class testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test2.addition(10, 15), 25)
        self.assertEqual(test2.addition(-10, 15), 5)
        self.assertEqual(test2.addition(-10, -15), -25)
        self.assertEqual(test2.addition(10, -15), -5)

    def test_sub(self):
        self.assertEqual(test2.substraction(10, 15), -5)
        self.assertEqual(test2.substraction(-10, 15), -25)
        self.assertEqual(test2.substraction(-10, -15), 5)
        self.assertEqual(test2.substraction(10, -15), 25)

    def test_mult(self):
        self.assertEqual(test2.multiply(10, 15), 150)
        self.assertEqual(test2.multiply(-10, 15), -150)
        self.assertEqual(test2.multiply(-10, -15), 150)
        self.assertEqual(test2.multiply(10, -15), -150)

    def test_div(self):
        self.assertEqual(test2.division(10, 15), 0.67)
        self.assertEqual(test2.division(-10, 15), -0.67)
        self.assertEqual(test2.division(-10, -15), 0.67)
        self.assertEqual(test2.division(10, -15), -0.67)

        #self.assertRaises(ValueError, test2.division, 20, 0)


if __name__ == "__main__":
    unittest.main()
