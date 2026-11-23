# Outer Product - multiply every pair from two vectors.
import numpy as np
def outer(a, b):
    return np.outer(a, b)

if __name__ == "__main__":
    assert outer(np.array([1, 2]), np.array([3, 4])).tolist() == [[3, 4], [6, 8]]
    print("ok")
