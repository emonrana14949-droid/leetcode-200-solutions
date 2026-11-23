# Cumulative Sum - running total of an array.
import numpy as np
def cumsum(a):
    return np.cumsum(a)

if __name__ == "__main__":
    assert cumsum(np.array([1, 2, 3, 4])).tolist() == [1, 3, 6, 10]
    print("ok")
