# GroupBy Transform - each mark minus its class mean.
import pandas as pd
def centred():
    df = pd.DataFrame({"cls": ["A", "A", "B"], "marks": [80, 90, 70]})
    df["centred"] = df["marks"] - df.groupby("cls")["marks"].transform("mean")
    return df

if __name__ == "__main__":
    assert centred()["centred"].tolist() == [-5.0, 5.0, 0.0]
    print("ok")
