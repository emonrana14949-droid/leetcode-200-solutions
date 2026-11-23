# Create a DataFrame - 3 students with name and marks.
import pandas as pd
def make_df():
    return pd.DataFrame({"name": ["Asha", "Babu", "Chadni"], "marks": [80, 90, 70]})

if __name__ == "__main__":
    df = make_df()
    assert df.shape == (3, 2)
    assert df["marks"].sum() == 240
    print("ok")
