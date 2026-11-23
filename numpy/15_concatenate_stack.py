# Concatenate - join two arrays, and stack them as rows.
import numpy as np
def join(a, b):
    return np.concatenate([a, b]), np.stack([a, b])

if __name__ == "__main__":
    c, s = join(np.array([1, 2]), np.array([3, 4]))
    assert c.tolist() == [1, 2, 3, 4]
    assert s.shape == (2, 2)
    print("ok")
