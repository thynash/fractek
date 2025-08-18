import numpy as np
import matplotlib.pyplot as plt

def regular_hexagon(x, y, s, theta=0):
    angles = np.linspace(0, 2*np.pi, 7) + theta
    return x + s * np.cos(angles), y + s * np.sin(angles)

def generate_hexaflake(order=3, x=0, y=0, s=1.0, theta=0):
    """Generate vertices for all hexagons in the Hexaflake."""
    hexes = []
    def recurse(x, y, s, order):
        if order == 0:
            hexes.append(regular_hexagon(x, y, s, theta))
        else:
            recurse(x, y, s/3, order-1)
            for angle in np.linspace(0, 2*np.pi, 7)[:-1]:
                recurse(
                    x + (2*s/3*np.cos(angle)),
                    y + (2*s/3*np.sin(angle)),
                    s/3, order-1)
    recurse(x, y, s, order)
    return hexes

def plot_hexaflake(hexes, ax=None, color='blue'):
    if ax is None:
        _, ax = plt.subplots()
    for hex_x, hex_y in hexes:
        ax.plot(hex_x, hex_y, color=color)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_title("Hexaflake Fractal")
    plt.show()

def info_hexaflake(order):
    return {"order": order, "num_hexagons": 7**order}

