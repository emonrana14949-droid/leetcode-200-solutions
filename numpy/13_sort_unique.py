# Sort and Unique - sorted array and its unique values.
import numpy as np
def sort_unique(a):
    return np.sort(a), np.unique(a)

if __name__ == "__main__":
    s, u = sort_unique(np.array([3, 1, 2, 1, 3]))
    assert s.tolist() == [1, 1, 2, 3, 3]
    assert u.tolist() == [1, 2, 3]
    print("ok")
