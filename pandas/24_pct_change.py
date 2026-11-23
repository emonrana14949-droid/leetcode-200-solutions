# Pct Change - sales growth from month to month.
import pandas as pd
def growth():
    s = pd.Series([100, 150, 120])
    return s.pct_change()

if __name__ == "__main__":
    g = growth()
    assert abs(g.iloc[1] - 0.5) < 1e-9
    assert abs(g.iloc[2] - (-0.2)) < 1e-9
    print("ok")
