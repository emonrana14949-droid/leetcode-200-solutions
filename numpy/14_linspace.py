# Linspace - 5 evenly spaced numbers from 0 to 1.
import numpy as np
def spaced():
    return np.linspace(0, 1, 5)

if __name__ == "__main__":
    assert spaced().tolist() == [0.0, 0.25, 0.5, 0.75, 1.0]
    print("ok")
