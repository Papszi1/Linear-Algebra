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

def matrix_addition(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if matrix1.shape != matrix2.shape:
        raise ValueError(f"Missmatch in shapes{matrix1.shape}, {matrix2.shape}")
    
    result = np.zeros(matrix1.shape)
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i, j] = matrix1[i, j] + matrix2[i, j]
    return result

def matrix_transpose(matrix: np.ndarray) -> np.ndarray:
    result = np.zeros((matrix.shape[1], matrix.shape[0]))
    print(matrix.shape, result.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[j, i] = matrix[i, j]
    return result


def matrix_mult(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if (matrix1.shape[1] != matrix2.shape[0]):
        raise ValueError(f"Wrong shape of the matrices{matrix1.shape}, {matrix2.shape}")
    
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(matrix1.shape[1]):
                result[i, j] += matrix1[i, k] * matrix2[k, j]
    return result
