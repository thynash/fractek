import numpy as np
import matplotlib.pyplot as plt

def box_counting(fractal_image, min_box_size=2, max_box_size=None, sizes=None):
    """
    Computes fractal (box-counting) dimension on a binary 2D array.
    """
    if sizes is None:
        h, w = fractal_image.shape
        max_box_size = min(h, w) if max_box_size is None else max_box_size
        sizes = np.logspace(np.log10(min_box_size), np.log10(max_box_size), num=8, base=10, dtype=int)
    counts = []
    for size in sizes:
        count = 0
        for i in range(0, fractal_image.shape[0], size):
            for j in range(0, fractal_image.shape[1], size):  # <-- Fix here
                if np.any(fractal_image[i:i+size, j:j+size]):
                    count += 1
        counts.append(count)
    return sizes, counts

def plot_box_counting(sizes, counts):
    plt.figure()
    plt.plot(np.log(1/sizes), np.log(counts), 'o-')
    plt.xlabel('log(1/box size)')
    plt.ylabel('log(box count)')
    plt.title('Box Counting Dimension')
    plt.show()

def calc_dimension(sizes, counts):
    log_sizes = np.log(1/np.array(sizes))
    log_counts = np.log(counts)
    coeffs = np.polyfit(log_sizes, log_counts, 1)
    dimension = coeffs[0]
    return dimension

