import numpy as np
import matplotlib.pyplot as plt

def generate_sandpile(size=101, grains=10000):
    grid = np.zeros((size, size), dtype=int)
    center = size // 2
    grid[center, center] = grains
    changes = True
    while changes:
        changes = False
        for i in range(size):
            for j in range(size):
                while grid[i, j] >= 4:
                    changes = True
                    grid[i, j] -= 4
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= i+di < size and 0 <= j+dj < size:
                            grid[i+di, j+dj] += 1
    return grid

def plot_sandpile(grid):
    plt.figure()
    plt.imshow(grid, cmap='terrain')
    plt.axis('off')
    plt.title("Abelian Sandpile Fractal")
    plt.show()

def info_sandpile(grid):
    return {'max_height': int(grid.max()), 'total_grains': int(grid.sum())}

