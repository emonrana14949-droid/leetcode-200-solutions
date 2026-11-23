# Mean and Std by Axis - column means of a 2x3 array.
import numpy as np
def col_stats(a):
    return a.mean(axis=0), a.std(axis=0)

if __name__ == "__main__":
    m, s = col_stats(np.array([[1, 2, 3], [4, 5, 6]], dtype=float))
    assert m.tolist() == [2.5, 3.5, 4.5]
    assert s.tolist() == [1.5, 1.5, 1.5]
    print("ok")
