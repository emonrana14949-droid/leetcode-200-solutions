# Valid Palindrome - True if it reads the same after removing non-letters.
def is_palindrome(s):
    t = "".join(c.lower() for c in s if c.isalnum())
    return t == t[::-1]

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    print("ok")
