import matrix_utils
import numpy as np

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

#sample = np.array([[3,8],[4,6]])
sample = np.array([[1,2,3],[0,4,5],[1,0,6]])
print(matrix_det_small(sample))