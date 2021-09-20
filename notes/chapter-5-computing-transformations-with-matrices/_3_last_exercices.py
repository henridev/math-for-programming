from exercices_helpers import *
from vectors import *


'''
Exercise 5.26: Show that the 3D ‘magic’ 
matrix transformation does not work if you move a 2D figure such as the
dinosaur we have been using to the plane z = 2. What happens instead?
'''

dino_vectors = [
    (6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
    (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
    (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
]
dino_vectors_3d = [(x, y, 1) for x, y in dino_vectors]

def translate_2d(translation, z=1):
    '''
    takes a translation vector
    returns a new function that applies that translation to a 2D vector
    '''
    def new_function(target):
        a, b = translation
        x, y = target
        matrix = ((1, 0, a),
                  (0, 1, b),
                  (0, 0, 1))  # 2 Builds the 4x4 matrix for the translation, and on the next line, turns (x,y,z) into a 4D vector with a fourth coordinate 1
        vector = (x, y, z)
        # 3 Does the 4D matrix transformation
        x_out, y_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out)
    return new_function

def polygon_segments_3d(points, color='blue'):
    count = len(points)
    return [Segment3D(points[i], points[(i+1) % count], color=color) for i in
            range(0, count)]


translation_z_one = translate_2d((1, 1))
translation_z_two = translate_2d((1, 1), z=4)

translated_z_one = [translation_z_one(v) for v in dino_vectors]
translated_z_two = [translation_z_two(v) for v in dino_vectors]

# draw(
#     Points(*translated_z_one, color='C3'),
#     Polygon(*translated_z_one, color='C3'),
#     Points(*translated_z_two, color='C4'),
#     Polygon(*translated_z_two, color='C4'),
# )


'''
Exercise 5.27: Come up with a matrix to translate the dinosaur 
by -2 units in the x direction and -2 units in the y direction. 
Execute the transformation and show the result.
'''

translation = translate_2d((-2, -2))
translated = [translation(v) for v in dino_vectors]

# draw(
#     Points(*dino_vectors, color='C2'),
#     Polygon(*dino_vectors, color='C2'),
#     Points(*translated, color='C3'),
#     Polygon(*translated, color='C3'),
# )


'''
Mini-project 5.29: Find a 3x3 matrix that rotates a 2D figure in the plane z = 1 by 45°, 
decreases its size by a factor of 2, and translates it by the vector (2, 2). 
Demonstrate that it works by applying it to the vertices of the dinosaur.
'''

def curry2(f):
    def g(x):
        def new_function(y):
            return f(x, y)
        return new_function
    return g

def infer_matrix(n, transformation):
    def standard_basis_vector(i):
        return tuple(1 if i == j else 0 for j in range(1, n+1))  # 1
    standard_basis = [standard_basis_vector(i) for i in range(1, n+1)]  # 2
    cols = [transformation(v) for v in standard_basis]  # 3
    return tuple(zip(*cols))  # 4


rotate_45_degrees = curry2(rotate2d)(pi/4)
rotation_matrix = infer_matrix(2, rotate_45_degrees)

matrix_scaled = (
    (0.5, 0),
    (0, 0.5)
)


rotate_scale_matrix = matrix_multiply(matrix_scaled, rotation_matrix)
((a, b), (c, d)) = rotate_scale_matrix

matrix = (
    (a, b, 2),
    (c, d, 2),
    (0, 0, 1)
)

def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
    return add(*scaled)

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))


translated = [
    (x, y)
    for (x, y, _) in [
        multiply_matrix_vector(matrix, (x, y, 1))
        for (x, y) in dino_vectors
    ]
]

draw(
    Points(*dino_vectors, color='C2'),
    Polygon(*dino_vectors, color='C2'),
    Points(*translated, color='C3'),
    Polygon(*translated, color='C3'),
)

'''
Exercise 5.31: Write a function analogous to translate_3d called translate_4d that uses a 5x5 matrix to
translate a 4D vector by another 4D vector. Run an example to show that the coordinates are translated.
'''

def translate_4d(translation):
    '''
    takes a translation vector
    returns a new function that applies that translation to a 3D vector
    '''
    def new_function(target):
        a, b, c, d = translation
        x, y, z, q = target
        matrix = ((1, 0, 0, 0, a),
                  (0, 1, 0, 0, b),
                  (0, 0, 1, 0, c),
                  (0, 0, 0, 1, d),
                  (0, 0, 0, 0, 1))  # 2 Builds the 4x4 matrix for the translation, and on the next line, turns (x,y,z) into a 4D vector with a fourth coordinate 1
        vector = (x, y, z, q, 1)
        # 3 Does the 4D matrix transformation
        x_out, y_out, z_out, q_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out, q_out)
    return new_function
