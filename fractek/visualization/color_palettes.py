import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def get_palette(palette_name='inferno', n=256):
    return cm.get_cmap(palette_name, n)

def plot_palette(palette_name='inferno', n=256):
    cmap = get_palette(palette_name, n)
    arr = np.linspace(0,1,n)[None, :]
    plt.figure(figsize=(10,1))
    plt.imshow(arr, cmap=cmap, aspect='auto')
    plt.title(palette_name + " palette")
    plt.axis('off')
    plt.show()

def available_palettes():
    return sorted(m for m in plt.colormaps() if not m.endswith("_r"))

