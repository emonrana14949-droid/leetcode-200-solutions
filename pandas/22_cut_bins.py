# Cut Bins - turn marks into grades A/B/C.
import pandas as pd
def grades():
    s = pd.Series([95, 75, 55])
    return pd.cut(s, bins=[0, 60, 80, 100], labels=["C", "B", "A"])

if __name__ == "__main__":
    assert grades().tolist() == ["A", "B", "C"]
    print("ok")
