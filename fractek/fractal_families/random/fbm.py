import numpy as np
import matplotlib.pyplot as plt

def generate_fbm(n=16384, hurst=0.7):
    """Generate 1D fractional Brownian motion."""
    if not (0 < hurst < 1):
        raise ValueError("Hurst parameter must be in (0,1)")
    G = np.zeros(n)
    G[0] = np.random.randn()
    for i in range(1, n):
        G[i] = G[i-1] + np.random.randn() * n**(-hurst)
    return G

def plot_fbm(G, ax=None, color='coral'):
    if ax is None:
        _, ax = plt.subplots()
    ax.plot(np.arange(len(G)), G, color=color)
    ax.set_title("1D Fractional Brownian Motion")
    plt.show()

def info_fbm(G):
    """Returns length, min, max, and a roughness estimate (standard deviation)."""
    return {
        'length': len(G),
        'min': np.min(G),
        'max': np.max(G),
        'roughness': np.std(np.diff(G))
    }

