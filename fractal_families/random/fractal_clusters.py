import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_cluster(size=200, p_fire=0.01, p_growth=0.05, steps=1000):
    forest = np.zeros((size, size), dtype=int)
    for _ in range(steps):
        growth = np.random.rand(size, size) < p_growth
        forest[growth] = 1
        fire = np.random.rand(size, size) < p_fire
        burning = (forest == 1) & fire
        forest[burning] = 0
    return forest

def plot_fractal_cluster(forest):
    plt.figure()
    plt.imshow(forest, cmap='BuGn', origin='lower')
    plt.axis('off')
    plt.title("Fractal Cluster (Forest Fire Model)")
    plt.show()

def info_fractal_cluster(forest):
    return {'trees': int(np.sum(forest))}

