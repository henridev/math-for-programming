
import numpy as np
from math import sqrt

def slope(x_1, y_1, x_2, y_2):
    print(f'x_1 {x_1} y_1 {y_1} x_2 {x_2} y_2 {y_2}')
    if(y_1 == 0 and y_2 == 0):
        return 0
    return (y_2-y_1) / (x_1-x_2)


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def distance(v1, v2):
    def subtract(v1, v2):
        return tuple(v1-v2 for (v1, v2) in zip(v1, v2))
    return length(subtract(v1, v2))

def standard_form(start_segment, end_segment):
    '''
    POINT-SLOPE FORM:
    y - y_1 = (y_2-y_1 / x_2-x_1) * (x - x_1)
    STANDARD FORM: 
    Ax + By = C

    POINT-FORM:
    (x,y)=(x_1,y_1)+t*(x_2-x_1,y_2-y_1) 
    x=x_1+t*(x_2-x_1)
    y=y_1+t*(y_2-y_1)
    ... (get rid of t)
    gives a, b and c formula
    '''
    start_segment_x, start_segment_y = start_segment
    end_segment_x, end_segment_y = end_segment
    a = end_segment_y - start_segment_y
    b = start_segment_x - end_segment_x
    c = start_segment_x * end_segment_y - start_segment_y * end_segment_x
    return a, b, c


def segment_intersect_check(s1, s2):
    s1_standard_form = standard_form(s1[0], s1[1])
    s2_standard_form = standard_form(s2[0], s2[1])

    s1_a, s1_b, s1_c = s1_standard_form
    s2_a, s2_b, s2_c = s2_standard_form

    row_1_transform_matrix = (s1_a, s1_b)
    row_2_transform_matrix = (s2_a, s2_b)
    transform_matrix = np.array((row_1_transform_matrix, row_2_transform_matrix))

    output_vector = (s1_c, s2_c)

    intersection = np.linalg.solve(transform_matrix, output_vector)

    return intersection

def check_if_in_bound(s1, s2, intersection):
    s1_start, s1_end = s1
    s2_start, s2_end = s2
    s1_start_x, s1_start_y = s1_start
    s1_end_x, s1_end_y = s1_end
    s2_start_x, s2_start_y = s2_start
    s2_end_x, s2_end_y = s2_end
    intersection_x, intersection_y = intersection

    s1_min_x = min(s1_start_x, s1_end_x)
    s1_max_x = max(s1_start_x, s1_end_x)
    s1_min_y = min(s1_start_y, s1_end_y)
    s1_max_y = max(s1_start_y, s1_end_y)
    s2_min_x = min(s2_start_x, s2_end_x)
    s2_max_x = max(s2_start_x, s2_end_x)
    s2_min_y = min(s2_start_y, s2_end_y)
    s2_max_y = max(s2_start_y, s2_end_y)

    s1_in_x_bounds = s1_min_x <= intersection_x <= s1_max_x
    s1_in_y_bounds = s1_min_y <= intersection_y <= s1_max_y
    s2_in_x_bounds = s2_min_x <= intersection_x <= s2_max_x
    s2_in_y_bounds = s2_min_y <= intersection_y <= s2_max_y

    return s1_in_x_bounds and s1_in_y_bounds and s2_in_x_bounds and s2_in_y_bounds

def check_if_in_bound_return_check_results(s1, s2, intersection):
    s1_start, s1_end = s1
    s2_start, s2_end = s2
    s1_start_x, s1_start_y = s1_start
    s1_end_x, s1_end_y = s1_end
    s2_start_x, s2_start_y = s2_start
    s2_end_x, s2_end_y = s2_end
    intersection_x, intersection_y = intersection

    s1_min_x = min(s1_start_x, s1_end_x)
    s1_max_x = max(s1_start_x, s1_end_x)
    s1_min_y = min(s1_start_y, s1_end_y)
    s1_max_y = max(s1_start_y, s1_end_y)
    s2_min_x = min(s2_start_x, s2_end_x)
    s2_max_x = max(s2_start_x, s2_end_x)
    s2_min_y = min(s2_start_y, s2_end_y)
    s2_max_y = max(s2_start_y, s2_end_y)

    s1_in_x_min_bounds = s1_min_x <= intersection_x
    s1_in_x_max_bounds = intersection_x <= s1_max_x

    s1_in_y_min_bounds = s1_min_y <= intersection_y
    s1_in_y_max_bounds = intersection_y <= s1_max_y

    s2_in_x_min_bounds = s2_min_x <= intersection_x
    s2_in_x_max_bounds = intersection_x <= s2_max_x

    s2_in_y_min_bounds = s2_min_y <= intersection_y
    s2_in_y_max_bounds = intersection_y <= s2_max_y

    return {
        's1_in_x_min_bounds': s1_in_x_min_bounds,
        's1_in_x_max_bounds': s1_in_x_max_bounds,
        's1_in_y_min_bounds': s1_in_y_min_bounds,
        's1_in_y_max_bounds': s1_in_y_max_bounds,
        's2_in_x_min_bounds': s2_in_x_min_bounds,
        's2_in_x_max_bounds': s2_in_x_max_bounds,
        's2_in_y_min_bounds': s2_in_y_min_bounds,
        's2_in_y_max_bounds': s2_in_y_max_bounds
    }


def check_if_segments_intersect(s1, s2):
    try:
        intersection = segment_intersect_check(s1, s2)
        return check_if_in_bound(s1, s2, intersection)
    except np.linalg.linalg.LinAlgError:
        return False

def check_segment_intersections(s1, s2):
    try:
        intersection = segment_intersect_check(s1, s2)
        return check_if_in_bound_return_check_results(s1, s2, intersection)
    except np.linalg.linalg.LinAlgError:
        return False


# s1 = ((1, 5), (2, 3))
# s2 = ((2, 2), (4, 4))

# intersection = segment_intersect_check(s1, s2)

# check_if_in_bound(s1, s2, intersection)


# s1 = ((0, 4), (2, 3))
# s2 = ((2, 2), (4, 4))

# intersection = segment_intersect_check(s1, s2)

# print(check_if_in_bound(s1, s2, intersection))


# s1 = ((0, 4), (4, 2))
# s2 = ((2, 2), (4, 4))

# intersection = segment_intersect_check(s1, s2)

# print(check_if_in_bound(s1, s2, intersection))
