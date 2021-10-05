import math
from numpy import mat
import pygame
from random import uniform, randint
from find_intersection import check_if_segments_intersect, slope
from utils import *
from const import *


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0
        self.vx = 0.002
        self.vy = 0.002
        self.velocity = 1
        self.angular_velocity = 0

    def apply_rotation_translation(self, point):
        x, y = rotate2d(self.rotation_angle, point)
        return (self.x + x, self.y + y)

    def transformed(self):
        '''
        Exercise 7.1: Implement a transformed() method on the PolygonModel that returns the points of the model
        translated by the object’s x and y attributes and rotated by its rotation_angle attribute.
        '''
        return [
            self.apply_rotation_translation(point)
            for point in self.points
        ]

    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [
            (points[i], points[(i+1) % point_count])
            for i in range(0, point_count)
        ]

    def does_intersect(self, laser):
        for segment in self.segments():
            if check_if_segments_intersect(segment, laser):
                return True
        return False

    def does_collide(self, other_polygon):
        for segment in self.segments():
            for other_segment in other_polygon.segments():
                if check_if_segments_intersect(segment, other_segment):
                    return True
        return False

    def check_if_in_bounds(self, direction):
        '''
        check if the ship remains in it's required bounds
        '''
        x, y = to_pixels(self.x, self.y)
        if direction == 'up':
            return 0 < y
        if direction == 'down':
            return y < HEIGHT
        if direction == 'right':
            return x < WIDTH
        if direction == 'left':
            return 0 < x

    def move(self, milliseconds):
        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = add((self.x, self.y), (dx, dy))
        self.rotation_angle += self.angular_velocity * milliseconds / 1000.0


class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])

    def laser_segment(self):
        '''
        draw a laser starting from the top of the ship
        '''
        hypothenus = 20. * sqrt(2)
        cos_a = cos(self.rotation_angle)
        sin_a = sin(self.rotation_angle)
        # cos(A) = adjacent / hypothenus
        # sin(A) = opposite / hypothenus
        adjacent = hypothenus * cos_a
        opposite = hypothenus * sin_a
        x, y = self.apply_rotation_translation(self.points[0])  # <2>
        end_x = x + adjacent
        end_y = y + opposite
        return (x, y), (end_x, end_y)

    def move_straight(self, milliseconds):
        '''
        move in the line to which the front of the ship is pointing
        '''
        # cos is the ratio in which we point to the x direction
        self.x += (self.velocity * cos(self.rotation_angle) * milliseconds / 1000.0)
        # sin is the ratio in which we point to the y direction
        self.y += (self.velocity * sin(self.rotation_angle) * milliseconds / 1000.0)


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        vs = [to_cartesian((uniform(0.5, 1.0), 2*pi*i/sides)) for i in range(0, sides)]
        super().__init__(vs)


asteroid_count = 10
ship = Ship()
asteroids = [Asteroid() for _ in range(0, asteroid_count)]

for ast in asteroids:
    ast.x = randint(-9, -1) if randint(0, 1) < 0.5 else randint(1, 9)
    ast.y = randint(-9, -1) if randint(0, 1) < 0.5 else randint(1, 9)


'''
test_coor = (10, 10)
normalized_coor = normalize(
    test_coor,
    MIN_PIXEL_COOR,
    MAX_PIXEL_COOR,
    MIN_CARTESIAN_COOR,
    MAX_CARTESIAN_COOR
)
pixel_coor = from_cartesian_to_pygame_coor(normalized_coor, width=WIDTH, height=HEIGHT)
pixel_coor_classic = to_pixels(test_coor[0], test_coor[1])

print(f'normalized_coor {normalized_coor} pixel_coor {pixel_coor}')
print(f'pixel_coor_classic {pixel_coor_classic}')
'''

'''
Exercise 7.2: Write a function to_pixels(x,y) 
that takes a pair of x- and y-coordinates in the 
square where -10 < x < 10 and -10 < y < 10 
and maps them to the corresponding PyGame x 
and y pixel coordinates, each ranging from 0 to 400.
'''
to_pixel = create_to_pixel(WIDTH, HEIGHT, MIN_PIXEL_COOR, MAX_PIXEL_COOR, MIN_CARTESIAN_COOR, MAX_CARTESIAN_COOR)


def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)

def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)


def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Asteroids!")
    clock = pygame.time.Clock()
    done = False

    def handleArrowMovement(keys, ship, milliseconds):
        if keys[pygame.K_a]:
            if ship.check_if_in_bounds('left'):
                ship.x -= milliseconds * ship.vx

        if keys[pygame.K_d]:
            if ship.check_if_in_bounds('right'):
                ship.x += milliseconds * ship.vx

        if keys[pygame.K_s]:
            if ship.check_if_in_bounds('down'):
                ship.y -= milliseconds * ship.vy

        if keys[pygame.K_w]:
            if ship.check_if_in_bounds('up'):
                ship.y += milliseconds * ship.vy

    def handleRotation(keys, ship, milliseconds):
        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)

    def handleStraightMovement(keys, ship, milliseconds):
        if keys[pygame.K_x]:
            ship.move_straight(milliseconds)

    def handleLaserShooting(keys, ship, asteroids):
        if keys[pygame.K_SPACE]:
            laser = ship.laser_segment()
            draw_segment(screen, *laser)
            for asteroid in asteroids:
                if asteroid.does_intersect(laser):  # <3>
                    asteroids.remove(asteroid)

    while not done:
        clock.tick()

        keys = pygame.key.get_pressed()
        milliseconds = clock.get_time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        handleLaserShooting(keys, ship, asteroids)

        handleRotation(keys, ship, milliseconds)

        handleArrowMovement(keys, ship, milliseconds)

        handleStraightMovement(keys, ship, milliseconds)

        for asteroid in asteroids:
            draw_poly(screen, asteroid, color=GREEN)

        draw_poly(screen, ship, color=BLUE)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
