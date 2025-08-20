import numpy as np
import matplotlib.pyplot as plt

def generate_binary_tree(order=6, length=50, angle=25):
    """Generates coordinates for a binary tree using simple recursion."""
    coords = []
    def recurse(x, y, heading, depth):
        if depth == 0: return
        x1 = x + length * np.cos(np.deg2rad(heading))
        y1 = y + length * np.sin(np.deg2rad(heading))
        coords.append(((x, y), (x1, y1)))
        recurse(x1, y1, heading - angle, depth - 1)
        recurse(x1, y1, heading + angle, depth - 1)
    recurse(0, 0, 90, order)
    return coords

def plot_binary_tree(coords):
    plt.figure()
    for (p0, p1) in coords:
        plt.plot([p0, p1], [p0[1], p1[1]], color='darkgreen')
    plt.axis('equal')
    plt.axis('off')
    plt.title("Binary Tree (L-system style)")
    plt.show()

def info_binary_tree(order):
    """Returns total segments and terminal leaves."""
    segments = 2**order - 1
    leaves = 2**(order-1) if order>0 else 0
    return {'order': order, 'segments': segments, 'leaves': leaves}

