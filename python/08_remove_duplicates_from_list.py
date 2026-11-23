# Remove Duplicates - keep order, drop repeated values.
def remove_duplicates(nums):
    seen, out = set(), []
    for n in nums:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out

if __name__ == "__main__":
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    print("ok")
