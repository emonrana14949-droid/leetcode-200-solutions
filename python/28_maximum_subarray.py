# Maximum Subarray - largest sum of a contiguous part (Kadane).
def max_sub_array(nums):
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best

if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("ok")
