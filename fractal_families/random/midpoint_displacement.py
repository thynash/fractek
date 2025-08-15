import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_terrain(n=1025, roughness=0.5, seed=None):
    """Generate a 1D fractal terrain using midpoint displacement."""
    if seed is not None:
        np.random.seed(seed)
    h = [0] * n
    h, h[-1] = 0, 0
    step = n - 1
    d = 1.0
    while step > 1:
        half = step // 2
        for i in range(half, n - 1, step):
            mid = (h[i - half] + h[i + half]) / 2 + np.random.uniform(-d, d)
            h[i] = mid
        for i in range(0, n-1, half):
            next_i = (i + half) % (n-1)
            if h[i + half] == 0:
                h[i + half] = (h[i] + h[next_i]) / 2 + np.random.uniform(-d, d)
        step //= 2
        d *= roughness
    return np.arange(n), np.array(h)

def plot_fractal_terrain(x, y, ax=None, color='teal'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_title("Fractal Terrain (Midpoint Displacement)")
    plt.show()

def info_fractal_terrain(y):
    """Returns terrain roughness (std of differences)."""
    return {'min': np.min(y), 'max': np.max(y), 'roughness': np.std(np.diff(y))}

