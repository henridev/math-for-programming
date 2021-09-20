from abc import ABCMeta, abstractmethod

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        '''
        vectors are equal when their coordinates are equal
        '''
        return self.x == other.x and self.y == other.y

    def __mul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __rmul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __add__(self, v):
        '''
        overrride + operator
        '''
        return self.add(v)

    def __repr__(self):
        '''
        overrid memory address returned as representation
        '''
        return "Vec2({},{})".format(self.x, self.y)


v1 = Vec2(1, 2)
v2 = Vec2(2, 1)
v3 = v1.add(v2)


print(v1 * 3 + v2 * 2)

class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def scale(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, num):
        return self.scale(num)

    def __rmul__(self, num):
        return self.scale(num)

    def __add__(self, v):
        return self.add(v)

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)


v1 = Vec3(1, 2, 4)
v2 = Vec3(2, 1, 3)
v3 = v1.add(v2)


print(v1 * 3 + v2 * 2)

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

class Vec():
    def __init__(self, *coords):
        self.coords = coords

    def add(self, v):
        return Vec(*map(sum, (zip(self.coords, v.coords))))

    def scale(self, s):
        return Vec(*[s * coor for coor in self.coords])

    def __eq__(self, other):
        for (coor_other, soor_self) in zip(other.coords), self.coords:
            if coor_other != soor_self:
                return False
        return True

    def __mul__(self, num):
        return self.scale(num)

    def __rmul__(self, num):
        return self.scale(num)

    def __add__(self, v):
        return self.add(v)

    def __repr__(self):
        return "Vec{}".format(self.coords)


v1 = Vec(1, 2, 4)
v2 = Vec(2, 1, 3)
v3 = v1.add(v2)

print(v3)
print(Vec(1, 3, 4))
print(v1 * 3 + v2 * 2)


class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def zero_vector(self):
        pass

    @abstractmethod
    def negation_vector(self):
        pass

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

class Vec2(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def subtract(self, v):
        return self.add(v * -1)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def zero_vector(self):
        return Vec2(0, 0)

    def negation_vector(self):
        return self.scale(-1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Vec2({},{})".format(self.x, self.y)

class Vec3(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def subtract(self, v):
        return self.add(v * -1)

    def scale(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def zero_vector(self):
        return Vec3(0, 0, 0)

    def negation_vector(self):
        return self.scale(-1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)
