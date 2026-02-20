import matrix_utils
import numpy as np

def identity_matrix_gen(value: int) -> np.ndarray:
    result = np.zeros((value, value))
    for i in range(value):
        result[i, i] = 1 
    return result