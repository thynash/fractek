import numpy as np
import matplotlib.pyplot as plt

def generate_brownian_tree(size=200, steps=20000):
    grid = np.zeros((size, size), dtype=bool)
    grid[size//2, size//2] = True
    for s in range(steps):
        x, y = np.random.randint(0, size, 2)
        while not grid[x, y]:
            x0, y0 = x, y
            direction = np.random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up': y = min(y+1, size-1)
            elif direction == 'down': y = max(y-1, 0)
            elif direction == 'left': x = max(x-1, 0)
            elif direction == 'right': x = min(x+1, size-1)
            if grid[x, y]:
                grid[x0, y0] = True
                break
    return grid

def plot_brownian_tree(grid, ax=None, color='purple'):
    if ax is None:
        _, ax = plt.subplots()
    ax.imshow(grid, cmap='magma', origin='lower')
    ax.set_title("Brownian Tree (DLA)")
    ax.axis('off')
    plt.show()

def info_brownian_tree(grid):
    return {"occupied_cells": np.sum(grid)}

