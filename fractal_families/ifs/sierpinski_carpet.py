import numpy as np
import matplotlib.pyplot as plt

def generate_sierpinski_carpet(order=5):
    """Return x, y points of Sierpinski carpet using IFS approach."""
    n = 3**order
    grid = np.zeros((n, n), dtype=bool)
    def fill(x, y, size):
        if size == 1:
            grid[x, y] = 1
        else:
            step = size//3
            for i in range(3):
                for j in range(3):
                    if (i, j) != (1, 1):  # leave center empty
                        fill(x + i*step, y + j*step, step)
    fill(0, 0, n)
    pts = np.argwhere(grid)
    return pts[:,0], pts[:,1]

def plot_sierpinski_carpet(x, y, ax=None, color='navy'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, '.', color=color, markersize=0.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Sierpinski Carpet")
    plt.show()

def info_sierpinski_carpet(order):
    """Returns number of points/cells remaining."""
    count = 8**order
    return {'order': order, 'black_cells': count}

