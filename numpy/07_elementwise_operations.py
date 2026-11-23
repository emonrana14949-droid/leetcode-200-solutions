# Element-wise Ops - add, multiply and square an array.
import numpy as np
def ops(a, b):
    return a + b, a * b, a ** 2

if __name__ == "__main__":
    s, p, q = ops(np.array([1, 2, 3]), np.array([4, 5, 6]))
    assert s.tolist() == [5, 7, 9]
    assert p.tolist() == [4, 10, 18]
    assert q.tolist() == [1, 4, 9]
    print("ok")
