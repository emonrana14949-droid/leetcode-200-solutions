# Cumulative Sum - running total of monthly sales.
import pandas as pd
def cum():
    s = pd.Series([10, 20, 30])
    return s.cumsum()

if __name__ == "__main__":
    assert cum().tolist() == [10, 30, 60]
    print("ok")
