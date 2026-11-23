# Create an Array - arange 0-11, reshape to 3x4.
import numpy as np
def make_grid():
    return np.arange(12).reshape(3, 4)

if __name__ == "__main__":
    a = make_grid()
    assert a.shape == (3, 4)
    assert a[0, 0] == 0 and a[2, 3] == 11
    print("ok")
