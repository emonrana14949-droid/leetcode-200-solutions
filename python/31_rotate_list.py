# Rotate a List - move the last k items to the front.
def rotate(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]

if __name__ == "__main__":
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    print("ok")
