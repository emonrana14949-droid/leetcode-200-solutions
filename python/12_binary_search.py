# Binary Search - find target index in a sorted list, or -1.
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    print("ok")
