# Decorator - count how many times a function is called.
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet(name):
    return "Hello " + name

if __name__ == "__main__":
    greet("Emon"); greet("A")
    assert greet.calls == 2
    print("ok")
