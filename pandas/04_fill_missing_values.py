# Fill Missing - replace NaN marks with the mean.
import pandas as pd
import numpy as np
def filled():
    df = pd.DataFrame({"marks": [80, np.nan, 90]})
    return df.fillna(df["marks"].mean())

if __name__ == "__main__":
    assert filled()["marks"].tolist() == [80.0, 85.0, 90.0]
    print("ok")
