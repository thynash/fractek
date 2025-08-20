import numpy as np
import matplotlib.pyplot as plt

def _hilbert_curve(order, angle=90):
    def L(level):
        if level == 0: return ""
        return "+RF-LFL-FR+"
    def R(level):
        if level == 0: return ""
        return "-LF+RFR+FL-"
    seq = "L"
    for _ in range(order):
        seq = seq.replace("L", L(order)).replace("R", R(order))
    return seq

def generate_hilbert_curve(order=3, step=10):
    seq = _hilbert_curve(order)
    x, y, ang = [0],[0], 0
    for cmd in seq:
        if cmd == "F":
            x.append(x[-1] + step * np.cos(np.deg2rad(ang)))
            y.append(y[-1] + step * np.sin(np.deg2rad(ang)))
        elif cmd == "+":
            ang += 90
        elif cmd == "-":
            ang -= 90
    return np.array(x), np.array(y)

def plot_hilbert_curve(x, y, ax=None, color='brown'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title("Hilbert Curve")
    plt.show()

def info_hilbert_curve(order):
    """Returns number of segments and total path length (unit step)."""
    segments = 2**(2*order) - 1
    length = segments
    return {'order': order, 'segments': segments, 'unit_total_length': length}

