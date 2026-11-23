# Dot Product - matrix multiply a 2x3 by a 3x2.
import numpy as np
def matmul(a, b):
    return a @ b

if __name__ == "__main__":
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8], [9, 10], [11, 12]])
    assert matmul(a, b).tolist() == [[58, 64], [139, 154]]
    print("ok")
