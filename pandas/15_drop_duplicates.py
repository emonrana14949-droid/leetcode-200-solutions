# Drop Duplicates - keep one row per name.
import pandas as pd
def dedup():
    df = pd.DataFrame({"name": ["A", "A", "B"], "marks": [80, 80, 90]})
    return df.drop_duplicates()

if __name__ == "__main__":
    assert len(dedup()) == 2
    print("ok")
