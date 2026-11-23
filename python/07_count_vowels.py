# Count Vowels - count a, e, i, o, u in a string.
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == "__main__":
    assert count_vowels("hello world") == 3
    assert count_vowels("AEIOU") == 5
    print("ok")
