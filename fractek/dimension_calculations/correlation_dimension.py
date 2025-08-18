import numpy as np

def correlation_dimension(points, r_values=None):
    """
    Computes correlation dimension of a point cloud by counting pairs within radius r.
    """
    if r_values is None:
        max_dist = np.max(points) - np.min(points)
        r_values = np.logspace(np.log10(max_dist/100), np.log10(max_dist/2), num=10)
    N = len(points)
    C = []
    for r in r_values:
        pairs = 0
        for i in range(N):
            for j in range(i+1, N):
                if np.linalg.norm(points[i]-points[j]) < r:
                    pairs += 1
        C.append(2*pairs/(N*(N-1)))
    log_r = np.log(r_values)
    log_C = np.log(C)
    coeffs = np.polyfit(log_r, log_C, 1)
    d_corr = coeffs[0]
    return r_values, C, d_corr

