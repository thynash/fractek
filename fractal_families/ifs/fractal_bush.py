import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_bush(order=6, x=0, y=0, length=1, angle=np.pi/2, branches=3, spread=np.pi/3):
    lines = []
    def recur(x, y, length, angle, order):
        if order == 0: return
        x1, y1 = x + length*np.cos(angle), y + length*np.sin(angle)
        lines.append(((x, y, x1, y1)))
        for i in range(branches):
            a = angle - spread/2 + i*spread/(branches-1)
            recur(x1, y1, length*0.7, a, order-1)
    recur(x, y, length, angle, order)
    return lines

def plot_fractal_bush(lines):
    plt.figure()
    for (x0, y0, x1, y1) in lines:
        plt.plot([x0, x1], [y0, y1], color='olive')
    plt.axis('off')
    plt.title("Fractal Bush")
    plt.show()

def info_fractal_bush(order, branches):
    return {"order": order, "approx_segments": (branches**order-1)//(branches-1)}

