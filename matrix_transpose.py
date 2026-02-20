import matrix_utils
import numpy as np

def matrix_transpose(matrix: np.ndarray) -> np.ndarray:
    result = np.zeros((matrix.shape[1], matrix.shape[0]))
    print(matrix.shape, result.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[j, i] = matrix[i, j]
    return result



sample = np.array([[1,2,3], [4,5,6]])
matrix_transpose(sample)