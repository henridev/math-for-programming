from vectors import *
from draw_model import *
from teapot import load_triangles
from hypothesis import given, note, strategies as st

A_i_hat = (1, 1, 1)  # 1
A_j_hat = (1, 0, -1)
A_k_hat = (0, 1, 1)
def apply_A(v):  # 2
    return add(  # 3
        scale(v[0], A_i_hat),
        scale(v[1], A_j_hat),
        scale(v[2], A_k_hat)
    )


# draw_model(polygon_map(apply_A, load_triangles()))  # 4


'''
Exercise 4.10: Considering S again, the vector transformation that squares all coordinates, 
show algebraically that S(sv) = sS(v) 
does not hold for all choices of scalars s and 2D vectors v.
'''

def square_coords(v):
    return tuple((coor**2 for coor in v))

# v = (x, y)
# scalar = s

# S(sv) = ((x*s)**2, (y*s)**2)
# sS(v) = (s*(x**2), s*(y**2))

# sS(v) = (s^2x^2, s^2y^2) = s^2 · (x^2, y^2) = s^2 · S(v). <== distributive property

# s^2 · S(v) !== s · S(v)


'''
Exercise 4.11: Suppose T is a vector transformation and T(0) ≠ 0, where 0 represents the vector with all coordinates
equal to zero. Why is T not linear according to the definition?
'''

# one of the properties of linear trnasformations is that it origin remains
#  which is not the case if T changes ir

'''
Exercise 4.12: The identity transformation is 
the vector transformation that returns the same vector it is passed. 
It is denoted with a capital I, so we could write its definition 
as I(v) = v for all vectors v. Explain why I is a linear transformation.
'''

# I(s_1*v + s_2*u) = s_1*I(v) + s_2*I(u)
# given I(v) = v and I(u) = u
# s_1*v + s_2*u = s_1*v + s_2*u
# vector sums and scalar multiples are preserved therefore this
# is a linear transformations

'''
Exercise 4.13: What is the midpoint between (5, 3) and (-2, 1)? 
Plot all three of these points to see that you are correct.
'''

#  midpoint is the scaled linear combination of both vectors

def linear_combo_scaled(v, u, v_scale=0.5, u_scale=0.5):
    return add(scale(v_scale, v), scale(u_scale, u))


v = (5, 3)
u = (-2, 1)
print(linear_combo_scaled(v, u))


'''
Exercise 4.14: Consider again the non-linear transformation 
S(v) sending v = (x, y) to (x2, y2). Plot all 36 vectors v with
integer coordinates 0 to 5 as points using the drawing code from chapter 2 and then plot S(v) for each of them. What
happens geometrically to vectors under the action of S?
'''

'''
def S(v):
    return tuple((coor**2 for coor in v))

def points_between(steps = 5):
    points = []
    for x in range(0, steps):
        for y in range(0, steps):
            points.append((x,y))
    return points

point_0_to_5 = points_between(5)

draw(
    Points(*points_between(5), color=colors.red),
    Points(*[S(point) for point in points_between(5)], color=colors.blue),
)
'''


# https://res.cloudinary.com/dri8yyakb/image/upload/v1631087037/8D68C0B1-F6B9-4E88-ABC0-500AF8E2F326_yewrhq.png

'''
Mini-project 4.15: Property-based testing is a type of unit testing 
that involves inventing arbitrary input data for a program 
and then checking that the outputs satisfy desired conditions. 
There are popular Python libraries like Hypothesis (available through pip)
that make it easy to set this up. 

Using your library of choice, implement propertybased tests 
that check if a vector transformation is linear.
Specifically, given a vector transformation T implemented 
as a Python function, generate a large number of pairs of
random vectors and assert for all of those that their sum is 
preserved by T. Then, do the same thing for pairs of a scalar
and a vector, and ensure that T preserves scalar multiples. 
You should find that linear transformations like rotate_x_by(pi/2) 
pass the test, but non-linear transformations like the 
coordinate-squaring transformation do not pass.
'''

def round_tuple(t):
    return tuple((int(round(coor)) for coor in v))

def compareTuples(T1, T2):
    index = 0
    length = len(T1)
    while index < length:
        # If they are equal, move to the next pair, else stop.
        if T1[index] == T2[index]:
            index += 1
        else:
            return False
    return True

def test_addition(u, v, transformation):
    result_1 = add(transformation(v), transformation(u))
    result_2 = transformation(add(v, u))

    return compareTuples(round_tuple(result_1), round_tuple(result_2))

def test_scaling(v, transformation, scalar):
    result_1 = scale(scalar, transformation(v))
    result_2 = transformation(scale(scalar, v))

    return compareTuples(round_tuple(result_1), round_tuple(result_2))

def is_linear_transformation(u, v, transformation, scalar):
    return test_addition(u, v, transformation) and test_scaling(u, transformation, scalar) and test_scaling(v, transformation, scalar)

def rotate45d(vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+(pi/4)))

@given(
    st.tuples(st.integers(), st.integers()),
    st.tuples(st.integers(), st.integers()),
    st.integers()
)
def test_linear_transformation(u, v, scalar):
    result = is_linear_transformation(u, v, rotate45d, scalar=scalar)
    note(f"Result: {result!r}")
    assert result == True


try:
    test_linear_transformation()
except AssertionError:
    print("result != True")

'''
Exercise 4.16: One 2D vector transformation is a reflection across the x-axis. This transformation takes a vector and
returns another one, which is the mirror image with respect to the x-axis. Its x-coordinate should be unchanged, and its
y-coordinate should change its sign. Denoting this transformation Sx, here is an image of a vector v = (3, 2) and the
transformed vector Sx(v)

Draw two vectors and their sum, as well as the reflection of these three vectors to demonstrate that this transformation
preserves vector addition. Draw another diagram to show similarly that scalar multiplication is preserved, thereby
demonstrating both criteria for linearity.s
'''


'''
Solution: Here’s an example of reflection
over the x-axis that preserves a vector sum: For u + v = w as shown, 
reflection over the x-axis preserves the sum; that is, Sx(u) + Sx(v) = Sx(w).
Here’s an example showing reflection preserving a scalar multiple: 
Sx(sv) lies where sSx(v) is expected to be.
Reflection across the x-axis preserves this scalar multiple.
'''

'''
Mini-project 4.17: Suppose S and T are both linear transformations. 
Explain why the composition of S and T is also linear.
'''

# S(sv) = sS(v)
# S(v + u) = S(v) + S(u)

# S(T(sv)) = sS(T(v))
# S(T(v + u)) = S(T(v)) + S(T(u))

'''
Suppose first that u + v = w for any given input vectors u and v. 
Then by the linearity of T, we also know that T(u) + T(v) = T(w). 
Because this sum holds, the linearity of S tells us that the sum is preserved under S:
S(T(u)) + S(T(v)) = S(T(w)). That means that S(T(v)) preserves vector sums.
Similarly, for any scalar multiple sv, the linearity of T tells us that s · T(v) = T(sv). 
By linearity of S, s · S(T(v)) = S(T(sv)) as well. 
This means S(T(v)) preserves scalar multiplication and, 
therefore, that S(T(v)) satisfies the full definition of linearity
as previously stated. 
We can conclude that the composition of two linear transformations 
is linear.
'''


'''
Exercise 4.18: Let T be the linear transformation 
done by the Python function rotate_x_by(pi/2), what are T(e1),
T(e2), and T(e3)?
'''

# T(e1) stays the same
# T(e2) = (0,0,1)
# T(e3) = (0,-1,0)
# right hand rule applied middle to top thumb to you index unchanged


'''
Exercise 4.19: Write a linear_combination(scalars, *vectors) that takes a list of scalars and the same
number of vectors, and returns a single vector. For example, linear_combination([1,2,3], (1,0,0),
(0,1,0), (0,0,1)) should return 1 · (1, 0, 0) + 2 · (0, 1, 0) + 3 · (0, 0, 1) or (1, 2, 3).
'''

def linear_combination(scalars, *vectors):
    return add(*[scale(scalar, vector) for scalar, vector in zip(scalars, vectors)])


print(linear_combination([1, 2, 3], (1, 0, 0), (0, 1, 0), (0, 0, 1)))

'''
Exercise 4.20: Write a function transform_standard_basis(transform) that takes a 3D vector transformation
as an input and outputs the effect it has on the standard basis. It should output a tuple of 3 vectors that are the results
of transform acting on e1, e2, and e3, respectively.
'''

def transform_standard_basis(transform):
    return transform((1, 0, 0)), transform((0, 1, 0)), transform((0, 0, 1))


'''
Exercise 4.21: Suppose B is a linear transformation, with B(e1) = (0, 0, 1), B(e2) = (2, 1, 0), B(e3) = (-1, 0, -1), and v = (-1,
1, 2). What is B(v)?
'''

# (-1 * (0, 0, 1)) + (1 * (2, 1, 0)) + (2 * (-1, 0, -1)) = (0,0,-1) + (2,1,0) + (-2, 0, -2) = (0,1,-3)


'''
Exercise 4.22: Suppose A and B are both linear transformations 
with A(e1) = (1, 1, 1), A(e2) = (1, 0, -1), and A(e3) = (0, 1,1), and 
B(e1) = (0, 0, 1), B(e2) = (2, 1, 0), and B(e3) = (-1, 0, -1). 
What is A(B(e1)), A(B(e2)), and A(B(e3))?
'''


# a transformation of a vector can be written as a linear combination containing the already transformed basis vectors
# A(v) = v_x * A(i_hat) + v_y * A(j_hat) + v_z * A(j_hat)

# A(B(e1)) = 0 * A(e1) + 0 * A(e2) + 1 * A(e3) = A(e3) = (0, 1, 1)
# A(B(e2)) = 2 * A(e1) + 1 * A(e2) + 0 * A(e3) = (3, 2, 1)
# A(B(e3)) = -1 * A(e1) + 0 * A(e2) + -1 * A(e3) = (-1, -2, -2)
