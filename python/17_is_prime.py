# Check Prime - True if n is a prime number.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert is_prime(2) is True
    print("ok")
