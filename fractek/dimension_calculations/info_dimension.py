def dimension_summary(result_tuple, method_name):
    """Returns the method, estimated dimension, and parameters."""
    if method_name == 'box-counting':
        sizes, counts = result_tuple
        dim = calc_dimension(sizes, counts)
        return {'method': method_name, 'dimension': dim}
    elif method_name == 'hausdorff':
        _, _, dim = result_tuple
        return {'method': method_name, 'dimension': dim}
    elif method_name == 'correlation':
        _, _, dim = result_tuple
        return {'method': method_name, 'dimension': dim}
    else:
        return {'method': 'unknown', 'dimension': None}

