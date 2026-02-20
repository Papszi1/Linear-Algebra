import numpy as np

def print_matrix(matrix: np.ndarray) -> None:
    for i in range(matrix.shape[0]):
        print("[", end=" ")
        for j in range(matrix.shape[1]):
            print(matrix[i, j], end=" ")
        print("] ")


sample = np.array([[1,2,3],[4,5,6],[7,8,9]])
print_matrix(sample)