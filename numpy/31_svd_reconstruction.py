# SVD - rebuild a matrix from its SVD, error is near zero.
import numpy as np
def svd_rebuild(a):
    u, s, vt = np.linalg.svd(a)
    return u[:, :len(s)] @ np.diag(s) @ vt

if __name__ == "__main__":
    a = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    assert np.allclose(svd_rebuild(a), a)
    print("ok")
