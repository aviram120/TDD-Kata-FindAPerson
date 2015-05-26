
import math

class mathFu():
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def Area_Square(self):
        a=self.l*self.w
        return a
    def Scope_Square(self):
        s=(self.l*2)+(self.w*2)
        return s
    def square_sulution(self,a,b,c):
            d = b ** 2 - 4 * a * c
            if d >= 0:
                 disc = math.sqrt(d)
                 root1 = (-b + disc) / (2 * a)
                 root2 = (-b - disc) / (2 * a)
            else:
                return (-1),(-1)

            return root1,root2