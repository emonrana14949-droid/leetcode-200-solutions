# np.where - replace negatives with 0.
import numpy as np
def clip_neg(a):
    return np.where(a < 0, 0, a)

if __name__ == "__main__":
    assert clip_neg(np.array([-1, 2, -3, 4])).tolist() == [0, 2, 0, 4]
    print("ok")
