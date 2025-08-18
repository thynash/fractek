import numpy as np

def complex_abs(z):
    """Return the absolute value (modulus) of a complex number or array."""
    return np.abs(z)

def complex_arg(z):
    """Return the argument (angle) of a complex number or array."""
    return np.angle(z)

def complex_pow(z, power):
    """Raise a complex number or array to a given real or complex power."""
    return np.power(z, power)

def complex_conj(z):
    """Return the complex conjugate."""
    return np.conjugate(z)

def complex_distance(z1, z2):
    """Euclidean distance between complex points (can be arrays)."""
    return np.abs(z1 - z2)

def mandelbrot_iter(c, max_iter=100):
    """Classic Mandelbrot escape-time (for any complex c)."""
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iter

def julia_iter(z0, c, max_iter=100):
    """Julia escape-time (for any complex start z0)."""
    z = z0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iter

