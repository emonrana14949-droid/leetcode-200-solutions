# Climbing Stairs - ways to climb n steps taking 1 or 2 at a time.
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    print("ok")
