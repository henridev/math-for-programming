from draw_model import *


pygame.init()
display = (display_height, display_width)  # 1
window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # 2


light = (1, 2, 3)
clock = pygame.time.Clock()
seconds = 5
degrees_per_second = 360./seconds
degrees_per_millisecond = degrees_per_second / 1000

def rotate_via_clock(milliseconds):
    glRotatef(milliseconds * degrees_per_millisecond, 0, 1, 0)


def initialize_rotating_figure(faces):
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
