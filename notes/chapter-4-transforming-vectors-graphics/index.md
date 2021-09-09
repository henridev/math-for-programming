# 4: transforming vectors and graphics

This chapter covers

- Transforming and drawing 3D objects by applying mathematical functions

- Creating computer animations using transformations to vector graphics

- Identifying linear transformations, which preserve lines and polygon

- Computing the effects of linear transformations on vectors and 3D models


With the techniques from the last two chapters and a little creativity, you can render any 2D or
3D figure you can think of. Whole objects, characters, and worlds can be built from line segments and polygons defined by vectors. But, there’s still one thing standing in between you and your first feature-length, computer-animated film or life-like action video game

=> you need to be able to draw objects that change over time = Animation

works the same way for computer graphics as it does for film: you render static
images and then display dozens of them every second. When we see that many snapshots of a
moving object, it looks like the image is continuously changing. In chapters 2 and 3, we looked
at a few mathematical operations that take in existing vectors and transform them geometrically

to output new ones. By chaining together sequences of small transformations, we can create
the illusion of continuous motion.

As a mental model for this, you can keep in mind our examples of rotating 2D vectors. You saw
that you could write a Python function, rotate, that took in a 2D vector and rotated it by, say,
45° in the counterclockwise direction. As figure 4.1 shows, you can think of the rotate function
as a machine that takes in a vector and outputs an appropriately transformed vector.  

```python
def to_cartesian(polar_vector):
    print(polar_vector)
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)

def rotate_2(angle, vectors):
    i_hat_length, i_hat_angle = to_polar((1.0, 0.0))
    i_hat_new = to_cartesian((i_hat_length, (i_hat_angle + angle)))
    j_hat_length, j_hat_angle = to_polar((0.0, 1.0))
    j_hat_new = to_cartesian((j_hat_length, (j_hat_angle + angle)))
    return [add(scale(v[0], i_hat_new), scale(v[1], j_hat_new)) for v in vectors]

def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a+angle)) for l, a in polars]

# rotate one counterclockwise
print(rotate(pi/4, [(1, 1), (2, 3)]))
print(rotate_2(pi/4, [(1, 1), (2, 3)]))

```

## linear transformation

- The “well-behaved” vector transformations of focus are linear transformations. 

- Along with vectors, linear transformations are the other main objects of study in linear algebra.
- Linear transformations are special transformations where vector arithmetic looks the same before and after the transformation. 

### Preserving vector arithmetic 

The two most important arithmetic operations on vectors are addition and scalar multiplication. 

- sum of two vectors as the new vector we arrive at when we place them tipto-tail, or as the vector to the tip of the parallelogram they define. 

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631002206/DD0CF735-9ABA-40DD-84E2-4A9B2A3A7C7F_wj60vz.png"/>

#### properties of linear transformations 

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631002391/024D069F-6127-43A8-AC5B-14DEE540977A_lkajwo.png"/>


$$
\text{conditions of linear vector transformation}\\

T:\R^n \rightarrow \R^m \\

L.T. \iff \vec{a}, \vec{b} \in \R^n \\

T(\vec{a} + \vec{b}) = T(\vec{a}) + T(\vec{b}) \\

T(c*\vec{a}) = c*T(\vec{a}) \\

\text{def: transformations preserving scalar multiplication and vector addition}\\
\text{are dubbed linear transformations}
$$
here is an example of a non linear transformation

```python
def add_two(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def non_linear_transformation(v):
    return tuple((coor**2 for coor in v))

def linear_transformation(v, angle=pi/4):
    result = vectors.rotate(angle, [v])
    return result[0]

v = (1, -1)
u = (2, 3)

sum_u_v = add_two(v, u)


linear_transformation_after_sum = linear_transformation(sum_u_v)

linear_transformation_befor_sum_u = linear_transformation(u)
linear_transformation_befor_sum_v = linear_transformation(v)
sum_u_v_after_linear_transformation = add_two(linear_transformation_befor_sum_v, linear_transformation_befor_sum_u)


draw(
    Arrow(v, color=colors.red),
    Arrow(u, color=colors.orange),
    Arrow(linear_transformation_after_sum, color=colors.purple),
    Arrow(sum_u_v_after_linear_transformation, color=colors.blue),
)


non_linear_transformation_after_sum = non_linear_transformation(sum_u_v)

non_linear_transformation_befor_sum_u = non_linear_transformation(u)
non_linear_transformation_befor_sum_v = non_linear_transformation(v)
sum_u_v_after_non_linear_transformation = add_two(non_linear_transformation_befor_sum_u, non_linear_transformation_befor_sum_v)


draw(
    Arrow(v, color=colors.red),
    Arrow(u, color=colors.orange),
    Arrow(non_linear_transformation_after_sum, color=colors.purple),
    Arrow(sum_u_v_after_non_linear_transformation, color=colors.blue),
)
```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631007729/81A4C7D4-3EAE-4807-98D9-2882CA0D4556_aqiyqq.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631007838/CE0161D1-0F8A-43AF-ACD6-CD57C3F2CB6A_wivgqe.png"/>

It turns out that for a transformation to be linear, it must not move the origin => (0, 0) has to stay at (0, 0)

Translation by any non-zero vector transforms the origin, which ends up at a
different point, so it cannot be linear.

Other examples of linear transformations include reflection, projection, shearing, and any 3D
analogy of the preceding linear transformations. 

These are defined in the exercises section and you should convince yourself with several examples that each of these transformations preserves vector addition and scalar multiplication. With practice, you can recognize which transformations are linear and which are not. Next, we’ll look at why the special properties of linear transformations are useful.  

### why linear transformations

Because linear transformations preserve vector sums and scalar multiples, they also preserve a
broader class of vector arithmetic operations. The most general operation is called a **linear**
**combination**. 

A linear combination of a collection of vectors is a sum of scalar multiples of them. For instance, one linear combination of two vectors u and v would be 
$$
3u - 2v \\
0.5u - v + 6w
$$
Because linear transformations preserve vector sums and scalar multiples, these preserve linear
combinations as well.  

We can restate this fact algebraically. If you have a collection of n vectors, v1, v2, …, vn, as well
as any choice of n scalars, s1, s2, s3, …, sn, a linear transformation T preserves the linear
combination:
$$
T(s_1v_1 + s_2v_2 + s_3v_3 + … + s_nv_n) = s_1T(v_1) + s_2T(v_2) + s_3T(v_3) + … + s_nT(v_n)
$$

One easy-to-picture linear combination we’ve seen before is 
$$
\frac{1}{2} u + \frac{1}{2} v \\
= \\
\frac{1}{2} (u + v)
$$
this linear combination of two vectors gives us the midpoint of the line segment connecting them.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631008457/BB748B31-BB8B-494D-B48A-C81DB9AAF859_cmcsqx.png"/>

This means linear transformations send midpoints to other midpoints: for example, T(½ u + ½
v) = ½ T(u) + ½ T(v), which is the midpoint of the segment connecting T(u) and T(v) as figure
4.25 shows.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631008781/2B67DBC3-F678-451F-86E7-37797453F6A7_gqjcxt.png" style="zoom: 100%;" />

It’s less obvious, but a linear combination like 0.25u + 0.75v also lies on the line segment
between u and v (figure 4.26). Specifically, this is the point 75% of the way from u to v.
Likewise, 0.6u + 0.4v is 40% of the way from u to v, and so on.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631008829/C6AE26AD-8E8C-4304-9A49-E2459C4D4288_rqx6rv.png" style="zoom:80%;" />

In fact, every point on the line segment between two vectors is a “weighted average” like this,
having the form

```python
def add_two(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def scale(scalar, v):
    return tuple(scalar * coord for coord in v)

def points_between(u, v, steps = 10):
    points = []
    s_frac = 1 / steps
    for i in range(1, steps):
        s = s_frac * i
        u_weighted = scale(s, u)
        v_weighted = scale((1 - s), v)
        points.append(add_two(u_weighted,v_weighted))
    return points

v = (1, -1)
u = (2, 3)


draw(
    Arrow(v, color=colors.red),
    Arrow(u, color=colors.orange),
    Points(*points_between(u,v)) 
)

```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631009507/E7089AF0-765D-4997-893F-ECDE73EABDAE_k6dsjg.png" style="zoom:50%;" />

Any point on the line segment connecting u and v is a weighted average of u and v, so it has
the form
$$
s · u + (1 - s) · v
$$
A linear transformation, T, transforms u and v to some new vectors T(u) and T(v). The point on the line segment is transformed to some new point 
$$
T(s · u + (1 - s) · v) \\ \or \\ s · T(u) + (1 - s) · T(v)
$$


This is, in turn, a weighted average of T(u) and T(v), so it is a point that lies on the segment connecting T(u) and T(v)

```python
v = (1, -1)
u = (2, 3)

tuv = [linear_transformation(point) for point in points_between(u,v)]

tu  = linear_transformation(u)
tv  = linear_transformation(v)


draw(
    Arrow(tv, color=colors.red),
    Arrow(tu, color=colors.orange),
    Points(*points_between(tu,tv, steps=20)),
    Points(*tuv, color=colors.red) 
)

```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631010497/80CD5771-EEDC-428C-9B32-9A60FD91B237_cqpqom.png"/>

Because of this, a linear transformation T takes every point on the line segment connecting u
and v to a point on the line segment connecting T(u) and T(v). This is a key property of linear
transformations: **they send every existing line segment to a new line segment.** Because our 3D
models are made up of polygons and polygons are outlined by line segments, linear
transformations can be expected to preserve the structure of our 3D models to some extent
(figure 4.29).  

By contrast, if we use the non-linear transformation , we can see that line segments are distorted. This means that a triangle defined by vectors u, v, and w is not really sent to another triangle defined \

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631016968/A1EE32A9-FBF0-4E0B-B8CE-E322BDDE5AEE_rit8uj.png" style="zoom:67%;" />

In summary:

- linear transformations respect the algebraic properties of vectors, preserving
  sums, scalar multiples, and linear combinations. 
- They respect the geometric properties of collections of vectors, sending line segments and polygons defined by vectors to new ones defined by the transformed vectors.
- linear transformations are not only special from a geometric perspective; they’re also easy to compute.  

### computing linear transformations

you saw how to break 2D and 3D vectors into components. eg
$$
\vec{x} = (4, 0, 0)\\
\vec{y} = (0, 3, 0)\\
\vec{z} = (0, 0, 5)\\
(4,3,5)=\vec{x}+\vec{y}+\vec{z}
$$

it easy to picture how far the vector extends in each of the three dimensions of the space that
we’re in. We can decompose this even further into **standard basis vectors** and then make a **linear combination**. the scalars in this linear combination correspond exactly to vector v
$$
\hat{i} = \begin{bmatrix}
    1 \\
    0 \\
    0 \\
\end{bmatrix} \

\hat{j} = \begin{bmatrix}
    0 \\
    1 \\
    0 \\
\end{bmatrix} \ 

\hat{k} = \begin{bmatrix}
    0 \\
    0 \\
    1 \\
\end{bmatrix} \\

\vec{v} = 

\begin{bmatrix}
    x \\
    y \\
    y \\
\end{bmatrix}

= x\hat{i} + y\hat{j} + z\hat{k} \\

\begin{bmatrix}
    4 \\
    3 \\
    5 \\
\end{bmatrix} = 4 \cdot \hat{i} + 3 \cdot \hat{j} + 5 \cdot \hat{k}
$$
<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631082361/82793DD3-AC92-4798-9A90-F1501663A0C6_jbnkp5.png"/>

We’ve only written the same vectors in a slightly different way, but it turns out this change in perspective makes it easy to compute linear transformations. Because **linear transformations** respect **linear combinations**, all we need to know to compute a linear transformation is how it affects standard basis vectors.

> transformations can take place by only adjusting the standard basis vectors (ref. 3blue1brown)

$$
\text{Say we know nothing about a 2D vector transformation T}\\
\text{except that it is linear and we know what } T(\hat{i})\text{ and } T(\hat{j}) \text{ are.}\\
\text{with this information we know where to find } T(\vec{v}) \\

T(v) = T(3\hat{i} + 2\hat{j}) = 3T(\hat{i}) + 2T(\hat{j})\\
\text{Because we already know where } T(\hat{i}), T(\hat{j}) \text{ are, we can locate T(v) }
$$

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631082921/1649753D-5888-45AE-8D97-9F35EAB6C4D5_gy1nki.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631082921/06B7544F-77DE-4E62-8F7E-7072D4D93F33_wmykeg.png"/>

To make this more concrete, let’s do a complete example in 3D. Say A is a linear transformation, and all we know about A is 
$$
A(\hat{i}) = (1, 1, 1) \\
A(\hat{j}) = (1, 0, -1) \\
A(\hat{k}) = (0, 1, 1) \\
 \\
\vec{v} = (-1, 2, 2) \\
A(\vec{v}) = -1A(\hat{i}) + 2A(\hat{j})  + 2A(\hat{k})
$$
The takeaway here is that a 

- 2D linear transformation T is defined completely by the values of T(i_hat) and T(j_hat): that’s two vectors or four numbers in total
- 3D linear transformation T is defined completely by the values of T(i_hat), T(j_hat), and T(k_hat), which are three vectors or nine numbers in total. 
- In any number of dimensions, the behaviour of a linear transformation is specified by a list of vectors or an array of-arrays of numbers. Such an array-of-arrays is called a matrix, and we’ll see how to use matrices in the next chapter.  

## Summary

- Vector transformations are functions that take vectors as inputs and return vectors as
  outputs. 
- To affect a geometric transformation of the model, apply a vector transformation to every
  vertex of every polygon of a 3D model.
- You can combine existing vector transformations by composition of functions to create
  new transformations, which are equivalent to applying the existing vector transformations sequentially.
- Functional programming is a programming paradigm that emphasizes composing and,
  otherwise, manipulating functions.
- The functional operation of currying turns a function that takes multiple arguments into a function that takes one argument and returns a new function. **Currying** lets you turn existing Python functions (like scale and add) into vector transformations.
- **Linear transformations** are vector transformations that preserve vector sums and scalar
  multiples. In particular, points lying on a line segment still lie on a line segment after a linear transformation is applied.
- A **linear combination** is the most general combination of scalar multiplication and vector
  addition. Every 3D vector is a linear combination of the 3D standard basis vectors, which
  are denoted e1 = (1, 0, 0), e2 = (0, 1, 0), and e3 = (0, 0, 1). Likewise, every 2D vector
  is a linear combination of the 2D standard basis vectors, which are e1 = (1, 0) and e2 =
  (0, 1).
- **Once you know how a given linear transformation acts on the standard basis vectors, you can determine how it acts on any vector by writing the vector as a linear combination**
  **of the standard basis and using the fact that linear combinations are preserved.**
  - In 3D, three vectors or nine total numbers specify a linear transformation.
  - In 2D, two vectors or four total numbers do the same.
  - This last point is critical: linear transformations are both well-behaved and easy-tocompute with because they can be specified with so little data.  
