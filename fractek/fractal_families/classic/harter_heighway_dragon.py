import numpy as np
import matplotlib.pyplot as plt

def generate_harter_heighway_dragon(order=12, step=8):
    seq = 'FX'
    for _ in range(order):
        seq = seq.replace("X", "X+YF+").replace("Y", "-FX-Y")
    x, y, a = [0],[0], 0
    for c in seq:
        if c == 'F':
            x.append(x[-1] + step*np.cos(a))
            y.append(y[-1] + step*np.sin(a))
        elif c == '+':
            a -= np.pi/2
        elif c == '-':
            a += np.pi/2
    return np.array(x), np.array(y)

def plot_harter_heighway_dragon(x, y):
    plt.figure()
    plt.plot(x, y, color='indigo')
    plt.axis('off')
    plt.title("Harter–Heighway Dragon")
    plt.show()

def info_harter_heighway_dragon(order):
    return {'order': order, 'segment_count': 2**order}

