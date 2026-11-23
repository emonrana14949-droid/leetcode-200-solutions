# Crosstab - count of pass/fail by class.
import pandas as pd
def tab():
    df = pd.DataFrame({"cls": ["A", "A", "B"], "res": ["pass", "fail", "pass"]})
    return pd.crosstab(df["cls"], df["res"])

if __name__ == "__main__":
    t = tab()
    assert t.loc["A", "pass"] == 1 and t.loc["A", "fail"] == 1
    print("ok")
