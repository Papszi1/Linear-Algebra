from matrix_utils import print_matrix

import numpy as np

def matrix_scalar_mult(matrix: np.ndarray, value: int) -> np.ndarray:
    result = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[i, j] = matrix[i, j] * value
    return result


sample = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_scalar_mult(sample, 4)