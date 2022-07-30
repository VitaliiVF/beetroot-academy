from functools import wraps

def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        @wraps(func)
        def wrapper_decorator(name):
            if type_ != type(name):
                return f"{False}, Type error"
            if max_length < len(name):
                return f"{False}, Length error"
            for i in contains:
                if i not in name:
                    value = f"{False}, No required characters"
            value = func(name)
            return value
        return wrapper_decorator
    return inner

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') == f"{False}, Length error"
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'