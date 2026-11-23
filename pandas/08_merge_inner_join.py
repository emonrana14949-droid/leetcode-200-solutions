# Merge Inner Join - join students with their city.
import pandas as pd
def merged():
    a = pd.DataFrame({"id": [1, 2], "name": ["A", "B"]})
    b = pd.DataFrame({"id": [1, 2], "city": ["Dhaka", "Sylhet"]})
    return a.merge(b, on="id")

if __name__ == "__main__":
    assert merged().shape == (2, 3)
    assert merged()["city"].tolist() == ["Dhaka", "Sylhet"]
    print("ok")
