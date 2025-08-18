import numpy as np
import matplotlib.pyplot as plt

def generate_pythagoras_tree(order=8, x=0, y=0, size=1, angle=0, heading=np.pi/2):
    lines = []
    def recurse(x, y, size, angle, heading, order):
        if order == 0:
            return
        x1 = x + size * np.cos(heading)
        y1 = y + size * np.sin(heading)
        lines.append(((x, y, x1, y1)))
        recurse(x1, y1, size*np.cos(angle), angle, heading+angle, order-1)
        recurse(x1, y1, size*np.sin(angle), angle, heading-angle, order-1)
    recurse(x, y, size, np.pi/4, heading, order)
    return lines

def plot_pythagoras_tree(lines, ax=None, color='forestgreen'):
    if ax is None:
        _, ax = plt.subplots()
    for (x0, y0, x1, y1) in lines:
        ax.plot([x0, x1], [y0, y1], color=color)
    ax.axis('off')
    ax.set_title("Pythagoras Tree")
    plt.show()

def info_pythagoras_tree(order):
    return {"order": order, "segments": 2**order-1}

