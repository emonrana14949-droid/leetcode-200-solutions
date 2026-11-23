# One-Hot Encoding - turn city names into 0/1 columns.
from sklearn.preprocessing import OneHotEncoder
import numpy as np
def run():
    enc = OneHotEncoder(sparse_output=False)
    return enc.fit_transform(np.array([["Dhaka"], ["Sylhet"], ["Dhaka"]]))

if __name__ == "__main__":
    out = run()
    assert out.shape == (3, 2)
    assert out[0].tolist() == [1.0, 0.0]
    print("ok")
