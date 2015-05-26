import unittest
from matFun import math

class testMatFunction(unittest.TestCase):
    def setUp(self):
        self.matFun=math(5,3)

    def test_Area_Square(self):
        area =self.matFun.Area_Square()
        self.assertEquals(20,area)


