import numpy as np
import matplotlib.pyplot as plt

def generate_peano_curve(order=2, step=10):
    """Returns X and Y points of the Peano curve."""
    seq = 'X'
    for _ in range(order):
        seq = seq.replace('X', 'XFYFX+F+YFXFY-F-XFYFX')\
                 .replace('Y', 'YFXFY-F-XFYFX+F+YFXFY')
    x, y, ang = [0],[0], 0
    for s in seq:
        if s == 'F':
            x.append(x[-1] + step*np.cos(np.deg2rad(ang)))
            y.append(y[-1] + step*np.sin(np.deg2rad(ang)))
        elif s == '+':
            ang += 90
        elif s == '-':
            ang -= 90
    return np.array(x), np.array(y)

def plot_peano_curve(x, y, ax=None, color='cyan'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title("Peano Curve")
    plt.show()

def info_peano_curve(order):
    seg = 9**order
    return {"order": order, "segments": seg}

