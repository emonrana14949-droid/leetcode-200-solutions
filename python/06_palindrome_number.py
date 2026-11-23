# Palindrome Number - True if the number reads the same backwards.
def is_palindrome_number(x):
    return str(x) == str(x)[::-1] if x >= 0 else False

if __name__ == "__main__":
    assert is_palindrome_number(121) is True
    assert is_palindrome_number(-121) is False
    assert is_palindrome_number(10) is False
    print("ok")
