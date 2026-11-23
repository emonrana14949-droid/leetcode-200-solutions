# Melt - turn Jan/Feb columns into rows.
import pandas as pd
def melted():
    df = pd.DataFrame({"id": [1], "Jan": [10], "Feb": [20]})
    return df.melt(id_vars="id", var_name="month", value_name="sales")

if __name__ == "__main__":
    m = melted()
    assert m["month"].tolist() == ["Jan", "Feb"]
    assert m["sales"].tolist() == [10, 20]
    print("ok")
