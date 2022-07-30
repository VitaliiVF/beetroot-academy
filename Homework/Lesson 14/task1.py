def logger(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

def say_hello():
    print("Hello, world!")

hello = logger(say_hello)

hello()