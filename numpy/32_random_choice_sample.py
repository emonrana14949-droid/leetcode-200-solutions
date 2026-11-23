# Random Choice - pick 3 different numbers from 0-9, seed 7.
import numpy as np
def sample():
    rng = np.random.default_rng(7)
    return rng.choice(10, size=3, replace=False)

if __name__ == "__main__":
    s = sample()
    assert len(s) == 3 and len(set(s.tolist())) == 3
    print("ok")
