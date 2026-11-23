# Fibonacci - first n Fibonacci numbers.
def fibonacci(n):
    out = []
    a, b = 0, 1
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out

if __name__ == "__main__":
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    print("ok")
