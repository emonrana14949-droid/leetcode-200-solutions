# FizzBuzz - print Fizz for 3, Buzz for 5, FizzBuzz for both.
def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        out.append(s or str(i))
    return out

if __name__ == "__main__":
    assert fizzbuzz(15)[-1] == "FizzBuzz"
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    print("ok")
