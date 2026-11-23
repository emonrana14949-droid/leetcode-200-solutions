# NaN Handling - replace NaN with the column mean.
import numpy as np
def fill_nan(a):
    a = a.astype(float).copy()
    m = np.nanmean(a)
    a[np.isnan(a)] = m
    return a

if __name__ == "__main__":
    out = fill_nan(np.array([1, float("nan"), 3]))
    assert out.tolist() == [1.0, 2.0, 3.0]
    print("ok")
