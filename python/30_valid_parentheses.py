# Valid Parentheses - True if brackets open and close in the right order.
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif not stack or stack.pop() != pairs[c]:
            return False
    return not stack

if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    print("ok")
