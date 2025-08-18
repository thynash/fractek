import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk(n_steps=10000):
    angles = np.random.uniform(0, 2*np.pi, n_steps)
    x = np.cumsum(np.cos(angles))
    y = np.cumsum(np.sin(angles))
    return x, y

def plot_random_walk(x, y):
    plt.figure()
    plt.plot(x, y, color='maroon')
    plt.axis('equal')
    plt.axis('off')
    plt.title("2D Random Walk")
    plt.show()

def info_random_walk(x, y):
    dist = np.hypot(x[-1] - x[0], y[-1] - y)
    return {'steps': len(x), 'net_distance': float(dist)}

