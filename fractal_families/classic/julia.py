import numpy as np
import matplotlib.pyplot as plt

def generate_julia(width=800, height=800, c=-0.7+0.27015j, max_iter=300, zoom=1):
    x = np.linspace(-2/zoom, 2/zoom, width)
    y = np.linspace(-2/zoom, 2/zoom, height)
    Z = x[:, None] + 1j*y[None, :]
    output = np.zeros(Z.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        output[mask] = i
        Z[mask] = Z[mask]**2 + c
    return output

def plot_julia(arr, ax=None, cmap='inferno'):
    if ax is None:
        _, ax = plt.subplots()
    ax.imshow(arr, cmap=cmap, extent=[-2,2,-2,2])
    ax.set_axis_off()
    ax.set_title("Julia Set")
    plt.show()

def info_julia(arr):
    return {"max_iter_point": int(np.max(arr)), "pixels": int(arr.size)}

