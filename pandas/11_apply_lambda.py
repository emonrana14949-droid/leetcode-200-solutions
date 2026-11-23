# Apply Lambda - double every mark.
import pandas as pd
def doubled():
    df = pd.DataFrame({"marks": [10, 20, 30]})
    return df["marks"].apply(lambda x: x * 2)

if __name__ == "__main__":
    assert doubled().tolist() == [20, 40, 60]
    print("ok")
