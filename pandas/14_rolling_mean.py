# Rolling Mean - 3-day rolling average of sales.
import pandas as pd
def rolling():
    s = pd.Series([1, 2, 3, 4, 5])
    return s.rolling(3).mean()

if __name__ == "__main__":
    r = rolling()
    assert r.iloc[2] == 2.0 and r.iloc[4] == 4.0
    print("ok")
