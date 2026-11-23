# SimpleImputer - fill missing values with the mean.
from sklearn.impute import SimpleImputer
import numpy as np
def run():
    a = np.array([[1, 2], [np.nan, 3], [7, 6]], dtype=float)
    return SimpleImputer(strategy="mean").fit_transform(a)

if __name__ == "__main__":
    out = run()
    assert out[1, 0] == 4.0
    print("ok")
