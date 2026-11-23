# Second Largest - the second biggest unique number in a list.
def second_largest(nums):
    uniq = sorted(set(nums))
    return uniq[-2]

if __name__ == "__main__":
    assert second_largest([1, 5, 3, 5, 2]) == 3
    assert second_largest([10, 20, 30]) == 20
    print("ok")
