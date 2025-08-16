import numpy as np
import matplotlib.pyplot as plt

def generate_apollonian(order=4, cx=0, cy=0, r=1):
    """Returns circle list: (cx,cy,r) for Apollonian gasket (approximate, recursive)."""
    circles = []
    def recurse(cx, cy, r, order):
        circles.append((cx, cy, r))
        if order == 0:
            return
        for i in range(3):
            theta = 2*np.pi*i/3
            recurse(cx + r*np.cos(theta), cy + r*np.sin(theta), r/2, order-1)
    recurse(cx, cy, r, order)
    return circles

def plot_apollonian(circles, ax=None, color='magenta'):
    if ax is None:
        _, ax = plt.subplots()
    for cx, cy, r in circles:
        circle = plt.Circle((cx, cy), r, color=color, fill=False, lw=0.7)
        ax.add_patch(circle)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title("Apollonian Gasket")
    plt.show()

def info_apollonian(order):
    n = (3**(order+1)-1)//2
    return {"order": order, "num_circles": n}

