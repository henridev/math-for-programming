from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractproperty

class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractclassmethod
    @abstractproperty
    def zero_vector(self):
        pass

    def negation_vector(self):
        return self.scale(-1)

    def subtract(self, other):
        return self.add(other.scale(-1))

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)


class Vec1(Vector):
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return Vec1(self.x + other.x)

    def scale(self, scalar):
        return Vec1(scalar * self.x)

    def zero_vector(cls):
        return Vec1(0)

    def __eq__(self, other):
        return self.x == other.x

    def __repr__(self):
        return "Vec1({})".format(self.x)


print(Vec1(2) + Vec1(2))
