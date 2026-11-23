# Eigenvalues - eigenvalues of a symmetric 2x2 matrix.
import numpy as np
def eigvals(a):
    return np.linalg.eigvalsh(a)

if __name__ == "__main__":
    v = eigvals(np.array([[2.0, 0.0], [0.0, 3.0]]))
    assert np.allclose(sorted(v), [2.0, 3.0])
    print("ok")
