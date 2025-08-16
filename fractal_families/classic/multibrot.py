import numpy as np
import matplotlib.pyplot as plt

def generate_multibrot(xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800,
                       power=3, max_iter=300):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    Z = np.zeros(C.shape, dtype=complex)
    output = np.zeros(C.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        output[mask] = i
        Z[mask] = Z[mask]**power + C[mask]
    return output

def plot_multibrot(arr):
    plt.figure()
    plt.imshow(arr, cmap='twilight_shifted', extent=[-2, 2, -2, 2])
    plt.axis('off')
    plt.title('Multibrot Set')
    plt.show()

def escape_multibrot(c, power=3, max_iter=300):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z**power + c
