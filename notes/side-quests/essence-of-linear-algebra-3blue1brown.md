# 3Blue1Brown: Essence of linear algebra

1. vectors
2. linear combinations spans and basis vectors
3. matrices and linear transformations
4. Matrix multiplication as composition
5. Three dimensional transformations
6. Determinant



## 1: Vectors



<img src="https://docs.driveworkspro.com/TopicImages/KnowledgeBase/Vector.png"/>



**Magnitude**: This is a synonym for “length.” We can also think about this as “how far we’ve traveled.”

**Direction:** Unlike our point, our line actually moves towards a certain direction.



## 2: linear combinations / spans and basis vectors

$$
\text{conditions of linear vector transformation}\\
T:\R^n \rightarrow \R^m \\
L.T. \iff  \vec{a}, \vec{b} \in \R^n \\
T(\vec{a} + \vec{b}) = T(\vec{a}) + T(\vec{b}) \\
T(c*\vec{a}) = c*T(\vec{a}) \\
$$

```python
'''
result (8, 3), vut (8, 3)
uscaled_t (6, 2), ut_scaled (6, 2)
'''

v = (3, 2)
u = (2, 1)
i_hat = (1, 0)
j_hat = (1, 1)
transformation = (i_hat, j_hat)

scaling_factor = 2

def transform_2d(vector, transformation):
    (i_hat, j_hat) = transformation
    (x, y) = vector
    return add(*[scale(x, i_hat), scale(y, j_hat)]) 

ut = transform_2d(u, transformation)
vt = transform_2d(v, transformation)
# T(v) + T(u)
result = add(*[ut, vt])

vu = add(*[v,u])
# T(v+u)
vut = transform_2d(vu, transformation)

print(f'result {result}, vut {vut}')


# T(cu)
u_scaled = scale(scaling_factor, u)
uscaled_t = transform_2d(u_scaled, transformation) 

# cT(u)
ut_scaled = scale(scaling_factor, ut)

print(f'uscaled_t {uscaled_t}, ut_scaled {ut_scaled}')
```

$$
\text{proof that the transformation of the sum of vectors equals the sum of the transformed vectors} \\

T(\begin{bmatrix}
     x_1 \\
     x_2 \\
\end{bmatrix} ) = \begin{bmatrix}
     x_1 + x_2 \\
     3x_1 \\
\end{bmatrix} \\

\vec{a} = \begin{bmatrix}
     a_1 \\
     a_2 \\
\end{bmatrix} 
\
\vec{b} = \begin{bmatrix}
     b_1 \\
     b_2 \\
\end{bmatrix}  \\

\vec{a} + \vec{b} =  \begin{bmatrix}
     a_1 + b_1 \\
     a_2 + b_2 \\
\end{bmatrix} \\

\text{the transformation of the sum} \rightarrow
T{(\begin{bmatrix}
     a_1 + b_1 \\
     a_2 + b_2 \\
\end{bmatrix})} =
\begin{bmatrix}
    (a_1 + b_1) + (a_2 + b_2) \\
     3(a_2 + ab_2) \\
\end{bmatrix}  =
\begin{bmatrix}
     a_1 + a_2 + b_1 + b_2 \\
     3a_2 + 3b_2 \\
\end{bmatrix}

\\ \\ 
\text{the sum of the transformation} \rightarrow
T{(\begin{bmatrix}
     a_1 \\
     a_2 \\
\end{bmatrix})} + T{(\begin{bmatrix}
     b_1 \\
     b_2 \\
\end{bmatrix})} =
\begin{bmatrix}
    (a_1 + a_2) \\
     3a_2 \\
\end{bmatrix}+\begin{bmatrix}
    (b_1 + b_2) \\
     3b_2 \\
\end{bmatrix}  =
\begin{bmatrix}
    a_1 + a_2 + b_1 + b_2 \\
    3a_2 + 3b_2 \\
\end{bmatrix} \\
$$

$$
\text{proof that the transformation of the scaled vector equals the scale of the transformed vectors} \\

c = 2 \\

c * \vec{a} = \begin{bmatrix}
     2a_1 \\
     2a_2 \\
\end{bmatrix} \\

\text{transformation of the scaled vector} \rightarrow \ T(\begin{bmatrix}
     2a_1 \\
     2a_2 \\
\end{bmatrix}) = \begin{bmatrix}
     2a_1 + 2a_2 \\
     6a_2 \\
\end{bmatrix} \\ 

\text{scale of transformed vector} \rightarrow \ c * T(\begin{bmatrix}
     a_1 \\
     a_2 \\
\end{bmatrix}) = 2 \begin{bmatrix}
     a_1 + a_2 \\
     3a_2 \\
\end{bmatrix} = \begin{bmatrix}
     2a_1 + 2a_2 \\
     6a_2 \\
\end{bmatrix}
$$


$$
\hat{i} =  

\begin{bmatrix}
     1 \\
     0 \\
\end{bmatrix} 

\ \ \ \

\hat{j} =  

\begin{bmatrix}
     0 \\
     1 \\
\end{bmatrix} \\

\vec{v} =  

\begin{bmatrix}
     v_x \\
     v_y \\
\end{bmatrix} 

= v_x * \hat{i} + v_y * \hat{j}
$$



```python
i_hat = (1,0)
j_hat = (0,1)
vector = (3,2)

def transform_2d_via_basis_vectors(vector, transformation):
    (i_hat, j_hat) = transformation
    (x, y) = vector
    return add(*[scale(x, i_hat), scale(y, j_hat)]) 

vector_via_basis_vectors =  transform_2d_via_basis_vectors(vector, (i_hat,j_hat))

print('the vector can be interpreted as the sum of the basis vector i scaled by x and the basis vector j scaled by y')
print('this interpretation is called the linear combination')

print('SPAN = all reachable linear combinations with a set of vectors')
print('BASIS = Set of lineary independent vectors describing the span of the full space')
print('all possible vectors can be reached with the linear combination as long as they don\'t point in the same direction')


draw2d(
    Arrow2D(i_hat, color=green),
    Arrow2D(j_hat, color=red),
    Arrow2D(vector, color=blue),
    Arrow2D(vector_via_basis_vectors, color=blue),
);
```



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629816913/438BDCAE-1E56-40C0-BB98-868FE5BA694B_ndx09m.png"/>

```python
# with two vectors we can cover an entire plain in 3d space

u = (3,4,2)
v = (4,-2,3)

u_options = [(u[0] * i, u[1] * i, u[2] * i) for i in np.arange(-10,10, 0.1)]
v_options = [(v[0] * i, v[1] * i, v[2] * i) for i in np.arange(-10,10, 0.1)]

result = [add(*[u,v]) for (u, v) in zip(u_options, v_options)]
result_2 = [add(*[u,v]) for (u, v) in zip(u_options, reversed(v_options))] 

points_u = [Points3D(pnt, color=green) for pnt in u_options]
points_v = [Points3D(pnt, color=blue) for pnt in v_options]
points_result = [Points3D(pnt, color=red) for pnt in result]
points_result_2 = [Points3D(pnt, color=red) for pnt in result_2]

surface = Polygon3D(*[
    add(*[u_options[0],v_options[-1]]),
    add(*[u_options[0],v_options[0]]),
    add(*[u_options[-1],v_options[0]]),
    add(*[u_options[-1],v_options[-1]]),
  ],
  color=purple
)

draw3d(
    *points_u,
    *points_v,
    surface
);
```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629817647/B43B8C6D-7C64-4999-9B87-0369A4415CED_bk2vj9.png"/>



## 3: matrices and linear transformations

> this provides us with an intuitive explanation for matrix multiplication

$$
\begin{bmatrix}
     a \ \ b  \\
     c \ \ d \\
\end{bmatrix} 

*

\begin{bmatrix}
     x \\
     y \\
\end{bmatrix} 

= 

\begin{bmatrix}
     ax + by \\
     cx + dy \\
\end{bmatrix} 


\ \ \ \ \ \ \ \

\text{movement by } \hat{i} = \begin{bmatrix}
     a  \\
     c  \\
\end{bmatrix} 

\ \ \

\text{movement by } \hat{j} = \begin{bmatrix}
     b  \\
     d  \\
\end{bmatrix}  \\
$$

linear transformation properties

- lines remain lines
- origin stays fixed
- gridlines remain parallel and evenly spaced



a transformation can take place by only using the linear transformation with the transformed î and ĵ
$$
\hat{i} = \begin{bmatrix}
     a \\
     c \\
\end{bmatrix} 

\ \

\hat{j} = \begin{bmatrix}
     b \\
     d \\
\end{bmatrix} 

\\

x * \hat{i} + y * \hat{j} = 

\begin{bmatrix}
     ax \\
     cx \\
\end{bmatrix} 

+ 

\begin{bmatrix}
     by \\
     dy \\
\end{bmatrix} =

\begin{bmatrix}
     ax + by \\
     cx + dy \\
\end{bmatrix} \rightarrow

\text{ the same as vector multiplication }
$$
as long as we track  î and ĵ in a transformation we can deduce all other vectors as a result of the transformation.

we will only need 4 numbers to describe any transformation in 2d space.

```python
dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

shearI = (1,0)
shearJ = (1,1) # putting the j hat at this coord is called a sheer tranformation

def transform_2d_vectors(transformation, *vectors):
    (i_hat, j_hat) = transformation
    return [add(scale(x, i_hat), scale(y, j_hat)) for (x, y) in  vectors]

shearTransformedDino = transform_2d_vectors((shearI, shearJ), *dino_vectors)


draw2d(
    Points2D(*dino_vectors),
    Polygon2D(*dino_vectors),
    Points2D(*shearTransformedDino, color=red),
    Polygon2D(*shearTransformedDino, color=red),
)
```

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629818795/911EABFF-D24A-437C-9D3F-A9B2067AD76A_p4xseo.png"/>



`linear transformations are entirly determined by where the basis vectors are taken`

`this is because any vector can be described as a scaled combination of the basis vectors `

> multiplying a matrix by a vector is applying that transformation to that vector



## 4: Matrix multiplication as composition

- multiplication of 2 matrices means applying transformation a and then b. 
- in matrix multiplication the matrix on the right is applied before the one on the left

$$
\begin{bmatrix}
     0 & 2\\
     1 & 0\\ 
 \end{bmatrix} \\
 \begin{bmatrix}
     1 &-2\\
     1 & 0\\ 
 \end{bmatrix} \ = 
 \begin{bmatrix}
     ? & ?\\
     ? & ?\\ 
 \end{bmatrix} \
$$


$$
\hat{i} =  

\begin{bmatrix}
     1 \\
     1  \\
\end{bmatrix} 

\ \ \ \

\hat{j} =  

\begin{bmatrix}
     -2 \\
     0 \\
\end{bmatrix} \\

\text{multiply matrix of M2 by the vector (1, 1) => first i hat transformation}\\

\begin{bmatrix}
     0 \ \ 2\\
     1  \ \ 0\\ 
 \end{bmatrix} \hat{i} =
 \begin{bmatrix}
     0 \ \ 2\\
     1  \ \ 0\\ 
 \end{bmatrix}
 \begin{bmatrix}
     1 \\
     1  \\
\end{bmatrix} =

1*\begin{bmatrix}
     0 \\
     1  \\
\end{bmatrix} +
1*\begin{bmatrix}
     2 \\
     0  \\
\end{bmatrix} = 
\begin{bmatrix}
     2 \\
     1  \\
\end{bmatrix}\\

\text{multiply matrix of M2 by the vector (-2, 0) => first j hat transformation}\\


\begin{bmatrix}
     0 \ \ 2\\
     1  \ \ 0\\ 
 \end{bmatrix} \hat{j} =
 \begin{bmatrix}
     0 \ \ 2\\
     1  \ \ 0\\ 
 \end{bmatrix}
 \begin{bmatrix}
     -2 \\
     0  \\
\end{bmatrix} =

-2*\begin{bmatrix}
     0 \\
     1  \\
\end{bmatrix} +
0*\begin{bmatrix}
     2 \\
     0  \\
\end{bmatrix} = 
\begin{bmatrix}
    0 \\
     -2  \\
\end{bmatrix}\\


\text{this gives us respectively the first and second column of the composition matrix}\\

\\

\begin{bmatrix}
    2 \ \ \ \ \ \  \ 0 \\
    1 \ \ -2  \\
\end{bmatrix}\\
$$

$$
\begin{bmatrix}
    a \ \ b \\
    c \ \ d  \\
\end{bmatrix}\\
\begin{bmatrix}
    e \ \ f \\
    g \ \ h  \\
\end{bmatrix}\\ = 
\begin{bmatrix}
    (a*e+b*g) \ \ (a*f+b*h) \\
    (c*e+d*g) \ \ (c*f+d*h)  \\
\end{bmatrix}
$$

$$
\hat{i} = \begin{bmatrix}
    e  \\
    g  \\
\end{bmatrix}

\\


\begin{bmatrix}
    a \ \ b \\
    c \ \ d  \\
\end{bmatrix}
\begin{bmatrix}
    e  \\
    g  \\
\end{bmatrix} = 

e
\begin{bmatrix}
    a \\
    c \\
\end{bmatrix}

+ 

g
\begin{bmatrix}
    b  \\
    d  \\
\end{bmatrix}
= \text{left column of composition}
\\

\hat{j} = \begin{bmatrix}
    f  \\
    h  \\
\end{bmatrix}

\\


\begin{bmatrix}
    a \ \ b \\
    c \ \ d  \\
\end{bmatrix}
\begin{bmatrix}
    f  \\
    h  \\
\end{bmatrix} = 

f
\begin{bmatrix}
    a \\
    c \\
\end{bmatrix}

+ 

h
\begin{bmatrix}
    b  \\
    d  \\
\end{bmatrix}
= \text{right column of composition}
\\


\begin{bmatrix}
    (a*e+b*g) & (a*f+b*h) \\
    (c*e+d*g) & (c*f+d*h)  \\
\end{bmatrix}
$$



```python
rotateI = (-1,0)
rotateJ = (0,1) 

shearI = (1,0)
shearJ = (1,1)

'''
|-1 0|  |1 1|
|0  1|  |0 1|
'''

def apply_transformation(i_hat, j_hat, coord):
    (x,y) = coord
    return add(scale(x, i_hat), scale(y, j_hat))

# long form of transformation 
# apply first transformation to all vertices
# apply second transformation to all vertices

dinoRotated = [apply_transformation(rotateI, rotateJ, coord) for coord in  dino_vectors]
dinoRotatedAndSheer = [apply_transformation(shearI, shearJ, coord) for coord in  dinoRotated]


# short form of transformation
# combine the transformations into one matrix 
# then apply that matrix to all vertices


def combine_transformations(transformation_first, transformation_second):
    (i_hat, j_hat) = transformation_first
    (i_hat_2, j_hat_2) = transformation_second

    first_column = apply_transformation(i_hat_2, j_hat_2, i_hat)
    second_column = apply_transformation(i_hat_2, j_hat_2, j_hat)
    return (first_column, second_column)


(composition_i, composition_j) = combine_transformations((rotateI, rotateJ), (shearI, shearJ))

dinoComposition = [apply_transformation(composition_i, composition_j, coord) for coord in  dino_vectors]

draw2d(
    Points2D(*dinoComposition, color=green),
    Polygon2D(*dinoComposition, color=green),
)
```



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629876051/960E7EF9-4356-441D-ABB9-C75B442367D3_nd2aij.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629876051/8A53D4C6-A76A-4CD6-80B4-C44EB663E6FD_b46dil.png"/>



## 5: Three dimensional transformations

we need to add one extra unit vector k̂ along the z-axis.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629877032/C3C5A9DC-CEB8-440A-8F87-EA06804D0FFA_lbrase.png" style="zoom:67%;" />

> green = i | red= j | blue = k

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
$$

let's say we apply the transformation visualized below, this will give us the following basis vectors.

which we can represent in total as a 3x3 matrix.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1629877290/DB672F04-218B-4837-BFAD-F1A426F29560_sffpq5.png"/>

$$
\hat{i} = \begin{bmatrix}
    1 \\
    0 \\
    -1 \\
\end{bmatrix} \

\hat{j} = \begin{bmatrix}
    1 \\
    1 \\
    0 \\
\end{bmatrix} \ 

\hat{k} = \begin{bmatrix}
    1 \\
    0 \\
    1 \\
\end{bmatrix} \\

\hat{ijk} = \begin{bmatrix}
    1 & 1 & 1  \\
    0 & 1 & 0 \\
    -1 & 0 & 1 \\
\end{bmatrix} \\
$$

a vector can be thought of just like in 2d as the following:

multiply the coordinates with corresponding columns of the transformation matrix


$$
\vec{v} = 

\begin{bmatrix}
    x \\
    y \\
    y \\
\end{bmatrix}

= x\hat{i} + y\hat{j} + z\hat{k}
$$
an example of matrix multiplication
$$
\begin{bmatrix}
    0 & -2 & 2 \\
    5 & 1 & 5\\
    1 & 4 & -1\\
\end{bmatrix} \\
\begin{bmatrix}
    0 & 1 & 2 \\
    3 & 4 & 5\\
    6 & 7 & 8\\
\end{bmatrix}
$$

$$
\text{column 1 = } \begin{bmatrix}
    0 & -2 & 2 \\
    5 & 1 & 5\\
    1 & 4 & -1\\
\end{bmatrix} * \vec{v}_{\hat{i}} 
= \begin{bmatrix}
    0 \\
    5 \\
    1 \\
\end{bmatrix} 0 +
\begin{bmatrix}
    -2 \\
    1 \\
    4 \\
\end{bmatrix}3 +
\begin{bmatrix}
    2 \\
    5 \\
    -1 \\
\end{bmatrix}6 
= \begin{bmatrix}
	0 \\
	0 \\
	0 \\
\end{bmatrix}
+
\begin{bmatrix}
    -6 \\
    3 \\
    12 \\
\end{bmatrix}
+
\begin{bmatrix}
    12 \\
    30 \\
    -6 \\
\end{bmatrix}
=
\begin{bmatrix}
    6 \\
    33 \\
    6 \\
\end{bmatrix}
\\

\text{column 2 = } \begin{bmatrix}
    0 & -2 & 2 \\
    5 & 1 & 5\\
    1 & 4 & -1\\
\end{bmatrix} * \vec{v}_{\hat{j}} 
= \begin{bmatrix}
    0 \\
    5 \\
    1 \\
\end{bmatrix} 1 +
\begin{bmatrix}
    -2 \\
    1 \\
    4 \\
\end{bmatrix}4 +
\begin{bmatrix}
    2 \\
    5 \\
    -1 \\
\end{bmatrix}7 =

\begin{bmatrix}
    0 \\
    5 \\
    1 \\
\end{bmatrix} +
\begin{bmatrix}
    -8 \\
    4 \\
    16 \\
\end{bmatrix} +
\begin{bmatrix}
    14 \\
    35 \\
    -7 \\
\end{bmatrix} =
\begin{bmatrix}
    6 \\
    44 \\
    10 \\
\end{bmatrix}
\\

\text{column 3 = } \begin{bmatrix}
    0 & -2 & 2 \\
    5 & 1 & 5\\
    1 & 4 & -1\\
\end{bmatrix} * \vec{v}_{\hat{i}} 
= \begin{bmatrix}
    0 \\
    5 \\
    1 \\
\end{bmatrix}2 +
\begin{bmatrix}
    -2 \\
    1 \\
    4 \\
\end{bmatrix}5 +
\begin{bmatrix}
    2 \\
    5 \\
    -1 \\
\end{bmatrix}8 =

\begin{bmatrix}
    0 \\
    10 \\
    2 \\
\end{bmatrix}
+
\begin{bmatrix}
    -10 \\
    5 \\
    20 \\
\end{bmatrix}
+
\begin{bmatrix}
    16 \\
    40 \\
    -8 \\
\end{bmatrix}

=

\begin{bmatrix}
    6 \\
    55 \\
    14 \\
\end{bmatrix}
\\

\begin{bmatrix}
    6 & 6 & 6\\
    33 & 44 & 55 \\
    6 & 10 & 14 \\
\end{bmatrix}
$$

```python
m1 = (
    (0,5, 1), (-2, 1, 4), (2, 5, -1)
)

m2 = (
    (0, 3, 6), (1, 4, 7), (2, 5, 8)
)

m3 = (
    (0, 1, 0), (0, 2, 3), (4, 5, 3)
)

m4 = (
    (6,), (3,)
)

m5 = (
    (2, 6), (-3, -5), (2, 1)
)

m6 = (
    (-6, -3, 4), (2, 5, 5)
)

def scale(scalar,v):
    return tuple(scalar * coord for coord in v)

def add(*vectors):
    return tuple(map(sum,zip(*vectors)))

def matrice_multiplier(*matrices):
    row_length_first_transform = len(matrices[-1][0])
    column_length_next_transform = len(matrices[-2])
    if row_length_first_transform != column_length_next_transform:
        ValueError(f'inaproriate matrix dimensions first transform rows {row_length_first_transform} and second transform columns {column_length_next_transform}')
    

    result = tuple(add(*[scale(coor,matrices[-2][i]) for i, coor in enumerate(ht)]) for  ht in matrices[-1])
    print(*list(result), sep='\n')

    if len(matrices) > 2:
        return matrice_multiplier(*[matrices[-3], result])

    return result

matrice_multiplier(*[m1, m2, m3])
matrice_multiplier(*[m4, m5, m6])
```



## 6: Determinant

every grid square undergoes the same **scaling factor** change in surface because of a specific transformation

**scaling factor** = **determinant** of a transformation

- a scaling factor becomes negative if the orientation of space gets inverted 
- absolute value shows the factor by which the area scaled
- in 3d the scaling of the volume in stead of the surface is given
- in 3d the orientation is flipped if the right hand rule is not applicable


$$
\det(\begin{bmatrix}
    \textcolor{blue}a & \textcolor{red}b \\
    \textcolor{blue}c & \textcolor{red}d\\
\end{bmatrix}) = \textcolor{blue}a\textcolor{red}d - \textcolor{red}b\textcolor{blue}c
$$
the intuition behind the formula
$$
\det(\begin{bmatrix}
    \textcolor{blue}a & \textcolor{red}0 \\
    \textcolor{blue}0 & \textcolor{red}d\\
\end{bmatrix}) = \textcolor{blue}a\textcolor{red}d - \textcolor{red}0\textcolor{blue}0 \\

\text{a gives us the stretch in x and d the stretch in y} \\

\det(\begin{bmatrix}
    \textcolor{blue}a & \textcolor{red}b \\
    \textcolor{blue}0 & \textcolor{red}d\\
\end{bmatrix}) = \textcolor{blue}a\textcolor{red}d - \textcolor{red}b\textcolor{blue}0 \\

\text{this gives us a parallelogram with base a and height d} \\

\det(\begin{bmatrix}
    \textcolor{blue}a & \textcolor{red}b \\
    \textcolor{blue}c & \textcolor{red}d\\
\end{bmatrix}) = \textcolor{blue}a\textcolor{red}d - \textcolor{red}b\textcolor{blue}c \\

\text{b * c gives us how much the area is cramped down diagonal} \\
$$