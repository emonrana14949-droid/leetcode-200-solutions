# Zeros, Ones, Identity - make the three basic arrays.
import numpy as np
def basics():
    return np.zeros((2, 3)), np.ones((2, 2)), np.eye(3)

if __name__ == "__main__":
    z, o, e = basics()
    assert z.shape == (2, 3) and z.sum() == 0
    assert o.sum() == 4
    assert e[1, 1] == 1 and e[0, 1] == 0
    print("ok")
