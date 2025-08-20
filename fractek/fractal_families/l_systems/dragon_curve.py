import numpy as np
import matplotlib.pyplot as plt

def generate_dragon_curve(order=10, scale=10):
    """Generate points (x, y) of the Dragon Curve using L-system."""
    seq = "FX"
    for _ in range(order):
        seq = seq.replace("X", "X+YF+").replace("Y", "-FX-Y")
    x, y, angle = [0],[0], 0
    stack = []
    for cmd in seq:
        if cmd == "F":
            x.append(x[-1] + scale * np.cos(angle))
            y.append(y[-1] + scale * np.sin(angle))
        elif cmd == "+":
            angle -= np.pi/2
        elif cmd == "-":
            angle += np.pi/2
    return np.array(x), np.array(y)

def plot_dragon_curve(x, y, ax=None, color='orange'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title("Dragon Curve")
    plt.show()

def info_dragon_curve(x, y):
    """Returns number of segments and path length."""
    segments = len(x) - 1
    plength = np.sum(np.sqrt(np.diff(x)**2 + np.diff(y)**2))
    return {'segments': segments, 'path_length': plength}

