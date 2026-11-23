# Solve Ax = b - find x for a small linear system.
import numpy as np
def solve(a, b):
    return np.linalg.solve(a, b)

if __name__ == "__main__":
    x = solve(np.array([[1.0, 2.0], [3.0, 4.0]]), np.array([5.0, 11.0]))
    assert np.allclose(x, [1.0, 2.0])
    print("ok")
