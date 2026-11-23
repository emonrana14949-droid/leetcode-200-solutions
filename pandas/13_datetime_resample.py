# Datetime Resample - monthly total sales from daily data.
import pandas as pd
def monthly():
    idx = pd.date_range("2024-01-01", periods=60, freq="D")
    df = pd.DataFrame({"sales": [1] * 60}, index=idx)
    return df.resample("ME")["sales"].sum()

if __name__ == "__main__":
    m = monthly()
    assert m.iloc[0] == 31 and m.iloc[1] == 29
    print("ok")
