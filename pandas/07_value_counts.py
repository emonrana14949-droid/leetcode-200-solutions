# Value Counts - how many of each city.
import pandas as pd
def counts():
    s = pd.Series(["Dhaka", "Dhaka", "Chittagong", "Dhaka"])
    return s.value_counts()

if __name__ == "__main__":
    c = counts()
    assert c["Dhaka"] == 3 and c["Chittagong"] == 1
    print("ok")
