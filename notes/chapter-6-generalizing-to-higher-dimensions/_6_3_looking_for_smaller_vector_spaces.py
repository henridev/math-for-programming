from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractproperty
from PIL import Image
from vector import Vector
from math import *
from plot import plot, plot2
from datetime import timedelta, datetime
from hypothesis import given, note, strategies as st
from _6_2_5_manipulating_images import ImageVector
from car_for_sale import CarForSale
from math import isclose
from random import uniform, random, randint

# result = 0.5 * ImageVector("clinton.JPG") + 0.5 * ImageVector("cruise.JPG")
# result.image().show()

white = ImageVector([(255, 255, 255) for _ in range(0, 300*300)])
inverse = white - ImageVector("clinton.jpg")
# inverse.image().show()


'''
Exercise 6.8: Run the vector space unit tests with float values for u, v, and w, rather than with objects inheriting from
the Vector class. This demonstrates that real numbers are indeed vectors.
'''

@given(
    st.integers(), st.integers()
)
def commutative_vectors(u, v):
    result = u + v == v + u
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers()
)
def associative_vectors(u, v, w):
    result = (u + v) + w == u + (v + w)
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers()
)
def multiply_several_scalars_multiply_all_scalars(v, scalar_1, scalar_2):
    result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers()
)
def multiply_one_unchanged(v):
    result = v == v * 1
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers()
)
def test_addition_scalars_compatible_scalar_multiplication(v, scalar_1, scalar_2):
    result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers()
)
def test_addition_vectors_compatible_scalar_multiplication(u, v, scalar):
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
Mini-project 6.9: Run the vector space unit tests for CarForSale
to show its objects form a vector space (ignoring their textual attributes).
'''

def random_time():
    return CarForSale.retrieved_date - timedelta(days=uniform(0, 10))


def random_car():
    return CarForSale(randint(1990, 2019), randint(0, 250000), 27000. * random(), random_time())

def random_scalar():
    return uniform(-10, 10)


def commutative_vectors(u, v):
    result = u + v == v + u
    assert result == True

def associative_vectors(u, v, w):
    result = (u + v) + w == u + (v + w)
    assert result == True

def multiply_several_scalars_multiply_all_scalars(v, scalar_1, scalar_2):
    result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
    assert result == True

def multiply_one_unchanged(v):
    result = v == v * 1
    assert result == True

def test_addition_scalars_compatible_scalar_multiplication(v, scalar_1, scalar_2):
    result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
    assert result == True

def test_addition_vectors_compatible_scalar_multiplication(u, v, scalar):
    result = scalar * (u + v) == scalar * v + scalar * u
    assert result == True


for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_car(), random_car(), random_car()
    commutative_vectors(u, v)
    associative_vectors(u, v, w)
    multiply_several_scalars_multiply_all_scalars(v, a, b)
    multiply_one_unchanged(v)
    test_addition_scalars_compatible_scalar_multiplication(v, a, b)
    test_addition_vectors_compatible_scalar_multiplication(u, v, a)


'''
Exercise 6.10: Implement the class Function(Vector) that takes a function
of one variable as an argument to its constructor and implement
a __call__ method so you can treat it as a function. You should be able to run
'''


class Function(Vector):
    def __init__(
            self, f
    ):
        self.f = f

    def add(self, other):
        return Function(lambda x: self.f(x) + other.f(x))

    def scale(self, scalar):
        return Function(lambda x: self.f(x) * scalar)

    @classmethod
    def zero():
        return Function(lambda x: 0)

    def __call__(self, x):
        return self.f(x)


f = Function(lambda x: 0.5 * x + 3)
g = Function(sin)

# plot([f, g, f+g, 3*g], -10, 10).show()


'''
Mini-project 6.13: Implement a class Function2(Vector)
that stores a function of two variables like f(x, y) = x + y
'''

class Function2(Vector):
    def __init__(
            self, f
    ):
        self.f = f

    def add(self, other):
        return Function2(lambda x, y: self.f(x, y) + other.f(x, y))

    def scale(self, scalar):
        return Function2(lambda x, y: self.f(x, y) * scalar)

    @classmethod
    def zero(cls):
        return Function2(lambda x, y: 0)

    def __call__(self, *args):
        return self.f(*args)


f = Function2(lambda x, y: x+y)
g = Function2(lambda x, y: x-y+1)

result = (f+g)
# print(result(3, 10))
# plot2([f, g, result], -10, 10).show()

'''
Mini-project 6.15: Implement a Matrix class inheriting from Vector
with abstract properties representing the number of rows and number of columns.
You should not be able to instantiate a Matrix class, but you could make a
Matrix5_by_3 class by inheriting from Matrix and explicitly specifying
the number of rows and columns.
'''


class Matrix(Vector):
    def __init__(self, matrix):
        self.matrix = matrix

    @abstractproperty
    def rows(self):
        pass

    @abstractproperty
    def cols(self):
        pass

    def add(self, other):
        return self.__class__(tuple(
            tuple(a + b for a, b in zip(row1, row2))
            for (row1, row2) in zip(self.matrix, other.matrix)
        ))

    def scale(self, scalar):
        return self.__class__(
            tuple(
                tuple(scalar * x for x in row)
                for row in self.matrix
            )
        )

    def zero(self):
        return Matrix(
            tuple(
                tuple(0 for _ in range(0, self.columns()))
                for _ in range(0, self.rows())
            )
        )

    def __repr__(self):
        return "%s%r" % (self.__class__.__qualname__, self.matrix)

class Matrix3_by_2(Matrix):
    def rows(self):
        return 3

    def cols(self):
        return 2

class Matrix5_by_3(Matrix):
    def rows(self):
        return 5

    def cols(self):
        return 3


# print(2 * Matrix2_by_2(((1, 2), (3, 4))) + Matrix2_by_2(((1, 2), (3, 4))))


'''
Mini-project 6.18: Write a LinearMap3d_to_5d class inheriting from Vector that uses a 5x3 matrix as its data but
implements __call__ to act as a linear map from ℝ3 to ℝ5. Show that it agrees with Matrix5_by_3 in its
underlying computations and that it independently passes the defining properties of a vector space.
'''

def transpose(matrix):
    return tuple(zip(*matrix))


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


class LinearMap3d_to_5d(Vector):
    def __init__(self, matrix_class):
        assert (matrix_class.rows() == 5)
        assert (matrix_class.cols() == 3)
        self.matrix_class = matrix_class

    def add(self, other):
        return LinearMap3d_to_5d(self.matrix_class.add(other.matrix))

    def scale(self, scalar):
        return LinearMap3d_to_5d(self.matrix_class.scale(scalar))

    def zero(self):
        return LinearMap3d_to_5d(self.matrix_class.zero())

    def __call__(self, other):
        '''
        other has three row and needs to be multiplied with self 5 X 3 matrix

        (5 x 3) * (3 x ?)

        (
            (a, b, c)
            (d, e, f)
            (g, h, i)
            (j, k, l)
            (m, n, o)
        )

        (
            (p, q)
            (s, t)
            (v, w)
        )

        (
            ((a,b,c) * (p,s,v), (a,b,c) * (q,t,w))
            ((d,e,f) * (p,s,v), (d,e,f) * (q,t,w))
            ((g,h,i) * (p,s,v), (g,h,i) * (q,t,w))
            ((j,k,l) * (p,s,v), (j,k,l) * (q,t,w))
            ((m,n,o) * (p,s,v), (m,n,o) * (q,t,w))
        )

        '''
        assert (other.rows() == 3)
        transposed_other_matrix = transpose(other.matrix)

        return tuple(
            tuple(dot(row, col) for col in transposed_other_matrix)
            for row in self.matrix_class.matrix
        )

    def __repr__(self):
        return "%s%r" % (self.__class__.__qualname__, self.matrix)


# print(LinearMap3d_to_5d(Matrix5_by_3((
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     (10, 11, 12),
#     (13, 14, 15),
# )))(Matrix3_by_2((
#     (1, 2),
#     (3, 4),
#     (5, 6),
# ))))

'''
Mini-project 6.19: Write a Python function enabling you to multiply Matrix5_by_3 objects 
by Vec3 objects in the sense of matrix multiplication. 
Update your overloading of the * operator for the vector and matrix classes so you can
multiply vectors on their left by either scalars or matrices.
'''

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

    def __rmul__(self, matrix_5_by_3):
        transposed_other_matrix = transpose((
            (self.x,),
            (self.y,),
            (self.z,)
        ))

        return tuple(
            tuple(dot(row, col) for col in transposed_other_matrix)
            for row in matrix_5_by_3.matrix
        )

class Matrix5_by_3(Matrix):
    def rows(self):
        return 5

    def cols(self):
        return 3

    #  this will get called first

    def __mul__(self, vector_3d):
        transposed_other_matrix = transpose((
            (vector_3d.x,),
            (vector_3d.y,),
            (vector_3d.z,)
        ))

        return tuple(
            tuple(dot(row, col) for col in transposed_other_matrix)
            for row in self.matrix
        )


def multiply_5_by_3_with_vec3(matrix_5_by_3, vector_3d):
    return matrix_5_by_3 * vector_3d


print(multiply_5_by_3_with_vec3(Matrix5_by_3((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
)),
    Vec3(1, 2, 3)
))


'''
Exercise 6.20: Convince yourself that the zero vector for the ImageVector class doesn’t 
visibly alter any image when it is added.
'''

image = ImageVector('cruise.jpg')
image_zero_added = image.add(image.zero())
# image_zero_added.image().show()

'''
Exercise 6.21: Pick two images and display 10 different weighted averages of them.
These will be points on a line segment connecting the images in 270,000-dimensional space!
'''

repetitions = 10
image_1 = ImageVector('cartman-smart.jpg')
image_2 = ImageVector('cartman.jpg')
new_size = (image_1.size[0]*repetitions, image_1.size[1])

appended_image = Image.new("RGB", new_size)
fractions = [enumerator/repetitions for enumerator in range(repetitions)]
weighted_images = [image_1.scale(fraction).add(image_2.scale(1-fraction)) for fraction in fractions]

x_offset = 0
for im in weighted_images:
    appended_image.paste(im.image(), (x_offset, 0))
    x_offset += im.size[0]

# appended_image.save('test.jpg')


'''
Exercise 6.22: Adapt the vector space unit tests to images and run them. 
What do your randomized unit tests look like as images?

we will just get some noise screen
'''

# @st.composite
# def random_image(_):
#     fixed_length_list = st.lists(st.integers(), min_size=270000, max_size=270000)
#     return ImageVector(fixed_length_list)


# @given(
#     random_image(), random_image()
# )
# def commutative_vectors(u, v):
#     result = u + v == v + u
#     note(f"Result: {result}")
#     assert result == True

# @given(
#     random_image(), random_image(), random_image()
# )
# def associative_vectors(u, v, w):
#     result = (u + v) + w == u + (v + w)
#     note(f"Result: {result}")
#     assert result == True

# @given(
#     random_image(), st.integers(), st.integers()
# )
# def multiply_several_scalars_multiply_all_scalars(v, scalar_1, scalar_2):
#     result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
#     note(f"Result: {result}")
#     assert result == True

# @given(
#     random_image()
# )
# def multiply_one_unchanged(v):
#     result = v == v * 1
#     note(f"Result: {result}")
#     assert result == True

# @given(
#     random_image(), st.integers(), st.integers()
# )
# def test_addition_scalars_compatible_scalar_multiplication(v, scalar_1, scalar_2):
#     result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
#     note(f"Result: {result}")
#     assert result == True

# @given(
#     random_image(), random_image(), st.integers()
# )
# def test_addition_vectors_compatible_scalar_multiplication(u, v, scalar):
#     result = scalar * (u + v) == scalar * v + scalar * u
#     note(f"Result: {result}")
#     result.image().show()
#     assert result == True


# try:
#     commutative_vectors()
#     associative_vectors()
#     multiply_several_scalars_multiply_all_scalars()
#     multiply_one_unchanged()
#     test_addition_scalars_compatible_scalar_multiplication()
# except AssertionError:
#     print("result != True")


def random_image():
    img = []
    for _ in range(0, 300*300):
        img.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    print(img)
    return ImageVector(img)


# random_image().image().show()
