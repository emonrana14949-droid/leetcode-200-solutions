# Reshape and Flatten - 2x3 to flat, then to 3x2.
import numpy as np
def reshaped():
    a = np.arange(6).reshape(2, 3)
    return a.flatten(), a.reshape(3, 2)

if __name__ == "__main__":
    f, r = reshaped()
    assert f.tolist() == [0, 1, 2, 3, 4, 5]
    assert r.shape == (3, 2)
    print("ok")
