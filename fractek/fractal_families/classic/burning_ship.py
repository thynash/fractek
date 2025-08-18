import numpy as np
import matplotlib.pyplot as plt

def generate_burning_ship(xmin=-2.2, xmax=1.2, ymin=-2.2, ymax=1.2,
                          width=800, height=800, max_iter=200):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    C = np.copy(Z)
    output = np.zeros(Z.shape, dtype=int)
    for i in range(max_iter):
        mask = (np.abs(Z) <= 2)
        output[mask] = i
        Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag))**2 + C[mask]
    return output

def plot_burning_ship(arr):
    plt.figure()
    plt.imshow(arr, cmap='hot', extent=[-2.2, 1.2, -2.2, 1.2])
    plt.axis('off')
    plt.title('Burning Ship Fractal')
    plt.show()

def escape_burning_ship(c, max_iter=200):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = (abs(z.real) + 1j * abs(z.imag))**2 + c
    return max_iter

