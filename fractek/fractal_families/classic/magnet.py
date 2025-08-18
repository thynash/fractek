import numpy as np
import matplotlib.pyplot as plt

def generate_magnet(xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=100):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    Z = C.copy()
    output = np.zeros(C.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        output[mask] = i
        Z[mask] = (Z[mask]**2 + C[mask] - 1)/(2*Z[mask] + C[mask] - 2)
    return output

def plot_magnet(arr):
    plt.figure()
    plt.imshow(arr, cmap='viridis', extent=[-2,2,-2,2])
    plt.axis('off')
    plt.title("Magnet Fractal")
    plt.show()

def escape_magnet(c, max_iter=100):
    z = c
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = (z**2 + c - 1) / (2*z + c - 2)
    return max_iter

