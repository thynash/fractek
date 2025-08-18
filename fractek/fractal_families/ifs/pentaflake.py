import numpy as np
import matplotlib.pyplot as plt

def generate_pentaflake(order=3, scale=1.0, cx=0.0, cy=0.0, heading=0.0):
    """Generates points of the Pentaflake fractal up to a given order."""
    polys = []
    def draw(x, y, length, order, angle):
        if order == 0:
            t = np.linspace(0, 2 * np.pi, 6)
            poly_x = x + length * np.cos(t + angle)
            poly_y = y + length * np.sin(t + angle)
            polys.append((poly_x, poly_y))
        else:
            for a in np.linspace(0, 2 * np.pi, 6)[:-1]:
                dx, dy = (length * np.cos(a), length * np.sin(a))
                draw(x + dx * 1.5, y + dy * 1.5, length / 3, order - 1, angle)
            draw(x, y, length, 0, angle)
    draw(cx, cy, scale, order, heading)
    return polys

def plot_pentaflake(polys, ax=None, color='cyan'):
    if ax is None:
        _, ax = plt.subplots()
    for (x, y) in polys:
        ax.fill(x, y, color=color, alpha=0.2, linewidth=0.5, edgecolor='black')
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title("Pentaflake")
    plt.show()

def info_pentaflake(order):
    num_pentagons = sum(5**n for n in range(order+1))
    return {"order": order, "total_pentagons": num_pentagons}

