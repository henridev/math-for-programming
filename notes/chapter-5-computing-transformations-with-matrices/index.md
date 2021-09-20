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

We already saw a vector function that accepts 3D vectors and produces 2D vectors: a projection of a 3D vector onto the x, y plane (section 3.5.2). This transformation (we can call it P) takes vectors of the form (x, y, z) and returns these with their z component deleted: (x, y). I’ll spend some time carefully showing why this is a **linear map** and how it preserves vector addition and scalar multiplication.

First of all, let’s write P as a matrix. To accept 3D vectors and return 2D vectors, it should be a 2x3 matrix. Let’s follow our trusty formula for finding a matrix by testing the action of P on standard basis vectors. Remember, in 3D the standard basis vectors are defined as e1 = (1, 0,
0), e2 = (0, 1, 0), and e3 = (0, 0, 1), and when we apply the projection to these three vectors,
we get (1, 0), (0, 1), and (0, 0), respectively. We can write these as column vectors  
$$
\hat{i} = \begin{bmatrix}
     1 \\
     0 \\
\end{bmatrix}

\hat{j} = \begin{bmatrix}
     0 \\
     1 \\
\end{bmatrix}

\hat{k} = \begin{bmatrix}
     0 \\
     0 \\
\end{bmatrix}

\\

\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
\end{bmatrix}
$$
To check this, let’s multiply it by a test vector (a, b, c). The dot product of (a, b, c) with (1, 0,,0) is a, so that’s the first entry of the result. The second entry is the dot product of (a, b, c) with (0, 1, 0), or b. You can picture this matrix as grabbing a and b from (a, b, c) and ignoring c (figure 5.16).  


$$
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
\end{bmatrix} 
\begin{bmatrix}
    a \\
    b \\
    c \\
\end{bmatrix} \\
\\ =
$$

$$
a\begin{bmatrix}
    1 \\
    0 \\
\end{bmatrix} +
b\begin{bmatrix}
    0 \\
    1 \\
\end{bmatrix} +
c\begin{bmatrix}
    0 \\
    0 \\
\end{bmatrix} =
\begin{bmatrix}
    a \\
    b \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
    (1, 0, 0) \cdot (a, b, c) \\
    (0, 1, 0) \cdot (a, b, c) \\
\end{bmatrix} =
\begin{bmatrix}
    a \\
    b \\
\end{bmatrix}
$$

This matrix does what we want: it deletes the third coordinate of a 3D vector, leaving us with
only the first two coordinates. It’s good news that we can write this projection as a matrix, but
let’s also give an algebraic proof that this is a linear map. To do this, we have to show that the
two key conditions of linearity are satisfied.  

#### PROVING PROJECTION PRESERVES VECTOR SUMS

If P (a 3d to 2d projection) is linear,That is, 

- vector sum u + v = w should be respected by P =>  P(u) + P(v) = P(w)

- scalar multiplication s * u  = w should be respected by P => P(s * u) = s * P(u)
  $$
  \vec{u} = \begin{bmatrix}
      u_1 \\
      u_2 \\
      u_3 \\
  \end{bmatrix} \\
  \vec{v} = \begin{bmatrix}
      v_1 \\
      v_2 \\
      v_3 \\
  \end{bmatrix} \\
  \vec{w} = \begin{bmatrix}
      u_1 + v_1 \\
      u_2 + v_2 \\
      u_3 + v_3 \\
  \end{bmatrix} \\
  
  P = \begin{bmatrix}
      1 & 0 & 0 \\
      0 & 1 & 0 \\
  \end{bmatrix}
  $$

  $$
  P(\vec{u}) = \begin{bmatrix}
      u_1 \\
      u_2 \\
  \end{bmatrix} \\
  P(\vec{v}) = \begin{bmatrix}
      v_1 \\
      v_2 \\
  \end{bmatrix} \\
  P(\vec{u}) + P(\vec{v}) = \begin{bmatrix}
     u_1 + v_1 \\
     v_2 + v_2 \\
  \end{bmatrix} \\
  P(\vec{w}) = = \begin{bmatrix}
     u_1 + v_1 \\
     v_2 + v_2 \\
  \end{bmatrix}
  $$

$$
P(s*\vec{u}) = \begin{bmatrix}
   s * u_1 \\
   s * u_2 \\
\end{bmatrix} \\
s*P(\vec{u}) = \begin{bmatrix}
   s * u_1 \\
   s * u_2 \\
\end{bmatrix}
$$

visual representation

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631687764/D4D83AC1-5F32-401F-B39D-E70BE359D0BA_vta4ko.png"/>



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631687753/BF2F8C71-364E-47ED-895D-6AF3E8D1D7D8_jd8iob.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631687751/82BF540B-B988-457B-975C-B67EFA89EFBF_kurqdm.png"/>

In other words, if three vectors u, v, and w form a vector sum u + v = w, then their “shadows”
in the x,y plane also form a vector sum. Now that you’ve got some insight into linear
transformation from 3D to 2D and a matrix that represents it, let’s return to our discussion of
linear maps in general.  

If Q (a 2d to 3d projection) is linear
$$
Q = \begin{bmatrix}
    1 & 0 \\
    0 & 1 \\
    0 & 0 \\
\end{bmatrix} 
\\
\vec{u} = \begin{bmatrix}
    u_1 \\
    u_2 \\
\end{bmatrix} \\
\vec{v} = \begin{bmatrix}
    u_1 \\
    u_2 \\
\end{bmatrix}
$$

$$
Q(\vec{u}) = \begin{bmatrix}
    u_1 \\
    u_2 \\
    0
\end{bmatrix} \\
Q(\vec{v}) = \begin{bmatrix}
    v_1 \\
    v_2 \\
    0
\end{bmatrix} \\
Q(\vec{u}) + Q(\vec{v}) = \begin{bmatrix}
   u_1 + v_1 \\
   v_2 + v_2 \\
   0
\end{bmatrix} \\
Q(\vec{w}) =  \begin{bmatrix}
   u_1 + v_1 \\
   v_2 + v_2 \\
   0
\end{bmatrix}
$$

### composing linear maps

The beauty of matrices is that they store all of the data required to evaluate a linear function
on a given vector. What’s more, the dimensions of a matrix tell us the dimensions of input
vectors and output vectors for the underlying function. We captured that visually in figure 5.20
by drawing machines for matrices of varying dimensions, whose input and output slots have
different shapes. Here are four examples we’ve seen, labelled with letters so we can refer back
to them.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631688026/5B265E78-247A-4E72-A1BF-05302E7BD7F5_hawb1c.png"/>

Drawn like this, it’s easy to pick out which pairs of linear function machines could be welded
together to build a new one. For instance, the output slot of M has the same shape as the input
slot of P, so we could make the composition P(M(v)) for a 3D vector v. The output of M is a 3D
vector that can be passed right along into the input slot of P (figure 5.21).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631688206/48830168-B7D2-4F91-92A3-E1E32EEED461_oyvp8b.png"/>

When the dimensions match in this way, so do the slots, and we can compose the linear functions and multiply their matrices.  

Thinking of P and M as matrices, the composition of P and M is written PM as a matrix product.
**(Remember, if PM acts on a vector v as PMv, M is applied first and then P.)** When v = (1, 1, 1),
the product PMv is a product of two matrices and a column vector, and it can be simplified into
a single matrix times a column vector if we evaluate **PM** (figure 5.23).  
$$
P = \begin{bmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
\end{bmatrix} (2X3) \\
M = \begin{bmatrix}
   -1 & -1 & 0 \\
   -2 & 1 & 2 \\
   1 & 0 & -1 \\
\end{bmatrix}  (3X3) \\

\text{first M should be applied then P should be applied} \\


\begin{bmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
   -1 & -1 & 0 \\
   -2 & 1 & 2 \\
   1 & 0 & -1 \\
\end{bmatrix} = \\
\begin{bmatrix}
   (1, 0, 0)(-1, -2, 1) & (1, 0, 0)(-1, 1, 0) & (1, 0, 0)(0, 2, -1) \\
   (0, 1, 0)(-1, -2, 1) & (0, 1, 0)(-1, 1, 0) & (0, 1, 0)(0, 2, -1)\\
\end{bmatrix} = \\
\begin{bmatrix}
   -1 & -1 & 0 \\
   -2 & 1 & 2\\
\end{bmatrix}
$$
now things are easier to calculate instead of applying M and then P to each vector we can just apply the matrix PM to the vectors.

As a programmer, you’re used to thinking of functions in terms of the types of data they
consume and produce. I’ve given you a lot of notation and terminology to digest thus far in this
chapter, but as long as you grasp this core concept, you’ll get the hang of it eventually.
I strongly encourage you to work through the following exercises to make sure you understand
the language of matrices. For the rest of this chapter and the next, there won’t be many big
new concepts, only applications of what we’ve seen so far. These applications will give you even
more practice with matrix and vector computations.  
$$
\begin{bmatrix}
   0 & 0 & 0 & 0 & 1 \\
   0 & 0 & 0 & 1 & 0 \\
   1 & 0 & 0 & 0 & 0 \\
   0 & 1 & 0 & 0 & 0 \\
   0 & 0 & 1 & 0 & 0 \\
   0 & 0 & 0 & 1 & 0 \\
\end{bmatrix}\begin{bmatrix}
   l \\
   e \\
   m \\
   o \\
   n \\
   s
\end{bmatrix} = 
\begin{bmatrix}
   s \\
   o \\
   l \\
   e \\
   m \\
   n
\end{bmatrix}
$$

## 5.3 translating vectors with matrices

- advantage of matrices => computations look the same in any number of dimensions.
- no worries about picturing the configurations of vectors in 2D or 3D, they can be plugged into the formulas for matrix multiplication
- especially useful when we want to do computations in more than three
  dimensions.

In this section, we’ll cover a computation that requires doing computation in higher dimensions: translating vectors using a matrix.  

### making plane translations linear

- translations are not linear transformations.
  - the origin moves
  - vector sums are not preserved.

How can we hope to execute a 2D transformation with a matrix if it is not a linear
transformation? =>The trick is that we can think of our 2D points to translate as living in 3D. Let’s return to our dinosaur from chapter 2. The dinosaur was composed of 21 points.

If we want to translate the dinosaur to the right by 3 units and up by 1 unit, we could simply
add the vector (3, 1) to each of the dinosaur’s vertices. But this isn’t a linear map, so we can’t
produce a 2x2 matrix that does this translation. If we think of the dinosaur as an inhabitant of
3D space instead of the 2D plane, it turns out we can formulate the translation as a matrix.
Bear with me for a moment while I show you the trick; I’ll explain how it works shortly. 

Let’s give every point of the dinosaur a z-coordinate of 1. Then we can draw it in 3D by connecting
each of the points with segments and see that the resulting polygon lies on the plane where z
= 1

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631860309/55CBD7F7-9D35-4EF0-A052-FFD26E047509_rmfnby.png"/>

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631860301/067CAFFC-B39D-4821-884F-18D41E46850C_blaa7a.png"/>

 “skews” 3D space, so that the origin stays put, but the plane where z = 1 is translated as desired. and the dino moves three to the right and one up

### finding a 3d matrix for 2d translation

- columns of our “magic” matrix, like the columns of any matrix, tell us where the standard
  basis vectors end up after being transformed. 
- Calling this matrix T, the vectors e1, e2, and e3 would be transformed into the vectors Te1 = (1, 0, 0), Te2 = (0, 1, 0), and Te3 = (3, 1, 1). 
- e1 and e2 are unaffected, and e3 changes only its x- and y-components (figure 5.29).  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631861887/4F3D71F3-BFD7-463C-A965-BD75B384ED31_hdozra.png"/>

Any point in 3D and, therefore, any point on our dinosaur is built as a linear combination of e1,
e2, and e3. 
$$
x \hat{e_1} + y \hat{e_2} + z \hat{e_3} \\
\\
\text{For instance, the tip of the dinosaur’s tail is at (6, 4, 1)}\\
\\
6 \hat{e_1} + 4 \hat{e_2} + 1 \hat{e_3} \\
\\
\text{only the effect on e3 moves the point } \\
T(\hat{e_3}_{original}) = \hat{e_3}_{original} + (3, 1, 0) \\
\\
\text{so that the point is translated by +3 in the x direction and +1 in the y direction. } \\
\text{You can also see this algebraically. Any vector (x, y, 1) is translated by (3, 1, 0) by this matrix: } \\
$$

$$
\begin{bmatrix}
   (1,0,3) \cdot (x,y,1) \\
   (0,1,1) \cdot (x,y,1) \\
   (0,0,1) \cdot (x,y,1)\\
\end{bmatrix} =
\begin{bmatrix}
   x + 3 \\
   y + 1 \\
   1 \\
\end{bmatrix}
$$

If you want to translate a collection of 2D vectors by some vector (a, b), the general steps are
as follows:

1. Move the 2D vectors into the plane in 3D space, where z = 1 and each has a z-coordinate
   of 1 

2. Multiply the vectors by the matrix with your given choices of a and b plugged in:  

   

$$
\begin{bmatrix}
   1 & 0 & a \\
   0 & 1 & b \\
   0 & 0 & 1\\
\end{bmatrix}
$$

3. Delete the z-coordinate of all of the vectors so you are left with 2D vectors as a result.  

Now that we can do translations with matrices, we can creatively combine them with other linear
transformations.  



### combining translations with other linear transformations

In the previous matrix, the first two columns are exactly e1 and e2, meaning that only the change
in e3 moves a figure. We don’t want T(e1) or T(e2) to have any z-component because that would
move the figure out of the plane z = 1. But we can modify or interchange the other components



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631863239/Inked_B4465215-5AFD-40AA-99C2-60B26CD74A1D__LI_kqpo5f.jpg"/>

It turns out you can put any 2x2 matrix in the top left by doing the corresponding linear transformation in addition to the translation specified in the third column via the a and b tuple. For instance, this matrix  
$$
\begin{bmatrix}
   0 & -1 \\
   1 & 0 \\
\end{bmatrix}
$$
produces a 90° counterclockwise rotation. Inserting it in the translation matrix, we get a new
matrix that rotates the x,y plane by 90° and then translates it by (3, 1)
$$
\begin{bmatrix}
   0 & -1 & 3 \\
   1 & 0 & 1 \\
   0 & 0 & 1 \\
\end{bmatrix}
$$
<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631863662/Figure_1_iukdr2.png"/>

Once you get the hang of doing 2D translations and transformations with a matrix, you can apply the same approach to doing a 3D translation. To do that, you’ll have to use a 4x4 matrix and enter the mysterious
world of 4D.  

### translating 3d objects in 4d world

What is the fourth dimension? A 4D vector would be an arrow with some length, width, depth,
and one other dimension. When we built 3D space from 2D space, we added a z-coordinate.
That means that 3D vectors can live in the x,y plane, where z = 0, or they can live in any other
parallel plane, where z takes a different value. Figure 5.33 shows some of these parallel planes.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631889912/870AC566-1AFD-47F9-9027-75D55D528C61_qrla7f.png"/>

We can think of four dimensions in analogy to this model: a collection of 3D spaces that are
indexed by some fourth coordinate. One way to interpret the fourth coordinate is “time.” Each
snapshot at a given time is a 3D space, but the collection of all of the snapshots is a fourth
dimension called a spacetime. The origin of the spacetime is the origin of the space at the
moment when time, t, is equal to 0.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1631890098/19EDD58C-0E15-48F9-88E7-42075CB2484B_slofhc.png"/>

This is the starting point for Einstein’s theory of relativity. (In fact, you are now qualified to go
read about this theory because it is based on 4D spacetime and linear transformations given by
4x4 matrices.)

Vector math is indispensable in higher dimensions because we quickly run out of good analogies.
For five, six, seven, or more dimensions, I have a hard time picturing them, but the coordinate
math is no harder than in two or three dimensions. For our current purposes, it’s sufficient to
think of a 4D vector as a four-tuple of numbers.

Let’s replicate the trick that worked for translating 2D vectors in 3D. If we start with a 3D vector
like (x, y, z) and we want to translate it by a vector (a, b, c), we can attach a fourth coordinate  
$$
\text{2d translation and transformation} \\
\\
\text{translation stand alone} \\
\begin{bmatrix}
   1 & 0 & a_{translation} \\
   0 & 1 &  b_{translation} \\
   0 & 0 & 1 \\
\end{bmatrix} 
\begin{bmatrix}
   x + a_{translation} \\
   y + b_{translation} \\
   1 \\
\end{bmatrix} \\
\\
\\
\text{transformation and translation combined} \\
\begin{bmatrix}
   \hat{i_x}_{transformation} & \hat{j_x}_{transformation} & a_{translation} \\
   \hat{i_y}_{transformation} & \hat{j_y}_{transformation} &  b_{translation} \\
   0 & 0 & 1 \\
\end{bmatrix} \\
$$


now in 3  ...
$$
\text{3d translation and transformation}\\
\\
\text{translation stand alone} \\
\begin{bmatrix}
   1 & 0 & 0 & a_{translation} \\
   0 & 1 & 0 & b_{translation} \\
   0 & 0 & 1 & c_{translation} \\
   0 & 0 & 0 & 1 \\
\end{bmatrix} 
\begin{bmatrix}
   x \\
   y \\
   z \\
   1 \\
\end{bmatrix} =\begin{bmatrix}
   x + a_{translation} \\
   y + b_{translation}\\
   z + c_{translation} \\
   1 \\
\end{bmatrix} \\
\\
\\
\text{transformation and translation combined} \\
\begin{bmatrix}
   \hat{i_x}_{transformation} & \hat{j_x}_{transformation} & a_{translation} \\
   \hat{i_y}_{transformation} & \hat{j_y}_{transformation} &  b_{translation} \\
   \hat{i_z}_{transformation} & \hat{j_z}_{transformation} &  c_{translation} \\
   0 & 0 & 1 \\
\end{bmatrix}
$$
This matrix increases the x-coordinate by a, the y-coordinate by b, and the z-coordinate by c,
so it does the transformation required to translate by the vector (a, b, c). We can package in a
Python function the work of adding a fourth coordinate, applying this 4x4 matrix, and then
deleting the fourth coordinate:  

```python
def translate_3d(translation):
    '''
    takes a translation vector
    returns a new function that applies that translation to a 3D vector
    '''
    def new_function(target):
        a, b, c = translation
        x, y, z = target
        matrix = ((1, 0, 0, a),
                  (0, 1, 0, b),
                  (0, 0, 1, c),
                  (0, 0, 0, 1))  # 2 Builds the 4x4 matrix for the translation, and on the next line, turns (x,y,z) into a 4D vector with a fourth coordinate 1
        vector = (x, y, z, 1)
        # 3 Does the 4D matrix transformation
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out)
    return new_function
```

With translation packaged as a matrix operation, we can now combine that operation with other
3D linear transformations and do them in one step. It turns out you can interpret the artificial
fourth-coordinate in this setup as time, t.

The two images in figure 5.36 could be snapshots of a teapot at t = 0 and t = 1, which is moving
in the direction (2, 2, -3) at a constant speed. If you’re looking for a fun challenge, you can
replace the vector (x, y, z, 1) in this implementation with vectors of the form (x, y, z, t), where
the coordinate t changes over time. With t = 0 and t = 1, the teapot should match the frames
in figure 5.36, and at the time between the two, it should move smoothly between the two
positions. If you can figure out how this works, you’ll catch up with Einstein!
So far, we’ve focused exclusively on vectors as points in space that we can render to a computer
screen. This is clearly an important use case, but it only scratches the surface of what we can
do with vectors and matrices. The study of how vectors and linear transformations work together
in general is called linear algebra, and I’ll give you a broader picture of this subject in the next
chapter, along with some fresh examples that are relevant to programmers.  

```python
import pygame
import camera
import sys
import matplotlib.cm
from vectors import *
from math import *
from transforms import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, multiply_matrix_vector

# lighting stuff
def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1, 2, 3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

# helper Axis
def Axes():
    axes = [
        [(-1000, 0, 0), (1000, 0, 0)],
        [(0, -1000, 0), (0, 1000, 0)],
        [(0, 0, -1000), (0, 0, 1000)]
    ]
    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glColor3fv((1, 1, 1))
            glVertex3fv(vertex)
    glEnd()

def draw_model(
    faces, 
    color_map=blues, 
    light=(1, 2, 3), 
    glRotatefArgs=None, 
    get_matrix=None, 
    translation_over_time=False, 
    translation_speed=1
):
    # 1: Setup pygame
    pygame.init()
    display = (400, 400)
    window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    cam = camera.default_camera
    cam.set_window(window)
    gluPerspective(45, 1, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
 
    if glRotatefArgs:
        glRotatef(*glRotatefArgs)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glCullFace(GL_BACK)

    # 2: Handlers
    while cam.is_shooting():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Axes()
        glBegin(GL_TRIANGLES)

        # 3: Handlers
        def do_matrix_transform(v):
            if get_matrix:
                # get 3x3 form matrix transformation
                m = get_matrix(pygame.time.get_ticks())
                # apply 3x3 to 3x1 vector
                if translation_over_time and len(v) == 3:
                    x, y, z = v
                    t_dimension = pygame.time.get_ticks() / (10000/translation_speed)
                    vector = (x, y, z, t_dimension)
                    x_out, y_out, z_out, _ = multiply_matrix_vector(m, vector)
                    return (x_out, y_out, z_out)
                return multiply_matrix_vector(m, v)
            else:
                return v

        transformed_faces = polygon_map(do_matrix_transform, faces)
        for face in transformed_faces:
            color = shade(face, color_map, light)
            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()
        cam.tick()
        pygame.display.flip()
        
def translate_3d(translation):
    def new_function(target): 
        a, b, c = translation
        x, y, z = target
        matrix = ((1, 0, 0, a), (0, 1, 0, b), (0, 0, 1, c), (0, 0, 0, 1))
        vector = (x, y, z, 1)
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out)
    return new_function

translation_steps = (2, 2, -3)

def get_matrix(_t):
    a, b, c = translation_steps
    return (
        (1, 0, 0, a),
        (0, 1, 0, b),
        (0, 0, 1, c),
        (0, 0, 0, 1)
    )

draw_model(load_triangles(), get_matrix=get_matrix, translation_over_time=(2, 2, -3), translation_speed=0.6)


```

In the previous chapters, we used visual examples in 2D and 3D to motivate vector and matrix
arithmetic. As we’ve gone along, we’ve put more emphasis on computation. At the end of this
chapter, we calculated vector transformations in higher dimensions where we didn’t have any
physical insight. This is one of the benefits of linear algebra: it gives you the tools to solve
geometric problems that are too complicated to picture. We’ll survey the broad range of this
application in the next chapter.  

## 4: summary

- A linear transformation is defined by what it does to standard basis vectors. When you
  apply a linear transformation to the standard basis, the resulting vectors contain all the
  data required to do the transformation. This means that only nine numbers are required
  to specify a 3D linear transformation of any kind (the three coordinates of each of these
  three resulting vectors). For a 2D linear transformation, four numbers are required.
- In matrix notation, we represent a linear transformation by putting these numbers in a rectangular grid. By convention, you build a matrix by applying a transformation to the  standard basis vectors and putting the resulting coordinate vectors side by side as columns.
- Using a matrix to evaluate the result of the linear transformation it represents on a given
  vector is called multiplying the matrix by the vector. When you do this multiplication, the
  vector is typically written as a column of its coordinates from top to bottom rather than
  as a tuple.
- Two square matrices can also be multiplied together. The resulting matrix represents the composition of the linear transformations of the original two matrices.
- To calculate the product of two matrices, you take the dot products of the rows of the
  first with the columns of the second. For instance, the dot product of row i of the first
  matrix and column j of the second matrix gives you the value in row i and column j of
  the product.
- As square matrices represent linear transformations, non-square matrices represent
  linear functions from vectors of one dimension to vectors of another dimension. That is,
  these functions send vector sums to vector sums and scalar multiples to scalar multiples.
- The dimension of a matrix tells you what kind of vectors its corresponding linear function
  accepts and returns. A matrix with m rows and n columns is called an m-by-n matrix
  (sometimes written mxn). It defines a linear function from n-dimensional space to mdimensional space.
- Translation is not a linear function, but it can be made linear if you perform it in a higher
  dimension. This observation allows us to do translations (simultaneously with other linear
  transformations) by matrix multiplication.  

