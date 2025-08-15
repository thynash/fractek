import numpy as np
import matplotlib.pyplot as plt

def generate_koch_snowflake(order=4, scale=10):
    """Generates Koch snowflake vertices for given depth/order."""
    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        else:
            p1, p2 = np.array(p1), np.array(p2)
            v = (p2 - p1) / 3
            pA = p1 + v
            pB = p1 + 2 * v
            angle = np.deg2rad(60)
            # triangle apex
            pC = pA + np.dot([[np.cos(angle), -np.sin(angle)],
                              [np.sin(angle), np.cos(angle)]], (v))
            return (koch_curve(p1, pA, order-1)[:-1] +
                    koch_curve(pA, pC, order-1)[:-1] +
                    koch_curve(pC, pB, order-1)[:-1] +
                    koch_curve(pB, p2, order-1))
    # Outer points of triangle with scale
    t = np.sqrt(3) / 2 * scale
    points = [(0, 0), (scale/2, t), (scale, 0)]
    curve = []
    for i in range(3):
        curve += koch_curve(points[i], points[(i+1)%3], order)[:-1]
    curve.append(points[0])
    return np.array(curve)

def plot_koch_snowflake(vertices, ax=None, color='blue'):
    """Plots Koch Snowflake from vertices."""
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Koch Snowflake")
    plt.show()

def info_koch_snowflake(order=4, scale=10):
    """Returns number of sides and approximate total length of the snowflake."""
    sides = 3 * (4 ** order)
    base = scale
    length = base * (4/3) ** order
    return {'order': order, 'sides': sides, 'approx_total_length': length}

