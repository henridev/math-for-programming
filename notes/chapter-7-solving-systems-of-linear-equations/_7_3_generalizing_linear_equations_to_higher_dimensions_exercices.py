from draw3d import *
from colors import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import matplotlib.pyplot as plt
from colors import *

'''
Exercise 7.16: What’s the equation for a line that passes through
(5, 4) and that is perpendicular to (-3, 3)? 
Solution: Here’s the set up:

If we call the given point `(x0, y0)` and the given vector `(a, b)`, 
we can write a criterion for a point `(x, y)` to lie on the line. 
Specifically, if `(x, y)` lies on the line, then `(x-x0, y-y0)` 
is parallel to the line and perpendicular to `(a, b)` 
as shown in figure 7.21. Because two perpendicular vectors have 
a zero dot product, that’s equivalent to the algebraic statement: 

(x-4, y-5)\cdot(3,-3) \\
3(x-4) + -3(y-5) = 0 \\
3x-12-3y+15 = 0 \\
3x-3y+3 = 0
'''


'''
Mini-project 7.17: Consider a system of 
two linear equations in 4D:

x1 + 2x2 + 2x3 + x4 = 0
x1 - x4 = 0
Explain algebraically (rather than geometrically) why the 
solutions form a vector subspace of 4D.

they form a subspace of 3d because the degree of freedom 
is constrained  in at least one dimension

>>>

-   A collection of vectors is **linearly dependent** 
    if any of its members can be obtained as 
    a linear combination of the others.
    we can reach higher dimensions when 
    a non linearly dependent vector gets 
    added to the collection of vectors

We can show that 
if (a1, a2, a3, a4) and (b1, b2, b3, b4) are two solutions, 
then a linear combination of those is a solution as well. 
That would imply that the solution set contains all 
linear combinations of its vectors, making it a vector subspace.

x_1 + 2*x_2 + 2*x_3 + x_4 = 0 \\
x_1 - x_4 = 0 \\
\\

(a_1, a_2, a_3, a_4)\\
(b_1, b_2, b_3, b_4) \\
\\ \text{assume these are solutions to the linear equation then } \\
\text{if they are a subspace than any linear of these solutions is a solution} \\ 
a_1 + 2a_2 + 2a_3 + a_4 = 0 \\
b_1 + 2b_2 + 2b_3 + b_4 = 0 \\
a_1 − a_4 = 0 \\
b_1 − b_4 = 0 \\
\\

scalar1 = c \\
scalar2 = b

\\ 
c*(a_1,a_2,a_3,a_4) + d*(b_1, b_2, b_3, b_4) =  \\
(ca_1 + db_1, ca_2 + db_2, ca_3 + db_3, ca_4 + db_4) \\
\\
\text{is this a solution to both equations?} \\
\\
\text{for equation 1} \\
(ca_1 + db_1) + 2(ca_2 + db_2) + 2(ca_3 + db_3) + (ca_4 + db_4) = 0 \\
ca_1 + db_1 + 2ca_2 + 2db_2 + 2ca_3 + 2db_3 + ca_4 + db_4 = 0 \\
ca_1 + 2ca_2 + 2ca_3 + ca_4 + db_1 + 2db_2 + 2db_3 + db_4 = 0 \\
c(a_1 + 2a_2 + 2a_3 + a_4) + d(b_1 + 2b_2 + 2b_3 + b_4) = 0 \\
c(0) + d(0) = 0 \\
\\
\text{for equation 2} \\
(ca_1 + db_1) - (ca_4 + db_4) = 0 \\
ca_1 - ca_4 + db_1 - db_4 = 0 \\
c(a_1 - a_4) + d(b_1 - b_4) = 0 \\
c(0) + d(0) = 0 \\

Any linear combination of any two solutions is also a solution, 
so the solution set contains all of its linear combinations.
That means the solution set is a vector subspace of 4D.
'''


'''
Exercise 7.18: What is the standard form equation for a plane 
that passes  through the point (1, 1, 1) and 
is perpendicular to the vector (1, 1, 1)?

(x-1, y-1, z-1)\cdot(1,1,1) \\
x-1 + y-1 + z-1 =  \\
x + y + z = 3 \\
'''

'''
Mini-project 7.19: Write a Python function that takes 
three 3D points as inputs and returns the standard form equation
of the plane that they lie in. 

For instance, if the standard form equation is ax + by + cz = d, 
the function could return the tuple (a, b, c, d).

Hint: Differences of any pairs of the three vectors 
are parallel to the plane, so cross products of the differences
are perpendicular.

(x-1, y-1, z-1)\cdot(1,1,1) 

'''


def subtract(v1, v2):
    return tuple(v1-v2 for (v1, v2) in zip(v1, v2))
def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)


p1 = (1, 1, 1)
p2 = (3, 0, 0)
p3 = (0, 3, 0)
dif_p2_p1 = subtract(p2, p1)
dif_p3_p1 = subtract(p3, p1)
crossing = cross(dif_p2_p1, dif_p3_p1)

# draw3d(
#     Arrow3D(p1, color=blue),
#     Arrow3D(p2, color=red),
#     Arrow3D(p3, color=green),
#     Arrow3D(dif_p2_p1, color=purple),
#     Arrow3D(dif_p3_p1, color=orange),
#     Arrow3D(crossing, color=black)
# )

'''
Exercise 7.24: Find 3 planes whose intersection is a single point, 3 planes whose intersection is a line, and 3 planes
whose intersection is a plane.
'''

fig = plt.figure()
fig.set_size_inches(7, 7)
ax = fig.gca(projection='3d')

def plot_scalar_field(funcs, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1, antialiased=False):

    for i, f in enumerate(funcs):
        fv = np.vectorize(f)

        # Make data.
        X = np.arange(xmin, xmax, xstep)
        Y = np.arange(ymin, ymax, ystep)
        X, Y = np.meshgrid(X, Y)
        Z = fv(X, Y)

        colors = [blue, red, green]
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=colors[i], alpha=alpha,
                               linewidth=0, antialiased=antialiased)


def u(x, y):
    return x+y+1
def r(x, y):
    return 2*y-3
def s(x, y):
    return -x+2


# plot_scalar_field([u, r, s], -5, 5, -5, 5, c=blue, cmap=None, alpha=0.5)
# matrix = np.array(((1, 1, -1), (0, 2, -1), (1, 0, 1)))
# vector = np.array((-1, 3, 2))
# solution = np.linalg.solve(matrix, vector)
# print(solution)

# xs, ys, zs = zip(*[tuple(solution)])
# ax.scatter(xs, ys, zs, color=red)


# def u(x, y):
#     return 2*x+2*y
# def r(x, y):
#     return x+y
# def s(x, y):
#     return -x/2 - y/2


# plot_scalar_field([u, r, s], -5, 5, -5, 5, c=blue, cmap=None, alpha=0.5)


# plt.show()


def plot_scalar_field(funcs, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1, antialiased=False):

    for i, f in enumerate(funcs):
        fv = np.vectorize(f)

        # Make data.
        X = np.arange(xmin, xmax, xstep)
        Y = np.arange(ymin, ymax, ystep)
        X, Y = np.meshgrid(X, Y)
        Z = fv(X, Y)

        colors = [blue, red, green]
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=colors[i], alpha=alpha,
                               linewidth=0, antialiased=antialiased)


def u(x, y):
    return 2*y
def r(x, y):
    return y
def s(x, y):
    return -y/2


plot_scalar_field([u, r, s], -5, 5, -5, 5, c=blue, cmap=None, alpha=0.5)


plt.show()
