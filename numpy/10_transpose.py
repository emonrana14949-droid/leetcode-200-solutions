# Transpose - flip rows and columns.
import numpy as np
def transpose(a):
    return a.T

if __name__ == "__main__":
    assert transpose(np.array([[1, 2], [3, 4]])).tolist() == [[1, 3], [2, 4]]
    print("ok")
