# Shift and Diff - daily change in temperature.
import pandas as pd
def diffs():
    s = pd.Series([30, 32, 31, 35])
    return s.diff()

if __name__ == "__main__":
    assert diffs().tolist()[1:] == [2.0, -1.0, 4.0]
    print("ok")
