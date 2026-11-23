# String Compression - aabcccccaaa becomes a2b1c5a3.
def compress(s):
    out, i = "", 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out += s[i] + str(j - i)
        i = j
    return out

if __name__ == "__main__":
    assert compress("aabcccccaaa") == "a2b1c5a3"
    print("ok")
