# Read CSV - read the sample sales file and keep big orders.
import pandas as pd
import os
def big_orders():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv")
    df = pd.read_csv(path)
    return df[df["amount"] > 100]

if __name__ == "__main__":
    assert len(big_orders()) == 3
    print("ok")
