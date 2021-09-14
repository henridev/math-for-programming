# 5: Computing transformations with
matrices  

This chapter covers

- Writing a linear transformation as a matrix
- Multiplying matrices to compose and apply linear transformations
- Operating on vectors of different dimensions with linear transformations
- Translating vectors in 2D or 3D with matrices

linear transformations can be put into matrix form factor. in 3 form example we need a 3x3 matrix to represent the transformation
$$
T = transformation  \\
T(\vec{v}) = 
\textcolor{orange}{v_x} * \textcolor{blue}{T(\hat{i})} + 
\textcolor{orange}{v_y} * \textcolor{red}{T(\hat{j})} + 
\textcolor{orange}{v_z} * \textcolor{green}{T(\hat{k})} \\


\begin{bmatrix}
    \textcolor{blue}a & \textcolor{red}b & \textcolor{green}c \\
    \textcolor{blue}d & \textcolor{red}e & \textcolor{green}f \\
    \textcolor{blue}g & \textcolor{red}h & \textcolor{green}i \\
\end{bmatrix}
\begin{bmatrix}
    \textcolor{orange}x \\ \textcolor{orange}y \\ \textcolor{orange}z 
\end{bmatrix}
= \begin{bmatrix}
    \textcolor{blue}{ax} + \textcolor{red}{by} + \textcolor{green}{cz}\\
    \textcolor{blue}{dx} + \textcolor{red}{ey} + \textcolor{green}{fz}\\
    \textcolor{blue}{gx} + \textcolor{red}{hy} + \textcolor{green}{iz}
\end{bmatrix}
$$
an example could be “a rotation counterclockwise by 90° about the z-axis” 
$$
\begin{bmatrix}
    \textcolor{blue}0 & \textcolor{red}{-1}& \textcolor{green}0 \\
    \textcolor{blue}1 & \textcolor{red}0 & \textcolor{green}0 \\
    \textcolor{blue}0 & \textcolor{red}0 & \textcolor{green}1 \\
\end{bmatrix}
$$
Whether we think of this transformation geometrically or as described by these three vectors (or nine
numbers), we’re thinking of the same imaginary machine.



<a href="https://ibb.co/jLhDTjK"><img src="https://i.ibb.co/FB6zKdv/A8-C6-E1-D8-1-B4-B-46-AE-8304-DA80826-E908-F.png" alt="A8-C6-E1-D8-1-B4-B-46-AE-8304-DA80826-E908-F" border="0"></a>

When arranged appropriately in a grid, the numbers that tell us how to execute a linear
transformation are called a matrix. This chapter focuses on using these grids of numbers as
computational tools, so there’s more number-crunching in this chapter than in the previous
ones. Don’t let this intimidate you! When it comes down to it, we’re still just carrying out vector
transformations. A matrix lets us compute a given linear transformation using the data of what that
transformation does to standard basis vectors.
$$
T(\vec{v}) = 
\textcolor{orange}{v_x} * \textcolor{blue}{T(\hat{i})} + 
\textcolor{orange}{v_y} * \textcolor{red}{T(\hat{j})} + 
\textcolor{orange}{v_z} * \textcolor{green}{T(\hat{k})} \\
$$
 thinking of linear transformations as matrices of numbers  

## 5.1 representing linear transformations with matrices

Let’s return to a concrete example of the nine numbers that specify a 3D linear transformation. These three vectors having nine components in total contain all of the information required to specify the linear transformation T.
$$
T(\vec{v}) = 
\textcolor{orange}{v_x} * \textcolor{blue}{T(\hat{i})} + 
\textcolor{orange}{v_y} * \textcolor{red}{T(\hat{j})} + 
\textcolor{orange}{v_z} * \textcolor{green}{T(\hat{k})} \\

\\
\textcolor{blue}{\hat{i} = \begin{bmatrix}
    \textcolor{blue}1 \\ \textcolor{blue}0 \\ \textcolor{blue}0
\end{bmatrix}} \ \textcolor{red}{\hat{j}} = \begin{bmatrix}
    \textcolor{red}0 \\ \textcolor{red}1 \\ \textcolor{red}{0}
\end{bmatrix} \ \textcolor{green}{\hat{k}} = \begin{bmatrix}
    \textcolor{green}0 \\ \textcolor{green}0 \\ \textcolor{green}1 
\end{bmatrix}

\\

\textcolor{blue}{T(\hat{i})} = \begin{bmatrix}
    \textcolor{blue}1 \\ \textcolor{blue}1 \\ \textcolor{blue}1 
\end{bmatrix} \ \textcolor{red}{T(\hat{j})} = \begin{bmatrix}
    \textcolor{red}1 \\ \textcolor{red}0 \\ \textcolor{red}{-1}
\end{bmatrix} \ \textcolor{green}{T(\hat{k})} = \begin{bmatrix}
    \textcolor{green}0 \\ \textcolor{green}1 \\ \textcolor{green}1 
\end{bmatrix}

\\

\begin{bmatrix}
    \textcolor{blue}1 & \textcolor{red}1 & \textcolor{green}0 \\
    \textcolor{blue}1 & \textcolor{red}0 & \textcolor{green}1 \\
    \textcolor{blue}1 & \textcolor{red}{-1} & \textcolor{green}1 \\
\end{bmatrix}
$$

$$
T(\vec{v}) = 
\textcolor{orange}{v_x} * \textcolor{blue}{T(\hat{i})} + 
\textcolor{orange}{v_y} * \textcolor{red}{T(\hat{j})} \\

\\
\textcolor{blue}{\hat{i} = \begin{bmatrix}
    \textcolor{blue}1 \\ \textcolor{blue}0 
\end{bmatrix}} \

\textcolor{red}{\hat{j}} = \begin{bmatrix} 
    \textcolor{red}0 \\ \textcolor{red}1  
\end{bmatrix}

\\

\textcolor{blue}{T(\hat{i})} = \begin{bmatrix}
    \textcolor{blue}2 \\ \textcolor{blue}0 \\
\end{bmatrix} \ \textcolor{red}{T(\hat{j})} = \begin{bmatrix}
    \textcolor{red}0 \\ \textcolor{red}2 
\end{bmatrix}

\\

\begin{bmatrix}
    \textcolor{blue}2 & \textcolor{red}0\\
    \textcolor{blue}0 & \textcolor{red}2\\
\end{bmatrix}
$$

### multiplying a matrix with a vector

As opposed to multiplying numbers, the order matters when you multiply matrices by vectors. In this case, **Av** is a valid product but **vA** is not.  (3x3 and 3x1 works 3x1 and 3x3 does not work). We can write Python code that multiplies a matrix by a vector. Let’s say we encode the matrix A as a tuple-of-tuples and the vector v as a tuple as usual. This is a bit different from how we originally thought about the matrix A. We originally created it by combining three columns, but here A is created as a sequence of rows. The advantage of defining a matrix in Python as a tuple of rows is that the numbers are laid out in the same order as we would write them on paper. We can, however, get the columns any time we want by using
Python’s zip function (covered in appendix B):  

```python
def multiply_matrices(a, b):
    result = []
    for row in a:
        res_num = 0
        for i, num in enumerate(row):
            coor = b[i]
            res_num += (coor * num)
        result.append(res_num)
    return tuple(result)

a = (
    (0, 2, 1),
    (0, 1, 0),
    (1, 0, -1)
)

print(list(zip(*a)))
# i_hat, j_hat, k_hay (conversion into columns)
# [(0, 0, 1), (2, 1, 0), (1, 0, -1)]


v = (3, -2, 5)

print(multiply_matrices(a, v))
# (1,-2,-2)

def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]  # [(3, (0,0,1)),(-2, (2,1,0)),(5, (1,0,-1))] => [3 * (0,0,1), -2 * (2,1,0), 5 * (1,0,-1)]
    return add(*scaled)

def multiply_matrix_vector(matrix, vector):
    return linear_combination(vector, *zip(*matrix))
```

There are two other mnemonic recipes for multiplying a matrix by a vector, both of which give
the same results. To see these, let’s write a prototypical matrix multiplication: 
$$
\begin{bmatrix}
     a & b  \\
     c & d \\
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
$$

$$
\begin{bmatrix}
     a & b & c \\
     d & e & f \\
     g & h & i \\
\end{bmatrix} 

*

\begin{bmatrix}
     x \\
     y \\
     z \\
\end{bmatrix} 

= 

x \cdot \begin{bmatrix}
    a \\
    d \\
    g \\
\end{bmatrix} +
y \cdot \begin{bmatrix}
    b \\
    e \\
    h \\
\end{bmatrix} +
z \cdot \begin{bmatrix}
    c \\
    f \\
    i \\
\end{bmatrix}
= 

\\

\begin{bmatrix}
     ax + by + cz\\
     dx + ey + fz\\
     gx + hy + iz\\
\end{bmatrix}
$$

****

- The first mnemonic is that each coordinate of the output vector is a function of all the coordinates
  of the input vector. For instance, the first coordinate of the 3D output is a function f(x, y, z) =
  ax + by + cz. Moreover, this is a linear function (in the sense that you used the word in high
  school algebra); it is a sum of a number times each variable. We originally introduced the term
  “linear transformation” because linear transformations preserve lines. Another reason to use
  that term:  a linear transformation is a collection of linear functions on the input coordinates that
  give the respective output coordinates.

- The second mnemonic presents the same formula differently: the coordinates of the output
  vector are **dot products of the rows of the matrix with the target vector.** For instance, the first
  row of the 3-by-3 matrix is (a, b, c) and the multiplied vector is (x, y, z), so the first coordinate
  of the output is (a, b, c) ∙ (x, y, z) = ax + by + cz. We can combine our two notations to state
  this fact in a formula:  

$$
\begin{bmatrix}
     a & b & c\\
     d & e & f\\
     g & h & i\\
\end{bmatrix}
\begin{bmatrix}
   x \\
   y \\
   z \\
\end{bmatrix}

=

\begin{bmatrix}
     (a , b , c) \cdot (x, y, z)\\
     (d , e , f) \cdot (x, y, z)\\
     (g , h , i) \cdot (x, y, z)\\
\end{bmatrix}
=
\begin{bmatrix}
     ax + by + cz\\
     dx + ey + fz\\
     gx + hy + iz\\
\end{bmatrix}
$$

### composing linear transformations by matrix multiplication

Some of the examples of linear transformations we’ve seen so far are rotations, reflections,
rescalings, and other geometric transformations. What’s more, any number of linear transformations chained together give us a new linear transformation. 

In math terminology, the **composition of any number of linear transformations is also a linear transformation**. Because any linear transformation can be represented by a matrix, any two composed linear transformations can be as well. 

In fact, if you want to compose linear transformations to build new ones, matrices are the best tools for the job.

> NOTE: Let me take off my mathematician hat and put on my programmer hat for a moment. Suppose you want to compute the result of, say, 1,000 composed linear transformations operating on a vector. This can come up if you are animating an object by applying additional, small transformations within every frame of the animation. In Python, it would be computationally expensive to apply 1,000 sequential functions because there is computational overhead for every function call. However, **if you were to find a matrix representing the composition of 1,000 linear transformations**, you would boil the whole process down to a handful of numbers and a handful of computations.

Let’s look at a composition of two linear transformations: A(B(v)), where the matrix representations of A and B are known to be the following:
$$
A = \begin{bmatrix}
     1 & 1 & 0\\
     1 & 0 & 1\\
     1 & -1 & 1\\
\end{bmatrix} 
\\
B = \begin{bmatrix}
     0 & 2 & 1\\
     0 & 1 & 0\\
     1 & 0 & -1\\
\end{bmatrix} 
$$
Here’s how the composition works step by step. First, the transformation B is applied to v,
yielding a new vector B(v), or Bv if we’re writing it as a multiplication. Second, this vector
becomes the input to the transformation A, yielding a final 3D vector as a result: A(Bv). Once
again, we’ll drop the parentheses and write A(Bv) as the product ABv. Writing this product out
for v = (x, y, z) gives us a formula that looks like this:  
$$
ABv = \begin{bmatrix}
     1 & 1 & 0\\
     1 & 0 & 1\\
     1 & -1 & 1\\
\end{bmatrix} 
\begin{bmatrix}
     0 & 2 & 1\\
     0 & 1 & 0\\
     1 & 0 & -1\\
\end{bmatrix} 
\begin{bmatrix}
     x \\
     y \\
     z \\
\end{bmatrix}
$$
If we work right to left, we know how to evaluate this. Now I’m going to claim that we can work
left to right as well and get the same result. Specifically, we can ascribe meaning to the product
matrix AB on its own; it will be a new matrix (to be discovered) representing the composition of
the linear transformations A and B:  
$$
\begin{bmatrix}
     \textcolor{blue}{1} & \textcolor{blue}{1} & \textcolor{blue}{0}\\
     \textcolor{green}{1} & \textcolor{green}{0} & \textcolor{green}{1}\\
     \textcolor{red}{1} & \textcolor{red}{-1} & \textcolor{red}{1}\\
\end{bmatrix} 
\begin{bmatrix}
     0 & 2 & 1\\
     0 & 1 & 0\\
     1 & 0 & -1\\
\end{bmatrix}=
\begin{bmatrix}
     \textcolor{blue}{?} & \textcolor{blue}{?} & \textcolor{blue}{?}\\
     \textcolor{green}{?} & \textcolor{green}{?} & \textcolor{green}{?}\\
     \textcolor{red}{?} & \textcolor{red}{?} & \textcolor{red}{?}\\
\end{bmatrix}
$$

$$
first \ column \\
0 
\begin{bmatrix}
     1 \\
     1 \\
     1 \\
\end{bmatrix} 
+
0 
\begin{bmatrix}
     1 \\
     0 \\
     -1 \\
\end{bmatrix} 
+
1 
\begin{bmatrix}
     0 \\
     1 \\
     1 \\
\end{bmatrix} 
=
\begin{bmatrix}
     0 \\
     1 \\
     1 \\
\end{bmatrix} 
\\
second \ column \\
2
\begin{bmatrix}
     1 \\
     1 \\
     1 \\
\end{bmatrix} 
+
1 
\begin{bmatrix}
     1 \\
     0 \\
     -1 \\
\end{bmatrix} 
+
0 
\begin{bmatrix}
     0 \\
     1 \\
     1 \\
\end{bmatrix} = 

\begin{bmatrix}
     3 \\
     2 \\
     1 \\
\end{bmatrix}
\\
third \ column \\
1
\begin{bmatrix}
     1 \\
     1 \\
     1 \\
\end{bmatrix} 
+
0
\begin{bmatrix}
     1 \\
     0 \\
     -1 \\
\end{bmatrix} 
+
-1 
\begin{bmatrix}
     0 \\
     1 \\
     1 \\
\end{bmatrix} = 

\begin{bmatrix}
     1 \\
     0 \\
     0 \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
     \textcolor{blue}{0} & \textcolor{blue}{3} & \textcolor{blue}{1}\\
     \textcolor{green}{1} & \textcolor{green}{2} & \textcolor{green}{0}\\
     \textcolor{red}{1} & \textcolor{red}{1} & \textcolor{red}{0}\\
\end{bmatrix}
$$

That’s how we do matrix multiplication. You can see there’s nothing to it besides carefully composing linear operators. Similarly, you can use mnemonics instead of reasoning through this  

process each time. Because multiplying a 3-by-3 matrix by a column vector is the same as doing three dot products, multiplying two 3-by-3 matrices together is the same as doing nine dot products—all possible dot products of rows of the first matrix with columns of the second
$$
(1,1,0) \cdot (0,0,1) = 1\cdot0 + 1\cdot0 + 0 \cdot 1 = 0 \\
(1,0,1) \cdot (0,0,1) = 1\cdot0 + 0\cdot0 + 1\cdot1 = 1 \\
(1,-1,1) \cdot (0,0,1) = 1\cdot0 + -1\cdot0 + 1\cdot1 = 1 \\
\\
(1,1,0) \cdot (2,1,0) = 1\cdot2 + 1\cdot1 + 0\cdot0 = 3 \\
(1,0,1) \cdot (2,1,0)= 1\cdot2 + 0\cdot1 + 1\cdot0 = 2 \\
(1,-1,1) \cdot (2,1,0) = 1\cdot2 + -1\cdot1 + 1\cdot0 = 1 \\
\\
(1,1,0) \cdot (1,0,-1) = 1\cdot1 + 1\cdot0 + 0\cdot-1 = 1 \\
(1,0,1) \cdot (1,0,-1) = 1\cdot1 + 0\cdot0 + 1\cdot-1 = 0 \\
(1,-1,1) \cdot (1,0,-1) = 1\cdot1 + -1\cdot0 + 1\cdot-1 = 0 \\
$$

### 3D animation with matrix transformations  

- To animate a 3D model => the original model is recalculated to new matrix formations each frame.
- To make the model appear to move or change over time, we need to use different   transformations as time progresses. If these transformations are linear transformations specified by matrices, we need a new matrix for every new frame of the animation.
- Because PyGame’s built-in clock keeps track of time (in milliseconds), one thing we can do is to
  generate matrices whose entries depend on time. In other words, instead of thinking of every
  entry of a matrix as a number, we can think of it as a function that takes the current time, t,
  and returns a number (figure 5.3).  

$$
\begin{bmatrix}
     \textcolor{blue}{a} & \textcolor{blue}{b} & \textcolor{blue}{c}\\
     \textcolor{green}{d} & \textcolor{green}{e} & \textcolor{green}{f}\\
     \textcolor{red}{g} & \textcolor{red}{h} & \textcolor{red}{i}\\
\end{bmatrix} 

\rightarrow

\begin{bmatrix}
     \textcolor{blue}{sin(t)} & \textcolor{blue}{0} & \textcolor{blue}{-sin(t)}\\
     \textcolor{green}{0} & \textcolor{green}{1} & \textcolor{green}{0}\\
     \textcolor{red}{sin(t)} & \textcolor{red}{0} & \textcolor{red}{cos(t)}\\
\end{bmatrix}
$$

As we covered in chapter 2, cosine and sine are both functions that take a number and return
another number as a result. The other five entries happen to not change over time, but if you
crave consistency, you can think of these as constant functions (as in f(t) = 1 in the center
entry). Given any value of t, this matrix represents the same linear transformation as rotate_y_by(t). Time moves forward and the value of t increases, so if we apply this matrix
transformation to each frame, we’ll get a bigger rotation each time.

Let’s give our `draw_model` function (covered in appendix C and used extensively in chapter 4) a
`get_matrix`keyword argument, where the value passed to get_matrix is a function that takes
time in milliseconds and returns the transformation matrix that should be applied at that time.
In the source code file, animate_teapot.py, I call it like this to animate the rotating teapot from
chapter 4:  


$$
\begin{bmatrix}
     \textcolor{blue}{1.3} & \textcolor{blue}{-0.7}\\
     \textcolor{green}{6.5} & \textcolor{green}{3.2}\\
\end{bmatrix} 
\begin{bmatrix}
     \textcolor{blue}{-2.5}\\
     \textcolor{green}{0.3}\\
\end{bmatrix}
=
\\
$$

$$
-2.5
\begin{bmatrix}
     \textcolor{blue}{1.3}\\
     \textcolor{green}{6.5}\\
\end{bmatrix}
+
0.3
\begin{bmatrix}
     \textcolor{blue}{-0.7}\\
     \textcolor{green}{3.2}\\
\end{bmatrix}

=

\begin{bmatrix}
     \textcolor{blue}{-3.25}\\
     \textcolor{green}{-16.25}\\
\end{bmatrix}
+
\begin{bmatrix}
     \textcolor{blue}{-0.21}\\
     \textcolor{green}{3.2}\\
\end{bmatrix}

= 

\begin{bmatrix}
     \textcolor{blue}{-3.46}\\
     \textcolor{green}{-15.29}\\
\end{bmatrix}
$$



## 5.2 interpreting matrices from different shapes

The matrix_multiply function doesn’t hard-code the size of the input matrices, so we can use
it to multiply either 2-by-2 or 3-by-3 matrices together. As it turns out, it can also handle
matrices of other sizes as well. For instance, it can handle these two 5-by-5 matrices:

There’s no reason we shouldn’t take this result seriously—our functions for vector addition,
scalar multiplication, dot products, and, therefore, matrix multiplication don’t depend on the
dimension of the vectors we use. Even though we can’t picture a 5D vector, we can do all the
same algebra on five tuples of numbers that we did on pairs and triples of numbers in 2D and
3D, respectively. In this 5D product, the entries of the resulting matrix are still dot products of
rows of the first matrix with columns of the second (figure 5.5):  


$$
\begin{bmatrix}
     \textcolor{blue}{-1} & \textcolor{blue}{0} & \textcolor{blue}{-1} & \textcolor{blue}{-2} & \textcolor{blue}{2}\\
     \textcolor{green}{0} & \textcolor{green}{0} & \textcolor{green}{2} & \textcolor{green}{-2} & \textcolor{green}{1}\\
     \textcolor{red}{-2} & \textcolor{red}{-1} & \textcolor{red}{-2} & \textcolor{red}{0} & \textcolor{red}{1}\\
     \textcolor{orange}{0} & \textcolor{orange}{2} & \textcolor{orange}{-2} & \textcolor{orange}{-1} & \textcolor{orange}{0}\\
     \textcolor{purple}{1} & \textcolor{purple}{1} & \textcolor{purple}{-1} & \textcolor{purple}{-1} & \textcolor{purple}{0}\\
\end{bmatrix}
\begin{bmatrix}
     \textcolor{blue}{2} & \textcolor{green}{0} & \textcolor{red}{0} & \textcolor{orange}{-1} & \textcolor{purple}{2}\\
     \textcolor{blue}{-1} & \textcolor{green}{-2} & \textcolor{red}{-1} & \textcolor{orange}{-2} & \textcolor{purple}{0}\\
     \textcolor{blue}{0} & \textcolor{green}{1} & \textcolor{red}{2} & \textcolor{orange}{2} & \textcolor{purple}{-2}\\
     \textcolor{blue}{2} & \textcolor{green}{-1} & \textcolor{red}{-1} & \textcolor{orange}{1} & \textcolor{purple}{0}\\
     \textcolor{blue}{2} & \textcolor{green}{1} & \textcolor{red}{-1} & \textcolor{orange}{-1} & \textcolor{purple}{-2}\\
\end{bmatrix}

=

\begin{bmatrix}
     -10 & -1 & 2 & -7 & 4\\
     -2 & 5 & 5 & 4 & -6\\
     -1 & 1 & -4 & 2 & -2\\
     -4 & -5 & -5 & -9 & 4\\
     -1 & -2 & -2 & -6 & 4\\
\end{bmatrix}
$$

$$
\text{let's say we take the only 4 of the resulting matrix} \\
\text{column 4 and row 2} \\
\text{row 2 means take \textcolor{green}{row 2} of the first} \\
\text{column 4 means take \textcolor{orange}{column 4} of the second} \\
\text{the dot product of both gives us the number 4}
$$

### column vectors as matrices 

Let’s return to the example of multiplying a matrix by a column vector. I already showed you
how to do a multiplication like this, but we treated it as its own case with the
multiply_matrix_vector function. It turns out matrix_multiply is capable of doing these
products as well, but we have to write the column vector as a matrix. As an example, let’s pass
the following square matrix and single-column matrix to our matrix_multiply function:  
$$
C = \begin{bmatrix}
    \textcolor{blue}{-1} & \textcolor{red}{-1} & \textcolor{green}0 \\
    \textcolor{blue}{-2} & \textcolor{red}1 & \textcolor{green}2 \\
    \textcolor{blue}1 & \textcolor{red}{0} & \textcolor{green}{-1} \\
\end{bmatrix}\\
D =\begin{bmatrix}
     1 \\
     1 \\
     1 \\
\end{bmatrix}
$$
I claimed before that you can think of a vector and a single-column matrix interchangeably, so
we might encode d as a vector (1,1,1). But this time, let’s force ourselves to think of it as a
matrix, having three rows with one entry each. Note that we have to write (1,) instead of (1) to
make Python think of it as a 1-tuple instead of as a number.  

```
c = ((-1, -1, 0), (-2, 1, 2), (1, 0, -1))
d_single_tuple = (-2,1, 0)
d_column_vector = ((-2,),(1,),(0,))
d_row_vector = ((-2,1,0),)

matrix_multiply(c,d_single_tuple) # error
matrix_multiply(c,d_row_vector) # error
matrix_multiply(c,d_column_vector) # all good 
```

This demonstrates that multiplying a matrix and a column vector is a special case of matrix
multiplication. We don’t need a separate function multiply_matrix_vector after all. We can
further see that the entries of the output are dot products of the rows of the first matrix with
the single column of the second (figure 5.6).  

On paper, you’ll see vectors represented interchangeably as tuples (with commas) or as column
vectors. But for the Python functions we’ve written, the distinction is critical. 

If you’ve seen this comparison in math class, you may have thought it was a pedantic notational
distinction. Once we represent these in Python, however, we see that they are really three
distinct objects that need to be treated differently. While these all represent the same geometric
data, which is a 3D arrow or point in space, only one of these, the column vector, can be  

multiplied by a 3-by-3 matrix. The row vector doesn’t work because, as shown in figure 5.7, we
can’t take the dot product of a row of the first matrix with a column of the second.  

For our definition of matrix multiplication to be consistent, we can only multiply a matrix on the
left of a column vector. This prompts the general question posed by the next section.  

### what pairs of matrices can be multiplied

We can make grids of numbers of any dimension. When can our matrix multiplication formula
work, and what does it mean when it does? The answer is that the number of columns of the first matrix has to match the number of rows of the second. 

In this language, we can make a general statement about the shapes of matrices that can be
multiplied: you can only multiply an n-by-m matrix by a p-by-q matrix if m = p. When that is
true, the resulting matrix will be a n-by-q matrix. For instance, a 17x9 matrix cannot be
multiplied by a 6x11 matrix. However, a 5x8 matrix can be multiplied by an 8x10 matrix. Figure
5.11 shows the result of the latter, which is a 5x10 matrix.  

### viewing square and non square matrices as vector functions

We can think of a 2x2 matrix as the data required to do a given linear transformation of a 2D
vector. Pictured as a machine in figure 5.12, this transformation takes a 2D vector into its input
slot and produces a 2D vector out of its output slot as a result.  

It’s fair to think of matrices as machines that take vectors as inputs and produce vectors as outputs. Figure 5.13, however, shows a matrix can’t take just any vector as input: it is a 2x2 matrix so it does a linear transformation of 2D vectors. Correspondingly, this matrix can only  be multiplied by a column vector with two entries. Let’s split up the machine’s input and output slots to suggest that these take and produce 2D vectors or pairs of numbers.  Likewise, a linear transformation machine (figure 5.14) powered by a 3x3 matrix can only take in 3D vectors and produce 3D vectors as a result.  



> they perform a dot product row by row



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631544801/88E4B2E4-CD13-4FED-974A-2C33D394A651_foh6k3.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631544893/B550CE3F-F1DD-435A-8F9C-B7345DBC9F93_mpeonq.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631544887/4BCEBAE6-76AC-4039-9131-136E63ADD04B_sq16f7.png"/>

Now we can ask ourselves, what would a machine look like if it were powered by a non-square
matrix? Perhaps the matrix would look something like this:  

As a specific example, what kinds of vectors could this 2x3 matrix act on? If we’re going to
multiply this matrix with a column vector, the column vector must have three entries to match
the size of the rows of this matrix. Multiplying our 2x3 matrix by a 3x1 column vector gives us
a 2x1 matrix as a result, or a 2D column vector. For example,  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631545280/80755252-6E09-41F7-A64A-C2C571A1A254_attpjk.png"/>

This tells us that this 2x3 matrix represents a function taking 3D vectors to 2D vectors. If we
were to draw it as a machine, like in figure 5.15, it would accept 3D vectors in its input slot and
produce 2D vectors from its output slot.  

In general, an m-by-n matrix defines a function taking n-dimensional vectors as inputs and
returning m-dimensional vectors as outputs. *Any such function is linear in the sense that it*
*preserves vector sums and scalar multiples*. **It’s not a transformation** because it doesn’t just
modify input, it returns an entirely different kind of output: a vector living in a different number
of dimensions. For this reason, we’ll use a more general terminology; we’ll call it a **linear function**
or a **linear map**. Let’s consider an in-depth example of a familiar linear map from 3D to 2D.  

### projecting as a linear map from 3d to 2d

We already saw a vector function that accepts 3D vectors and produces 2D vectors: a projection of a 3D vector onto the x, y plane (section 3.5.2). This transformation (we can call it P) takes vectors of the form (x, y, z) and returns these with their z component deleted: (x, y). I’ll spend some time carefully showing why this is a linear map and how it preserves vector addition and scalar multiplication.

First of all, let’s write P as a matrix. To accept 3D vectors and return 2D vectors, it should be a 2x3 matrix. Let’s follow our trusty formula for finding a matrix by testing the action of P on standard basis vectors. Remember, in 3D the standard basis vectors are defined as e1 = (1, 0,
0), e2 = (0, 1, 0), and e3 = (0, 0, 1), and when we apply the projection to these three vectors,
we get (1, 0), (0, 1), and (0, 0), respectively. We can write these as column vectors  
