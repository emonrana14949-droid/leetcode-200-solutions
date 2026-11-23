# Join on Index - join two frames by their index.
import pandas as pd
def joined():
    a = pd.DataFrame({"marks": [80, 90]}, index=[1, 2])
    b = pd.DataFrame({"city": ["Dhaka", "Sylhet"]}, index=[1, 2])
    return a.join(b)

if __name__ == "__main__":
    assert joined().shape == (2, 2)
    print("ok")
