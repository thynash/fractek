import numpy as np
import matplotlib.pyplot as plt

def generate_vicsek(order=4):
    """Generate points for the Vicsek fractal."""
    if order == 0:
        return np.array([[0, 0]])
    points = generate_vicsek(order-1)
    scale = 1 / (2 * 1.0)
    offsets = np.array([
        [-1,-1], [0,-1], [1,-1],
        [-1, 0], [0, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
    ]) * scale * (2**(order-1))
    new_points = []
    for (dx,dy) in [[0,0], [1,0], [-1,0], [0,1], [0,-1]]:
        for pt in points:
            new_points.append(pt + np.array([dx,dy]) * (2**(order-1)))
    return np.vstack(new_points)

def plot_vicsek(points, ax=None, color='deepskyblue'):
    if ax is None:
        _, ax = plt.subplots()
    ax.scatter(points[:,0], points[:,1], s=1, color=color)
    ax.axis('equal')
    ax.axis('off')
    ax.set_title("Vicsek Fractal")
    plt.show()

def info_vicsek(order):
    return {"order": order, "points": 5**order}

