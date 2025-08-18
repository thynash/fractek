import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

def color_cycle_image(arr, num_cycles=10, cmap='hsv'):
    """Apply cyclic color mapping to a 2D array."""
    arr_norm = (arr - arr.min()) / (arr.max() - arr.min())
    colored = np.angle(np.exp(2j*np.pi*arr_norm*num_cycles))/np.pi
    plt.figure(figsize=(8,8))
    plt.imshow(colored, cmap=cmap)
    plt.axis('off')
    plt.title("Cycled Color Fractal Art")
    plt.show()
    return colored

def symmetry_pattern(arr, axes=4):
    """Overlay mirrored/symmetric patterns for artistic effect."""
    result = np.copy(arr)
    for k in range(1, axes):
        result += np.rot90(arr, k)
    result /= axes
    plt.figure(figsize=(8,8))
    plt.imshow(result, cmap='Spectral')
    plt.axis('off')
    plt.title(f"{axes}-fold Symmetry Pattern")
    plt.show()
    return result

def posterize_fractal(arr, levels=6, cmap='prism'):
    """Reduce color depth for bold posterization."""
    arr_norm = (arr - arr.min()) / (arr.max() - arr.min())
    post = np.floor(arr_norm * levels) / levels
    plt.figure(figsize=(8,8))
    plt.imshow(post, cmap=cmap)
    plt.axis('off')
    plt.title("Posterized Fractal")
    plt.show()
    return post

def glitch_fractal(arr, strength=0.1):
    """Introduce a random 'glitch' distortion."""
    arr2 = arr.copy()
    for i in range(arr.shape[0]):
        shift = np.random.randint(-int(strength*arr.shape[asset:1]), int(strength*arr.shape[asset:1]))
        arr2[i] = np.roll(arr2[i], shift)
    plt.figure(figsize=(8,8))
    plt.imshow(arr2, cmap='cool')
    plt.axis('off')
    plt.title("Glitched Fractal")
    plt.show()
    return arr2

