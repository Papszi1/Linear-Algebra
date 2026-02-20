import matrix_utils
import numpy as np

def matrix_addition(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if matrix1.shape != matrix2.shape:
        raise ValueError(f"Missmatch in shapes{matrix1.shape}, {matrix2.shape}")
    
    result = np.zeros(matrix1.shape)
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i, j] = matrix1[i, j] + matrix2[i, j]
    return result

sample1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
sample2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_addition(sample1, sample2)