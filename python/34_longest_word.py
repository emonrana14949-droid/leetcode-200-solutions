# Longest Word - the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

if __name__ == "__main__":
    assert longest_word("I love data science") == "science"
    print("ok")
