1. As with 2D vectors, 3D vectors can be added, subtracted, and multiplied by scalars. 


```python
def scale(scalar, v):
    return (scalar * coor for coor in v)
def add(*vectors):
    return tuple(map(sum,zip(*vectors)))
def sub(*vectors):
    min_vectors = [(x*-1,y*-1,z*-1) for (x,y,z) in vectors[1:]] 
    min_vectors.insert(0, vectors[0])
    return tuple(map(sum,zip(*min_vectors)))
```

2. We can find their lengths using a 3D analogy of the Pythagorean theorem.

```python
def length(v):
    return sqrt(sum([coor**2 for coor in v]))
```

3. The dot product is a way to multiply two vectors and get a scalar. 

- It measures how aligned two vectors are
- and we can use its value to find the angle between two vectors.

<img src="https://res.cloudinary.com/dri8yyakb/image/upload/v1630505776/Untitled_Diagram-dot-product_2_dnlk7k.png" width=600/>

```python
from math import * ;

# It turns out the dot product is proportional to each of the lengths of its input vectors. If you take
# the dot product of two vectors !!!in the same direction!!!, the dot product is precisely equal to the product of the lengths. 

# dot product equals the sum of the products of point coordinates
def dot(u,v):
    return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])


def lengths_angles_to_dot(length1, length2 ,angle = 0, in_radians = True):
    length1 * length2 * cos(angle if in_radians else radians(angle))

def angle_between_coords(v1, v2, in_radians = True):
    dot_product = dot(*[v1, v2])
    length_v1 = sqrt(v1[0]**2+v1[1]**2)
    length_v2 = sqrt(v2[0]**2+v2[1]**2)
    angle_radians = acos(dot_product / (length_v1 * length_v2))
    angle = angle_radians if in_radians else degrees(angle_radians)
    return angle

angle_between_coords((3,4), (4,3), False)
```

4. The cross product is a way to multiply two vectors and get a third vector that is perpendicular to both input vectors. 

- The magnitude of the output of the cross product is the area of the parallelogram spanned by the two input vectors.

```python
def cross(u, v):
    ux,uy,uz = u
    vx,vy,vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)
```

1. We can represent the surface of any 3D object as a collection of triangles, where each triangle is respectively defined by three vectors representing its vertices.

- Using the cross product, we can decide which direction a triangle is visible from in 3D. This can tell us whether a viewer can see it or how illuminated it is by a given light source.
- By drawing and shading all of the triangles defining an object’s surface, we can make it look three-dimensional