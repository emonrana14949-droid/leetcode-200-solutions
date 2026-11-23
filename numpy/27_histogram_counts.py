# Histogram - count values in bins 0-2, 2-4, 4-6.
import numpy as np
def hist(a):
    counts, edges = np.histogram(a, bins=[0, 2, 4, 6])
    return counts

if __name__ == "__main__":
    assert hist(np.array([1, 2, 3, 5])).tolist() == [1, 2, 1]
    print("ok")
