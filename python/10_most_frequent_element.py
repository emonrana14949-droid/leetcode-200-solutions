# Most Frequent Element - the value that appears most often.
def most_frequent(nums):
    from collections import Counter
    return Counter(nums).most_common(1)[0][0]

if __name__ == "__main__":
    assert most_frequent([1, 2, 2, 3, 2, 1]) == 2
    print("ok")
