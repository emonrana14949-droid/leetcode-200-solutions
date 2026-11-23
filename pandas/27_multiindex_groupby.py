# MultiIndex - average marks by class and section.
import pandas as pd
def grouped():
    df = pd.DataFrame({"cls": ["A", "A", "B"], "sec": [1, 2, 1], "marks": [80, 90, 70]})
    return df.groupby(["cls", "sec"])["marks"].mean()

if __name__ == "__main__":
    g = grouped()
    assert g[("A", 1)] == 80.0 and g[("A", 2)] == 90.0
    print("ok")
