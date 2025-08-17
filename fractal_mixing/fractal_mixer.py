import numpy as np
import matplotlib.pyplot as plt

def linear_mix(frac1, frac2, alpha=0.5):
    """
    Linear morphing between two arrays (images or point clouds).
    alpha=0: frac1, alpha=1: frac2, 0<alpha<1: blend.
    Works for same shape arrays or point clouds (Nx2 or Nx3).
    """
    if frac1.shape != frac2.shape:
        raise ValueError("Shapes must match to blend.")
    return (1-alpha)*frac1 + alpha*frac2

def set_union(frac1, frac2):
    """
    Union of two point clouds.
    """
    return np.vstack([frac1, frac2])

def set_intersection(frac1, frac2, tol=1e-5):
    """
    Intersection of two point clouds (returns points within tol).
    Useful only if point clouds overlap.
    """
    return np.array([p1 for p1 in frac1 if any(np.all(np.abs(p1-p2)<tol) for p2 in frac2)])

def plot_mixed_fractal(frac, plot_type="scatter", color='magenta'):
    plt.figure()
    if frac.ndim == 2 and frac.shape[1] == 2:
        plt.scatter(frac[:,0], frac[:,1], s=0.5, color=color)
        plt.axis('equal')
    else:
        plt.imshow(frac, cmap='magma')
    plt.title("Mixed Fractal")
    plt.axis('off')
    plt.show()

def weighted_mix(frac1, frac2, weight_map):
    """
    Blend two arrays based on an array of weights (same shape as arrays).
    weight_map = 0 uses frac1, 1 uses frac2, in between is blend.
    """
    if frac1.shape != frac2.shape or frac1.shape != weight_map.shape:
        raise ValueError("All shapes must match.")
    return frac1 * (1 - weight_map) + frac2 * weight_map

def composite_mix(frac_list, weights=None):
    """
    Blend more than two fractals with weights (sum/average).
    """
    n = len(frac_list)
    if weights is None:
        weights = np.ones(n) / n
    result = np.zeros_like(frac_list[0], dtype=float)
    for f, w in zip(frac_list, weights):
        result += f * w
    return result


def swap_checkerboard(frac1, frac2, blocksize=20):
    """
    Swap blocks (checkerboard-style) between two arrays/images.
    """
    h, w = frac1.shape
    result = frac1.copy()
    for i in range(0, h, blocksize):
        for j in range(0, w, blocksize):
            if ((i//blocksize)+(j//blocksize)) % 2 == 1:
                result[i:i+blocksize, j:j+blocksize] = frac2[i:i+blocksize, j:j+blocksize]
    return result

def morph_parameter(frac_func, param1, param2, num_steps, fixed_kwargs):
    """
    Animate morph between two parameter sets via generating a sequence.
    Returns a list of generated fractals across the morph path.
    """
    outs = []
    for t in np.linspace(0, 1, num_steps):
        p = param1 * (1-t) + param2 * t
        outs.append(frac_func(**fixed_kwargs, param=p))
    return outs

def info_mixed_fractal(frac):
    """
    Example: length, shape, etc.
    """
    if frac.ndim == 2:
        return {'num_points': len(frac), 'dimension': frac.shape[asset:1]}
    else:
        return {'shape': frac.shape, 'min': float(frac.min()), 'max': float(frac.max())}

