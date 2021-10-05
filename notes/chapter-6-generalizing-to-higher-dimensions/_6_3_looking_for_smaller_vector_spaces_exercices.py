from _6_1_generalizing_vectors import Vec2, Vector
from plot import plot
from _6_2_5_manipulating_images import ImageVector

'''
Exercise 6.23: Give a geometric argument for why the following region S 
of the plane can’t be a vector subspace of the plane.

we can reach any point in the plane via a linear combination of 2 vectors in the current selected area

it is impossible for it to be a vector space because it would need to include the zero vector (scalar = 0)
'''


'''
Exercise 6.24: Show that the region of the plane where x = 0 forms a 1D vector space

this region is just the line through the y-axis which is a 1D vector subspace with coordinate (0, y) 
==> this is just an R in disguise
'''

'''
Exercise 6.25: Show that three vectors (1, 0), (1, 1), and (-1, 1) are linearly 
dependent by writing each one as a linear combination of the other two.

https://res.cloudinary.com/dri8yyakb/image/upload/v1632414804/116FECF1-B683-4834-A8F1-11F52395D010_zdjjuv.png
'''

'''
Exercise 6.26: Show that you can get any vector (x, y) 
as a linear combination of (1, 0) and (1, 1).

https://res.cloudinary.com/dri8yyakb/image/upload/v1632415103/17B9C25B-52C4-4020-83CF-0B300BD9008A_qxq5qu.png
'''


'''
Exercise 6.27: Given a single vector v, 
explain why the set of all linear combinations of v is the same as the set of all
scalar multiples of v.

vector space law 2.3 Addition of scalars should be compatible with scalar multiplication  

s_1 * v + s_2 * v = (s_1 + s_2) * v
ex. 2v  +  2v  = 4v
'''


'''
Exercise 6.28: From a geometric perspective, explain why a line that doesn’t pass through the origin is not a vector
subspace (of the plane or of the 3D space).

because ant vector can be made the zero vector by scalar 0 multiplication
'''


'''
Exercise 6.29: Any two of {e1, e2, e3} will fail to span all of ℝ3 and will instead span 2D subspaces of a 3D space. What
are these subspaces?

the plane x and y 
{e1, e2} =  a · (1, 0, 0) + b · (0, 1, 0) = (a, b, 0)

the plane x and z 
{e1, e3} =  a · (1, 0, 0) + c · (0, 0, 1) = (a, 0, c)

the plane y and z
{e2, e3} =  b · (0, 1, 0) + c · (0, 0, 1) = (0, b, c)
'''


'''
Exercise 6.30: Write the vector (-5, 4) as a linear combination of (0, 3) and (-2, 1)

https://res.cloudinary.com/dri8yyakb/image/upload/v1632723476/3536D1B1-01D8-4F0F-B943-C8DF2DA11800_xz80i1.png
'''

'''
Mini-project 6.31: Are (1, 2, 0), (5, 0, 5), and (2, -6,5) linearly independent or linearly dependent vectors?

Solution: It’s not easy to find, but there is a linear combination of the first two vectors that yields the third
-3 · (1, 2, 0) + (5, 0, 5) = (2, -6, 5) This means that the third vector is redundant, and the vectors are linearly dependent. They only span a 2D subspace of
3D rather than all of 3D space.
'''

'''
Exercise 6.32: Explain why the linear function 
f(x) = ax + b is not a linear map from the vector space ℝ to itself unless b = 0.

https://res.cloudinary.com/dri8yyakb/image/upload/v1632723870/9B78D6C7-CDA0-4D6B-86AF-DFDDE0F4BC89_jqr0wn.png
'''

'''
Exercise 6.33: Rebuild the LinearFunction class by inheriting from Vec2 and implementing the __call__
method.
'''

class LinearFunction(Vec2):
    def __call__(self, input):
        return self.x * input + self.y


'''
Exercise 6.34: Prove (algebraically!) that the linear function
f(x) = ax + b forms a vector subspace of the vector space of functions.

Solution: To prove this, you need to be sure a linear combination of two 
linear functions is another linear function. If f(x) ax + b and g(x) = cx + d, 
then 

r * f + s * g = 
rax + rb + scx + sd =
(ra + sc) * x + (rb + sd)
(ra + sc) => scalar
(rb + sd) => scalar
(ra + sc) * x + (rb + sd) => form ax + b  

thus these linear functions are closed under linear combinations
'''


'''
Exercise 6.35: Find a basis for the set of 3-by-3 matrices. 
What is the dimension of this vector space?


this wil be a set of 9 matrices as we have nine entries on each vector 
all entries will be set to zero while one entry is set to 1. with this set we
can reach each point in a 3*3 matrix via linear combinations.
'''


'''
Mini-project 6.36: Implement a class QuadraticFunction(Vector) that represents the vector subspace of
functions of the form ax2 + bx + c. What is a basis for this subspace?
'''

class QuadraticFunction(Vector):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, v):
        return QuadraticFunction(self.a + v.a, self.b + v.b, self.c + v.c)

    def scale(self, scalar):
        return QuadraticFunction(scalar * self.a, scalar * self.b, scalar * self.c)

    def __call__(self, x):
        return self.a * (x**2) + self.b * x + self.c

    @classmethod
    def zero(cls):
        return QuadraticFunction(0, 0, 0)


# plot([QuadraticFunction(1, 2, 1)], -5, 5).show()

# it's like a linear combination of the basises {x^2, x, 1}
# they span the whole space and none can be written as a combination of the others


'''
Mini-project 6.37: I claimed that {4x + 1, x − 2} are a basis for the set of linear functions.
Show that you can write -2x + 5 as a linear combination of these two functions.


1 = 0*f
x = 1/7 * (g - 2(f))

-2[1/7 * (g - 2(f))] + 5*(0*f) = 
-2/7g + 4/7f
'''

# plot([LinearFunction(4, 1), LinearFunction(1, -2), LinearFunction(-2, 5)], -5, 5).show()


'''
Mini-project 6.38: The vector space of all polynomials is an infinite-dimensional subspace. 
Implement that vector space as a class and describe a basis (which must be an infinite set!).
'''


class Polynomial(Vector):
    def __init__(self, *coefs):
        self.coefs = coefs

    def add(self, v):
        return Polynomial(*map(sum, zip(v.coefs, self.coefs)))

    def scale(self, scalar):
        return Polynomial(*[scalar * coef for coef in self.coefs])

    def __call__(self, x):
        return sum([coef * (x**(i)) for i, coef in enumerate(reversed(self.coefs))])

    def __repr__(self) -> str:
        return f'coefs {self.coefs}'

    @classmethod
    def zero(cls):
        return Polynomial(0)


print(Polynomial(3, 2, 1)(2))


'''
Exercise 6.39: I showed you pseudocode for a basis vector for the 
270,000 dimensional space of images. What would the second basis vector look like?

Solution: The second basis vector could be given by putting a one in the next possible place. 
It would yield a dim green pixel in the very top left of the image:

ImageVector([
    (0,1,0), (0,0,0), (0,0,0), ..., (0,0,0), #<1>
    (0,0,0), (0,0,0), (0,0,0), ..., (0,0,0), #<2>
    ...
])

#1 For the second basis vector, the 1 has moved to the second possible slot.
#2 All other rows remain empty.
'''

'''
Exercise 6.40: Write a function solid_color(r,g,b) that returns 
a solid color ImageVector with the given red, green, and blue content at every pixel.
'''


def solid_color(r, g, b):
    return ImageVector([(r, g, b) for _ in range(0, 300*300)])


solid_color(100, 255, 100).image().show()


'''
Mini-project 6.41: Write a linear map that generates an ImageVector from a 30x30 grayscale image, 
implemented as a 30x30 matrix of brightness values. Then, implement the linear map that 
takes a 300x300 image to a 30x30 grayscale image by averaging the brightness 
(average of red, green, and blue) at each pixel. 
'''

image_size = (300, 300)
total_pixels = image_size[0] * image_size[1]
square_count = 30  # <1>
square_width = 10

def ij(n):
    return (n // image_size[0], n % image_size[1])
def to_lowres_grayscale(img):  # <2>
    matrix = [
        [0 for i in range(0, square_count)]
        for j in range(0, square_count)
    ]
    for (n, p) in enumerate(img.pixels):
        i, j = ij(n)
        weight = 1.0 / (3 * square_width * square_width)
        matrix[i // square_width][j // square_width] += (sum(p) * weight)

    return matrix

def from_lowres_grayscale(matrix):  # <3>
    def lowres(pixels, ij):
        i, j = ij
        return pixels[i // square_width][j // square_width]

    def make_highres(limg):
        pixels = list(matrix)
        def triple(x): return (x, x, x)
        return ImageVector([triple(lowres(matrix, ij(n))) for n in range(0, total_pixels)])
    return make_highres(matrix)

# 1 Indicates that we’re breaking the picture into a 30x30 grid
# 2 The function takes an ImageVector and returns an array of 30 arrays of 30 values each,
# giving grayscale values square by square.
# 3 The second function takes a 30x30 matrix and returns an image built from 10x10 pixel blocks,
# having a brightness given by the matrix values.
