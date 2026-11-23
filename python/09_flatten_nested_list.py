# Flatten a Nested List - turn [[1,2],[3,[4]]] into [1,2,3,4].
def flatten(items):
    out = []
    for x in items:
        if isinstance(x, list):
            out.extend(flatten(x))
        else:
            out.append(x)
    return out

if __name__ == "__main__":
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    print("ok")
