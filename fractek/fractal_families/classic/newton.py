import numpy as np
import matplotlib.pyplot as plt

def generate_newton(width=800, height=800, tolerance=1e-6, max_iter=50):
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    roots = [1, -1, 1j, -1j]
    for i in range(max_iter):
        Z = Z - (Z**4 - 1)/(4*Z**3)
    closest_root = np.argmin([np.abs(Z - r) for r in roots], axis=0)
    return closest_root

def plot_newton(arr):
    plt.figure()
    plt.imshow(arr, cmap='tab10', extent=[-2,2,-2,2])
    plt.axis('off')
    plt.title("Newton Fractal")
    plt.show()

def escape_newton(z0, roots=[1,-1,1j,-1j], tolerance=1e-6, max_iter=50):
    z = z0
    for i in range(max_iter):
        z = z - (z**4 - 1)/(4*z**3)
        if any(abs(z-root)<tolerance for root in roots):
            return i
    return max_iter

