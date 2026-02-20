import matrix_utils
import numpy as np

def matrix_trace(matrix: np.ndarray) -> float:
    if (matrix.shape[0] != matrix.shape[1]):
        raise ValueError(f"The input in not a square matrix{matrix.shape}")
    value = 0
    for i in range(matrix.shape[0]):
        value += matrix[i,i]
    return value

sample = np.array([[1,2],[0,1],[4,3]])
matrix_trace(sample)