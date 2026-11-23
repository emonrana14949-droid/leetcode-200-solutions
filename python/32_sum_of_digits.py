# Sum of Digits - add up all digits of a number.
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

if __name__ == "__main__":
    assert sum_of_digits(123) == 6
    assert sum_of_digits(999) == 27
    print("ok")
