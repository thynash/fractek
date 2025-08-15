import numpy as np
import matplotlib.pyplot as plt

def generate_sierpinski_triangle(n_points=10000):
    """Generates Sierpinski triangle points."""
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    x, y = np.zeros(n_points), np.zeros(n_points)
    x[0], y = 0.5, 0.25
    for i in range(1, n_points):
        j = np.random.randint(0, 3)
        x[i] = (x[i-1] + vertices[j, 0]) / 2
        y[i] = (y[i-1] + vertices[j, 1]) / 2
    return x, y

def plot_sierpinski_triangle(x, y, ax=None, color='purple'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, '.', color=color, markersize=0.2)
    ax.set_aspect('equal')
    ax.set_title("Sierpinski Triangle (Chaos Game)")
    ax.axis('off')
    plt.show()

def info_sierpinski_triangle(n_points, x, y):
    """Returns centroid and area approximation (bounding-box method)."""
    centroid = (np.mean(x), np.mean(y))
    area = (np.max(x) - np.min(x)) * (np.max(y) - np.min(y))
    return {'n_points': n_points, 'centroid': centroid, 'bounding_box_area': area}

