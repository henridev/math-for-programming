# 6: generalizing to higher dimensions

Even if you’re not interested in animating teapots, the machinery of vectors, linear transformations, and matrices can still be useful. In fact, these concepts are so useful there’s an entire branch of math devoted to them: linear algebra. 

Linear algebra generalizes everything we know about 2D and 3D geometry to study data in any number of dimensions. As a programmer, you’re probably skilled at generalizing ideas. When writing complex software, it’s common to find yourself writing similar code over and over.

At some point, you catch yourself doing this, and you consolidate the code into one class or function capable of handling all of the cases you see. This saves you typing and often improves code organization and maintainability. 

Mathematicians follow the same process: after encountering similar patterns over and over, they can better state exactly what they see and refine their definitions.

In this chapter, we use this kind of logic to define vector spaces. **Vector spaces** are collections
of objects we can treat like vectors. These can be arrows in the plane, tuples of numbers, or
objects completely different from the ones we’ve seen so far. For instance, you can treat images
as vectors and take a linear combination of them (figure 6.1).  

The key operations in a vector space are **vector addition** and **scalar multiplication**. With these,
you can make linear combinations (including negation, subtraction, weighted averages, and so
on), and you can reason about which transformations are linear. It turns out these operations
help us make sense of the word dimension. For instance, we’ll see that the images used in the figure are 270,000-dimensional objects! We’ll cover higher-dimensional and even infinite dimensional spaces soon enough, but let’s start by reviewing the 2D and 3D spaces we already know.  



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632034567/696AD483-5595-4D87-8ED3-C4132CC1B9BA_bksheb.png"/>

## 6.1 generalizing our definition of vectors

Python supports **object-oriented programming (OOP),** which is a great framework for
generalization. Specifically, Python classes support **inheritance**: you can create new classes of
objects that inherit properties and behaviours of an existing parent class. In our case, we want
to realize the 2D and 3D vectors we’ve already seen as instances of a more general class of
objects simply called **vectors**. Then any other objects that inherit behaviours from the parent
class can rightly be called vectors as well.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632034905/B000F4C9-05C1-4948-808C-ABFFAAF19968_dnjiyx.png"/>

### creating a class for 2d coordinate vectors.

In code, our 2D and 3D vectors have been coordinate vectors, meaning that they were defined
as tuples of numbers, which are their coordinates. (We also saw that vector arithmetic can be
defined geometrically in terms of arrows, but we can’t translate that approach directly into
Python code.) For 2D coordinate vectors, the data is the ordered pair of the x- and y-coordinates.
A tuple is a great way to store this data, but we can equivalently use a class. We’ll call the class
representing 2D coordinate vectors Vec2:  

```python
class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        '''
        vectors are equal when their coordinates are equal
        '''
        return self.x == other.x and self.y == other.y

    def __mul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __rmul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __add__(self, v):
        '''
        overrride + operator
        '''
        return self.add(v)

    def __repr__(self):
        '''
        overrid memory address returned as representation
        '''
        return "Vec2({},{})".format(self.x, self.y)


v1 = Vec2(1, 2)
v2 = Vec2(2, 1)
v3 = v1.add(v2)


print(v1 * 3 + v2 * 2)
# class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        '''
        vectors are equal when their coordinates are equal
        '''
        return self.x == other.x and self.y == other.y

    def __mul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __rmul__(self, num):
        '''
        overrride * operator
        '''
        return self.scale(num)

    def __add__(self, v):
        '''
        overrride + operator
        '''
        return self.add(v)

    def __repr__(self):
        '''
        overrid memory address returned as representation
        '''
        return "Vec2({},{})".format(self.x, self.y)


v1 = Vec2(1, 2)
v2 = Vec2(2, 1)
v3 = v1.add(v2)


print(v1 * 3 + v2 * 2)
# Vec2(7,8)
    
```

### repeating the process with 3d vectors

```python
class Vec3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def scale(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __mul__(self, num):
        return self.scale(num)

    def __rmul__(self, num):
        return self.scale(num)

    def __add__(self, v):
        return self.add(v)

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)
```

This Vec3 class puts us in a good place to think about generalization. There are a few different directions we can go, and like many software design choices, the decision is subjective. 

We could, for example, focus on simplifying the arithmetic. Instead of implementing add differently for Vec2 and Vec3; they can both use the add function we built in chapter 3, which already handles coordinate vectors of any size. We could also store coordinates  

internally as a tuple or list, letting the constructor accept any number of coordinates and create
a 2D, 3D, or other coordinate vector. I’ll leave these possibilities as exercises for you, however,
and take us in a different direction.

```python
class Vec():
    def __init__(self, *coords):
        self.coords = coords

    def add(self, v):
        return Vec(*map(sum, (zip(self.coords, v.coords))))

    def scale(self, s):
        return Vec(*[s * coor for coor in self.coords])

    def __eq__(self, other):
        for (coor_other, soor_self) in zip(other.coords), self.coords:
            if coor_other != soor_self:
                return False
        return True

    def __mul__(self, num):
        return self.scale(num)

    def __rmul__(self, num):
        return self.scale(num)

    def __add__(self, v):
        return self.add(v)

    def __repr__(self):
        return "Vec{}".format(self.coords)
```

The generalization I want to focus on is based on how we use the vectors, not on how they work. This gets us to a mental model that both organizes the code well and aligns with the mathematical definition of a vector. For instance, we can write a generic average function that can be used on any kind of vector:  

```python
def average(v1,v2):
	return 0.5 * v1 + 0.5 * v2
```

We can insert either 3D vectors or 2D vectors. for instance, `average(Vec2(9.0, 1.0), Vec2(8.0,6.0))`.

> As a spoiler, we will soon be able to average pictures together as well. Once we’ve implemented a suitable class for images, we’ll be able to write average(img1, img2) and get a new image back.

- beauty and the economy that comes with generalization. => single, generic function and use it for a wide variety of types of inputs. 
  - only constraint on the input is that it needs to support multiplication by scalars and addition with one another. 
  - The implementation of arithmetic varies between Vec2 objects, Vec3 objects, images,
    or other kinds of data, but there’s always an important overlap in what arithmetic we can do
    with them. 
  - When we separate the what from the how, we open the door for code reuse and far reaching mathematical statements.

How can we best describe what we can do with vectors separately from the details of how we carry them out? We can capture this in Python using an **abstract base class.**  

### building a vector base class

The basic things we can do with Vec2 or Vec3 include constructing a new instance, adding with other vectors, multiplying by a scalar, testing equality with another vector, and representing an instance as a string. Of these, only addition and scalar multiplication are distinctive vector operations. Any new Python class automatically includes the rest. This prompts a definition of a Vector base class:  

```python
from abc import ABCMeta, abstractmethod
'''
contains helper classes, functions, and method decorators that help define an abstract base class = a class that is not intended to be instantiated. Instead, it’s designed to be used as a template for classes that inherit from it. 
'''

class Vector(metaclass=ABCMeta):
    # a method is not implemented in the base class and needs to be implemented for any child class.
    @abstractmethod 
    def scale(self,scalar):
        pass
    @abstractmethod
    def add(self,other):
        pass
    
    # It is also useful to have this base class because we can equip it with 
    # all the methods that depend only on addition and scalar multiplication
    # In contrast to the abstract methods scale and add, 
    # these implementations are automatically available to any child class. 
    def __mul__(self, scalar):
		return self.scale(scalar)
	def __rmul__(self, scalar):
		return self.scale(scalar)
	def __add__(self,other):
		return self.add(other)
    def __sub__(self, other):
        return self.subtract(other)

# We can simplify Vec2 and Vec3 to inherit from Vector. 
class Vec2(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)
    
    def subtract(self, v):
        return self.add(v * -1)

    def scale(self, s):
        return Vec2(self.x * s, self.y * s)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return "Vec2({},{})".format(self.x, self.y)
```

This has indeed saved us from repeating ourselves! The methods that were identical between Vec2 and Vec3 now live in the Vector class. All remaining methods on Vec2 are specific to 2D vectors; they need to be modified to work for Vec3 (as you will see in the exercises) or for vectors with any other number of coordinates. The Vector base class is a good representation of what we can do with vectors. If we can add any useful methods to it, chances are they will be useful for any kind of vector. 

This abstract class makes it easier to implement general vector operations, and it also agrees with the mathematical definition of a vector. Let’s switch languages from Python to English and see how the abstraction carries over from code to become a real mathematical definition.  

### defining vector spaces

In math, a vector is defined by what it does rather than what it is, much like how we defined the abstract Vector class. 

Here’s a first (incomplete) definition of a vector.

> A vector is an object equipped with a **suitable** way to add it to other vectors and multiply it by scalars.

Our Vec2 or Vec3 objects, or any other objects inheriting from the Vector class can be added to each other and multiplied by scalars. This definition is incomplete because I haven’t said what “suitable” means, and that ends up being the most important part of the definition!

There are a few important rules outlawing weird behaviours, many of which you might have already assumed. It’s not necessary to memorize all these rules.

If you ever find yourself testing whether a new kind of object can be thought of as a vector, you can refer back to these rules.

1. The first set of rules says that addition should be **well-behaved**. Specifically:

- Adding vectors in any order shouldn’t matter
  $$
  \text{commutative} \\
  \vec{v} + \vec{w} = \vec{w} + \vec{v}
  $$
  
- Adding vectors in any grouping shouldn’t matter
  $$
  \text{associative} \\
  \vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}
  $$



A good counterexample is adding strings by concatenation. In Python, you can do the sum "hot" + "dog", but this doesn’t support the case that strings can be vectors because the sums "hot" + "dog" and "dog" + "hot" are not equal, violating rule 1.

2. Scalar multiplication also needs to be **well-behaved** and compatible with addition. For instance, a whole number scalar multiple should be equal to a repeated addition (like 3v = v + v + v). Here are the specific rules:

- Multiplying vectors by several scalars should be the same as multiplying by all the scalars at once.
  $$
  \text{distributive} \\
  s_1 * (s_2 * \vec{v}) = (s_1 * s_2) * \vec{v}
  $$
  
- Multiplying a vector by 1 should leave it unchanged
  $$
  \vec{u} * 1 = \vec{u}
  $$
  
- Addition of scalars should be compatible with scalar multiplication  
  $$
  \text{distributive} \\
  s_1 * \vec{v} + s_2 * \vec{v} = (s_1 + s_2) * \vec{v}
  $$

- Addition of vectors should also be compatible with scalar multiplication  
  $$
  \text{distributive} \\
  (\vec{v} + \vec{u}) * s  = (\vec{v} * s) +  (\vec{u} * s)
  $$
  

None of these rules should be too surprising. For instance, `3 · v + 5 · v` could be translated to English as “3 of v added together plus 5 of v added together.” Of course, this is the same as 8 of v added together, or `8 · v`, agreeing with rule 2.3.

The takeaway from these rules is that not all addition and multiplication operations are created equal. We need to verify each of the rules to ensure that addition and multiplication behave as expected. If so, the objects in question can rightly be called vectors. A vector space is a collection of compatible vectors. Here’s the definition:  

> **vector space** is a collection of objects (called vectors), equipped with suitable vector addition
> and scalar multiplication operations, such that every linear combination of vectors in the collection produces a
> vector that is also in the collection  

A collection like `[Vec2(1,0), Vec2(5,-3), Vec2(1.1,0.8)]` is a group of vectors that can be suitably added and multiplied, but it is not a vector space. For instance, `1 * Vec2(1,0) + 1 * Vec2(5,-3) = Vec2(6,-3)` the result is not in the collection.

One example of a vector space is the infinite collection of all possible 2D vectors. In fact, most vector spaces you meet are **infinite sets**: there are infinitely many linear combinations using infinitely many scalars after all!

There are two implications of the fact that vector spaces need to contain all their scalar multiples, and these implications are important enough to mention on their own. 

- no matter what vector `v` you pick in a vector space, `0 · v` gives you the same result, which is called the **zero vector** and denoted as `0`. Adding the zero vector to any vector leaves that vector unchanged: `0 + v = v + 0 = v`. 
- every vector v has an opposite vector, `-1 * v`, written as `-v`. Due to rule 2.3, `v + -v = (1 + -1)
  · v = 0 · v = 0`. For every vector, there is another vector in the vector space that “cancels it out” by addition. 

As an exercise, you can improve the Vector class by adding a zero vector and a negation function as required members. A class like Vec2 or Vec3 is not a collection per se, but it does describe a collection of values. In this way, we can think of the classes Vec2 and Vec3 as representing two different vector spaces,and their instances represent vectors. 

We’ll see a lot more examples of vector spaces with classes that represent them in the next section, but first, let’s look at how to validate that they satisfy the specific rules we’ve covered.  

### unit testing vector spaces

It was helpful to use an abstract Vector base class to think about what a vector should be able to do, rather than how it’s done. 

>  Program to an interface, not an *implementation*.

But even giving the base class an abstract add method doesn’t guarantee every inheriting class will implement a suitable addition operation.

In math, the usual way we guarantee suitability is by writing a proof. In code, and especially in a dynamic language like Python, the best we can do is to write unit tests. 

For instance, we can check rule 2.4 from the previous section by creating two vectors and a scalar and making sure the equality holds:

```python
s = -3
u, v = Vec2(42,-10), Vec2(1.5, 8)
s * (u + v) == s * v + s * u
# true 
```

This is often how unit tests are written, but it’s a pretty weak test because we’re only trying one example. We can make it stronger by plugging in random numbers and ensuring that it works. Here I use the random.uniform function to generate evenly distributed floating-point numbers between -10 and 10:

```python
from hypothesis import given, note, strategies as st


@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def commutative_vectors(u_x, u_y, v_x, v_y):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    result = u + v == v + u
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def associative_vectors(u_x, u_y, v_x, v_y, w_x, w_y):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    w = Vec2(w_x, w_y)
    result = (u + v) + w == u + (v + w)
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def multiply_several_scalars_multiply_all_scalars(v_x, v_y, scalar_1, scalar_2):
    v = Vec2(v_x, v_y)
    result = scalar_1 * (scalar_2 * v) == (scalar_1 * scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers()
)
def multiply_one_unchanged(v_x, v_y):
    v = Vec2(v_x, v_y)
    result = v == v * 1
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_scalars_compatible_scalar_multiplication(v_x, v_y, scalar_1, scalar_2):
    v = Vec2(v_x, v_y)
    result = scalar_1 * v + scalar_2 * v == (scalar_1 + scalar_2) * v
    note(f"Result: {result}")
    assert result == True

@given(
    st.integers(), st.integers(), st.integers(), st.integers(), st.integers()
)
def test_addition_vectors_compatible_scalar_multiplication(u_x, u_y, v_x, v_y, scalar):
    u = Vec2(u_x, u_y)
    v = Vec2(v_x, v_y)
    result = scalar * (u + v) == scalar * v + scalar * u
    note(f"Result: {result}")
    assert result == True


try:
    commutative_vectors()
    associative_vectors()
    multiply_several_scalars_multiply_all_scalars()
    multiply_one_unchanged()
    test_addition_scalars_compatible_scalar_multiplication()
except AssertionError:
    print("result != True")

```

## 6.2 Exploring different vector spaces

Now that you know what a vector space is, let’s look at some examples. In each case, we take a new kind of object and implement it as a class that inherits from Vector. At that point, no matter what kind of object it is, we can do addition, scalar multiplication, or any other vector operation with it.  

### enumerate all coordinate vector spaces

We’ve spent a lot of time on the coordinate vectors Vec2 and Vec3 so far, so coordinate vectors in 2D and 3D don’t need much more explanation. It is worth reviewing, however, that a vector space of coordinate vectors can have any number of coordinates. Vec2 vectors have two coordinates, Vec3 vectors have three, and we could just as well have a Vec15 class with 15 coordinates. We can’t picture it geometrically, but Vec15 objects represent points in a 15D space.

One special case worth mentioning is the class we might call Vec1, vectors with a single coordinate. The implementation looks like this:  

```python
from abc import ABCMeta, abstractmethod, abstractclassmethod, abstractproperty

class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractclassmethod
    @abstractproperty
    def zero_vector(self):
        pass

    def negation_vector(self):
        return self.scale(-1)

    def subtract(self, other):
        return self.add(other.scale(-1))

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)


class Vec1(Vector):
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return Vec1(self.x + other.x)

    def scale(self, scalar):
        return Vec1(scalar * self.x)

    def zero_vector(cls):
        return Vec1(0)

    def __eq__(self, other):
        return self.x == other.x

    def __repr__(self):
        return "Vec1({})".format(self.x)

class Vec0(Vector):
    def __init__(self):
        pass

    def add(self, other):
        return Vec0()

    def scale(self, scalar):
        return Vec0()

    def zero_vector(cls):
        return Vec0()

    def __eq__(self, other):
        return self.__class__ == other.__class__ == Vec0

    def __repr__(self):
        return "Vec0()"
```

This is a lot of boilerplate to wrap a single number, and it doesn’t give us any arithmetic we don’t already have. Adding and multiplying Vec1 scalar objects is just addition and multiplication of the underlying numbers:  

For this reason, we probably will never need a Vec1 class. But it is important to know that numbers on their own are vectors. The set of all real numbers (including integers, fractions, and irrational numbers like 𝜋𝜋) is denoted as ℝ, and it is a vector space in its own right. This is a special case where the scalars and the vectors are the same kind of objects.

Coordinate vector spaces are denoted `ℝn`, where n is the dimension or number of coordinates. For instance, the 2D plane is denoted as `ℝ2` and 3D space is denoted as `ℝ3`. As long as you use real numbers as your scalars, any vector space you stumble across is some ℝn in disguise.1 This is why we need to mention the vector space ℝ, even if it is boring. The other vector space we need to mention is the zero-dimensional one, `ℝ0`. This is the set of vectors with zero coordinates that we can describe as empty tuples or as a Vec0 class inheriting from Vector:  

That covers it for coordinate vectors of dimensions zero, one, two, three, or more. Now, when you see a vector in the wild, you’ll be able to match it up with one of these vector spaces.  

### identifying vector spaces in the wild

Let’s return to an example from chapter 1 and look at a data set of used Toyota Priuses. In the source code, you’ll see how to load the data set generously provided by my friend Dan Rathbone at CarGraph.com. To make the cars easy to work with, I’ve loaded them into a class:  

It would be useful to think of CarForSale objects as vectors. Then, for example, I could average them together as a linear combination to see what the typical Prius for sale looks like. To do that, I need to retrofit this class to inherit from Vector.

How can we add two cars? The numeric fields model_year, mileage, and price can be added like components of a vector, but the string properties can’t be added in a meaningful way. (Remember, you saw that we can’t think of strings as vectors.) When we do arithmetic on cars, the result is not a real car for sale but a virtual car defined by its properties. To represent this, I'll change all the string properties to the string “(virtual)” to remind us of this. Finally, we
can’t add datetimes, but we can add time spans. In figure 6.3, I use the day I retrieved the data as a reference point and add the time spans since the cars were posted for sale. 

The sum of the first two cars is evidently a Prius from model year 4012 (maybe it can fly?) with 306,000 miles on it and going for an asking price of $6,100. It was posted for sale at 3:59 AM on the same day I looked at CarGraph.com. This unusual car doesn’t look too helpful, but bear with me, averages (as shown in the following) look a lot more meaningful:  

We can learn real things from this result. The average Prius for sale is about 6 years old, has about 88,000 miles on it, is selling for about $12,500, and was posted at 9:49 AM the morning I accessed the website. (In Part 3, we spend a lot of time learning from data sets by treating them as vectors.) Ignoring the text data, CarForSale behaves like a vector. In fact, it behaves like a 4D vector having dimensions of price, model year, mileage, and datetime of posting. It’s not quite a coordinate vector because the posting date is not a number. Even though the data is not numeric, the class satisfies the vector space properties (you verify this with unit tests in the exercises), so its objects are vectors and can be manipulated as such. Specifically, they are 4D vectors, so it is possible to write a 1-to-1 mapping between CarForSale objects and Vec4 objects (also an exercise for you). For our next example, we’ll see some objects that look even less like coordinate vectors but still satisfy the defining properties.  

### treating functions a vectors

It turns out that mathematical functions can be thought of as vectors. Specifically, I’m talking about functions that take in a single real number and return a single real number, though there are plenty of other types of mathematical functions. The mathematical shorthand to say that a function f takes any real number and returns a real number is 
$$
f: \R \rightarrow \R
$$
With Python, we’ll think of functions that take float values in and return float values. As with 2D or 3D vectors, we can do addition and scalar multiplication of functions visually or algebraically. To start, we can write functions algebraically; for instance, 
$$
f(x) = 0.5 · x + 3  \\
g(x) = \sin(x)
$$
Alternatively, we can visualize these with a graph.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632050304/75F260D4-3603-4862-B0B3-33B74558FD90_tdbt4a.png"/>

In the source code, I’ve written a simple plot function that draws the graph of one or more functions on a specified range of inputs (figure 6.4). For instance, the following code plots both of our functions f(x) and g(x) on x values between -10 and 10:  

```python
def f(x):
	return 0.5 * x + 3
def g(x):
	return sin(x)
plot([f,g],-10,10)
```

Algebraically, we can add functions by adding the expressions that define them. This means 
$$
f+g \\
(f + g)(x) = f(x) + g(x) = 0.5 · x + 3 + sin(x)
$$
Graphically, the y values of each point are added, so it’s something like stacking the two functions together



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632050521/8497105B-D7B3-4B95-8F74-3EED6F0389D7_icwcby.png"/>

To implement this sum, you can write some functional Python code. This code takes two functions as inputs and returns a new one, which is their sum:  

```python
def add_functions(f,g):
    def new_function(x):
    	return f(x) + g(x)
    return new_function
```

Likewise, we can multiply a function by a scalar by multiplying its expression by the scalar. For instance
$$
3g \\
(3g)(x) = 3 · g(x) = 3 · sin(x)
$$
This has the effect of stretching the graph of the function g in the y direction by a factor of 3.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632050662/A903BDC4-524A-4C69-A08A-91435C354EF5_t4qq2w.png"/>

```python
class Function(Vector):
    def __init__(
            self, f
    ):
        self.f = f

    def add(self, other):
        def new_function(x):
            return self.f(x) + other.f(x)
        return Function(new_function)

    def scale(self, scalar):
        def new_function(x):
            return self.f(x) * scalar
        return Function(new_function)

    def zero():
        return Function(lambda x: 0)

    def __call__(self, x):
        return self.f(x)


new_function = 3 * Function(lambda x: x * 3)

print(new_function(2))

new_function = 2 * Function(lambda x: x * 3) - 6 * Function(lambda x: x / 2)

print(new_function(2))
```

It’s possible to nicely wrap Python functions in a class that inherits from vector, and I leave it as an exercise for you. After doing so, you can write satisfying function arithmetic expressions like 3 * f or 2 * f - 6 * g. You can even make the class callable or able to accept arguments as if it were a function to allow expressions like (f + g)(6). Unfortunately, unit testing to determine if functions satisfy the vector space properties is much harder because it’s difficult to generate
random functions or to test whether two functions are equal. 

To really know if two functions are equal, you have to know that they return the same output for every single possible input. That means a test for every real number or at least every float value! This brings us to another question: what is the dimension of the vector space of functions? Or, to be concrete, how many real number coordinates are needed to uniquely identify a function? Instead of naming the coordinates of a Vec3 object x, y, and z, you could index them from i = 1 to 3. Likewise, you could index the coordinates of a Vec15 from i = 1 to 15. A function, however, has infinitely many numbers that define it; for instance, the values f(x) for any value of x. In other words, you can think of the coordinates of f as being its values at every point, indexed by all real numbers instead of the first few integers. This means that the vector space of functions is infinite dimensional. This has important implications, but it mostly makes the vector space of all functions hard to work with. We’ll return to this space later, specifically looking at some subsets that are simpler. For now, let’s return to the comfort of finitely many dimensions and look at two more examples.  

### treating matrices as vectors 

Because an n-by-m matrix is a list of nXm numbers, albeit arranged in a rectangle, we can treat it as a nXm-dimensional vector. The only difference between the vector space of, say, 5×3 matrices from the vector space of 15D coordinate vectors is that the coordinates ar presented in a matrix. We still add and scalar multiply coordinate by coordinate. 


<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632065372/5E0109A6-30BC-44B0-9683-C55836524EA9_zedhip.png"/>

Implementing a class for 5×3 matrices inheriting from Vector is more typing than simply implementing a Vec15 class because you need two loops to iterate over a matrix. The arithmetic, however, is no more complicated than as that shown in this listing.  

You could just as well create a Matrix2_by_2 class or a Matrix99_by_17 class to represent different vector spaces. In these cases, much of the implementation would be the same, but the dimensions would no longer be 15, they would be 2 · 2 = 4 or 99 · 17 = 1,683. As an exercise, you can create a Matrix class inheriting from Vector that includes all the data except for specified numbers of rows and columns. Then any `MatrixM_by_N` class could inherit from Matrix.

The interesting thing about matrices isn’t that they are numbers arranged in grids, but rather that we can think of them as representing linear functions. We already saw that *lists of numbers and functions are two cases of vector spaces, but it turns out that matrices are vectors in both senses.* If a matrix A has n rows and m columns, it represents a linear function from m dimensional space (columns) to n-dimensional space (rows). (You can write A : `ℝm → ℝn` to say this same sentence in mathematical shorthand.) Just as we added and scalar-multiplied functions from `ℝ → ℝ`, so can we add and scalar multiply functions from `ℝm → ℝn`. In a mini-project at the end of this section, you can try running the
vector space unit tests on matrices to check they are vectors in both senses. That doesn’t mean grids of numbers aren’t useful in their own right; sometimes we don’t care to interpret them as functions. For instance, we can use arrays of numbers to represent images.

### manipulating images with vector operations

On a computer, images are displayed as arrays of colored squares called pixels. A typical image can be a few hundred pixels tall by a few hundred pixels wide. In a colour image, three numbers are needed to specify the red, green, and blue (RGB) content of the colour of any given pixel In total, a 300x300 pixel image is specified by 300 · 300 · 3 = 270,000 numbers. When thinking of images of this size as vectors, the pixels live in a 270,000-dimensional space! .  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632066198/AD078849-0BB8-4F6A-8F3B-C0806149368C_v1793n.png"/>

Depending on what format you’re reading this, you may or may not see the pink color of Melba’s tongue. But because we’ll represent colour numerically rather than visually in this discussion, everything should still make sense. You can also see the pictures in full color in the source code for this book.

Python has a de-facto standard image manipulation library, PIL, which is distributed in pip under the package name pillow. You won’t need to learn much about the library because we immediately encapsulate our use of it inside a new class (listing 6.3). This class, ImageVector, inherits from Vector, stores the pixel data of a 300x300 image, and supports addition and scalar multiplication.  



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632067282/97E516D5-B37B-4AB5-877F-E3F96AA81C7F_izmiwa.png"/>



While any ImageVector is valid, the minimum and maximum color values that render as visually different are 0 and 255, respectively. Because of this, the negative of any image you import will be black, having gone below the minimum brightness at every pixel. Likewise, positive scalar multiples quickly become washed out with most pixels exceeding the maximum displayable brightness. <img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632067282/24D8EEF0-E073-47F6-867E-6A78A62BE7B2_izvk6e.png"/>

Vector arithmetic is clearly a general concept: the defining concepts of addition and scalar multiplication apply to numbers, coordinate vectors, functions, matrices, images, and many other kinds of objects. It’s striking to see such visual results when we apply the same math across unrelated domains. We’ll keep all of these examples of vector spaces in mind and continue to explore the generalizations we can make across them.  

## 6.3 looking for smaller vector spaces



The vector space of 300x300 color images has a whopping 270,000 dimensions, meaning we need to list as many numbers to specify any image of that size. This isn’t a problematic amount of data on its own, but when we have larger images, a large quantity of images, or thousands of images chained together to make a movie, the data can add up. 



In this section, we look at how to start with a vector space and find smaller ones (having fewer dimensions) that retain most of the interesting data from the original space. With images, we can reduce the number of distinct pixels used in an image or convert it to black and white. The result may not be beautiful, but it can still be recognizable. For instance, the image on the right in figure 6.12 takes 900 numbers to specify, compared to the 270,000 numbers to specify the
image on the left.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632121592/5BC6285D-9884-4D2A-809C-4BCD849064CF_orrmxr.png"/>



Pictures that look like the one on the right live in a 900-dimensional subspace of a 270,000- dimensional space. That means that they are still 270,000-dimensional image vectors, but they can be represented or stored with only 900 coordinates. This is a starting point for a study of compression. We won’t go too deep into the best practices of compression, but we will take a close look at subspaces of vector spaces.  

### identifying subspaces

vector subspace, or subspace for short, is just what it sounds like: a vector space that exists inside another vector space. One example we’ve looked at a few times already is the 2D x,y plane within 3D space as the plane where z = 0. To be specific, the subspace consists of vectors of the form (x, y, 0). These vectors have three components, so they are veritable 3D vectors, but they form a subset that happens to be constrained to lie on a plane. For that reason, we say this is a 2D subspace of `ℝ3`.

NOTE: At the risk of being pedantic, the 2D vector space `ℝ2`, which consists of the ordered pairs (x, y), is not
technically a subspace of 3D space `ℝ3`. That’s because vectors of the form (x, y) are not 3D vectors. However, it
has a one-to-one correspondence with the set of vectors (x, y, 0), and vector arithmetic looks the same whether
or not the extra zero z-coordinate is present. For these reasons, I consider it okay to call `ℝ2` a subspace of `ℝ3`.
Not every subset of 3D vectors is a subspace. The plane where z = 0 is special because the vectors (x, y, 0) form a self-contained vector space. 

There’s no way to build a linear combination of vectors in this plane that somehow “escapes” it; the third coordinate always remains zero. In math lingo, the precise way to say that a subspace is **self-contained** is to say *it is closed under linear combinations*.

To get the feel for what a vector subspace looks like in general, let’s search for subsets of vector spaces that are also subspaces (figure 6.13). What subsets of vectors in the plane can make a standalone vector space? 



> Can we just draw any region in the plane and only take vectors that live within it?  
>
> The answer is no: the subset in figure 6.13 contains some vectors that lie on the x-axis and some that live on the y-axis. These can respectively be scaled to give us the standard basis vectors e1 = (1, 0) and e2 = (0, 1). From these vectors, we can make linear combinations to get to any point in the plane, not only the ones in S (figure 6.14). 



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632122013/6F2947C9-E625-4C9A-9F6D-73EAD392EB0F_qz1rju.png"/>



> we can reach any point in R2 opposed to the previous example where we were contained to R2 within R3



Instead of drawing a random subspace, let’s mimic the example of the plane in 3D. There is no z-coordinate, so let’s instead choose the points where y = 0. This leaves us with the points on the x-axis, having the form (x, 0). No matter how hard we try, we can’t find a linear combination of vectors of this form that have a non-zero y-coordinate (figure 6.15).  



> here we do have a subspace because we are constrained within R1 in an R2 vector space

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632122158/51DCBB25-BB58-49A1-908D-47DF773EC607_dk0lsx.png"/>

This line, y = 0, is a vector subspace of `ℝ2`. As we originally found a 2D subspace of 3D, we also have found a 1D subspace of 2D. Instead of a 3D space or a 2D plane, a 1D vector space like this is called a line. In fact, we can identify this subspace as the real number line `ℝ`.  



The next step could be to set x = 0 as well. Once we’ve set both x = 0 and y = 0 to zero, there’s only one point remaining: the zero vector. This is a vector subspace as well! No matter how you take linear combinations of the zero vector, the result is the zero vector. This is a zerodimensional subspace of the 1D line, the 2D plane, and the 3D space. Geometrically, a zerodimensional subspace is a point, and that point has to be zero. If it were some other point, v for instance, it would also contain 0 · v = 0 and an infinity of other different scalar multiples like 3 · v and -42 · v. Let’s run with this idea.  



### starting with a single vector

A vector subspace containing a non-zero vector v contains (at least) all of the scalar multiples of v. Geometrically, the set of all scalar multiples of a non-zero vector v lie on a line through the origin as shown in figure 6.16.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632122297/58FAFD5F-92F5-4D38-9C93-BFD3DB5C0CEB_vtggec.png"/>

Each of these lines through the origin is a vector space. you can't escape any line by adding or scaling vectors that lie in it. the same goes for lines through the origin in 3D: they are all of the linear combinations of a single 3D vector, and they form a vector space. This is the first example of a general way of building subspaces: picking a vector and seeing all of the linear combinations that must come with it.  



### spanning bigger space

Given a set of one or more vectors, their **span** is defined as the set of all linear combinations. The important part of the span is that *it’s automatically a vector subspace*. 

To rephrase what we just discovered, the span of a single vector v is a line through the origin. We denote a **set** of
objects by including them in curly braces, so the set containing only v is `{v}`, and the span of this set could be written `span({v})`.

As soon as we include another vector w, which is **not parallel** to v, the space gets bigger because we are no longer constrained to a single linear direction. The span of the set of two vectors `{v,w}` includes two lines, `span({v})` and `span({w})`, as well as linear combinations including both v and w, which lie on neither line (figure 6.17).  

> once we have 2 non parallel vectors we can reach any point in the plane with a linear combination
>
> entire-plane = span({v,w})
>
> most strikingly for the standard basis vectors. Any point (x, y) can be reached as the linear combination 
> $$
> x · (1, 0) + y · (0, 1).
> $$
> 

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632123135/092AB3E2-EDDC-42A0-ADEA-523A1ED4705B_p6onvz.png"/>

A single non-zero vector spans a line in 2D or 3D, and it turns out, two non-parallel vectors can span either the whole 2D plane or a plane passing through the origin in 3D space. 



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632123362/79F2929C-214F-47AE-955A-4A1B6EB41815_ockfz1.png"/>



It’s slanted, so it doesn’t look like the plane where z = 0, and it doesn’t contain any of the three standard basis vectors. But it’s still a plane and a vector subspace of 3D space. One vector spans a 1D space, and two non-parallel vectors span a 2D space. If we add a third non-parallel vector to the mix, do the three vectors span a 3D space? Figure 6.20 shows that clearly the answer is no.  *because the keep living in 2d space and thus we can't adjust our 3th dimension*

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632123467/4EFAB8AF-ED74-45B2-A7FE-4473D931371E_bg7ws7.png"/>



No pair of the vectors u, v, and w is parallel, but these vectors don’t span a 3D space. They all live in the 2D plane, so no linear combination of them can magically obtain a z-coordinate. We need a better generalization of the concept of **“non-parallel” vectors**.  



If we want to add a vector to a set and span a higher dimensional space, the new vector needs to point in a new direction that isn’t included in the span of the existing ones. In the plane, three vectors always have some redundancy. For instance, as shown in figure 6.21, a linear combination of u and w gives us v.  



<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632123582/50FA0259-22DA-413A-A3ED-05E42CF25C62_rlufti.png"/>



The right generalization of **“non-parallel”** is **“linearly independent.”** 

> A collection of vectors is **linearly dependent** if any of its members can be obtained as a linear combination of the others.

Two parallel vectors are linearly dependent because they are scalar multiples of each other. Likewise, the set of three vectors `{u, v, w}` is linearly dependent because we can make v out of a linear combination of u and w (or w out of a linear combination of u and v, and so on).

You should make sure to get a feel for this concept yourself. As one of the exercises at the end of this section, you can check that any of the three vectors (1, 0), (1, 1) and (-1, 1) can be written as a linear combination of the other two.


$$
\vec{a}=\begin{bmatrix}
    1 \\
    0
\end{bmatrix}
\\
\vec{b}=\begin{bmatrix}
    1 \\
    1
\end{bmatrix}
\\
\vec{c}=\begin{bmatrix}
    -1 \\
    1
\end{bmatrix}
\\
\begin{bmatrix}
    1 \\
    0
\end{bmatrix} = x\begin{bmatrix}
    1 \\
    1
\end{bmatrix} + y\begin{bmatrix}
    -1 \\
    1
\end{bmatrix}
\\
\vec{a} = \begin{bmatrix}
    -1 \\
    -1
\end{bmatrix} \begin{bmatrix}
    2 \\
    2
\end{bmatrix}
$$

By contrast, the `set {u,v}` is **linearly independent** because the components are non-parallel and cannot be scalar multiples of one another. This means that u and v span a bigger space than either on its own. Similarly, the **standard basis** `{e1, e2, e3}` for `ℝ3` is a **linearly independent** set. None of these vectors can be built as a linear combination of the other two, and all three are required to span 3D space. We’re starting to get at the properties of a vector space or subspace that indicate its dimension.  

### defining the word dimensions

Here’s a motivational question: is the following set of 3D vectors linearly independent? 

`{(1, 1, 1), (2, 0, -3), (0, 0, 1), (-1, -2, 0)}`



To answer this, you could draw these vectors in 3D or attempt to find a linear combination of three of them to get the fourth. But there’s an easier answer: only three vectors are needed to span all of 3D space, so any list of four 3D vectors has to have some redundancy. We know that a set with one or two 3D vectors will span a line or plane, respectively, rather than all of `ℝ3`. Three is the magic number of vectors that can both span a 3D space and still be
linearly independent. That’s really why we call it three-dimensional: there are three independent directions after all.

A linearly independent set of vectors that spans a whole vector space like `{e1, e2, e3}` for `ℝ3` is called a **basis**. Any basis for a space has the same number of vectors, and that number is its dimension. For instance, we saw (1, 0) and (1, 1) are linearly independent and span the whole plane, so they are a basis for the vector space `ℝ2`. Likewise (1, 0, 0) and (0, 1, 0) are linearly independent and span the plane where z = 0 in ℝ3. That makes them a basis for this 2D subspace, albeit not a basis for all of ℝ3.

I have already used the word basis in the context of the “standard basis” for `ℝ2` and for `ℝ3`. These are called “**standard**” because they are such natural choices. It takes no computation to decompose a coordinate vector in the **standard basis**; the coordinates are the scalars in this decomposition. For instance, (3, 2) means the linear combination 
$$
3 * (1, 0) + 2 * (0, 1) \\ 3e1 + 2e2.
$$

In general, deciding whether vectors are linearly independent requires some work. Even if you know that a vector is a linear combination of some other vectors, finding that linear combination requires doing some algebra. In the next chapter, we cover how to do that; it ends up being a ubiquitous computational problem in linear algebra. But before that let’s get in some more practice identifying subspaces and measuring their dimensions.  

> in the next chapter we will see how to find the right scalar to get a given coordinate using **standard vectors**

### finding subspaces of the vector space of functions

Mathematical functions from `ℝ` to `ℝ` contain an infinite amount of data, namely the output value when they are given any of infinitely many real numbers as inputs. That doesn’t mean that it takes infinite data to describe a function though. For instance, a linear function requires only two real numbers. They are the values of a and b in this general formula that you’ve probably seen: f(x) = ax + b

where a and b can be any real number. This is much more tractable than the infinite-dimensional space of all functions. Any linear function can be specified by two real numbers, so it looks like the subspace of linear functions will be 2D. 

CAUTION: I’ve used the word linear in a lot of new contexts in the last few chapters. Here, I’m returning to a meaning you used in high school algebra: a **linear function** is a function whose graph is a straight line. Unfortunately, functions of this form are not linear in the sense we spent all of chapter 4 discussing (linear transformations that preserve scalar multiplication and vector addition), and you can prove it yourself in an exercise. Because of this, I’ll try to be clear as to which sense of the word linear I’m using at any point.


$$
 f(x) = ax + b \\
 s f(x) =  f(sx) \ ? \text{ no this is different}\\
 f(x + y) =  f(x) + f(y) \ ? \text{ no this is different} 
$$
We can quickly implement a `LinearFunction` class inheriting from Vector. Instead of holding a function as its underlying data, it can hold two numbers for the coefficients a and b. We can add these functions by adding coefficients because:
$$
\text{proof that addition works}\\
(ax + b) + (cx + d) = \\ 
\text{commutative}\\ 
(ax + cx) + (b + d) = \\
\text{distributive}\\ 
(a + c)x + (b + d)\\
\\
\text{proof that scaling works}\\
\text{distributive}\\
r(ax + b) = rax + rb \\
\\
\text{zero function}\\
f(x) = 0 \ (a = b = 0)
$$

```python
class LinearFunction(Vector):
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self,v):
		return LinearFunction(self.a + v.a, self.b + v.b)
	def scale(self,scalar):
		return LinearFunction(scalar * self.a, scalar * self.b)
	def __call__(self,x):
		return self.a * x + self.b
	@classmethod
	def zero(cls):
		return LinearFunction(0,0,0)
```

> We can prove to ourselves that linear functions form a vector subspace of dimension 2 by writing a **basis**. The basis vectors should both be **functions**, they should span the whole space of linear functions, and they should be **linearly independent** (*not multiples of one another* / *not scalar multiples of each other*). Such a set is `{x, 1}` or, more specifically, `{f(x) = x, g(x) = 1}`. Named this way, functions of the form `ax + b` can be written as a linear combination `a · f + b · g`.  

This is as close as we can get to a **standard basis** for linear functions: `f(x) = x` and `f(x) = 1` are clearly different functions, not scalar multiples of one another. By contrast, `f(x) = x` and `h(x) = 4x` are scalar multiples of one another and would not be a linearly independent pair. But `{x, 1}` is not the only basis we could have chosen; `{4x + 1, x - 3}` is also a basis. 

The same concept applies to **quadratic functions** having the form `f(x) = ax2 + bx + c`. These form a 3D subspace of the vector space of functions with one choice of basis being `{x2, x, 1}`. *Linear functions form a vector subspace of the space of quadratic functions where the `x2` component is zero*. Linear functions and quadratic functions are examples of **polynomial functions**, which are *linear combinations of powers of x*; for example, 
$$
f(x) = a0 + a1x + a2x2 + … + an
$$
xn Linear and quadratic functions have degree 1 and 2, respectively, because those are the highest powers of x that appear in each. The polynomial written in the previous equation has degree n and n + 1 coefficients in total. In the exercises, 

> you’ll see that the space of polynomials of any degree forms another vector subspace of the space of functions (of a higher degree).  

### subspace of images

Because our ImageVector objects are represented by 270,000 numbers, we could follow the standard basis formula and construct a basis of 270,000 images, each with one of the 270,000 numbers equal to 1 and all others equal to 0. The listing shows what the first basis vector would look like.

```
// 1D subspace

ImageVector([
    (1,0,0), (0,0,0), (0,0,0), ..., (0,0,0), #<1>
    (0,0,0), (0,0,0), (0,0,0), ..., (0,0,0), #<2>
    ... #<3>
])

// This single vector spans a 1D subspace consisting of the images 
// that are black except for a single, red pixel in the top left corner.
// Scalar multiples of this image could have brighter or dimmer red pixels at this location
```

#1 Only the first pixel in the first row is non-zero: it has a red value of 1. All the other pixels have a value of (0,0,0).
#2 The second row consists of 300 black pixels, each with a value (0,0,0).
#3 I skipped the next 298 rows, but they are all identical to row 2; no pixels have any color values.

to show more pixels, we need more basis vectors. There’s not too much to be learned from writing out these 270,000 basis vectors. Let’s instead look for a small set of vectors that span an interesting subspace. Here’s a single ImageVector consisting of dark gray pixels at every position:  

```
gray = ImageVector([
(1,1,1), (1,1,1), (1,1,1), ..., (1,1,1),
(1,1,1), (1,1,1), (1,1,1), ..., (1,1,1),
...
])
```

More concisely, we could write this instead: `gray = ImageVector([(1,1,1) for _ in range(0,300*300)])`. One way to picture the subspace spanned by the single vector gray is to look at some vectors that belong to it.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632241512/B0CB77C4-894B-4183-AC06-4DFCA2FE2696_k1kvcr.png"/>

This collection of images is “one-dimensional” in the colloquial sense. There’s only one thing changing about them, their brightness. Another way we can look at this subspace is by thinking about the pixel values. In this subspace,
any image has the same value at each pixel. For any given pixel, there is a 3D space of color possibilities measured by red, green, and blue coordinates. *Gray pixels form a 1D subspace of this*, containing points with all coordinates s * (1, 1, 1) for some scalar s 

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632241888/E29B64DD-370A-4A99-A824-5EBF7D6CADD3_apq6rd.png"/>

Each of the images in the basis would be black, except for one pixel that would be a very dim red, green, or blue. Changing one pixel at a time doesn’t yield striking results, so let’s look for smaller and more interesting subspaces. 

There are many subspaces of images you can explore. You could look at solid color images of any color. These would be images of the form:  



```
ImageVector([
(r,g,b), (r,g,b), (r,g,b), ..., (r,g,b),
(r,g,b), (r,g,b), (r,g,b), ..., (r,g,b),
...
])
```

There are no constraints on the pixels themselves; the only constraint on a solid color image is that every pixel is the same. As a final example, you could consider a subspace consisting of low resolution, grayscale images like that shown in figure 6.25.  

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1632242215/88509503-8B7C-47DE-A3AD-8548E137C342_zdspgg.png"/>

Each 10x10 pixel block has a constant gray value across its pixels, making it look like a 30x30 grid. There are only 30 · 30 = 900 numbers defining this image, so images like this one define a 900-dimensional subspace of the 270,000 dimensional space of images. It’s a lot less data, but it’s still possible to create recognizable images. One way to make an image in this subspace is to start with any image and average all red, green, and blue values in each 10x10 pixel block. This average gives you the brightness b, and you can set all pixels in the block to (b, b, b) to build your new image. This turns out to be a linear map (figure 6.26), and you can implement it later as a mini-project.  



