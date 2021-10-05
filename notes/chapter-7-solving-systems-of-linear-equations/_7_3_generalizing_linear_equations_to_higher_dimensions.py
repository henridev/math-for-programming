import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import matplotlib.pyplot as plt
from colors import *

def u(x, y):
    return x+y+1
def r(x, y):
    return 2*y-3
def s(x, y):
    return -x+2

def plot_scalar_field(funcs, xmin, xmax, ymin, ymax, xstep=0.25, ystep=0.25, c=None, cmap=cm.coolwarm, alpha=1, antialiased=False):
    fig = plt.figure()
    fig.set_size_inches(7, 7)
    ax = fig.gca(projection='3d')

    for i, f in enumerate(funcs):
        fv = np.vectorize(f)

        # Make data.
        X = np.arange(xmin, xmax, xstep)
        Y = np.arange(ymin, ymax, ystep)
        X, Y = np.meshgrid(X, Y)
        Z = fv(X, Y)

        colors = [blue, red, green]
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cmap, color=colors[i], alpha=alpha,
                               linewidth=0, antialiased=antialiased)


# plot_scalar_field([u, r, s], -5, 5, -5, 5, c=blue, cmap=None, alpha=0.5)
# plt.show()


matrix = np.array(((1, 1, -1), (0, 2, -1), (1, 0, 1)))
vector = np.array((-1, 3, 2))
print(np.linalg.solve(matrix, vector))
