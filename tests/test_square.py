import unittest
from square import square

class TestSquare(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(square(5), 25)

    def test_negative_number(self):
        self.assertEqual(square(-3), 9)

    def test_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()

