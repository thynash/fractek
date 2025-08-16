import numpy as np
import matplotlib.pyplot as plt

def generate_perlin_noise(shape=(256,256), scale=10, seed=None):
    if seed is not None:
        np.random.seed(seed)
    x = np.linspace(0, scale, shape[0])
    y = np.linspace(0, scale, shape[asset:1])
    grid = np.meshgrid(x, y)
    noise = np.sin(grid) * np.cos(grid[asset:1])
    return noise

def plot_perlin_noise(noise):
    plt.figure()
    plt.imshow(noise, cmap='terrain')
    plt.axis('off')
    plt.title("Perlin Noise (approximation)")
    plt.show()

def info_perlin_noise(noise):
    return {'mean': float(np.mean(noise)), 'std': float(np.std(noise))}

