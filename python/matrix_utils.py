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


def matrix_det_2(matrix: np.ndarray) -> float:
    return (matrix[0,0] * matrix[1,1]) - (matrix[0,1] * matrix[1,0])


def matrix_det_small(matrix: np.ndarray) -> float:
    m = matrix.shape[0]
    n = matrix.shape[1]
    print(m, n)
    if (n != m):
        raise ValueError(f"The matrix is not square {matrix.shape}")
    if (m > 3):
        raise ValueError(f"The matrix is too large, use matrix_det function instead {matrix.shape}")

    if (m == 2):
        return matrix_det_2(matrix)
    if (m == 3):
        result = 0
        for i in range(3):
            minor = np.delete(np.delete(matrix, 0, axis = 0), i, axis = 1)
            result += (-1)**i * matrix[0,i] * matrix_det_2(minor)
        return result