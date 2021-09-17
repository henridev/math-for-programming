import math

from OpenGL.error import Error
from vectors import *
from teapot import load_triangles
from draw_model import draw_model
from math import *
import random


def multiply_matrices(a, b):
    result = []
    for row in a:
        res_num = 0
        for i, num in enumerate(row):
            coor = b[i]
            res_num += (coor * num)
        result.append(res_num)
    return tuple(result)


a = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

v = (3, -2, 5)

print(multiply_matrices(a, v))
# ((1,-2,-2))

def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]  # [(3, (0,0,1)),(-2, (2,1,0)),(5, (1,0,-1))] => [3 * (0,0,1), -2 * (2,1,0), 5 * (1,0,-1)]
    return add(*scaled)

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))


def matrix_multiply(a, b):
    '''
    when multiplying matrices with each other it can be interpreted as
    taking taking dot product of first row and first col then of the first row and second col

    The outer comprehension builds the rows of the result, and the inner one builds the entries of
    each row. Because the output rows are formed by the various dot products with rows of a, the
    outer comprehension iterates over a.

        Our matrix_multiply function doesn’t have any hard-coded dimensions. That means we can
    use it to do the matrix multiplications from the preceding 2D and 3D examples:  
    '''
    return tuple(
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )


def get_rotation_matrix(t):  # 1 Generates a new transformation matrix for any numeric input representing time
    seconds = t/1000  # 2 Converts the time to seconds so the transformation doesn’t happen too fast
    return (
        (cos(seconds), 0, -sin(seconds)),
        (0, 1, 0),
        (-sin(seconds), 0, cos(seconds))
    )


# draw_model(load_triangles(), get_matrix=get_rotation_matrix)  # 3 pass rotation matrix as callback each frame new tick is passed

'''
Exercise 5.1: Write a function infer_matrix(n, transformation) that takes a dimension (like 2 or 3) and a
function that is a vector transformation assumed to be linear. It should return an n-by-n square matrix 
(an n-tuple of ntuples of numbers, which is the matrix representing the linear transformation). 
Of course, the output is only meaningful if the input transformation is linear. 
Otherwise, it represents an entirely different function!
'''

def rotate_z_axis(angle, vector, in_radians=True):
    x, y, z = vector
    rotate_x, rotate_y = rotate2d(angle if in_radians else radians(angle), (x, y))
    return rotate_x, rotate_y, z

def rotate_x_axis(angle, vector, in_radians=True):
    x, y, z = vector
    rotate_y, rotate_z = rotate2d(angle if in_radians else radians(angle), (y, z))
    return x, rotate_y, rotate_z

def rotate_y_axis(angle, vector, in_radians=True):
    x, y, z = vector
    rotate_z, rotate_x = rotate2d(angle if in_radians else radians(angle), (z, x))
    return rotate_x, y, rotate_z


def translate(v, translation=(-1, 0, 0)):
    return add(translation, v)


def translate_by(translation=(-1, 0, 0)):
    def translate_function(v):
        return translate(v, translation)
    return translate_function

def infer_matrix(n, transformation):
    original_hats = []
    for position_for_1 in range(n):
        basis_vector = [0 for position_for_1 in range(n)]
        basis_vector[position_for_1] = 1
        original_hats.append(tuple(basis_vector))
    transformed_hats = []
    for basis_vector in original_hats:
        transformed_hats.append(transformation(basis_vector))

    return tuple(zip(*transformed_hats))


print(infer_matrix(3, translate_by()))

def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i == j else 0 for j in range(1, n+1))  # 1
    standard_basis = [standard_basis_vector(i) for i in range(1, n+1)]  # 2
    cols = [transformation(v) for v in standard_basis]  # 3
    return tuple(zip(*cols))  # 4


print(infer_matrix(3, translate_by()))


'''
Mini-project 5.3: Write a random_matrix function that generates matrices of a specified size with random whole
number entries. Use the function to generate five pairs of 3-by-3 matrices. Multiply each of the pairs together by hand
(for practice) and then check your work with the matrix_multiply function.
'''

def random_matrix(row, col, max=2, min=-2):
    random_matrix = []
    for y in range(0, row):
        random_row = []
        for x in range(0, col):
            random_row.append(random.randint(min, max))
        random_matrix.append(tuple(random_row))
    return tuple(random_matrix)


print(random_matrix(3, 3, 5, -5))


def random_matrix(rows, cols, min=-2, max=2):
    return tuple(tuple(random.randint(min, max) for j in range(0, cols))for i in range(0, rows))


'''
Exercise 5.4: For each of your pairs of matrices from the previous exercise, 
multiply them in the opposite order. Do you get the same result?
'''

rand_matrix_a = random_matrix(3, 3, -5, 5)
rand_matrix_b = random_matrix(3, 3, -5, 5)
rand_matrix_c = random_matrix(3, 3, -5, 5)
rand_matrix_d = random_matrix(3, 3, -5, 5)


# print(matrix_multiply(rand_matrix_a, rand_matrix_b))
# print(matrix_multiply(rand_matrix_b, rand_matrix_a))
# print(matrix_multiply(rand_matrix_c, rand_matrix_d))
# print(matrix_multiply(rand_matrix_d, rand_matrix_c))


'''
Solution: Unless you get very lucky, your results will all be different. 
Most pairs of matrices give different results when multiplied in different orders.
In math jargon, we say an operation is commutative 
if it gives the same result regardless of the order of inputs. 
For instance, multiplying numbers is a commutative operation because 
xy = yx for any choice of numbers x and y.
However, matrix multiplication is not commutative because for 
two square matrices A and B, AB does not always equal BA.
'''


'''
Exercise 5.5: In either 2D or 3D, there is a boring but important 
vector transformation called the identity transformation that takes in a vector 
and returns the same vector as output. 
This transformation is linear because it takes any input
vector sum, scalar multiple, or linear combination and returns the same thing as output. What are the matrices
representing the identity transformation in 2D and 3D, respectively?
'''

identity_2d = (
    (1, 0),
    (0, 1)
)

identity_3d = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)

'''
Exercise 5.6: Apply the matrix ((2,1,1),(1,2,1),(1,1,2)) 
to all the vectors defining the teapot. What happens
to the teapot and why?
'''

def get_rotation_matrix(t):
    return (
        (2, 1, 1),
        (1, 2, 1),
        (1, 1, 2)
    )


# draw_model(load_triangles(), get_matrix=get_rotation_matrix)


'''
Exercise 5.7: Implement multiply_matrix_vector in a different way
by using two nested comprehensions: one traversing the rows of the matrix 
and one traversing the entries of each row.
'''

def multiply_matrix_vector(matrix, vector):
    '''
    in : 
    (
        (1,2),
        (3,4)
    )
    (5,6)

    intermediate: 

    [
        ((5,1), (6,2)), => dot product of this
        ((5,3), (6,4))
    ]

    out : 

    [
       (17, 39),
       (1, 2)
    ]
    '''
    return tuple(
        sum(vector_entry * matrix_entry for vector_entry, matrix_entry in zip(row, vector))
        for row in matrix
    )


matrix = (
    (1, 2),
    (3, 4)
)

vector = (5, 6)


'''
Exercise 5.8: Implement multiply_matrix_vector yet another way
using the fact that the output coordinates are
the dot products of the input matrix rows with the input vector.
'''

def multiply_matrix_vector(matrix, vector):
    return tuple(
        dot(row, vector)
        for row in matrix
    )


'''
Mini-project 5.9: 
I first told you what a linear transformation was
(transformations that preserve scalar multiplication and vector addition)
and then showed you that any linear transformation can be represented by a matrix.

Let’s prove the converse fact now: all matrices represent linear transformations.

Starting with the explicit formulas for multiplying a 2D vector by a 2-by-2 matrix 
or multiplying a 3D vector by a 3-by-3 matrix, prove that algebraically. 
That is, show that matrix multiplication preserves sums and scalar multiples.
'''

# https://res.cloudinary.com/dri8yyakb/image/upload/v1631526584/4F154E10-DBDA-4020-9B34-E1CD20F6FA9A_pvb6fz.png


'''
Exercise 5.10: Once again, let’s use the two matrices from section 5.1.3:
Write a function compose_a_b that executes the composition of the linear transformation 
for A and the linear transformation for B. 
Then use the infer_matrix function from a previous exercise in this section to show that
infer_matrix(3, compose_a_b) is the same as the matrix product AB.
'''

A = (
    (1, 1, 0),
    (1, 0, 1),
    (1, -1, 1)
)

B = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

def transform_a(v):
    return multiply_matrix_vector(A, v)
def transform_b(v):
    return multiply_matrix_vector(B, v)

def compose(*transformations):
    def composed_function(v):
        transformed_v = v
        for t in reversed(transformations):
            transformed_v = t(transformed_v)
        return transformed_v
    return composed_function


compose_a_b = compose(transform_a, transform_b)
# print(infer_matrix(3, compose_a_b))
# print(matrix_multiply(A, B))


'''
Mini-project 5.11: 
Find two, 2-by-2 matrices, neither of which is the identity matrix
I2, but whose product is the identity matrix.
'''


print(matrix_multiply((
    (0, 1),
    (1, 0)
), (
    (0, 1),
    (1, 0)
)))


def get_rotation_matrix(t):
    return matrix_multiply((
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0)
    ),
        (
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0)
    )
    )


# draw_model(load_triangles(), get_matrix=get_rotation_matrix)


'''
Exercise 5.12: 
We can multiply a square matrix by itself any number of times. 
We can then think of successive matrix multiplications as 
“raising a matrix to a power.” For a square matrix A, 
A * A can be written A2; A * A * A can be written A3; and so on. 
Write a matrix_power(power,matrix) function 
that raises a matrix to the specified (whole number) power.
'''

def matrix_power(power, matrix):
    new_matrix = matrix
    for _ in range(power):
        new_matrix = matrix_multiply(new_matrix, matrix)
    return new_matrix


print(
    matrix_multiply(
        (
            (1, 1, 0),
            (0, 1, 0),
            (0, 0, 1)
        ),
        ((0,), (0,), (1,)))  # specify , to show its a tuple
)


'''
Exercise 5.13: What are the dimensions of this matrix?
3x5 =>  3 rows and 5 columns
'''

'''
Exercise 5.14: What are the dimensions of a 2D column vector considered as a matrix? => 2x1
What about a 2D row vector? => 1x2 A 3D column vector? => 3x1 A 3D row vector? => 1x3
'''

'''
Mini-project 5.15: Many of our vector and matrix operations make use of the Python zip function. When given input
lists of different sizes, this function truncates the longer of the two rather than failing. This means that when we pass
invalid inputs, we get meaningless results back. For instance, there is no such thing as a dot product between a 2D
vector and a 3D vector, but our dot function returns something anyway:

Add safeguards to all of the vector arithmetic functions so that they throw exceptions rather than returning values for
vectors of invalid sizes. Once you’ve done that, show that matrix_multiply no longer accepts a product of a 3x2
and a 4x5 matrix.
'''

def check_matrix_multiplication_validity(a, b):
    a_rows = len(a)
    b_rows = len(b)
    subs_a = iter(a)
    len_a = len(next(subs_a))
    subs_b = iter(b)
    len_b = len(next(subs_b))
    valid_b_columns = all(len(sub) == len_a for sub in subs_a)
    valid_a_columns = all(len(sub) == len_b for sub in subs_b)
    print(valid_b_columns, valid_a_columns)
    if not valid_b_columns or not valid_a_columns:
        raise Error("incongruent column lengths")
    a_columns = len(a[0])
    b_columns = len(b[0])
    if a_columns != b_rows:
        raise Error(f'{a_rows} rows of a not compatible with {b_columns} columns of b')
    print(f'result will be a {a_rows} X {b_columns} matrix')


def matrix_multiply(a, b):
    check_matrix_multiplication_validity(a, b)
    return tuple(
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )


# matrix_multiply(
#     (
#         (1,),
#         (1,)
#     ),
#     (
#         (1,),
#         (1,),
#         (1,)
#     )
# )


'''
Exercise 5.16: Which of the following are valid matrix products? For those that are valid, what dimension is the product
matrix?

2x2 | 4x4 => not
2x4 | 4x2 => yes
3x1 | 1x8 => yes
3x3 | 2x3 => not
'''


'''
Exercise 5.17: A matrix with 15 total entries is multiplied by a matrix with 6 total entries. What are the dimensions of
the two matrices, and what is the dimension of the product matrix?

mXn = 15 
kXr = 6


n=k

mXn = 5x3
kXr = 3x2

or

mXn = 15x1
kXr = 1x6
'''


'''
Exercise 5.18: Write a function that turns a column vector into a row vector, or vice versa. Flipping a matrix on its side
like this is called transposition and the resulting matrix is called the transpose of the original.

(
    (-2,),
    (1,),
    (0,)
) => col vector

((-2,1,0),) => row vector
'''

def transpose(matrix):
    return tuple(zip(*matrix))


'''
Exercise 5.20: We want to multiply three matrices together: 
A is 5x7, B is 2x3, and C is 3x5. 
What order can they be multiplied in and what is the size of the result?

BCA
'''

'''
Exercise 5.21: Projection onto the y,z plane and onto the x,z plane are also linear maps from 3D to 2D. 
What are their matrices?

project onto x,z

   1 & 0 & 0 
   0 & 0 & 1

project onto y,z

   0 & 1 & 0 
   0 & 0 & 1 

'''


'''
Exercise 5.22: Show by example that the infer_matrix function from a previous exercise can create matrices for
linear functions whose inputs and outputs have different dimensions.
Solution: One function we could test would be projection onto the x,y plane, which takes in 3D vectors and returns 2D
vectors. We can implement this linear transformation as a Python function and then infer its 2x3 matrix:
'''

def project_xy(v):
    x, y, z = v
    return (x, y)


print(infer_matrix(3, project_xy))

'''
Exercise 5.23: Write a 4x5 matrix that acts on a 5D vector by deleting the third of its five entries, thereby producing a
4D vector. For instance, multiplying it with the column vector form of (1, 2, 3, 4, 5) should return (1, 2, 4, 5).

   1 & 0 & 0 & 0 & 0
   0 & 1 & 0 & 0 & 0
   0 & 0 & 0 & 1 & 0
   0 & 0 & 0 & 0 & 1
'''
