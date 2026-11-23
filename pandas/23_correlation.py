# Correlation - marks and study hours move together (r = 1 here).
import pandas as pd
def corr():
    df = pd.DataFrame({"hours": [1, 2, 3], "marks": [10, 20, 30]})
    return df["hours"].corr(df["marks"])

if __name__ == "__main__":
    assert abs(corr() - 1.0) < 1e-9
    print("ok")
