# Query - pick rows where marks > 80 using df.query.
import pandas as pd
def queried():
    df = pd.DataFrame({"name": ["A", "B", "C"], "marks": [70, 90, 85]})
    return df.query("marks > 80")

if __name__ == "__main__":
    assert queried()["name"].tolist() == ["B", "C"]
    print("ok")
