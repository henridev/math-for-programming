# 3: Ascending to 3d

## 1: vectors in 2d space

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629694520/Untitled_Diagram_1_zrpkf3.png" width=700/>

### radians

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629696379/Untitled_Diagram-Page-2_bamtit.png"/>


- radian = unit of angle measure 
- 1 rad = 57.3°
- pi = circumference / diameter => 1 unit in diameter added is pi units in circumference added
- 360° = 2pi rad
- ° to rad => ° * (pi / 180°)
-  rad to ° => rad * (180° / pi)

> what is 30° in radians
>
> 360° / 12 = 2pi rad / 12
>
> 30° = pi/6 rad

## 2. vector arithmetic in 3d 

![image-20210823091848001](https://res.cloudinary.com/dri8yyakb/image/upload/v1629703150/image-20210823091848001_pnz5xc.png)
$$
A = (a,b,c) \\ B = (d,e,f) \\ S = scalar\\


\text{addition of 3d vector} = (a+d, b+e, c+f) \\ 

\text{subtraction of 3d vector} = (a-d, b-e, c-f) \\ \text{ displacement to go from B to A}  \\

\text{scalar of 3d vector} = (a * S, b * S, c * S) \\ 

\text{length of 3d vector} = \sqrt{(\sqrt{x^2+y^2})^{2} + z^{2}} \\
= \sqrt{x^{2} +y^{2} + z^{2}}
$$

```python
def add(*vectors):
    return tuple(map(sum,zip(*vectors)))
def scalar(*vectors, scalar):
    return [(x*scalar,y*scalar,x*scalar) for (x,y,x) in vectors]
def sub(*vectors):
    min_vectors = [(x*-1,y*-1,z*-1) for (x,y,z) in vectors[1:]] 
    min_vectors.insert(0, vectors[0])
    return tuple(map(sum,zip(*min_vectors)))
def length_3d_point(point):
    length_in_2d = sqrt(point[0]**2 + point[1]**2)
    return sqrt(length_in_2d**2 + point[2]**2)
def length_point(v):
    return sqrt(sum([coord ** 2 for coord in v]))

```



## 3. dot product for measuring vector alignment


$$
\vec{u} = (u_1,u_2) \\
\vec{v} = (v_1,v_2) \\
\text{dot product => } u \cdot v \\
\text{cross product => } u \times v \\
\\

u \cdot v =

\begin{bmatrix}
u_1\\
u_2
\end{bmatrix}
\cdot
\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} 

= (u_1 * v_1) + (u_2 * v_2)\\
= \cos{(\theta)} * |\vec{v}| * |\vec{u}| \\ 
\\
\text{hoek tussen 2 vectoren gebasseerd op 2 vector coordinaten} \\
 \theta=\arccos{(\frac{(u \cdot v)}{(|\vec{v}| * |\vec{u}|)})} 
$$

- cross product 
  - means that you project v on to u and multiply the length of this projection with the length of v
  - 3 options
    - negative = vectors point in opposite directions
    - positive = vectors point in the same direction 
    - 0 = vectors are perpendicular
  - the projection can be interpreted as followed

> <img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629710208/Untitled_Diagram-dot-product_xrmvb4.png"/>
>
> <img src="https://qph.fs.quoracdn.net/main-qimg-234168ed4b95aa311a4cd1d8985253e7" style="zoom:67%;" />
>
> ```python
> from draw2d import * ;
> 
> # dot product equals the sum of the products of point coordinates
> def dot(u,v):
>     return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])
> 
> def length(v):
>     return sqrt(v[0]**2 + v[1]**2)
> 
> def to_polar(vector, inRadians = True):
>     x = vector[0]
>     y = vector[1]
>     angle = atan2(y,x)
>     return (length(vector), angle if inRadians else degrees(angle))
> 
> def to_cartesian(v, inRadians = True):
>     (length, degrees) = v
>     return (length * cos(degrees), length * sin(degrees)) if inRadians else (length * cos(radians(degrees)), length * sin(radians(degrees)))
> 
> 
> 
> A = (4,2)
> B = (2,3)
> (lengte_b, hoek_b) = to_polar(B)
> (lengte_a, hoek_a) = to_polar(A)
> angle_a_to_b = hoek_b - hoek_a
> 
> print(f'lengte_b = {lengte_b}, hoek_b = {hoek_b}')
> print(f'lengte_a = {lengte_a}, hoek_a = {hoek_a}')
> print(f'angle_a_to_b = {angle_a_to_b}')
> 
> projectie_lengte = cos(angle_a_to_b) * lengte_b
> projectie_vector = to_cartesian((projectie_lengte,hoek_a))
> 
> print(f'projectie_vector = {list(projectie_vector)}, projectie_lengte = {projectie_lengte}')
> 
> 
> dot_product_via_projection = projectie_lengte * lengte_a
> dot_product_via_formula = dot(A,B)
> dot_product_coords_via_projection = to_cartesian((dot_product_via_projection, hoek_a))
> dot_product_coords_via_formula= to_cartesian((dot_product_via_formula, hoek_a))
> 
> print(f'dot_product_coords_via_projection = {list(dot_product_coords_via_projection)}, dot_product_via_projection = {dot_product_via_projection}')
> print(f'dot_product_coords_via_formula = {list(dot_product_coords_via_formula)}, dot_product_via_formula = {dot_product_via_formula}')
> 
> draw2d(
>     Arrow2D(*[projectie_vector], color = gray),
>     Arrow2D(*[dot_product_coords_via_projection], color = blue),
>     Arrow2D(*[dot_product_coords_via_formula], color = purple),
>     Arrow2D(*[A]),
>     Arrow2D(*[B], color=green),
> )
> 
> '''
> lengte_b = 3.605551275463989, hoek_b = 0.982793723247329
> lengte_a = 4.47213595499958, hoek_a = 0.4636476090008061
> angle_a_to_b = 0.519146114246523
> projectie_vector = [2.8, 1.4], projectie_lengte = 3.1304951684997055
> dot_product_coords_via_projection = [12.521980673998822, 6.260990336999411], dot_product_via_projection = 14.0
> dot_product_coords_via_formula = [12.521980673998822, 6.260990336999411], dot_product_via_formula = 14
> '''
> ```
>
> ```python
> def lengths_angles_to_dot(length1, length2 ,angle = 0, in_radians = True):
>     length1 * length2 * cos(angle if in_radians else radians(angle))
> 
> def angle_between_coords(v1, v2, in_radians = True):
>     dot_product = dot(*[v1, v2])
>     length_v1 = sqrt(v1[0]**2+v1[1]**2)
>     length_v2 = sqrt(v2[0]**2+v2[1]**2)
>     angle_radians = acos(dot_product / (length_v1 * length_v2))
>     return angle_radians if in_radians else degrees(angle_radians)
> ```
>
> 

## 4. cross-product: measuring oriented area

- similar to the dot product in that the lengths and relative directions of the input vectors determine the output
- different in that the output has not only a magnitude but also a direction. 



What I didn’t announce clearly was that the positive z direction was up instead of down.  

In other words, if we look at the x,y plane from the usual perspective, we would see the positive
z-axis emerging out of the plane toward us. The other choice we could make is sending the
positive z-axis away from us (figure 3.29).  

The difference here is not a matter of perspective; the two choices represent different
orientations of 3D space, and they are distinguishable from any perspective. Suppose we are
floating at some positive z-coordinate like the stick figure on the left in figure 3.29. We should
see the positive y-axis positioned a quarter-turn counterclockwise from the positive x-axis;
otherwise, the axes are arranged in the wrong orientation.

Plenty of things in the real world have orientations and don’t look identical to their mirror images.
For instance, left and right shoes have identical size and shape but different orientations. A plain
coffee mug does not have an orientation: we cannot look at two pictures of an unmarked coffee
mug and decide if they are different. But as figure 3.30 shows, two coffee mugs with graphics
on opposite sides are distinguishable.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629733351/8ECF5BBD-8ADF-4932-8D19-CF8E0B093642_i3hueh.png"/>



The readily available object most mathematicians use to detect orientation is a hand. Our hands
are oriented objects, so we can tell right hands from left hands even if they were unluckily
detached from our bodies. 

Mathematicians can use their hands to distinguish the two possible orientations of coordinate axes, and they call the two possibilities right-handed and left-handed orientations. Here’s the rule as illustrated in
figure 3.32: if you point your right index finger along the positive x-axis and curl your remaining
fingers toward the positive y-axis, your thumb tells you the direction of the positive z-axis.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629733805/93CD120A-BB79-4345-BF2A-4CD26B80A108_gdbzti.png"/>

This is called the **right-hand rule**, and if it agrees with your axes, then you are (correctly!) using
the right-handed orientation. Orientation matters! If you are writing a program to steer a drone
or control a laparoscopic surgery robot, you need to keep your ups, downs, lefts, rights,
forwards, and backwards consistent. The cross product is an oriented machine, so it can help
us keep track of orientation throughout all of our computations.  

### finding the direction of the cross product

this is the visualisation => Given two input vectors, the cross product outputs a result that is perpendicular to both. For instance, if u = (1,0,0) and v = (0,1,0), then it happens that the cross product u × v is (0, 0, 1)

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629733936/5C77F173-8192-4B71-9541-96DF35F111DD_o5nsjf.png"/>

In fact, as figure 3.34 shows, any two vectors in the x,y plane have a cross product that lies
along the z-axis.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629734049/959B5999-5ACB-423C-9752-C28CA4AFD555_jqdkif.png"/>



This makes it clear why the cross product doesn’t work in 2D: it returns a vector that lies outside
of the plane containing the two input vectors. We can see the output of the cross product is
perpendicular to both inputs even if they don’t lie in the x,y plane (figure 3.35).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629734116/53B8857D-44BB-4529-82D8-AEE3E8FC2FA8_rqwuxt.png"/>

Two possible perpendicular directions => the cross product selects only one. 

Here’s where **orientation** comes in: the cross product obeys the right-hand rule as well. Once
you’ve found the direction perpendicular to two input vectors u and v, the cross product u × v
lies in a direction that puts the three vectors u, v, and u × v in a right-handed configuration.
That is, we can point our right index finger in the direction of u, curl our other fingers toward v,
and our thumb points in the direction of u × v (figure 3.36).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629734338/B31C89C1-6112-4617-BE9D-A100B4DDE2B1_jlyzen.png"/>

Like the dot product, the length of the cross product is a number that gives us information about
the **relative position** of the input vectors. 

- Instead of measuring how aligned two vectors are, 
- it tells us something closer to “how perpendicular they are.” More precisely, it tells us how big of
  an area its two inputs span (figure 3.37).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629734460/869FF1F1-76A8-4C6A-998A-25E34F13B059_dvqpis.png"/>

The parallelogram bounded by u and v as in figure 3.37 has an area that is the same as the
length of the cross product u × v. For two vectors of given lengths, 

- they span the most area if they are perpendicular. 
- On the other hand, if u and v are in the same direction, they don’t span any area; the cross product has zero length. This is convenient: we can’t choose a unique perpendicular direction if the two input vectors are parallel.

Paired with the direction of the result, the length of the result gives us an exact vector. Two
vectors in the plane are guaranteed to have a cross product pointing in the +z or -z direction.
We can see in figure 3.38 that the bigger the parallelogram that the plane vectors span, the
longer the cross product.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629734652/C0001C9A-08C7-4619-9B46-AFC59F3D311C_jabnfr.png"/>

There’s a trigonometric formula for the area of this parallelogram: if u and v are separated by
an angle θ, the area is 
$$
|u| \cdot |v| \cdot \sin(θ)
$$


We can put the length and direction together to see some simple cross products. For instance, what is the cross product of (0, 2, 0) and (0, 0, -2)? These vectors lie on the y- and z-axes, respectively, so to be perpendicular to both, the cross product must lie on the x-axis. Let’s find the direction of the result using the right-hand rule. Pointing in the direction of the first vector with our index finger (the positive y direction) and bending our fingers in the direction of the second vector (the negative z direction), we find our  

thumb is in the negative x direction. The magnitude of the cross product is 2 ∙ 2 ∙ sin(90°)
because the y- and z-axes meet at a 90° angle. (The parallelogram happens to be a square in
this case, having a side length of 2). This comes out to 4, so the result is (-4, 0, 0): a vector of
length 4 in the -x direction.

It’s nice to convince ourselves that the cross product is a well-defined operation by computing
it **geometrically**. But that’s not practical, in general, when vectors don’t always lie on an axis
and it’s not obvious what coordinates you need to find a perpendicular result. Fortunately,
there’s an explicit formula for the coordinates of the cross product in terms of the coordinates
of its inputs  



### computing the cross product of 3d vectors

$$
u = (u_x, u_y, u_z) \\
v = (v_x, v_y, v_z) \\
\\
u \times v = (u_yv_z - u_zv_y, u_zv_x - v_zu_x, u_xv_y - u_yv_x)
$$

<img src="https://lh3.googleusercontent.com/proxy/YeJIdnI8hzXhrzGWA-gxuUpdgVvqi5WPnSVGRRspkPrOoGKbjE26zyicWe7FIbiRnc0x6SHZjovSoKRIA8y3PQtxevEacUftizU57bpaOD8woBat99_H7d7OfTjPecFtF2_-LdGZjRP2MISNoy1IhvglWfUHfg"/>



You can test-drive this formula in the exercises. Note that in contrast to most of the formulas
we used so far, this one doesn’t appear to generalize well to other dimensions. It requires that
the input vectors have exactly three components.
This algebraic procedure agrees with the geometric description we built in this chapter. Because
it tells us area and direction, the cross product helps us decide whether an occupant of 3D space
would see a polygon floating in space with them. For instance, as figure 3.39 shows, an observer
standing on the x-axis would not see the parallelogram spanned by u = (1, 1, 0) and v = (-2,
1, 0)  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629736588/AE74306D-674B-4293-9554-313D959E7860_vdsvfn.png"/>

In other words, the polygon in figure 3.39 is parallel to the observer’s line of sight. Using the
cross product, we could tell this without drawing the picture. Because the cross product is
perpendicular to the person’s line of sight, none of the polygon is visible.
Now it’s time for our culminating project: building a 3D object out of polygons and drawing it
on a 2D canvas. You’ll use all of the vector operations you’ve seen so far. In particular, the cross
product will help you to decide which polygons are visible.  