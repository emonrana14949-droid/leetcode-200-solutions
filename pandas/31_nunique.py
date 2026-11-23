# Nunique - how many different cities are in the data.
import pandas as pd
def n_unique():
    s = pd.Series(["Dhaka", "Dhaka", "Sylhet", "Khulna"])
    return s.nunique()

if __name__ == "__main__":
    assert n_unique() == 3
    print("ok")
