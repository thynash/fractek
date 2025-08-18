import numpy as np
import matplotlib.pyplot as plt

def generate_plasma_fractal(size=513, roughness=0.7, seed=None):
    if seed is not None:
        np.random.seed(seed)
    arr = np.zeros((size, size), dtype='float64')
    arr[0,0] = arr[0,-1] = arr[-1,0] = arr[-1,-1] = 0
    side = size-1
    d = 1.0
    while side > 1:
        half = side // 2
        for x in range(0, size-1, side):
            for y in range(0, size-1, side):
                avg = (arr[x, y] + arr[x+side, y] + arr[x, y+side] + arr[x+side, y+side]) / 4
                arr[x+half, y+half] = avg + np.random.uniform(-d, d)
        for x in range(0, size, half):
            for y in range((x+half)%side, size, side):
                s = []
                if x-half >= 0: s.append(arr[x-half, y])
                if x+half < size: s.append(arr[x+half, y])
                if y-half >= 0: s.append(arr[x, y-half])
                if y+half < size: s.append(arr[x, y+half])
                arr[x, y] = np.mean(s) + np.random.uniform(-d, d)
        side //= 2
        d *= roughness
    return arr

def plot_plasma_fractal(arr, ax=None, cmap='plasma'):
    if ax is None:
        _, ax = plt.subplots()
    ax.imshow(arr, cmap=cmap)
    ax.set_axis_off()
    ax.set_title("Plasma (Diamond-Square) Fractal")
    plt.show()

def info_plasma_fractal(arr):
    return {"range": (float(np.min(arr)), float(np.max(arr))), "mean": float(np.mean(arr))}

