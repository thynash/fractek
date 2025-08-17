import numpy as np
import matplotlib.pyplot as plt
try:
    from noise import pnoise2, pnoise3  # Perlin/Simplex via the 'noise' package
    noise_available = True
except ImportError:
    noise_available = False

#### Perlin Noise ####

def perlin_noise_2d(width, height, scale=10, octaves=1, persistence=0.5, lacunarity=2, seed=None):
    if not noise_available:
        raise ImportError("Please install `noise` package for Perlin/Simplex noise.")
    arr = np.zeros((height, width), dtype=np.float32)
    if seed is None:
        seed = np.random.randint(0, 10000)
    for y in range(height):
        for x in range(width):
            arr[y][x] = pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence,
                                lacunarity=lacunarity, repeatx=width, repeaty=height, base=seed)
    # Normalize to [0,1]
    arr = (arr - arr.min()) / (arr.max() - arr.min())
    return arr

def plot_noise_2d(arr, cmap='cividis', title='Perlin Noise Field'):
    plt.figure(figsize=(7,7))
    plt.imshow(arr, cmap=cmap)
    plt.colorbar()
    plt.axis('off')
    plt.title(title)
    plt.show()

def noise_roughness(arr):
    # Estimate roughness via std of differences
    gy, gx = np.gradient(arr)
    return {'std_grad_x': float(np.std(gx)), 'std_grad_y': float(np.std(gy))}

#### Fractal Brownian Motion using Perlin ####

def fbm_noise_2d(width, height, scale=10, octaves=6, persistence=0.5, lacunarity=2, seed=None):
    """Fractal Brownian Motion (fBm) using summed Perlin noise at multiple frequencies."""
    if not noise_available:
        raise ImportError("Please install `noise` package for Perlin/Simplex noise.")
    arr = np.zeros((height, width), dtype=np.float32)
    amplitude = 1.0
    freq = 1.0
    max_amplitude = 0.0
    for o in range(octaves):
        arr += amplitude * perlin_noise_2d(width, height, scale*freq, octaves=1, seed=seed+o if seed else None)
        max_amplitude += amplitude
        amplitude *= persistence
        freq *= lacunarity
    arr = arr / max_amplitude
    arr = (arr - arr.min()) / (arr.max() - arr.min())
    return arr

def plot_fbm_2d(arr, cmap='plasma', title='fBm (Fractal Brownian Motion) Noise'):
    plt.figure(figsize=(7,7))
    plt.imshow(arr, cmap=cmap)
    plt.colorbar()
    plt.axis('off')
    plt.title(title)
    plt.show()

