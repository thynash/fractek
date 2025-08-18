import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot_l_system(axiom="A", rules={"A": "AB", "B": "A"}, iterations=7, step=5, angle=90):
    """
    Simple Mandelbrot-like L-system: string evolves according to rules.
    Does not compute Mandelbrot set, but visualizes recursive structure.
    """
    seq = axiom
    for _ in range(iterations):
        next_seq = ""
        for s in seq:
            next_seq += rules.get(s, s)
        seq = next_seq
    x, y, heading = [0], , 0
    for s in seq:
        if s == "A":
            x.append(x[-1] + step * np.cos(np.deg2rad(heading)))
            y.append(y[-1] + step * np.sin(np.deg2rad(heading)))
        elif s == "B":
            heading += angle
    return np.array(x), np.array(y), seq

def plot_mandelbrot_l_system(x, y):
    plt.figure()
    plt.plot(x, y, color='teal')
    plt.axis('equal')
    plt.axis('off')
    plt.title("Mandelbrot L-system (educational)")
    plt.show()

def info_mandelbrot_l_system(seq):
    return {"length": len(seq), "A_count": seq.count("A"), "B_count": seq.count("B")}

