import numpy as np
import matplotlib.pyplot as plt

def lacunarity(image, scales=None):
    """
    Estimates lacunarity of a binary/fractal image.
    """
    h, w = image.shape
    if scales is None:
        scales = np.array([2, 4, 8, 16, 32, min(h, w)//2])
    L = []
    for s in scales:
        windows = [image[i:i+s, j:j+s].sum()
                   for i in range(0, h-s+1, s)
                   for j in range(0, w-s+1, s)]
        windows = np.array(windows)
        if len(windows) == 0: continue
        mean = np.mean(windows)
        sq_mean = np.mean(windows**2)
        if mean == 0: continue
        L.append(sq_mean / mean**2)
    return scales[:len(L)], L

def plot_lacunarity(scales, L):
    plt.figure()
    plt.plot(scales, L, 'o-')
    plt.xlabel('Box Size')
    plt.ylabel('Lacunarity')
    plt.title('Lacunarity of Fractal')
    plt.show()

