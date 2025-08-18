import numpy as np
import matplotlib.pyplot as plt

def generate_levy_c(order=12, x0=0, y0=0, x1=1, y1=0):
    """Recursively generates the points of a Lévy C curve."""
    def recurse(x0, y0, x1, y1, order):
        if order == 0:
            return [(x0, y0), (x1, y1)]
        else:
            xm = (x0 + x1)/2 + (y1 - y0)/2
            ym = (y0 + y1)/2 - (x1 - x0)/2
            return (recurse(x0, y0, xm, ym, order-1)[:-1] +
                    recurse(xm, ym, x1, y1, order-1))
    points = recurse(x0, y0, x1, y1, order)
    return np.array(points).T  # (x, y) arrays

def plot_levy_c(x, y, ax=None, color='magenta'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title("Lévy C Curve")
    plt.show()

def info_levy_c(order):
    """Returns number of segments and total path length."""
    num_segments = 2**order
    length = (np.sqrt(2)/2)**order
    return {'order': order, 'segments': num_segments, 'scaling_total_length': length}

