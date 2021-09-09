from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *
from math import *
from vectors import *
from transforms import *
from draw_model import *

import pygame
import matplotlib.cm


def normal(face):
    '''
    3 vectors define a face subtraction defines the vectors between them the cross
    cross product takes the vector perpendicular to it
    '''
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))


blues = matplotlib.cm.get_cmap('Blues')


def shade(face, color_map=blues, light=(1, 2, 3)):
    '''
    the dot product is higher when there is more alignement
    in that case less shading has to be applied
    '''
    return color_map(1 - dot(unit(normal(face)), unit(light)))


light = (1, 2, 3)
faces = [
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
    [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
    [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, 0, 1), (0, 1, 0)],
    [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
]

pygame.init()
display = (display_height, display_width)  # 1
window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # 2


'''
animation = draw the object over and over repeatedly.
render a single frame => we loop through the vectors, decide how to shade them, draw them with OpenGL, and update the frame with PyGame.
'''

# description of perspective looking at the scene => we have a 45° viewing angle and a 1 aspect ratio (the vertical units and the horizontal units display as the same size).
# 0.1 and 50.0 put limits on the z-coordinates that are rendered => objects further than 50.0 units from the observer or closer than 0.1 units will not show up.
gluPerspective(90, 1, 0.1, 50.0)
# indicates that we’ll observe the scene from 5 units up the z-axis,
# meaning wemove the scene down by vector (0, 0, -5).
glTranslatef(0.0, -1.0, -5)
#  turns on an OpenGL option that automatically hides polygons oriented away from the viewer
glEnable(GL_CULL_FACE)
# ensures that we render polygons closer to us on top of those further from us
glEnable(GL_DEPTH_TEST)
# enables an OpenGL option that automatically hides polygons that are facing us but that are behind other polygons.
glCullFace(GL_BACK)

glRotatef(30, 0, 1, 1)

clock = pygame.time.Clock()  # 1

seconds = 5
degrees_per_second = 360./seconds
degrees_per_millisecond = degrees_per_second / 1000


def rotate_via_clock(milliseconds):
    '''
    glRotatef(theta, x, y, z) rotates
    scene by theta about an axis specified by the vector (x, y, z).
    clarify “rotating by an angle about an axis.”
    e.g. Earth rotating in space. The earth rotates by 360° every day or 15° every hour.
    The axis is the invisible line that the Earth rotates around:
    it passes through the North and South poles—the only two points that aren’t rotating.
    For the earth, the axis of rotation is not directly upright, rather it is tilted by 23.5°.
    '''
    glRotatef(milliseconds * degrees_per_millisecond, 1, 0, 0)


def initialize_rotating_octahedron():
    '''
    1. Initializes a clock to measure the advancement of time for PyGame
    2. In each iteration, checks the events PyGame receives and quits if the user closes the window
    3. Indicates to the clock that time should elapse
    4. Instructs OpenGL that we are about to draw triangles
    5. For each vertex of each face (triangle), sets the color based on the shading
    6. Specifies the next vertex of the current triangle
    7. Indicates to PyGame that the newest frame of the animation is ready and makes it visible
    '''
    while True:
        for event in pygame.event.get():  # 2
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            rotate_via_clock(clock.tick())  # 3
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glBegin(GL_TRIANGLES)  # 4
            for face in faces:
                color = shade(face, blues, light)
                for vertex in face:
                    glColor3fv((color[0], color[1], color[2]))  # 5
                    glVertex3fv(vertex)  # 6
            glEnd()
            pygame.display.flip()  # 7
            # print(clock.get_fps())


initialize_rotating_octahedron()


'''
- shading of the four visible sides of the octahedron has not changed => because none of the vectors change: the vertices of the octahedron and the light source are all the same! We have only changed the position of the “camera” relative to the octahedron.

- When we actually change the position of the octahedron, we’ll see the shading change too.

- To animate the rotation of the cube, we can call glRotate with a small angle in every frame.

- rotation rate is only accurate if PyGame draws exactly 60 fps. In the long run,
  this may not be true: if a complex scene requires more than a sixtieth of a second
  to compute all vectors and draw all polygons, the motion actually slows down.

- To keep the motion of the scene constant regardless of the frame rate, we can use **PyGame’s clock**.
  Let’s say we want our scene to rotate by a full rotation (360°) every 5 seconds. PyGame’s clock thinks in milliseconds,
  which are thousandths of a second. For a thousandth of a second, the angle rotated is divided by 1,000:
'''


'''
we could manually identify the vertices of any 3D object, organize them into triples representing triangles, and build the surface as a list of triangles.

an off file is a specification of the polygons that make up the surface of a 3D object and the 3D vectors that are vertices of the polygon. The
teapot.off file looks something like what is shown in this listing.

For the last lines of this file, specifying the faces, the first number of each line tells us what kind of polygon the face is. 

- 3 indicates a triangle
- 4 a quadrilateral (Most of the teapot’s faces turn out to be quadrilaterals)
- 5 a pentagon

*The next numbers on each line tell us the indices of the vertices from the previous lines that form the corners of the given polygon.*

In the file teapot.py in the appendix C source code, you’ll find the functions load_vertices() and load_polygons() that load the vertices and faces (polygons) from the teapot.off file. 

- `load_vertices()` returns a list of 440 vectors, which are all the vertices for the model. (the first lines)  

- `load_polygons()` returns a list of 448 lists, each one containing vectors that are the vertices of one of the 448 polygons making up the model. 

- `load_triangles()`, breaks up the polygons with four or more vertices so that our entire model is built out o triangles.


I’ve left it as a mini-project for you to dig deeper into my code or to try to load the teapot.of
file as well. For now, I’ll continue with the triangles loaded by teapot.py, so we can get to
drawing and playing with our teapot more quickly. The other step I skip is organizing the
PyGame and OpenGL initialization into a function so that we don’t have to repeat it every time
we draw a model. In draw_model.py, you’ll find the following function:
'''

vertices_coor_index_end = 481


def vector_info_string_to_tuple(vector_info_string):
    return tuple(map(lambda x: float(x), vector_info_string.rstrip('\n').split()))


def polygon_info_string_to_list(polygon_info_string):
    return list(map(lambda x: int(x), polygon_info_string.rstrip('\n').split()))


def polygon_indeces_to_vectors(vertices):
    def polygon_indeces_to_vectors_mapper(polygon_info):
        vertice_indeces = polygon_info[1:]
        return [vertices[vertice_index] for vertice_index in vertice_indeces]
    return polygon_indeces_to_vectors_mapper


def triangulate(poly):
    if len(poly) < 3:
        raise Exception("polygons must have at least 3 vertices")
    # elif len(poly) == 3:
    #     return [poly]
    else:
        for i in range(1, len(poly) - 1):
            yield (poly[0], poly[i+1], poly[i])


def load_triangles(polys):
    tris = []
    for poly in polys:
        for tri in triangulate(poly):
            assert(len(tri) == 3)
            for v in tri:
                assert(len(v) == 3)
            tris.append(tri)
    return tris


def draw_teapot():
    with open("teapot.off") as f:
        lines = f.readlines()
        vertex_count, face_count, edge_count = map(int, lines[1].split())
        vertex_start = 2

        vertices = list(map(
            vector_info_string_to_tuple,
            lines[vertex_start:vertex_start+vertex_count]
        ))

        vertices = [
            scale_by(3)(rotate_x_y_by(-pi/2, 0)
                        (translate_by((-0.5, 0, -0.6))(v)))
            for v in vertices
        ]

        polygons = list(map(
            polygon_info_string_to_list,
            lines[vertex_start+vertex_count:vertex_start+vertex_count+face_count]
        ))

        polygon_indeces_to_vectors_mapper = polygon_indeces_to_vectors(
            vertices)

        polygons = list(map(
            polygon_indeces_to_vectors_mapper,
            polygons
        ))

        print(load_triangles(polygons))
        draw_model(load_triangles(polygons))
