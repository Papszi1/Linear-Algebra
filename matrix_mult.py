import matrix_utils
import numpy as np

def matrix_mult(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if (matrix1.shape[1] != matrix2.shape[0]):
        raise ValueError(f"Wrong shape of the matrices{matrix1.shape}, {matrix2.shape}")
    
    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(matrix1.shape[1]):
                result[i, j] += matrix1[i, k] * matrix2[k, j]
    return result


#sample1 = np.array([[1,2,3],[4,5,6]])
#sample2 = np.array([[7,8],[9,10],[11,12] ])
sample1 = np.array([[1,2,3],[4,5,6],[7,8,9],[1,0,2],[3,4,5]])
sample2 = np.array([[1,2],[0,1],[4,3]])
matrix_mult(sample1, sample2)

