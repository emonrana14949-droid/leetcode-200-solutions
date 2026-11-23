# Check Anagrams - True if two words use the same letters.
def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

if __name__ == "__main__":
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "world") is False
    print("ok")
