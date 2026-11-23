# Word Count - count how many times each word appears.
def word_count(text):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts

if __name__ == "__main__":
    assert word_count("cat dog cat") == {"cat": 2, "dog": 1}
    print("ok")
