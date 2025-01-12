import numpy as np

def compute_cross_product(array1, array2):
    if len(array1) != 3 or len(array2) != 3:
        raise ValueError("Arrays must have exactly 3 elements")
    
    v1 = np.array(array1)
    v2 = np.array(array2)
    
    return np.cross(v1, v2)

array1 = [1, 0, 0]
array2 = [0, 1, 0]
compute_cross_product(array1, array2)

