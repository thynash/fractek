# To start off the fractal library development, I'll begin with the Mandelbrot fractal implementation.
# This includes a function to compute the Mandelbrot escape iteration count and a function to generate the Mandelbrot set grid.
# I will also include a simple plot function to visualize the Mandelbrot set as a heatmap.

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter=100):
    """Calculate the escape iteration count for a given complex number c in the Mandelbrot set."""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter=1000):
    """
    Generate a Mandelbrot set matrix corresponding to a rectangular portion of the complex plane.
    Args:
        xmin, xmax, ymin, ymax: floats defining the rectangle in the complex plane.
        width, height: dimensions of the resulting image grid.
        max_iter: maximum iterations for divergence test.
    Returns:
        2D numpy array of escape iteration counts.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_grid = np.empty((height, width), dtype=int)

    for i in range(height):
        for j in range(width):
            c = complex(r1[j], r2[i])
            mandelbrot_grid[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_grid


def plot_mandelbrot(mandelbrot_grid, cmap='hot'):
    """Plot the Mandelbrot set using matplotlib heatmap."""
    plt.figure(figsize=(10, 8))
    plt.imshow(mandelbrot_grid, extent=[-2, 1, -1.5, 1.5], cmap=cmap)
    plt.colorbar(label='Escape Iterations')
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

