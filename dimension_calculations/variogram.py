import numpy as np
import matplotlib.pyplot as plt

def variogram_dimension(data, lags=None):
    """
    Computes the variogram estimator for fractal dimension from 1D data.
    """
    N = len(data)
    if lags is None:
        lags = np.unique(np.logspace(0, np.log10(N//2), num=10, base=10, dtype=int))
    V = []
    for lag in lags:
        diffs = data[:-lag] - data[lag:]
        V.append(np.mean(diffs**2))
    log_lags = np.log(lags)
    log_V = np.log(V)
    slope, _ = np.polyfit(log_lags, log_V, 1)
    D = 2 - slope / 2
    return lags, V, D

def plot_variogram(lags, V):
    plt.figure()
    plt.loglog(lags, V, 'o-')
    plt.xlabel('Lag')
    plt.ylabel('Variogram')
    plt.title('Variogram/Divider (Richardson plot)')
    plt.show()

