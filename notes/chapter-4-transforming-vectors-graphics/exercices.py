from _2_transforming_3d_object import *
from draw_model import draw_model


'''
Exercise 4.1: Implement a translate_by function (referred to in section 4.1.2), 
taking a translation vector as input and returning a translation function as output.
'''

# def translate_by(translation=(0, 0, 0)):
#     def translator(v):
#         translate(v, translation)
#     return translator

'''
Exercise 4.2: Render the teapot translated by 20 units in the negative z direction. What does the resulting image look
like?
'''


# composition = compose(*[translate_by(translation=(0, 0, -20))])

# distant_teapot = polygon_map(composition, load_triangles())

# draw_model(distant_teapot)

'''
looking at the teapot from five units up the z-axis. This transformation brings the teapot 20 units
further from us, so it looks much smaller than the original.
'''

'''
Mini-project 4.3: What happens to the teapot when you scale every vector by a scalar between 0 and 1?
What happens when you scale it by a factor of -1?
'''

# composition_inside_out_flipped = compose(*[scale_by(-0.5), translate_by((0, -1, 0)), rotate_axis_by(pi/2, axis="x")])
# composition = compose(*[scale_by(0.5), translate_by((0, 1, 0))])

# first_teapot = polygon_map(composition_inside_out_flipped, load_triangles())
# flipped_reversed_teapot = polygon_map(composition, load_triangles())

# draw_model(first_teapot + flipped_reversed_teapot)


'''
As you can see, scale_by(0.5) shrinks the teapot to half its original size. The action of scale_by(-1) seems to
rotate the teapot by 180°, but the situation is a bit more complicated. It’s actually turned inside-out as well! Each
triangle has been reflected, so each normal vector now points into the teapot rather than outward from its surface.
'''

'''
Exercise 4.4: First apply translate1left to the teapot and then apply scale2. 
How is the result different from the opposite order of composition? Why?
'''

# composition_inside_out_flipped = compose(*[scale_by(2), translate_by((-1, 0, 0))])
# composition = compose(*[translate_by((-1, 0, 0)), scale_by(2)])

# first_teapot = polygon_map(composition_inside_out_flipped, load_triangles())
# second_teapot = polygon_map(composition, load_triangles())

# draw_model(first_teapot + second_teapot)

'''
the scaling doubles the translation if the scaling happens after the translation in 
that case the pot will thus be moved further to the left
'''


'''
Exercise 4.5: What is the effect of the transformation compose(scale_by(0.4), scale_by(1.5))?
'''

'''
Applying this to a vector scales it by 1.5 and then by 0.4  = (1.5*0.4) = 0.6
'''


'''
Exercise 4.6: Modify the compose(f,g) function to compose(*args), which takes several functions as arguments
and returns a new function that is their composition.
'''

def compose(*transformations):
    def composed_function(v):
        transformed_v = v
        for t in transformations:
            transformed_v = t(transformed_v)
        return transformed_v
    return composed_function


'''
Exercise 4.7: Write a curry2(f) function that takes a Python function f(x,y) with two arguments and returns a
curried version. For instance, once you write g = curry2(f), the two expressions f(x,y) and g(x)(y) should
return the same result.
'''

def curry2(function_2_args):
    def new_function_y(y):
        def new_function_x(x):
            return function_2_args(x, y)
        return new_function_x
    return new_function_y


'''
Exercise 4.8: Without running it, what is the result of applying the transformation
compose(rotate_z_by(pi/2),rotate_x_by(pi/2))? What if you switch the order of the composition?


This composition is equivalent to a clockwise rotation by 𝜋/2 about the y-axis. Reversing the order gives a
counterclockwise rotation by 𝜋/2 about the y-axis.
'''

composition_rotation_2_steps = compose(*
                                       [
                                           scale_by(0.5),
                                           translate_by(translation=(0, 0, -2)),
                                           rotate_axis_by(pi/2, axis="z"),
                                           rotate_axis_by(pi/2, axis="x")
                                       ]
                                       )
composition_rotation_1_step_first = compose(*
                                            [
                                                scale_by(0.5),
                                                translate_by(translation=(0, 0, 0)),
                                                rotate_axis_by(pi/2, axis="y"),
                                            ]
                                            )

composition_rotation_1_step_second = compose(*
                                             [
                                                 scale_by(0.5),
                                                 translate_by((0, -1, 0)),
                                                 rotate_axis_by(pi/2, axis="y"),
                                             ]
                                             )
first_teapot = polygon_map(composition_rotation_2_steps, load_triangles())
second_teapot = polygon_map(composition_rotation_1_step_first, load_triangles())
third_teapot = polygon_map(composition_rotation_1_step_second, load_triangles())

draw_model(first_teapot)

'''
Exercise 4.9: Write a function stretch_x(scalar,vector) that scales the target vector by the given factor but
only in the x direction. Also write a curried version stretch_x_by so that stretch_x_by(scalar)(vector)
returns the same result.
'''

def stretch_x(scalar, vector):
    x, y, z = vector
    return scalar * x, y, z


def stretch_x_by(scalar):
    def new_func(v):
        return stretch_x(scalar, v)
    return new_func
