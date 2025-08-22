import numpy as np

def hausdorff_dimension_general(points, min_boxes=4, max_boxes=32, num_scales=8):
    """
    Estimates the Hausdorff (box-counting) dimension of an arbitrary point cloud.
    - points: ndarray of shape (n_points, n_dims)
    """
    points = np.asarray(points)
    mins = np.min(points, axis=0)
    maxs = np.max(points, axis=0)
    overall_range = np.max(maxs - mins)
    # Logspace for scales: from large (few boxes) to small (more boxes)
    box_counts = np.logspace(np.log10(min_boxes), np.log10(max_boxes), num=num_scales, dtype=int)
    scales = overall_range / box_counts
    
    counts = []
    for eps in scales:
        boxes = set()
        for p in points:
            idx = tuple(np.floor((p - mins) / eps))
            boxes.add(idx)
        counts.append(len(boxes))

    log_inv_scales = np.log(1 / scales)
    log_counts = np.log(counts)
    coeffs = np.polyfit(log_inv_scales, log_counts, 1)
    dimension = coeffs[0]
    return scales, counts, dimension

