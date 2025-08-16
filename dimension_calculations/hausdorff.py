import numpy as np

def hausdorff_dimension(points, min_scale=1e-2, max_scale=1, num_scales=10):
    """
    Estimates the Hausdorff dimension by covering a point set with balls (epsilon-nets).
    """
    scales = np.logspace(np.log10(min_scale), np.log10(max_scale), num=num_scales)
    counts = []
    for eps in scales:
        covered = set()
        for p in points:
            key = tuple(np.round(np.array(p)/eps))
            covered.add(key)
        counts.append(len(covered))
    # Linear regression on log-log scale
    log_scales = np.log(1/scales)
    log_counts = np.log(counts)
    coeffs = np.polyfit(log_scales, log_counts, 1)
    dimension = coeffs[0]
    return scales, counts, dimension

