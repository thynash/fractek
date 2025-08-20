import numpy as np
import matplotlib.pyplot as plt

def generate_sierpinski_arrowhead(order=6, step=10):
    rules = {'A': 'B-A-B', 'B': 'A+B+A'}
    seq, angle, state = 'A', 60, 0
    for _ in range(order):
        seq = ''.join([rules[c] if c in rules else c for c in seq])
    x, y, a = [0], [0], 0
    for c in seq:
        if c in 'AB':
            x.append(x[-1] + step*np.cos(np.deg2rad(a)))
            y.append(y[-1] + step*np.sin(np.deg2rad(a)))
        elif c == '+':
            a += angle
        elif c == '-':
            a -= angle
    return np.array(x), np.array(y)

def plot_sierpinski_arrowhead(x, y):
    plt.figure()
    plt.plot(x, y, color='purple')
    plt.axis('off')
    plt.axis('equal')
    plt.title("Sierpinski Arrowhead Curve")
    plt.show()

def info_sierpinski_arrowhead(order):
    return {"order": order, "segments": 2**order}

