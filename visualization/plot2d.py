import matplotlib.pyplot as plt
import numpy as np

def plot_fractal_2d(array, extent=(-2,2,-2,2), cmap='inferno', title='2D Fractal', save_path=None, colorbar=True):
    """Show a fractal image or escape-time plot, optionally save/export."""
    fig, ax = plt.subplots(figsize=(8,8))
    im = ax.imshow(array, cmap=cmap, extent=extent, origin='lower')
    if colorbar:
        plt.colorbar(im, ax=ax, shrink=0.7)
    ax.set_title(title)
    ax.axis('off')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_points_2d(points, color='blue', size=0.3, alpha=0.6, title="Fractal Point Cloud", save_path=None):
    plt.figure(figsize=(8, 8))
    plt.scatter(points[:,0], points[:,1], s=size, c=color, alpha=alpha)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.title(title)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

def plot_overlay_2d(arrays, labels=None, colors=None, extent=(-2,2,-2,2), alpha=0.7, title="Overlayed Fractals"):
    """Overlay multiple fractal images (ex: for mixing, comparison)."""
    plt.figure(figsize=(8,8))
    for i, arr in enumerate(arrays):
        cmap = colors[i] if colors is not None else 'inferno'
        plt.imshow(arr, cmap=cmap, extent=extent, origin='lower', alpha=alpha)
    if labels:
        plt.legend(labels)
    plt.title(title)
    plt.axis('off')
    plt.show()

