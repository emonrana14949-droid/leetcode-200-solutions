# File Handling - count words in a text file.
def count_words_in_file(path):
    with open(path) as f:
        return len(f.read().split())

if __name__ == "__main__":
    import tempfile, os
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt") as f:
        f.write("hello world from python")
        path = f.name
    assert count_words_in_file(path) == 4
    os.remove(path)
    print("ok")
