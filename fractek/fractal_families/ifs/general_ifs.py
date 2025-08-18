import numpy as np
import matplotlib.pyplot as plt

def generate_ifs(transforms, probs=None, n_points=100000, start=(0,0)):
    """General IFS point generator."""
    k = len(transforms)
    if probs is None:
        probs = [1/k for _ in range(k)]
    x, y = np.zeros(n_points), np.zeros(n_points)
    x[0], y = start
    cum_prob = np.cumsum(probs)
    for i in range(1, n_points):
        r = np.random.rand()
        for j, cp in enumerate(cum_prob):
            if r < cp:
                a, b, c, d, e, f = transforms[j]
                x[i] = a*x[i-1] + b*y[i-1] + e
                y[i] = c*x[i-1] + d*y[i-1] + f
                break
    return x, y

def plot_ifs(x, y, ax=None, color='black'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, '.', color=color, markersize=0.2)
    ax.axis('off')
    ax.set_title('IFS Fractal')
    plt.show()

def info_ifs(x, y):
    """Returns a bounding box and number of unique points."""
    min_x, max_x = np.min(x), np.max(x)
    min_y, max_y = np.min(y), np.max(y)
    unique_points = len(set(zip(np.round(x, 5), np.round(y, 5))))
    return {'min_x': min_x, 'max_x': max_x, 'min_y': min_y, 'max_y': max_y, 'unique_points': unique_points}

