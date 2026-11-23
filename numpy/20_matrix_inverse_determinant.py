# Inverse and Determinant - invert a 2x2 matrix, check A @ inv(A) is identity.
import numpy as np
def inv_det(a):
    return np.linalg.inv(a), np.linalg.det(a)

if __name__ == "__main__":
    inv, det = inv_det(np.array([[1.0, 2.0], [3.0, 4.0]]))
    assert abs(det - (-2.0)) < 1e-9
    assert np.allclose(np.array([[1.0, 2.0], [3.0, 4.0]]) @ inv, np.eye(2))
    print("ok")
