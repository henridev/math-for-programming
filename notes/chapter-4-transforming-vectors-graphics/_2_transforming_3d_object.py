from math import radians
from vectors import *
from teapot import *
from draw_model import draw_model
from intialize_rotating_figure import initialize_rotating_figure


def scale_vector(v, scale_factor=1.0):
    return scale(scale_factor, v)


def translate1left(v, translation=(-1, 0, 0)):
    return add(translation, v)


original_triangles = load_triangles()

modified_triangles = [
    [scale_vector(vector, scale_factor=0.5)for vector in triangles]
    for triangles in original_triangles
]


# initialize_rotating_figure(modified_triangles)


def scaled_translation(v, scale_factor=1.0, translation=(-1, 0, 0)):
    translate1left(scale_vector(v, scale_factor), translation)

def compose(*transformations):
    def composed_function(v):
        transformed_v = v
        for t in transformations:
            transformed_v = t(transformed_v)
        return transformed_v
    return composed_function


scaled_translation_composition = compose(*[translate1left, scale_vector])

# modified_triangles = [
#     [scale_vector(vector, scale_factor=0.5)for vector in triangles]
#     for triangles in original_triangles
# ]

modified_triangleas = [
    [scaled_translation_composition(vector)for vector in triangles]
    for triangles in original_triangles
]

# initialize_rotating_figure(modified_triangles)

def polygon_map(transformation, polygons):
    '''
    takes a vector transformation and a list of polygons (usually triangles)
    and applies the transformation to each vertex of each polygon,
    yielding a new list of new polygons:
    '''
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]


'''
Applying ransformations sequentially defines a new transformation.
package this new transformation as its own Python function:

important principle! vector transformations = vectors inputs and return vectors outputs,
combine them as we want by function composition. If you haven’t heard this term before,
it means defining new functions by applying two or more existing ones in a specified order.

“welding” of functions can be done in code as well.
We can write a general purpose compose function that takes two Python functions (for vector transformations, for instance)
and returns a new function, which is their composition:

Python treats functions as “first-class objects.”
- functions can be assigned to variables
- passed as inputs to other functions
- created on-the-fly and returned as output values.

These are functional programming techniques, meaning that they help us build complex programs by combining existing functions to make new ones.

namely vector transformations, are our central objects of study. With the compose function covered,
I’ll show you a few more functional “recipes” that justify this digression.

Each of these is added in a new helper file called transforms.py in the source code for this book.
Something we’ll be doing repeatedly is taking a vector transformation and applying it to every
vertex in every triangle defining a 3D model. We can write a reusable function for this rather
than writing a new list comprehension each time.
'''

def translate(v, translation=(-1, 0, 0)):
    return add(translation, v)

def translate_by(v, translation=(-1, 0, 0)):
    def new_function(v):
        return add(v, translation)
    return new_function


# curried functions

def scale_by(scalar=0.3):
    def scaled_function(v):
        return scale_vector(v, scale_factor=scalar)
    return scaled_function

def translate_by(translation=(-1, 0, 0)):
    def translate_function(v):
        return translate(v, translation)
    return translate_function


# scaled_translation_composition = compose(*[translate_by(translation=(0, 0, 0)), scale_by(scalar=0.8)])

# modified_triangels = polygon_map(scaled_translation_composition, load_triangles())

# initialize_rotating_figure(modified_triangles)


'''
rotations in 2D in chapter 2: convert the Cartesian => polar => + or - angle by rotation factor => convert back.
- it is helpful in 3D because all 3D vector rotations are, in a sense, isolated in planes.
- for instance, a single point in 3D being rotated about the zaxis. Its x- and y-coordinates change, but its z-coordinate remains the same.
- If a given point is rotated around the z-axis, it stays in a circle with a constant z-coordinate, regardless of the rotation angle.
- we can rotate a 3D point around the z-axis by holding the z-coordinate constant and applying
  our 2D rotation function only to the x- and y-coordinates.




Continuing to think in the functional programming paradigm, we can curry this function. Given
any angle, the curried version produces a vector transformation that does the corresponding
rotation:


def rotate_z_by(angle):
def new_function(v):
return rotate_z(angle,v)
return new_function
Let’s see it in action. The following line yields the teapot in figure 4.11, which is rotated by 𝜋𝜋/4
or 45°:
draw_model(polygon_map(rotate_z_by(pi/4.), load_triangles()))

'''

def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+angle))

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


def rotate_axis_by(angle=pi/4, axis='z', in_radians=True):
    def rotation_x(v):
        return rotate_x_axis(angle, v, in_radians)

    def rotation_y(v):
        return rotate_y_axis(angle, v, in_radians)

    def rotation_z(v):
        return rotate_z_axis(angle, v, in_radians)

    if (axis == 'x'):
        return rotation_x
    if (axis == 'y'):
        return rotation_y
    if (axis == 'z'):
        return rotation_z


def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function


# scaled_rotated_composition = compose(*[rotate_axis_by(angle=-pi/4, axis='z'), scale_by(0.2)])
composition = compose(*[rotate_axis_by(angle=-pi/4, axis='z'), scale_by(scalar=0.2)])

pouring_teapot = polygon_map(composition, load_triangles())


# initialize_rotating_figure(pouring_teapot)


composition = compose(*[rotate_axis_by(angle=pi/2, axis='x'), scale_by(scalar=0.2)])

head_teapot = polygon_map(composition, load_triangles())

# initialize_rotating_figure(head_teapot)


'''
So far, I’ve focused on the vector transformations we already saw in some way in the preceding
chapters. Now, let’s throw caution to the wind and see what other interesting transformations
we can come up with. Remember, the only requirement for a 3D vector transformation is that
it accepts a single 3D vector as input and returns a new 3D vector as its output. Let’s look at a
few transformations that don’t quite fall in any of the categories we’ve seen so far.
'''


def stretch_axis_by(stretch_factor=4., axis='x'):
    def new_f_x(v):
        x, y, z = v
        return (stretch_factor*x, y, z)

    def new_f_y(v):
        x, y, z = v
        return (x, stretch_factor*y, z)

    def new_f_z(v):
        x, y, z = v
        return (x, y, stretch_factor*z)
    if axis == 'x':
        return new_f_x
    if axis == 'y':
        return new_f_y
    if axis == 'z':
        return new_f_z


# composition = compose(*[stretch_axis_by(stretch_factor=4, axis='x'), scale_by(scalar=0.2)])

# stretch_teapot = polygon_map(composition, load_triangles())

# initialize_rotating_figure(stretch_teapot)


def slant_xy(vector):
    x, y, z = vector
    return (x+y, y, z)


def cubedy(vector):
    x, y, z = vector
    return (x, y**2, z)

# def translate_by(translation=(0, 0, 0)):
#     def translator(v):
#         translate(v, translation)
#     return translator


# composition = compose(*[translate_by(translation=(0, 0, -20))])

# slanted_teapot = polygon_map(composition, load_triangles())

# draw_model(slanted_teapot)
