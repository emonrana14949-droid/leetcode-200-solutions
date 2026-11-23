# Zip Two Lists - pair names with marks into a dict.
def make_dict(names, marks):
    return dict(zip(names, marks))

if __name__ == "__main__":
    assert make_dict(["A", "B"], [80, 90]) == {"A": 80, "B": 90}
    print("ok")
