# Boolean Mask - keep only numbers bigger than 5.
import numpy as np
def over_five(a):
    return a[a > 5]

if __name__ == "__main__":
    assert over_five(np.array([1, 7, 3, 9, 5])).tolist() == [7, 9]
    print("ok")
