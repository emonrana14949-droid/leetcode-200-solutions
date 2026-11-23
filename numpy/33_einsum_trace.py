# Einsum - trace of a matrix and sum of all elements.
import numpy as np
def trace_and_sum(a):
    return float(np.einsum("ii->", a)), float(np.einsum("ij->", a))

if __name__ == "__main__":
    a = np.array([[1, 2], [3, 4]])
    assert trace_and_sum(a) == (5.0, 10.0)
    print("ok")
