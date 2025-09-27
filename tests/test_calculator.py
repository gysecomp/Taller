import unittest
from src.calculator import suma, resta

class TestCalculator(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 6)

    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
