# Meshgrid - make x and y grids for a 2x3 grid.
import numpy as np
def grid():
    x, y = np.meshgrid([0, 1, 2], [0, 1])
    return x, y

if __name__ == "__main__":
    x, y = grid()
    assert x.shape == (2, 3) and y.shape == (2, 3)
    assert x[0].tolist() == [0, 1, 2]
    print("ok")
