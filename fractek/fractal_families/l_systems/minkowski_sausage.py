import numpy as np
import matplotlib.pyplot as plt

def generate_minkowski_sausage(order=3, step=10):
    rules = {'F': 'FLFRRFLF'}
    seq = 'F'
    for _ in range(order):
        seq = ''.join(rules.get(c, c) for c in seq)
    x, y = [0],[0] 
    angle = 0
    for move in seq:
        if move == 'F':
            x.append(x[-1] + step * np.cos(np.deg2rad(angle)))
            y.append(y[-1] + step * np.sin(np.deg2rad(angle)))
        elif move == 'L':
            angle += 90
        elif move == 'R':
            angle -= 90
    return np.array(x), np.array(y)

def plot_minkowski_sausage(x, y):
    plt.figure()
    plt.plot(x, y, color='orange')
    plt.axis('off')
    plt.axis('equal')
    plt.title("Minkowski Sausage")
    plt.show()

def info_minkowski_sausage(order):
    return {"order": order, "curve_length": 8**order}

