# Describe - mean marks of a small class.
import pandas as pd
def mean_marks():
    df = pd.DataFrame({"marks": [70, 80, 90, 100]})
    return df["marks"].mean()

if __name__ == "__main__":
    assert mean_marks() == 85.0
    print("ok")
