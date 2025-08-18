import numpy as np
import matplotlib.pyplot as plt

def midpoint_displacement_1d(length=1025, roughness=0.7, seed=None):
    """Simple 1D midpoint displacement (fractal terrain profile)"""
    if seed is not None:
        np.random.seed(seed)
    h = np.zeros(length)
    h[0] = h[-1] = 0
    step = length - 1
    d = 1.0
    while step > 1:
        half = step // 2
        for i in range(half, length-1, step):
            mid = (h[i - half] + h[i + half]) / 2 + np.random.uniform(-d, d)
            h[i] = mid
        step //= 2
        d *= roughness
    return h

def diamond_square(size=129, roughness=0.7, seed=None):
    """Diamond-square/plasma for 2D landscapes; size = 2^n + 1."""
    if seed is not None:
        np.random.seed(seed)
    arr = np.zeros((size, size), dtype=float)
    arr[0,0] = arr[0,-1] = arr[-1,0] = arr[-1,-1] = 0
    side = size-1; d = 1.0
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
        side //= 2; d *= roughness
    arr = (arr - arr.min())/(arr.max()-arr.min())
    return arr

def plot_landscape_1d(h, title="1D Fractal Terrain"):
    plt.figure(figsize=(10,4))
    plt.plot(h, color='peru')
    plt.title(title)
    plt.xlabel("Position")
    plt.ylabel("Height")
    plt.show()

def plot_landscape_2d(arr, cmap='terrain', title="Fractal Landscape"):
    plt.figure(figsize=(7,6))
    plt.imshow(arr, cmap=cmap)
    plt.colorbar()
    plt.title(title)
    plt.axis('off')
    plt.show()

def landscape_stats(arr):
    return {'min': float(arr.min()), 'max': float(arr.max()), 'std': float(arr.std())}

