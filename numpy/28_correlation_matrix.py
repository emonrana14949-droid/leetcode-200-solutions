# Correlation - correlation matrix of two columns (perfectly linked = 1).
import numpy as np
def corr(a):
    return np.corrcoef(a, rowvar=False)

if __name__ == "__main__":
    a = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    assert abs(corr(a)[0, 1] - 1.0) < 1e-9
    print("ok")
