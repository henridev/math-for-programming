from _7_1_designing_arcade_game import PolygonModel
import pprint
from find_intersection import check_segment_intersections

'''
Exercise 7.3: It’s possible that u + t · v can be a line through the origin. In this case,
what can you say about the vectors u and v?

yes in that case u has to be (0,0)
'''

'''
Exercise 7.4: If v = 0 = (0,0), do points of the form u + t · v represent a line?

no we simply have a point defined by u
'''

'''
Exercise 7.5: It turns out that the formula u + t · v is not unique
that is, you can pick different values of u and v to
represent the same line. What is another line representing (2, 2) + t · (-1, 3)?

U = (1,1)
V = (0,4)
'''


'''
Exercise 7.6: Does a · x + b · y = c represent a line for any values of a, b, and c?

no not for zero
'''

'''
Exercise 7.7: Find another equation for the line 2x + y = 3,
showing that the choices of a, b, and c are not unique.

4x + 2y = 6
'''

'''
Exercise 7.8: The equation ax + by = c is equivalent to an equation involving a dot product of two 2D vectors: (a, b) · (x, y)
= c. You could, therefore, say that a line is a set of vectors whose dot product with a given vector is constant. What is
the geometric interpretation of this statement?

{(x,y)} = set of vectors
the dot product of this set with (a,b)
'''


'''
Exercise 7.9: Confirm that the vectors (0, 7) and (3.5, 0) both satisfy the equation 2x + y = 7.

2*0 + 7 = 7
2*3.5 + 0 = 7
'''

'''
Exercise 7.10: Draw a graph for (3, 0) + t (0, 1) and convert it to the standard form using the formula.

p1 = (3,0)
p2 = (3,1)

a = end_segment_y - start_segment_y
b = start_segment_x - end_segment_x
c = start_segment_x * end_segment_y - start_segment_y * end_segment_x

a = 1 - 0
b = 3 - 3
c = 3 * 1 - 0 * 3
x-0y=3

x=3  => straight line
'''

'''
Exercise 7.11: Write a Python function standard_form that takes two vectors v1 and v2 and finds the line ax + by = c
passing through both of them. Specifically, it should output the tuple of constants (a, b, c).
'''


def standard_form(v1, v2):
    start_segment_x, start_segment_y = v1
    end_segment_x, end_segment_y = v2
    a = end_segment_y - start_segment_y
    b = start_segment_x - end_segment_x
    c = start_segment_x * end_segment_y - start_segment_y * end_segment_x
    return (a, b, c)


'''
Mini-project 7.12: For each of the four distance checks in do_segments_intersect, find a pair of line segments
that fail one of the checks but pass the other three checks.
'''

pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(check_segment_intersections(((-3, 0), (-1, 0)), ((0, -1), (0, 1))))
# pp.pprint(check_segment_intersections(((1, 0), (3, 0)), ((0, -1), (0, 1))))

'''
Exercise 7.13: For the example laser line and asteroid, confirm the does_intersect function returns True. (Hint:
use grid lines to find the vertices of the asteroid and build a PolygonModel object representing it.)
'''

asteroid = PolygonModel([(2, 7), (1, 5), (2, 3), (4, 2), (6, 2), (7, 4), (6, 6), (4, 6)])
asteroid.does_intersect([(0, 0), (7, 7)])

'''
Exercise 7.14: Write a does_collide(other_polygon) method to decide whether 
the current PolygonModel object collides with another other_polygon by checking 
whether any of the segments that define the two are intersecting. 
This could help us decide whether an asteroid has hit the ship or another asteroid.
'''

square1 = PolygonModel([(0, 0), (3, 0), (3, 3), (0, 3)])
square2 = PolygonModel([(1, 1), (4, 1), (4, 4), (1, 4)])
print(square1.does_collide(square2))


square3 = PolygonModel([(-3, -3), (-2, -3), (-2, -2), (-3, -2)])
print(square1.does_collide(square3))

'''
Mini-project 7.15: We can’t pick a vector w so that the following system 

m = (
    (2,1),
    (4,2)
) 

m * v = w

has a unique solution v. Find a vector w such that there are infinitely 
many solutions to the system; that is, infinitely many values of v that
satisfy the equation.


(
    (2 * x + 1 * y),
    (4 * x + 2 * y)
) 

(
    (2 * -1 + 1 * 2),
    (4 * -1 + 2 * 2)
)  = 
(
    (0),
    (0)
)

possible solutions = 
x*(r*-1)
y*(r*2)



'''
