import numpy as np

def get_matrix_rank(A: np.array) -> int:
    print(A)
    columns = []
    columns.append(A[:,0])

A = np.array([[1,2,3],[1,4,5],[6,0,6]])
get_matrix_rank(A)