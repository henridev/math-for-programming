# 7: solving systems of linear equations

This chapter covers

- **collision detection** of objects in a 2D video game
- finding linear equation intersections in the plane
- Picturing and solving **systems of linear equations** in 3D or beyond
- Re-writing vectors as **linear combinations** of other vectors

When you think of algebra, you probably think of problems that require “solving for x.” For instance, you probably spent quite a bit of time in algebra class learning to solve equations like 3x2 + 2x + 4 = 0; that is, figuring out what value or values of x make the equation true. **Linear algebra**, being a branch of algebra, has the same kinds of computational  questions. The difference is that what *you want to solve for may be a vector or matrix rather than a number*. If you take a traditional linear algebra course, you might cover a lot of algorithms to solve these kinds of problems. But because you have Python at your disposal, you only need to know how to recognize the problem you’re facing and choose the right library to find the answer for you. I’m going to cover the most important class of linear algebra problems you’ll see in the wild: **systems of linear equations**. *These problems boil down to finding points where lines, planes, or their higher dimensional analogies intersect*. 

One example is the infamous high school math problem involving two trains leaving Boston and New York at different times and speeds. But because I don’t assume railroad operation interests you, I’ll use a more entertaining example. In this chapter, we build a simple remake of the classic Asteroids arcade game (figure 7.1). In this game, the player controls a triangle representing a spaceship and fires a laser at polygons floating around it, which represent asteroids. The player must destroy the asteroids to prevent them from hitting and destroying the spaceship. 

One of the key mechanics in this game is deciding whether the laser hits an asteroid. This requires us to figure out whether the line *defining the laser beam intersects with the line segments outlining the asteroids*. If these lines intersect, the asteroid is destroyed. We’ll set up the game first and then we’ll see how to solve the underlying linear algebra problem. After we implement our game, I’ll show you how this 2D example generalizes to 3D or any number of dimensions. The latter half of this chapter covers a bit more theory, but it will round out your linear algebra education. We’ll have covered many of the major concepts you’d find in a college-level linear algebra class, albeit in less depth. After completing this chapter, you should be well prepared to crack open a denser textbook on linear algebra and fill in the details. But for now, let’s focus on building our game  

## 7.1: designing an arcade game

In this chapter, I focus on a simplified version of the asteroid game where the ship and asteroids are static. In the source code, you’ll see that I already made the asteroids move, and we’ll cover how to make them move according to the laws of physics in part 2 of this book. To get started, we model the entities of the game—the spaceship, the laser, and the asteroids—and show how to render them onscreen.  

### modelling the game

In this section, we display the spaceship and the asteroids as polygons in the game. As before, we model these as collections of vectors. For instance, we can represent an eight-sided asteroid by eight vectors (indicated by arrows in figure 7.2), and we can connect them to draw its outline.  



The asteroid or spaceship translates or rotates as it travels through space, but its shape remains the same. Therefore, we store the vectors representing this shape separately from the x- and y-coordinates of its center, which can change over time. We also store an angle, indicating the rotation of the object at the current moment. The Polygon Model class represents a game entity (the ship or an asteroid) that keeps its shape but can translate or rotate. It’s initialized with a set of vector points that define the outline of the asteroid, and by default, its center x- and y coordinates and its angle of rotation are set to zero:  

```python
from random import uniform, randint
from utils import *

class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0

    def apply_translation_rotation(self, point):
        x, y = point
        return rotate2d(self.rotation_angle, (self.x + x, self.y + y))

    def get_actual_points(self):
        return [
            self.apply_translation_rotation(point)
            for point in self.points
        ]

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)  # <1>
        vs = [to_cartesian((uniform(0.5, 1.0), 2*pi*i/sides)) for i in range(0, sides)]
        super().__init__(vs)

        
```

When the spaceship or asteroid moves, we need to apply the translation by `self.x, self.y` and the rotation by `self.rotation_angle` to find out its actual location. As an exercise, you can give PolygonModel a method to compute the actual, transformed vectors outlining it. 

The spaceship and asteroids are specific cases of **PolygonModel** that initialize automatically with their respective shapes. For instance, the ship has a fixed triangular shape, given by three points:  

For the asteroid, we initialize it with somewhere between 5 and 9 vectors at equally spaced angles and random lengths between 0.5 and 1.0. This randomness gives the asteroids some character:  

With these objects defined, we can turn our attention to instantiating them and rendering them onscreen.  

### rendering the game

For the initial state of the game, we need a ship and several asteroids. The ship can begin at the center of the screen, but the asteroids should be randomly spread out over the screen. We can show an area of the plane ranging from -10 to 10 in the x and y directions like this:

I use a 400x400 pixel screen, which requires transforming the x- and y-coordinates before rendering them. Using PyGame’s built-in 2D graphics instead of OpenGL, the *top left pixel on the screen has the coordinate (0, 0) and the bottom right has the coordinate (400, 400)*. These coordinates are not only bigger, they’re also translated and upside down, so we need to write a to_pixels function (illustrated in figure 7.3) that does the transformation from our coordinate
system to PyGame’s pixels.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632749508/F30158F0-F887-4F70-B218-C75F23CC2A59_kvaqsi.png"/>

With the `to_pixels` function implemented, we can write a function to draw a polygon defined by points to the PyGame screen. First, we take the transformed points (translated and rotated) that define the polygon and convert them to pixels. Then we draw them with a PyGame function:


You can see the whole game loop in the source code, but it basically calls draw_poly for the ship and each asteroid every time a frame is rendered. The result is our simple triangular
spaceship surrounded by an asteroid field in a PyGame window (figure 7.4).  



### shooting the laser

Now it’s time for the most important part: giving our ship a way to defend itself! The player should be able to aim the ship using the left and right arrow keys and then shoot a laser by pressing the spacebar. The laser beam should come out of the tip of the spaceship and extend to the edge of the screen.

In the 2D world we’ve invented, the laser beam should be a line segment starting at the transformed tip of the spaceship and extending in whatever direction the ship is pointed. We can make sure it reaches the end of the screen by making it sufficiently long. Because the laser’s line segment is associated with the state of the Ship object, we can make a method on the Ship class to compute it:  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632820409/26504FAC-3C62-41EF-B914-5EDB3CF3C40E_chnap8.png"/>

In the source code, you can see how to make PyGame respond to keystrokes and draw the laser as a line segment only if the spacebar is pressed. Finally, if the player fires the laser and hits an asteroid, we want to know something happened. In every iteration of the game loop, we want to check each asteroid to see if it is currently hit by the laser. We do this with a does_intersect(segment) method on the PolygonModel class, which computes whether the input segment intersects any segment of the given PolygonModel. The final code includes some lines like the following:  

```python
if keys[pygame.K_SPACE]:
	laser = ship.laser_segment()
	draw_segment(screen, *laser)
	for asteroid in asteroids:
		if asteroid.does_intersect(laser):  # <3>
			asteroids.remove(asteroid)
```

## 7.2 finding intersection points between two lines

The problem at hand is to decide whether the laser beam hits the asteroid. To do this, we’ll look at each line segment defining the asteroid and decide whether it intersects with the segment defining the laser beam. There are a few algorithms we could use, but we’ll solve this as a system of linear equations in two variables. Geometrically, this means looking at the lines defined by an edge of the asteroid and the laser beam and seeing where they intersect (figure 7.6).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632820600/24A25D69-F639-46C0-A192-F8015A739EE7_lpzo4k.png"/>

Once we know the location of the intersection, we can see whether it lies within the bounds of both segments. If so, the segments collide and the asteroid is hit. We first review equations for lines in the plane, then cover how to find where pairs of lines intersect. Finally, we write the code for the does_intersect method for our game.  

### choosing the right line

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632822212/Animation_hquemx.gif"/>

In the previous chapter, we saw that 1D subspaces of the 2D plane are lines. These subspaces consist of all of the scalar multiples `t · v` for a single chosen vector v. Because one such scalar multiple is `0 · v`, these lines always pass through the **origin**, so `t · v` is not quite a general formula for any line we encounter. 

If we start with a line through the origin and translate it by another vector `u`, we can get any possible line. The points on this line have the form `u + t · v` for some scalar t. 

For instance, take `v = (2, -1)`. Points of the form `t · (2, -1)` lie on a line through the origin. But if we translate by a second vector, `u = (2, 3)`, the points are now `(2, 3) + t · (2, -1)`, which constitute a line that doesn’t pass through the origin (figure 7.7).  

Any line can be described as the points `u + t · v` for some selection of vectors u and v and all possible scalar multiples t. This is probably not the general formula for a line you’re used to. Instead of writing y as a function of x, we’ve given both the x- and y-coordinates of points on the line as functions of another parameter t. Sometimes, you’ll see the line written `r(t) = u + t · v` to indicate that this line is a vector-valued function of the scalar parameter t. The input t decides how many units of v you go from the starting point u to get the output r(t). 

The advantage of this kind of formula for a line is that it’s dead simple to find if you have two points on the line you can easily find the formula for the line connecting the two points. If your points are `u` and `w` then you can use `u` as the translation vector, an `w - u` as the vector that is scaled (figure 7.8)



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632831380/dd_qwu81y.gif"/>



The formula `r(t) = u + t · v` also has its downside. As you’ll see in the exercises, there are multiple ways to write the same line in this form. The extra parameter t also makes it harder to  solve equations because there is one extra unknown variable.


$$
r(t) = \vec{u} + t \cdot \vec{v} \\

line = \\ 
y=3x-6 = \\
(x,y)=(2,0)+t*(1,3)
$$


---

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632830449/l_drfgg4.gif"/>



Let’s look at some alternative formulas with other advantages. If you recall any formula for a line from high school, it is probably `y = m · x + b`. This formula is useful because it gives you a y-coordinate explicitly as a function of the x-coordinate. In this form, it’s easy to graph a line: you go through a bunch of x values, compute the corresponding y values, and put dots at the resulting (x, y) points. 

But this formula also has some limitations. Most importantly, *you **can’t** represent a vertical line*.
$$
A=\left(0,1\right) \\
B=\left(3,0\right) \\
r(t) = A + t * B \\
x = 3
$$
We’ll continue to use the parametric formula `r(t) = u + t · v` because it avoids this problem, but it would be great to have *a formula with no extra parameter t that can represent any line*. The one we use is the **standard formula**.. As an example, the line we’re looking at in the last few images can be written as `x + 2y = 8` (figure 7.9). It is the set of (x, y) points in the plane satisfying that equation. 
$$
ax + by = c
$$

$$
u = (2, 3) \\ v = (2, -1) \\
\\
r(t) = u + t*v \\
y = -1/2x + 4 \\
x + 2y = 8 \\
$$

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632830702/9F5E069C-0FDC-4FF8-A60F-92AE8D983141_eby8sm.png"/>

The form ax + by = c has no extra parameters and can represent any line. Even a vertical line can be written in this form; for instance, x = 3 is the same as 1 · x + 0 · y = 3. Any equation representing a line is called a linear equation and this, in particular, is called the standard form for a linear equation. We prefer to use it in this chapter because it makes it easy to organize our computations.  

### finding the standard form equation for a line

The formula `x + 2y = 8` is the equation for a line containing one of the segments on the example asteroid. Next, we’ll look at another one (figure 7.10) and then try to systematize finding the standard form for linear equations. Brace yourself for a bit of algebra! 

I’ll explain each of the steps carefully, but it may be a bit dry to read. You’ll have a better time if you follow along on
your own with a pencil and paper.
$$
\vec{v} = (1,5) \\
\vec{u} = (2,3) \\
\\
\text{u-to-v} = \vec{v} - \vec{u} = \vec{-1,2} \\
$$
<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632832052/dw_gaicuo.gif"/>

Knowing that all points on the line have the form `(2, 3) + t · (-1, 2)` for some t, how can we rewrite this condition to be a **standard form equation**? We need to do some algebra and, particularly, get rid of t. Because  we really have two equations to start with:  
$$
(x,y) = (2, 3) + t · (-1, 2) \\
x = 2 - t \\
y = 3 + 2t \\
\\
\text{let's manipulate both to equations equaling the same value} \\

2t = 4 - 2x \\
2t = y - 3 \\

\text{we no longer have a t and can write in standard form} \\

4 - 2x = y - 3 \\
7 - 2x = y \\
7 = y + 2x \\
\\

$$

$$
A = (x_1, y_1) \\
B = (x_2, y_2) \\ \\
\text{what is the equation of the line that passes through them (see figure 7.11)?} \\
\text{translating with A after finding steps to take to go from B to A} \\
(x,y)=(x_1,y_1)+t*(x_2-x_1,y_2-y_1) \\
\\
x=x_1+t*(x_2-x_1) \\
y=y_1+t*(y_2-y_1) \\ \\
\text{} \\
x-x_1=t*(x_2-x_1) \\
y-y_1=t*(y_2-y_1) \\ \\
\text{make both rights equal} \\ \\
x-x_1*(y_2-y_1)=t*(x_2-x_1)*(y_2-y_1) \\
y-y_1*(x_2-x_1)=t*(y_2-y_1)*(x_2-x_1) \\ \\ 
\text{equalize left side} \\ \\ 
x-x_1*(y_2-y_1)=y-y_1*(x_2-x_1) \\ \\
\text{form ax + by = c} \\ \\ 
(y_2-y_1)⋅x-(y_2-y_1)⋅x_1=(x_2-x_1)⋅y-(x_2-x_1)⋅y_1\\
[x*(y_2-y_1)] - [y * (x_2-x_1)] = [x_1*(y_2-y_1)] - [y_1*(x_2-x_1)] \\
$$

$$
\text{expand the right} \\
[x_1y_2-x_1y_1)] - [x_2y_1-x_1y_1)] \\
x_1y_2- x_1y_1 - x_2y_1 +x_1y_1 \\
x_1y_2 - x_2y_1  \\
$$

$$
[(y_2-y_1)*x] - [(x_2-x_1)*y] = x_1y_2 - x_2y_1 \\

\text{the standard form equals following} \\ \\
A = (y_2-y_1) \\
B = (x_2-x_1) \\ 
C = x_1y_2 - x_2y_1
$$

$$
\text{example laser} \\
start = (2,2) \\
end = (4,4) \\ 

\\
A = (4-2) \\
B = (4-2) \\ 
C = 2*4 - 4*2 = 0 \\
2x + 2y = 0 \\
\text{standard form} \\
x + y = 0
\text{}
$$

---

in summary given two points we can find it's standard form equation by using this formula
$$
A = (y_2-y_1) \\
B = (x_2-x_1) \\ 
C = x_1y_2 - x_2y_1
$$


### linear equation in matrix notation

After quite a bit of build-up, we’ve met our first real system of linear equations. It’s customary to write systems of linear equations in a grid like the following, so that the variables x and y line up:  
$$
x - y = 0 \\
x + 2y = 8
$$

$$
x\begin{bmatrix}
1 \\
1 
\end{bmatrix}
+
y\begin{bmatrix}
-1\\
2
\end{bmatrix} =
\begin{bmatrix}
0\\
8
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & -1\\
1 & 2
\end{bmatrix}
*
\begin{bmatrix}
x\\
y
\end{bmatrix} =
\begin{bmatrix}
0\\
8
\end{bmatrix}
$$



to solve the linear equation we should multiply by the inverse 
$$
A = \begin{bmatrix}
1 & -1\\
1 & 2
\end{bmatrix}\\
X = \begin{bmatrix}
x\\
y
\end{bmatrix}\\
B = \begin{bmatrix}
0\\
8
\end{bmatrix}\\
(A
X)*A^{-1}
=
B*A^{-1}
$$
This only a notational difference, but framing the problem in this form allows us to use pre-built tools to solve it. Specifically, Python’s NumPy library has a linear algebra module and a function that solves this kind of equation. Here’s an example:  



```python
matrix = np.array(((1,-1),(1,2)))
output = np.array((0,8)) 
intersection = np.linalg.solve(matrix,output)
# array([2.66666667, 2.66666667])
```

NumPy has told us that the x- and y-coordinates of the intersection are approximately 2⅔ or 8/3 each, which looks about right geometrically. Eyeballing the diagram, it looks like both coordinates of the intersection point should be between 2 and 3. We can check to see that this point lies on both lines by plugging it in to both equations:
$$
1x-1y=1⋅(2.66666667) -1⋅(2.66666667) =0 \\
1x+2y=1⋅(2.66666667)+2⋅(2.66666667) =8.00000001
$$
These results are close to (0, 8) and, indeed, make an exact solution. This solution vector, roughly (8/3, 8/3) is also the vector that satisfies the matrix equation.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632840752/C6DBD51D-35A6-45C7-82E4-101A2E906979_jvqxd2.png"/>

We can think of the Python function **numpy.linalg.solve** as a differently shaped machine that takes in matrices and output vectors, and returns the “solution” vectors for the linear equation they represent (figure 7.16).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632840902/01B639D1-4BF9-4523-A204-00A93BA70AA7_gf6af4.png"/>

This is perhaps the most important computational task in linear algebra: starting with a matrix `A`, and a vector `w`, and finding the vector v such that `Av = w`. Such a vector gives the solution to a system of linear equations represented by A and w. We’re lucky to have a Python function that can do this for us so we don’t have to worry about the tedious algebra required to do it by hand. We can now use this function to find out when our laser hits asteroids.  

### deciding if laser hits asteroid 

The missing piece of our game was an implementation for the `does_intersect` method on the PolygonModel class. For any instance of this class, which represents a polygon-shaped object living in our 2D game world, this method should return True if an input line segment intersects any line segment of the polygon. For this, we need a few helper functions. First, we need to convert the given line segments from pairs of endpoint vectors to linear equations in **standard form**. At the end of the section, I give you an exercise to implement the function `standard_form`, which takes two input vectors and returns a tuple `(a, b, c)` where `ax + by = c` is the line on which the segment lies. next, given two segments, each represented by its pair of endpoint vectors, we want to find out where their lines intersect. If u1 and u2 are endpoints of the first segment, and v1 and v2 are endpoints of the second, we need to first find the standard form equations and then pass them to NumPy to solve. For example,  

```python
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

# The output is the point where the two lines on which the segments lie intersect.
# But this point might not lie on either of the segments

'''
To detect whether the two segments intersect, we need to check that the intersection point of
their lines lies between the two pairs of endpoints. We can check that.
'''

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


```

### identifying unsolvable systems

Let me leave you with one final admonition: not every system of linear equations in 2D can be solved! It’s rare in an application like the asteroid game, but some pairs of linear equations in 2D don’t have unique solutions or even solutions at all. If we pass NumPy a system of linear equations with no solution, we get an exception, so we need to handle this case.

When a pair of lines in 2D are not parallel, they intersect somewhere. Even the two lines in figure 7.18 that are nearly parallel (but not quite) intersect somewhere off in the distance.  

Where we run into trouble is when the lines are parallel, meaning the lines never intersect (or they’re the same line!) as shown in figure 7.19.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632928621/6E6A210F-7365-4AE6-9FFB-741F22AE7C14_bm0y6y.png"/>

In the first case, there are zero intersection points, while in the second, there are infinitely many intersection points— every point on the line is an intersection point. Both of these cases are problematic computationally because our code demands a single, unique result. If we try to solve either of these systems with NumPy, for instance, the system consisting of `2x + y = 6` and `4x + 2y = 8`, we get an exception:  

NumPy points to the matrix as the source of the error. The matrix  
$$
\begin{bmatrix}
2 & 1 \\
4 & 2 
\end{bmatrix}
$$
is called a **singular matrix** (has no inverse and determinant is zero), meaning there is no unique solution to the linear system. A system of linear equations is defined by a matrix and a vector, but the matrix on its own is enough to tell us whether the lines are parallel and whether the system has a unique solution. For any non-zero w we pick, there won’t be a unique v that solves the system.  
$$
\begin{bmatrix}
2 & 1 \\
4 & 2 
\end{bmatrix} * v = w
$$
We’ll philosophize more about singular matrices later, but for now you can see that the rows (2,1) and (4, 2) and the columns (2, 4) and (1, 2) are both parallel and, therefore, **linearly dependent**. This is the key clue that tells us the lines are parallel and that the system does not have a unique solution. 

Solvability of linear systems is one of the central concepts in linear algebra; it closely relates to the notions of linear independence and dimension. We discuss that in the last two sections of this chapter.

For the purpose of our asteroid game, we can make the simplifying assumption that any parallel line segments don’t intersect. Given that we’re building the game with random floats, it’s highly unlikely that any two segments are exactly parallel. Even if the laser lined up exactly with the edge of an asteroid, this would be a glancing hit and the player doesn’t deserve to have the asteroid destroyed. We can modify do_segments_intersect to catch the exception and return the default result of False.



## 7.3 generalizing linear equations higher dimensions

Now that we’ve built a functional (albeit minimal) game, let’s broaden our perspective. We can represent a wide variety of problems as systems of linear equations, not just arcade games. Linear equations in the wild often have more than two “unknown” variables, x and y. Such equations describe collections of points in more than two dimensions. In more than three dimensions, it’s hard to picture much of anything, but the 3D case can be a useful mental model. Planes in 3D end up being the analogy of lines in 2D, and they are also represented by linear equations.  

### Representing planes in 3D  

To see why lines and planes are analogous, it’s useful to *think of lines in terms of dot products*. As you saw in a previous exercise, or may have noticed yourself, the equation `ax + by = c` is the set of points `(x, y)` in the 2D plane where the dot product with a fixed vector (a, b) is equal to a fixed number c. That is, the equation `ax + by = c` is equivalent to the equation `(a, b) · (x, y) = c` . In case you didn’t figure out how to interpret this geometrically in the exercise, let’s go through it here.  

If we have a point and a (non-zero) vector in 2D, there’s a unique line that is perpendicular to the vector and also passes through the point.

If we call the given point `(x0, y0)` and the given vector `(a, b)`, we can write a criterion for a point `(x, y)` to lie on the line. Specifically, if `(x, y)` lies on the line, then `(x-x0, y-y0)` is parallel to the line and perpendicular to `(a, b)` as shown in figure 7.21.  

Because two perpendicular vectors have a zero dot product, that’s equivalent to the algebraic statement:  
$$
(a,b) \cdot (x-x_0,y-y_0) = 0 \\
(a(x-x_0),b(y-y_0)) = 0 \ \or \ ax + by = ax_0 + by_0 \\
$$
The quantity on the right-hand side of this equation is a constant, so we can rename it `c`, giving us the general form equation for a line: `ax + by = c`. This is a handy geometric interpretation of the formula `ax + by = c`, and one that 

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1633181891/D916C2C4-08FA-4265-B403-855EAEBE3A5B_cwavxc.png"/>

we can generalize to 3D. Given a point and a vector in 3D, there is a unique plane perpendicular to the vector and passing through that point. If the vector is `(a, b, c)` and the point is `(x0, y0, z0)`, we can conclude that if a vector `(x, y, z)` lies in the plane, then `(x-x0, y-y0, z-z0)` is perpendicular to `(a, b, c)`.



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1633181448/95DA964D-B7F5-42B0-BF39-75C48E7D6253_pznxok.png"/>

Every point on the plane gives us such a perpendicular vector to `(a, b, c)`, and every vector perpendicular to `(a, b, c)` leads us to a point in the plane. We can express this perpendicularity as a dot product of the two vectors, so the equation satisfied by every point `(x, y, z)` in the plane is 
$$
(a, b, c) \cdot (x-x_0, y-y_0, z-z_0) = 0 \\
ax + by + cz - ax_0 - by_0 - cz_0 = 0 \\
ax + by + cz = ax_0 + by_0 + cz_0 \\
ax + by + cz = d
$$
In 3D, the computational problem is to decide where the planes intersect or which values of (x, y, z) simultaneously satisfy multiple linear equations like this.  

### solving linear equations in 3d

A pair of non-parallel lines in the plane intersects at exactly one point. Is that single intersection point true for planes as well? If we draw a pair of intersecting planes, we can see that it’s possible for non-parallel planes to intersect at many points. In fact, figure 7.23 shows there is a whole line, consisting of an infinite number of points where two non-parallel planes intersect.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1633186605/3B7A5DD6-B23E-4442-9E67-61D393137A31_ibjgut.png"/>

If you add a third plane that is not parallel to this intersection line, you can find a unique intersection point. Figure 7.24 shows that each pair among the three planes intersects along a line and the lines share a single point.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1633189019/E71BE3C2-B38A-4214-A8D5-8859BD9BF305_vpnnwd.png"/>

Finding this point algebraically requires finding a common solution to three linear equations in three variables, each representing one of the planes and having the form `ax + by + cz = d`. Such a system of three linear equations would have the form:
$$
a_1 x+b_1 y+c_1 z=d_1\\
a_2 x+b_2 y+c_2 z=d_2\\
a_3 x+b_3 y+c_3 z=d_3
$$
Each plane is determined by four numbers: ai, bi, ci, and di, where i = 1, 2, or 3 and is the index of the plane we’re looking at. Subscripts like this are useful for systems of linear equations where there can be a lot of variables that need to be named. These twelve numbers in total are enough to find the point (x, y, z) where the planes intersect, if there is one. To solve the system, we can convert the system into a matrix equation:  
$$
\begin{bmatrix}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} 
=
\begin{bmatrix}
d_1 \\
d_2 \\
d_3
\end{bmatrix}
$$
Let’s try an example. Say our three planes are given by the following equations: 
$$
x + y - z = -1  \\
2*y − z = 3 \\ 
x + z = 2
$$

```python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import matplotlib.pyplot as plt
from colors import *

def u(x, y):
    return x+y+1
def r(x, y):
    return 2*y-3
def s(x, y):
    return -x+2

def plot_scalar_field(funcs, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1, antialiased=False):
    fig = plt.figure()
    fig.set_size_inches(7, 7)
    ax = fig.gca(projection='3d')

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


plot_scalar_field([u, r, s], -5, 5, -5, 5, c=blue, cmap=None, alpha=0.5)
plt.show()

```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1633331502/Figure_1_vabgjd.png"/>

It’s not easy to see, but somewhere in there, the three planes intersect. To find that intersection point, we need the values of x, y, and z that simultaneously satisfy all three linear equations. Once again, we can convert the system to matrix form and use NumPy to solve it. The matrix
equation equivalent to this linear system is  
$$
\begin{bmatrix}
1 & 1 & -1 \\
0 & 2 & -1 \\
1 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} 
=
\begin{bmatrix}
-1 \\
3 \\
2
\end{bmatrix}
$$
Converting the matrix and vector to NumPy arrays in Python, we can quickly find the solution vector:

```python
matrix = np.array(((1, 1, -1), (0, 2, -1), (1, 0, 1)))
vector = np.array((-1, 3, 2))
print(np.linalg.solve(matrix, vector))
# [-1.  3.  3.]
```

This tells us that (-1, 3, 3) is the (x, y, z) point where all three planes intersect and the point that simultaneously satisfies all three linear equations.
While this result was easy to compute with NumPy, you can see it’s already a bit harder to visualize systems of linear equations in 3D. Beyond 3D, it’s difficult (if not impossible) to visualize linear systems, but solving them is mechanically the same. The analogy to a line or a plane in any number of dimensions is called a **hyperplane**, and the problem boils down to finding the points where multiple hyperplanes intersect.  

### studying hyperplanes algebraically

To be precise, a **hyperplane in n dimensions** is *a solution to a linear equation in n unknown variables*. A line is a 1D hyperplane living in 2D, and a plane is a 2D hyperplane living in 3D. As you might guess, a linear equation in standard form in 4D has the following form 
$$
aw + bx + cy + dz = e
$$
The set of solutions (w, x, y, z) form a region that is a 3D hyperplane living in 4D space. I need to be careful when I use the adjective 3D because it isn’t necessarily a 3D vector subspace of `ℝ4`. This is analogous to the 2D case: the lines passing through the origin in 2D are vector subspaces of `ℝ2`, but other lines are not. Vector space or not, the 3D hyperplane is 3D in the sense that there are three linearly independent directions you could travel in the solution set, like there are two linearly independent directions you can travel on any plane. I’ve included a mini-project at the end of this section to help you check your understanding of this. When we write linear equations in even higher numbers of dimensions, we’re in danger of running out of letters to represent coordinates and coefficients. To solve this, we’ll use letters with subscript indices. For instance, in 4D, we could write a linear equation in standard form as:
$$
a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4 = b
$$


Here, the coefficients are a1, a2, a3, and a4, and the 4D vector has the coordinates (x1, x2, x3, x4).  When the pattern of terms we’re summing is clear, we sometimes use an ellipsis (...) to save space. You may see equations like the previous one written a1x1 + a2x2 + ...+ a10x10 = b. Another
compact notation you’ll see involves the summation symbol (`Σ`), which is the Greek letter Sigma. If I want to write the sum of terms of the form 
$$
a_ix_i \\
\text{with the index i ranging from i = 1 to i = 10}\\
\sum_{i=1}^{10}a_ix_i=b
$$


This equation means the same thing as the earlier one: it is merely a more concise way of writing it. Whatever number of dimensions n we’re working in, the standard form of a linear equation has the same shape. 

To represent a system of m linear equations in n dimensions, we need even more indices. Our array of constants on the left-hand side of the equals sign can be denoted aij, where the subscript i indicates which equation we’re talking about and the subscript j indicates which coordinate (xj) the constant is multiplied by. For example,  
$$
a_{11}x_1 + a_{12}x_2 + … + a_{1nxn} = b_{1}\\
a_{21}x_1 + a_{22}x_2 + … + a_{2nxn} = b_{2}\\
…\\
a_{m1}x_1 + a_{m2}x_2 + … + a_{mn}x_n = bm
$$
You can see that I also used the ellipsis to skip equations three through m-1 in the middle. There are *m equations* and *n constants* in each equation, so there are **m*n constants of the form aij in total**. On the right-hand side, there are **m constants** in total, one per equation: b1, b2, …, bm.
Regardless of the number of dimensions (the same as the number of unknown variables) and the number of equations, we can represent such a system as a linear equation. The previous system with n unknowns and m equations can be rewritten as shown in figure 7.26.  
$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n}x_1 \\
a_{21} & a_{22} & \dots & a_{2n}x_1 \\
\dots & \dots & \ddots  & \dots \\
a_{m1} & a_{m2} & \dots & a_{mn}x_1 
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_3
\end{bmatrix} 
=
\begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_m
\end{bmatrix}
$$

### counting dimensions, equations and solutions

We saw in both 2D and 3D that it’s possible to write linear equations that don’t have a solution, or at least not a unique one. How will we know if a system of m equations in n unknowns is solvable? In other words, *how will we know if m hyperplanes in n-dimensions have a unique intersection point?* We’ll discuss this in detail in the last section of this chapter, but there’s one important conclusion we can draw now. 

- In 2D, a pair of lines can intersect at a single point. They won’t always (for instance, if the lines are parallel), but they can. The algebraic equivalent to this statement is that a system of two linear equations in two variables can have a unique solution. 
- In 3D, three planes can intersect at a single point. Likewise, this is not always the case, but three is the minimum number of planes (or linear equations) required to specify a point in 3D. With only two planes, you have at least a 1D space of possible solutions, which is the line of  intersection. 
- Algebraically, this means you need two linear equations to get a unique solution in 2D and three linear equations to get a unique solution in 3D. 
- *In general, you need n linear equations to be able to get a unique solution in n-dimensions.*

Here’s an example when working in 4D with the coordinates (x1, x2, x3, x4), which can seem overly simple but is useful because of how concrete it is. Let’s take 

- our first linear equation to be `x4 = 0`. The solutions to this linear equation form a 3D hyperplane, consisting of vectors of the form `(x1, x2, x3, 0)`. This is clearly a 3D space of solutions, and it turns out to be a vector subspace of `ℝ4` with basis `(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)`. 
- A second linear equation could be `x2 = 0`. The solutions of this equation on its own are also a 3D hyperplane. 
- The intersection of these two 3D hyperplanes is a 2D space, consisting of vectors of the form `(x1, 0, x3, 0)`, which satisfy both equations. If we could picture such a thing, we would see this as a 2D plane living in 4D space. Specifically, it is the plane spanned by `(1, 0, 0, 0)` and `(0, 0, 1, 0)`.
- Adding one more linear equation, `x1 = 0`, which defines its own hyperplane
- the solutions to all three equations are now a 1D space. The vectors in this 1D space lie on a line in 4D, and have the form `(0, 0, x3, 0)`. This line is exactly the x3-axis, which is a 1D subspace of `ℝ4`. 
- Finally, if we impose a fourth linear equation, `x3 = 0`, the only possible solution is (0, 0, 0, 0), a zero-dimensional vector space. The statements x4 = 0, x2 = 0, x1 = 0, and x3 = 0 are, in fact, linear equations, but these are so simple they describe the solution exactly: `(x1, x2, x3, x4) = (0, 0, 0, 0)`. Each time we add an equation, we reduced the dimension of the solution space by one, until we got a **zero-dimensional space** consisting of the single point `(0, 0, 0, 0)`.

Had we chosen different equations, each step would not have been as clear; we would have to test whether each successive hyperplane truly reduces the dimension of the solution space by one. For instance, if we started with `x1 = 0` and `x2 = 0` we would have reduced the solution set to a 2D space, but then adding another equation to the mix `x1 + x2 = 0` there is no effect on the solution space. Because x1 and x2 are already constrained to be zero, the equation `x1 + x2 = 0` is automatically satisfied. This third equation, therefore, adds no more specificity to the solution set. In the first case, four dimensions with three linear equations to satisfy left us with a 4 - 3 = 1 dimensional solution space. But in the second case, three equations described a less specific 2D solution space. 

If you have n dimensions (n unknown variables) and n linear equations, it’s possible there’s a unique solution—a zero-dimensional solution space—but this is not always the case. More generally, if you’re working in n dimensions, *the lowest dimensional solution space you can get with m linear equations is n - m*. In that case, we call the system of **linear equations independent**.

Every basis vector in a space gives us a new independent direction we can move in the space. Independent directions in a space are sometimes called degrees of freedom: the z direction, for instance, “freed” us from the plane into larger 3D space. By contrast, every independent linear
equation we introduce is a constraint: it removes a degree of freedom and restricts the space of solutions to have a smaller number of dimensions. When the number of independent degrees of freedom (dimensions) equals the number of independent constraints (linear equations), there are no longer any degrees of freedom, and we are left with a unique point. This is a major philosophical point in linear algebra, and one you can explore more in some mini projects that follow. In the final section of this chapter, we’ll connect the concepts of independent equations and (linearly) independent vectors.  

