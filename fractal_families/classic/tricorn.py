import numpy as np
import matplotlib.pyplot as plt

def generate_tricorn(xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=300):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    Z = np.zeros_like(C)
    output = np.zeros(C.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        output[mask] = i
        Z[mask] = np.conj(Z[mask])**2 + C[mask]
    return output

def plot_tricorn(arr):
    plt.figure()
    plt.imshow(arr, cmap='cubehelix', extent=[-2, 2, -2, 2])
    plt.axis('off')
    plt.title("Tricorn (Mandelbar) Fractal")
    plt.show()

def escape_tricorn(c, max_iter=300):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = np.conj(z)**2 + c
    return max_iter

