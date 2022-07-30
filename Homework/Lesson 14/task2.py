from functools import wraps

def stop_words(word):
    def inner(func):
        @wraps(func)
        def wrapper_decorator(*args, **kwargs):
            value = func(*args, **kwargs)
            for i in word:
                value = value.replace(i, "*")
            return value
        return wrapper_decorator
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"