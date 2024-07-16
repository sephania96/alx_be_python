import unittest
from simple_calculator import SimpleCalculator

class Testsimple_calculator(unittest.TestCase):

    def setUp(self):
        self.simple_calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.simple_calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.simple_calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.simple_calculator.multiply(10, 5), 50)
    
    def test_divide(self):
        self.assertEqual(self.simple_calculator.divide(10, 5), 2)

        with self.assertRaises(ValueError):
             self.simple_calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()