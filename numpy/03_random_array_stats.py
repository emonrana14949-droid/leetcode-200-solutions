# Random Array - seed 42, 100 numbers, mean is near 0.
import numpy as np
def stats():
    rng = np.random.default_rng(42)
    a = rng.standard_normal(100)
    return a.mean(), a.std()

if __name__ == "__main__":
    m, s = stats()
    assert abs(m) < 0.3
    assert 0.7 < s < 1.3
    print("ok")
