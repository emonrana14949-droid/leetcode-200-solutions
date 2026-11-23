# Standardize - subtract mean and divide by std, per column.
import numpy as np
def standardize(a):
    return (a - a.mean(axis=0)) / a.std(axis=0)

if __name__ == "__main__":
    a = np.array([[1.0, 10.0], [2.0, 20.0], [3.0, 30.0]])
    out = standardize(a)
    assert np.allclose(out.mean(axis=0), [0, 0])
    assert np.allclose(out.std(axis=0), [1, 1])
    print("ok")
