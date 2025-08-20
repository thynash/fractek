import numpy as np
import matplotlib.pyplot as plt

def generate_gosper_curve(order=2, step=10):
    """Generate points for the Gosper curve (flowsnake)."""
    seq = "A"
    ruleA = "A-B--B+A++AA+B-"
    ruleB = "+A-BB--B-A++A+B"
    for _ in range(order):
        next_seq = ""
        for c in seq:
            if c == "A":
                next_seq += ruleA
            elif c == "B":
                next_seq += ruleB
            else:
                next_seq += c
        seq = next_seq
    x, y, ang = [0],[0], 0
    for s in seq:
        if s in "AB":
            x.append(x[-1] + step*np.cos(np.deg2rad(ang)))
            y.append(y[-1] + step*np.sin(np.deg2rad(ang)))
        elif s == "+":
            ang += 60
        elif s == "-":
            ang -= 60
    return np.array(x), np.array(y)

def plot_gosper_curve(x, y, ax=None, color='lime'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_title("Gosper (Flowsnake) Curve")
    plt.show()

def info_gosper_curve(order):
    sides = 7**order
    return {"order": order, "sides": sides}

