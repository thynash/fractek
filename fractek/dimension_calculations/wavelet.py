import numpy as np
import matplotlib.pyplot as plt
try:
    import pywt
except ImportError:
    pywt = None

def wavelet_dimension(signal, wavelet='db2'):
    """
    Estimates fractal dimension using discrete wavelet transform (DWT).
    """
    if pywt is None:
        raise ImportError("Install pywt (PyWavelets) for wavelet analysis!")
    coeffs = pywt.wavedec(signal, wavelet)
    energies = [np.mean(np.abs(c)**2) for c in coeffs[1:]]
    scales = [2**i for i in range(1, len(coeffs))]
    log_scales = np.log(scales)
    log_energy = np.log(energies)
    slope, _ = np.polyfit(log_scales, log_energy, 1)
    D = 2 - slope / 2
    return scales, energies, D

def plot_wavelet(scales, energies):
    plt.figure()
    plt.plot(np.log(scales), np.log(energies), 'o-')
    plt.xlabel('log(Scale)')
    plt.ylabel('log(Energy)')
    plt.title('Wavelet Power Scaling')
    plt.show()

