import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

        with self.assertRaises(ValueError):
            calculator.fun1("2", 3)
        with self.assertRaises(ValueError):
            calculator.fun1(2, None)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

        with self.assertRaises(ValueError):
            calculator.fun2("2", 3)
        with self.assertRaises(ValueError):
            calculator.fun2(2, [])

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

        with self.assertRaises(ValueError):
            calculator.fun3("2", 3)
        with self.assertRaises(ValueError):
            calculator.fun3(2, {})

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

        with self.assertRaises(ValueError):
            calculator.fun4(1, 2, "3")
        with self.assertRaises(ValueError):
            calculator.fun4(1, None, 3)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(2, 3), 8)
        self.assertEqual(calculator.fun5(5, 0), 1)
        self.assertEqual(calculator.fun5(-2, 2), 4)

        with self.assertRaises(ValueError):
            calculator.fun5("2", 3)
        with self.assertRaises(ValueError):
            calculator.fun5(2, "3")

    def test_fun6(self):
        self.assertEqual(calculator.fun6(0), 1)
        self.assertEqual(calculator.fun6(1), 1)
        self.assertEqual(calculator.fun6(5), 120)

        with self.assertRaises(ValueError):
            calculator.fun6(-1)
        with self.assertRaises(ValueError):
            calculator.fun6(2.5)
        with self.assertRaises(ValueError):
            calculator.fun6("5")

    def test_fun7(self):
        self.assertEqual(calculator.fun7(10, 3), 10)
        self.assertEqual(calculator.fun7(-1, 1), 1)
        self.assertEqual(calculator.fun7(5, 5), 5)

        with self.assertRaises(ValueError):
            calculator.fun7("10", 3)
        with self.assertRaises(ValueError):
            calculator.fun7(10, None)

    def test_fun8(self):
        self.assertTrue(calculator.fun8(6))
        self.assertFalse(calculator.fun8(7))
        self.assertTrue(calculator.fun8(0))
        self.assertTrue(calculator.fun8(-2))

        with self.assertRaises(ValueError):
            calculator.fun8(2.0)
        with self.assertRaises(ValueError):
            calculator.fun8("6")

    def test_fun9(self):
        self.assertEqual(calculator.fun9(0), 0.0)
        self.assertEqual(calculator.fun9(9), 3.0)
        self.assertEqual(calculator.fun9(2.25), 1.5)

        with self.assertRaises(ValueError):
            calculator.fun9(-1)
        with self.assertRaises(ValueError):
            calculator.fun9("9")


if __name__ == '__main__':
    unittest.main()
