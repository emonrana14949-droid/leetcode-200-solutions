# Split - split 6 numbers into 3 equal parts.
import numpy as np
def split(a):
    return np.split(a, 3)

if __name__ == "__main__":
    parts = split(np.arange(6))
    assert [p.tolist() for p in parts] == [[0, 1], [2, 3], [4, 5]]
    print("ok")
