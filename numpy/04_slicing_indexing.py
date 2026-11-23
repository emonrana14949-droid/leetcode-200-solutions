# Slicing - take the middle 2x2 block of a 4x4 array.
import numpy as np
def middle(a):
    return a[1:3, 1:3]

if __name__ == "__main__":
    a = np.arange(16).reshape(4, 4)
    assert middle(a).tolist() == [[5, 6], [9, 10]]
    print("ok")
