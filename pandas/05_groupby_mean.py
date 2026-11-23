# GroupBy Mean - average marks per class.
import pandas as pd
def group_mean():
    df = pd.DataFrame({"cls": ["A", "A", "B", "B"], "marks": [80, 90, 70, 60]})
    return df.groupby("cls")["marks"].mean()

if __name__ == "__main__":
    g = group_mean()
    assert g["A"] == 85.0 and g["B"] == 65.0
    print("ok")
