import unittest
from matFun import math

class testMatFunction(unittest.TestCase):
    def setUp(self):
        self.matFun=math(5,3)

    def test_Area_Square(self):
        area =self.matFun.Area_Square()
        self.assertEquals(15,area)

    def test_Scope_Square(self):
        sq=self.matFun.Scope_Square()
        self.assertEquals(16,sq)
    def test_square_sulution(self):
        x1,x2=self.matFun.square_sulution(1,6,9)
        self.assertEquals(-3,x1)
        self.assertEquals(-3,x2)