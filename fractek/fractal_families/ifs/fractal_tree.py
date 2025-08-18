import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_tree(order=8, x=0, y=0, length=1, angle=np.pi/2, angle_delta=np.pi/6):
    lines = []
    def recur(x, y, length, angle, order):
        if order == 0: return
        x1, y1 = x + length*np.cos(angle), y + length*np.sin(angle)
        lines.append(((x, y, x1, y1)))
        recur(x1, y1, length*0.7, angle+angle_delta, order-1)
        recur(x1, y1, length*0.7, angle-angle_delta, order-1)
    recur(x, y, length, angle, order)
    return lines

def plot_fractal_tree(lines):
    plt.figure()
    for (x0, y0, x1, y1) in lines:
        plt.plot([x0, x1], [y0, y1], color='forestgreen')
    plt.axis('off')
    plt.title("Fractal Tree")
    plt.show()

def info_fractal_tree(order):
    return {"order": order, "branches": 2**order-1}

