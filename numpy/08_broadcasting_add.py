# Broadcasting - add [10, 20, 30] to every row of a 3x3 array.
import numpy as np
def add_row(a, row):
    return a + row

if __name__ == "__main__":
    a = np.zeros((3, 3))
    out = add_row(a, np.array([10, 20, 30]))
    assert out[2].tolist() == [10, 20, 30]
    print("ok")
