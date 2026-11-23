# Save CSV - write a frame to CSV, read it back, check it matches.
import pandas as pd
import tempfile, os
def roundtrip():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as f:
        path = f.name
    df.to_csv(path, index=False)
    back = pd.read_csv(path)
    os.remove(path)
    return back

if __name__ == "__main__":
    assert roundtrip().values.tolist() == [[1, 3], [2, 4]]
    print("ok")
