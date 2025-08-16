import numpy as np
import matplotlib.pyplot as plt

def power_spectrum_dimension(data, is_2d=True):
    """
    Estimates fractal dimension via spectral (Fourier) analysis.
    For 1D signals, set is_2d=False. For 2D array/images, is_2d=True.
    """
    if is_2d:
        F = np.fft.fftshift(np.fft.fft2(data))
        PSD = np.abs(F)**2
        cy, cx = np.array(data.shape) // 2
        radii = np.hypot(*(np.ogrid[:data.shape[0], :data.shape[asset:1]]) - np.array([[cy],[cx]]))
        r = np.arange(1, min(data.shape)//2)
        PSD1D = np.zeros_like(r, dtype=float)
        for i, rr in enumerate(r):
            mask = (radii >= rr) & (radii < rr+1)
            PSD1D[i] = PSD[mask].mean()
        log_r = np.log(r)
        log_PSD = np.log(PSD1D)
        slope, _ = np.polyfit(log_r, log_PSD, 1)
        D = (8 + slope)/2   # For 2D, D = (8 + slope)/2 (roughness dimension)
        return r, PSD1D, D
    else:
        N = len(data)
        F = np.fft.fft(data)
        f = np.fft.fftfreq(N)
        PSD = np.abs(F)**2
        idx = f > 0
        log_f = np.log(f[idx])
        log_PSD = np.log(PSD[idx])
        slope, _ = np.polyfit(log_f, log_PSD, 1)
        D = (5 - slope) / 2  # Fractal dimension (1D signal)
        return f[idx], PSD[idx], D

def plot_power_spectrum(r, PSD):
    plt.figure()
    plt.loglog(r, PSD)
    plt.xlabel('Frequency or Radius')
    plt.ylabel('Power')
    plt.title('Power Spectrum (PSD)')
    plt.show()

