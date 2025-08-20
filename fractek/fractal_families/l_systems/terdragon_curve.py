import numpy as np
import matplotlib.pyplot as plt

def generate_terdragon_curve(order=8, step=8):
    rules = {'F': 'F+F-F'}
    seq = 'F'
    for _ in range(order):
        seq = ''.join(rules.get(c, c) for c in seq)
    x, y, angle = [0],[0], 0
    for move in seq:
        if move == 'F':
            x.append(x[-1] + step * np.cos(np.deg2rad(angle)))
            y.append(y[-1] + step * np.sin(np.deg2rad(angle)))
        elif move == '+':
            angle -= 120
        elif move == '-':
            angle += 120
    return np.array(x), np.array(y)

def plot_terdragon_curve(x, y):
    plt.figure()
    plt.plot(x, y, color='crimson')
    plt.axis('off')
    plt.axis('equal')
    plt.title("Terdragon Curve")
    plt.show()

def info_terdragon_curve(order):
    return {"order": order, "length": 3**order}

