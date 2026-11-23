# Filter Rows - keep students with marks above 80.
import pandas as pd
def top_students():
    df = pd.DataFrame({"name": ["A", "B", "C"], "marks": [70, 90, 85]})
    return df[df["marks"] > 80]

if __name__ == "__main__":
    assert top_students()["name"].tolist() == ["B", "C"]
    print("ok")
