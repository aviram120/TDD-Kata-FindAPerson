import unittest


class testMatFunction(unittest.TestCase):
    def test_Area_Square(self):
        area = self.math.Area_Square(3,5)
        self.assertIn(20,area)

