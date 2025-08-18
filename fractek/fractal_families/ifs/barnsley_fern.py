import numpy as np
import matplotlib.pyplot as plt

def generate_barnsley_fern(n=100000):
    """Generates Barnsley Fern points (x, y arrays)."""
    coeffs = [
        (0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01),
        (0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85),
        (0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07),
        (-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07)
    ]
    p = [c[-1] for c in coeffs]
    x, y = np.zeros(n), np.zeros(n)
    for i in range(1, n):
        r = np.random.random()
        cum_prob = np.cumsum(p)
        for j, cp in enumerate(cum_prob):
            if r < cp:
                a, b, c, d, e, f, _ = coeffs[j]
                x[i] = a * x[i-1] + b * y[i-1] + e
                y[i] = c * x[i-1] + d * y[i-1] + f
                break
    return x, y

def plot_barnsley_fern(x, y, ax=None, color='green'):
    """Plots the Barnsley Fern from x, y arrays."""
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 6))
    ax.plot(x, y, '.', color=color, markersize=0.2)
    ax.set_title("Barnsley Fern (IFS)")
    ax.axis('off')
    plt.show()

def info_barnsley_fern(x, y):
    """Returns bounding box and estimated 'spread' of the fern."""
    min_x, max_x = np.min(x), np.max(x)
    min_y, max_y = np.min(y), np.max(y)
    spread = np.sqrt((max_x - min_x)**2 + (max_y - min_y)**2)
    return {'min_x': min_x, 'max_x': max_x, 'min_y': min_y, 'max_y': max_y, 'spread': spread}

