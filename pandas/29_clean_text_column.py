# Clean Text - strip spaces and title-case names.
import pandas as pd
def cleaned():
    s = pd.Series(["  asha ", "BABU", " chadni"])
    return s.str.strip().str.title()

if __name__ == "__main__":
    assert cleaned().tolist() == ["Asha", "Babu", "Chadni"]
    print("ok")
