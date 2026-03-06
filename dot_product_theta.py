import math
import numpy as np

def vector_length(vector: np.array) -> np.double:
    length = 0
    for component in vector:
        length += component ** 2
    return np.sqrt(length)

def dot_product_theta(v: np.array, w: np.array) -> np.double:
    if len(v) != len(w):
        raise ValueError("Length of vectors don't match")

    dot_product = 0
    for i in range(len(v)):
        dot_product += v[i] * w[i]

    costheta = dot_product / (vector_length(v) * vector_length(w))
    theta = np.arccos(costheta)
    return theta



v = np.array([1, np.sqrt(3)])
w = np.array([1, 0])

dot_product_theta(v,w)