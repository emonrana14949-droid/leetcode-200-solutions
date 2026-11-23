# Rename Columns - rename Marks to Score.
import pandas as pd
def renamed():
    df = pd.DataFrame({"Name": ["A"], "Marks": [80]})
    return df.rename(columns={"Name": "name", "Marks": "score"})

if __name__ == "__main__":
    assert list(renamed().columns) == ["name", "score"]
    print("ok")
