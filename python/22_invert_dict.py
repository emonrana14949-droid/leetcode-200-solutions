# Invert a Dict - swap keys and values.
def invert(d):
    return {v: k for k, v in d.items()}

if __name__ == "__main__":
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    print("ok")
