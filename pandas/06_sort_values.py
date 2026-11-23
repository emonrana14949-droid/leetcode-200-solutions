# Sort Values - sort sales by amount, biggest first.
import pandas as pd
def sorted_sales():
    df = pd.DataFrame({"item": ["a", "b", "c"], "sales": [10, 30, 20]})
    return df.sort_values("sales", ascending=False)

if __name__ == "__main__":
    assert sorted_sales()["item"].tolist() == ["b", "c", "a"]
    print("ok")
