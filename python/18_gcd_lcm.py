# GCD and LCM - greatest common divisor and least common multiple.
import math
def gcd_lcm(a, b):
    g = math.gcd(a, b)
    return g, a * b // g

if __name__ == "__main__":
    assert gcd_lcm(12, 18) == (6, 36)
    assert gcd_lcm(7, 5) == (1, 35)
    print("ok")
