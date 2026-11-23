# Concat - stack two months of sales into one frame.
import pandas as pd
def stacked():
    a = pd.DataFrame({"m": ["Jan"], "sales": [100]})
    b = pd.DataFrame({"m": ["Feb"], "sales": [150]})
    return pd.concat([a, b], ignore_index=True)

if __name__ == "__main__":
    assert stacked()["sales"].tolist() == [100, 150]
    print("ok")
