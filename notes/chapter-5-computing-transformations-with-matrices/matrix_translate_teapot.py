import camera
import sys
from teapot import load_triangles
from draw_model import draw_model
from transforms import polygon_map, multiply_matrix_vector

def translate_3d(translation):
    def new_function(target):  # 1
        a, b, c = translation
        x, y, z = target
        matrix = ((1, 0, 0, a), (0, 1, 0, b), (0, 0, 1, c), (0, 0, 0, 1))  # 2
        vector = (x, y, z, 1)
        x_out, y_out, z_out, _ = multiply_matrix_vector(matrix, vector)  # 3
        return (x_out, y_out, z_out)
    return new_function

def get_matrix(_t):
    a, b, c = (2, 2, -3)
    return (
        (1, 0, 0, a),
        (0, 1, 0, b),
        (0, 0, 1, c),
        (0, 0, 0, 1)
    )


####################################################################
# this code takes a snapshot to reproduce the exact figure
# shown in the book as an image saved in the "figs" directory
# to run it, run this script with command line arg --snapshot
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_5.36_translated_teapot', [0])
####################################################################

draw_model(load_triangles(), get_matrix=get_matrix, translation_over_time=(2, 2, -3), translation_speed=0.6)
