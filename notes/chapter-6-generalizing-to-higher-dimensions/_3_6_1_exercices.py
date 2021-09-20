from abc import ABCMeta, abstractmethod, abstractproperty
from hypothesis import given, note, strategies as st


'''
Exercise 6.1: Implement a Vec3 class inheriting from Vector.
'''

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

    @abstractproperty
    def zero_vector(self):
        pass

    def negation_vector(self):
        return self.scale(-1)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)


'''
Mini-project 6.2: Implement a CoordinateVector class inheriting from Vector
with an abstract property representing the dimension.
This should save repetitious work when implementing specific coordinate vector classes.
Inheriting from CoordinateVector and setting the dimension to 6
should be all you need to do to implement a Vec6 class.
'''

def add(*vectors):
    return tuple(map(sum, zip(*vectors)))

def scale(scalar, v):
    return tuple(scalar * coord for coord in v)

class CoordinateVector(Vector):
    @abstractproperty
    def dimension(self):
        pass

    def __init__(self, *coords):
        self.coords = tuple(x for x in coords)

    def add(self, v):
        return self.__class__(*add(self.coords, v.coords))

    def subtract(self, v):
        return self.__class__(*add(self.coords, v.coords * -1))

    def scale(self, s):
        return self.__class__(*scale(s, self.coords))

    def zero_vector(self):
        return Vec3(0, 0, 0)

    def negation_vector(self):
        return self.scale(-1)

    def __eq__(self, v):
        for (coor_other, soor_self) in zip(v.coords, self.coords):
            if coor_other != soor_self:
                return False
        return True

    def __repr__(self):
        return "{}{}".format(self.__class__.__qualname__, self.coords)

class Vec6(CoordinateVector):
    def dimension(self):
        return 6


print(Vec6(1, 2, 3, 4, 5, 6) + Vec6(1, 2, 3, 4, 5, 6))
# print(Vec6(1, 2, 3, 4, 5, 6) == Vec6(1, 2, 3, 4, 5, 6))


'''
Exercise 6.3: Add a zero abstract method to the Vector class to 
return the zero vector in a given vector space, as well as an 
implementation for the negation operator. 
These are useful because we’re required to have a zero vector and
negations of any vector in a vector space.
'''

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

    @abstractproperty
    def zero_vector(self):
        pass

    def negation_vector(self):
        return self.scale(-1)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __truediv__(self, scalar):
        return self.scale(1.0/scalar)

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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)


'''
Exercise 6.4: Write unit tests to show that the addition and scalar multiplication 
operations for Vec3 satisfy the vector space properties.
'''


@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def commutative_vectors(u_x, u_y, u_z, v_x, v_y, v_z):
    u = Vec3(u_x, u_y, u_z)
    v = Vec3(v_x, v_y, v_z)
    result = u + v == v + u
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def associative_vectors(u_x, u_y, u_z, v_x, v_y, v_z, w_x, w_y, w_z):
    u = Vec3(u_x, u_y, u_z)
    v = Vec3(v_x, v_y, v_z)
    w = Vec3(w_x, w_y, w_z)
    result = (u + v) + w == u + (v + w)
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def multiply_several_scalars_multiply_all_scalars(v_x, v_y, v_z, scalar_1, scalar_2):
    v = Vec3(v_x, v_y, v_z)
    result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers()
)
def multiply_one_unchanged(v_x, v_y, v_z):
    v = Vec3(v_x, v_y, v_z)
    result = v == v * 1
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_scalars_compatible_scalar_multiplication(v_x, v_y, v_z, scalar_1, scalar_2):
    v = Vec3(v_x, v_y, v_z)
    result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_vectors_compatible_scalar_multiplication(u_x, u_y, u_z, v_x, v_y, v_z, scalar):
    u = Vec3(u_x, u_y, u_z)
    v = Vec3(v_x, v_y, v_z)
    result = scalar * (u + v) == scalar * v + scalar * u
    note(f"Result: {result}")
    assert result == True


try:
    commutative_vectors()
    associative_vectors()
    multiply_several_scalars_multiply_all_scalars()
    multiply_one_unchanged()
    test_addition_scalars_compatible_scalar_multiplication()
except AssertionError:
    print("result != True")


'''
Exercise 6.5: Add unit tests to check that 
0 + v = v, 
0 · v = 0, 
and -v + v = 0 for any vector v, 
where again 0 is the number zero and 0 is the zero vector.
'''


@given(
    st.integers(), st.integers(), st.integers()
)
def test_zero_vector_addition(u_x, u_y, u_z,):
    u = Vec3(u_x, u_y, u_z)
    result = u + u.zero_vector()
    note(f"Result: {result}")
    assert result == u

@given(
    st.integers(), st.integers(), st.integers()
)
def test_zero_multiplication_vector(u_x, u_y, u_z):
    u = Vec3(u_x, u_y, u_z)
    result = u * u.zero_vector()
    note(f"Result: {result}")
    assert result == u

@given(
    st.integers(), st.integers(), st.integers()
)
def test_negation_addition_vector(u_x, u_y, u_z):
    u = Vec3(u_x, u_y, u_z)
    result = u + u.negation_vector()
    note(f"Result: {result}")
    assert result == u.zero_vector()


try:
    commutative_vectors()
    associative_vectors()
    multiply_several_scalars_multiply_all_scalars()
    multiply_one_unchanged()
    test_addition_scalars_compatible_scalar_multiplication()
except AssertionError:
    print("result != True")


'''
Exercise 6.6: As equality is implemented for Vec2 and Vec3,
it turns out that Vec2(1,2) == Vec3(1,2,3) returns True.
Python’s duck typing is too forgiving for its own good!
Fix this by adding a check that classes must match before
testing vector equality.

def __eq__(self, other):
    return (self.__class__ and other.__class__) and (self.x == other.x and self.y == other.y and self.z == other.z)

def add(self, other):
    assert self.__class__ and other.__class__
    return Vec2(self.x + other.x, self.y + other.y)
'''


'''
Exercise 6.7: Implement a __truediv__ function on Vector that allows you to divide vectors by scalars. You can
divide vectors by a non-zero scalar by multiplying them by the reciprocal of the scalar (1.0/scalar).

def __truediv__(self, scalar):
    return self.scale(1.0/scalar)
'''
