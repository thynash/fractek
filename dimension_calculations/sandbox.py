import numpy as np
import matplotlib.pyplot as plt

def sandbox_dimension(points, radii=None, n_centers=200):
    """
    Estimates fractal dimension using the sandbox method (for point clouds).
    """
    N = len(points)
    if radii is None:
        max_dist = np.max(np.linalg.norm(points - np.mean(points, axis=0), axis=1))
        radii = np.logspace(np.log10(max_dist/100), np.log10(max_dist/2), num=10)
    np.random.seed(42)
    center_idx = np.random.choice(N, size=min(n_centers, N), replace=False)
    counts = []
    for r in radii:
        c = 0
        for idx in center_idx:
            dists = np.linalg.norm(points - points[idx], axis=1)
            c += np.sum(dists < r) - 1  # exclude self
        counts.append(c / len(center_idx) if len(center_idx) > 0 else 0)
    log_r = np.log(radii)
    log_counts = np.log(counts)
    slope, _ = np.polyfit(log_r, log_counts, 1)
    return radii, counts, slope  # slope = correlation/sandbox dimension

def plot_sandbox(radii, counts):
    plt.figure()
    plt.loglog(radii, counts, 'o-')
    plt.xlabel('Radius')
    plt.ylabel('Num Points within Radius')
    plt.title('Sandbox Dimension Estimate')
    plt.show()

