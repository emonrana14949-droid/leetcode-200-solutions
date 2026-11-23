# Map, Filter, Lambda - double the even numbers in a list.
def double_evens(nums):
    return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))

if __name__ == "__main__":
    assert double_evens([1, 2, 3, 4, 5]) == [4, 8]
    print("ok")
