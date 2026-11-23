# String Methods - clean messy city names.
import pandas as pd
def cleaned():
    s = pd.Series(["  Dhaka ", "SYLHET", " Chittagong"])
    return s.str.strip().str.lower()

if __name__ == "__main__":
    assert cleaned().tolist() == ["dhaka", "sylhet", "chittagong"]
    print("ok")
