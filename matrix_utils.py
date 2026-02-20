import numpy as np

def print_matrix(matrix: np.ndarray) -> None:
    for i in range(matrix.shape[0]):
        print("[", end=" ")
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print("] ")

        
def matrix_scalar_mult(matrix: np.ndarray, value: int) -> np.ndarray:
    result = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[i, j] = matrix[i, j] * value
    return result
