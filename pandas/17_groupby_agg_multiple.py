# GroupBy Agg - sum and mean sales per city.
import pandas as pd
def agg():
    df = pd.DataFrame({"city": ["Dhaka", "Dhaka", "Sylhet"], "sales": [10, 20, 30]})
    return df.groupby("city")["sales"].agg(["sum", "mean"])

if __name__ == "__main__":
    a = agg()
    assert a.loc["Dhaka", "sum"] == 30 and a.loc["Dhaka", "mean"] == 15.0
    print("ok")
