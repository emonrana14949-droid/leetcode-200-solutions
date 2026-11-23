# List Comprehension - squares of even numbers from 1 to 10.
def even_squares():
    return [x * x for x in range(1, 11) if x % 2 == 0]

if __name__ == "__main__":
    assert even_squares() == [4, 16, 36, 64, 100]
    print("ok")
