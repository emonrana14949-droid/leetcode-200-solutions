# Merge Two Sorted Lists - merge two sorted lists into one sorted list.
def merge_lists(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]

if __name__ == "__main__":
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    print("ok")
