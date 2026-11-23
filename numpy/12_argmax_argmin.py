# Argmax / Argmin - index of the biggest and smallest value.
import numpy as np
def extremes(a):
    return int(np.argmax(a)), int(np.argmin(a))

if __name__ == "__main__":
    assert extremes(np.array([3, 9, 1, 7])) == (1, 2)
    print("ok")
