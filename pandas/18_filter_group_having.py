# Filter Groups - keep only classes with mean marks above 75.
import pandas as pd
def kept():
    df = pd.DataFrame({"cls": ["A", "A", "B", "B"], "marks": [80, 90, 60, 70]})
    return df.groupby("cls").filter(lambda g: g["marks"].mean() > 75)

if __name__ == "__main__":
    assert kept()["cls"].unique().tolist() == ["A"]
    print("ok")
