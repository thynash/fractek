import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot_l_system(axiom="A", rules=None, iterations=7, step=5, angle=90):
    """
    Simple L-system interpreter for A/B rules.
    String evolves recursively, and is then rendered with turns.
    By default, simulates A->AB, B->A, with left turn on 'B'.
    """
    if rules is None:
        rules = {"A": "AB", "B": "A"}
    seq = axiom
    for _ in range(iterations):
        next_seq = ""
        for s in seq:
            next_seq += rules.get(s, s)
        seq = next_seq

    # Draw using the seq
    x, y = [0],[0] 
    heading = 0
    for s in seq:
        if s == "A" or s == "B":
            x.append(x[-1] + step * np.cos(np.deg2rad(heading)))
            y.append(y[-1] + step * np.sin(np.deg2rad(heading)))
        # Use a turning rule:
        if s == "B":  # Let's turn left for 'B'
            heading += angle
        elif s == "A":  # Or turn right for 'A' (can be changed for variations)
            heading -= angle
    return np.array(x), np.array(y), seq

def plot_mandelbrot_l_system(x, y):
    plt.figure(figsize=(8,8))
    plt.plot(x, y, color='teal')
    plt.axis('equal')
    plt.axis('off')
    plt.title("Mandelbrot L-system (educational)")
    plt.show()

def info_mandelbrot_l_system(seq):
    return {"length": len(seq), "A_count": seq.count("A"), "B_count": seq.count("B")}

