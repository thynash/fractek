import numpy as np

def normalize(arr):
    """Normalize a numpy array to [0,1]."""
    arr = np.asarray(arr)
    minv, maxv = arr.min(), arr.max()
    return (arr - minv) / (maxv - minv) if maxv > minv else arr * 0

def random_seed(seed=None):
    """Set numpy random seed if provided."""
    if seed is not None:
        np.random.seed(seed)

def ensure_shape(arr, shape):
    """Reshape arr to shape if possible."""
    return np.reshape(arr, shape)

def ensure_type(arr, dtype):
    """Convert array to dtype."""
    return np.array(arr, dtype=dtype)

def safe_int(x, default=0):
    """Convert to int, or return default."""
    try:
        return int(x)
    except Exception:
        return default

def safe_float(x, default=0.0):
    """Convert to float, or return default."""
    try:
        return float(x)
    except Exception:
        return default

