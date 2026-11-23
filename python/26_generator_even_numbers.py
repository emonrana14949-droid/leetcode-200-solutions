# Generator - yield even numbers up to n, one at a time.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

if __name__ == "__main__":
    assert list(even_numbers(10)) == [0, 2, 4, 6, 8, 10]
    print("ok")
