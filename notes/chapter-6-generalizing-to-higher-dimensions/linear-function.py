from plot import plot
from vector import Vector

class LinearFunction(Vector):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, v):
        return LinearFunction(self.a + v.a, self.b + v.b)

    def scale(self, scalar):
        return LinearFunction(scalar * self.a, scalar * self.b)

    def __call__(self, x):
        return self.a * x + self.b

    @classmethod
    def zero(cls):
        return LinearFunction(0, 0, 0)


plot([LinearFunction(-2, 2)], -5, 5).show()
