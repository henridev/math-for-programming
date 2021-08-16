from math import sqrt, pi, ceil, floor
from shapes import *
from utils.extract_vectors import extract_vectors
import matplotlib
import matplotlib.patches
from matplotlib.collections import PatchCollection
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim

def draw(*objects, origin=True, axes=True, grid=(1, 1), nice_aspect_ratio=True,
         width=6, save_as=None):

    all_vectors = list(extract_vectors(objects))
    xs, ys = zip(*all_vectors)

    max_x, max_y, min_x, min_y = max(0, *xs), max(0, *ys), min(0, *xs), min(0, *ys)

    # sizing
    if grid:
        x_padding = max(ceil(0.05*(max_x-min_x)), grid[0])
        y_padding = max(ceil(0.05*(max_y-min_y)), grid[1])

        def round_up_to_multiple(val, size):
            return floor((val + size) / size) * size

        def round_down_to_multiple(val, size):
            return -floor((-val - size) / size) * size

        plt.xlim(floor((min_x - x_padding) / grid[0]) * grid[0],
                 ceil((max_x + x_padding) / grid[0]) * grid[0])
        plt.ylim(floor((min_y - y_padding) / grid[1]) * grid[1],
                 ceil((max_y + y_padding) / grid[1]) * grid[1])

    if origin:
        plt.scatter([0], [0], color='k', marker='x')

    if grid:
        plt.gca().set_xticks(np.arange(plt.xlim()[0], plt.xlim()[1], grid[0]))
        plt.gca().set_yticks(np.arange(plt.ylim()[0], plt.ylim()[1], grid[1]))
        plt.grid(True)
        plt.gca().set_axisbelow(True)

    if axes:
        plt.gca().axhline(linewidth=2, color='k')
        plt.gca().axvline(linewidth=2, color='k')

    for o in objects:
        if type(o) == Polygon:
            for i in range(0, len(o.vertices)):
                x1, y1 = o.vertices[i]
                x2, y2 = o.vertices[(i+1) % len(o.vertices)]
                plt.plot([x1, x2], [y1, y2], color=o.color)
            if o.fill:
                xs = [v[0] for v in o.vertices]
                ys = [v[1] for v in o.vertices]
                plt.gca().fill(xs, ys, o.fill, alpha=o.alpha)
        elif type(o) == Points:
            xs = [v[0] for v in o.vectors]
            ys = [v[1] for v in o.vectors]
            plt.scatter(xs, ys, color=o.color)
        elif type(o) == Arrow:
            tip, tail = o.tip, o.tail
            tip_length = (xlim()[1] - xlim()[0]) / 20.
            length = sqrt((tip[1]-tail[1])**2 + (tip[0]-tail[0])**2)
            new_length = length - tip_length
            new_y = (tip[1] - tail[1]) * (new_length / length)
            new_x = (tip[0] - tail[0]) * (new_length / length)
            plt.gca().arrow(tail[0], tail[1], new_x, new_y,
                            head_width=tip_length/1.5, head_length=tip_length,
                            fc=o.color, ec=o.color)
        elif type(o) == Segment:
            x1, y1 = o.start_point
            x2, y2 = o.end_point
            plt.plot([x1, x2], [y1, y2], color=o.color)
        else:
            raise TypeError("Unrecognized object: {}".format(o))

    fig = matplotlib.pyplot.gcf()

    if nice_aspect_ratio:
        coords_height = (ylim()[1] - ylim()[0])
        coords_width = (xlim()[1] - xlim()[0])
        fig.set_size_inches(width, width * coords_height / coords_width)

    if save_as:
        plt.savefig(save_as)

    plt.show()
