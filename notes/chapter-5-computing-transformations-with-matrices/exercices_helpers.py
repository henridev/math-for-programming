from matplotlib import colors
from draw3d import *
from vector_drawing import *
from OpenGL.error import Error
from vectors import dot

def check_matrix_multiplication_validity(a, b, isPrint=False):
    a_rows = len(a)
    b_rows = len(b)
    subs_a = iter(a)
    len_a = len(next(subs_a))
    subs_b = iter(b)
    len_b = len(next(subs_b))
    valid_b_columns = all(len(sub) == len_a for sub in subs_a)
    valid_a_columns = all(len(sub) == len_b for sub in subs_b)
    if not valid_b_columns or not valid_a_columns:
        raise Error("incongruent column lengths")
    a_columns = len(a[0])
    b_columns = len(b[0])
    if a_columns != b_rows:
        raise Error(f'{a_columns} columns of a not compatible with {b_rows} rows of b')
    if isPrint:
        print(f'result will be a {a_rows} X {b_columns} matrix')


def matrix_multiply(a, b, isPrint=False):
    check_matrix_multiplication_validity(a, b, isPrint)
    return tuple(
        tuple(dot(row, col) for col in zip(*b))
        for row in a
    )

def transpose(matrix):
    return tuple(zip(*matrix))

def transpose(matrix):
    return tuple(zip(*matrix))


def multiply_matrix_vector(matrix, vector):
    return tuple(
        dot(row, vector)
        for row in matrix
    )


def translate_3d(translation):
    '''
    takes a translation vector
    returns a new function that applies that translation to a 3D vector
    '''
    def new_function(target):
        a, b, c = translation
        x, y, z = target
        matrix = ((1, 0, 0, a),
                  (0, 1, 0, b),
                  (0, 0, 1, c),
                  (0, 0, 0, 1))  # 2 Builds the 4x4 matrix for the translation, and on the next line, turns (x,y,z) into a 4D vector with a fourth coordinate 1
        vector = (x, y, z, 1)
        # 3 Does the 4D matrix transformation
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out)
    return new_function
