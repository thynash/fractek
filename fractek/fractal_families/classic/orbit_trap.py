import numpy as np
import matplotlib.pyplot as plt

def generate_orbit_trap(xmin=-2, xmax=2, ymin=-2, ymax=2, width=800, height=800, max_iter=300, trap_type='line'):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j*Y
    Z = np.zeros_like(C)
    output = np.zeros(Z.shape, dtype=float)
    for i in range(1,max_iter+1):
        Z = Z**2 + C
        if trap_type == 'line':
            output = np.minimum(output+(np.abs(Z.real)), np.max(output))
        elif trap_type == 'circle':
            output = np.minimum(output+np.abs(np.abs(Z)-0.5), np.max(output))
    return output

def plot_orbit_trap(arr):
    plt.figure()
    plt.imshow(arr, cmap='cool', extent=[-2,2,-2,2])
    plt.axis('off')
    plt.title("Orbit Trap Fractal")
    plt.show()

def info_orbit_trap(arr):
    return {'min': float(np.min(arr)), 'max': float(np.max(arr)), 'mean': float(np.mean(arr))}

