# Vectorized Sum of Squares - sum of squares without a loop.
import numpy as np
def sum_squares(a):
    return float(np.sum(a ** 2))

if __name__ == "__main__":
    assert sum_squares(np.array([1, 2, 3])) == 14.0
    print("ok")
