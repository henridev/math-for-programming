from math import *

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)

def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+angle))


def from_cartesian_to_pygame_coor(coor, width=400, height=400):
    return (coor[0] + width/2, height/2 - coor[1])

def normalize(coor, min_original, max_original, min_new, max_new):
    new_x = coor[0] * (min_new / min_original)
    new_y = coor[1] * (max_new / max_original)
    return (new_x, new_y)

def create_to_pixel(width, height, min_original, max_original, min_new, max_new):
    scaling_x = (min_new / min_original)
    scaling_y = (max_new / max_original)
    tranform_x = width/2
    tranform_y = height/2

    def to_pixel(x, y):
        normalized_x = x * scaling_x
        normalized_y = y * scaling_y
        return (normalized_x + tranform_x, tranform_y - normalized_y)
    return to_pixel


def to_pixels(x, y, width=400, height=400):
    normalized_x = width * x / 20
    normalized_y = height * y / 20
    return (width/2 + normalized_x, height/2 - normalized_y)

def add(*vectors):
    return tuple(map(sum, zip(*vectors)))
