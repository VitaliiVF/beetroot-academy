from functools import wraps

class TypeDecorators:
    
    def __init__(self, func):
        self.func = func
        
    def to_int(func):
            @wraps(func)
            def inner(*args, **kwargs):
                try:
                    value = func(*args, **kwargs)
                    value = int(value)
                    return value
                except ValueError:
                    print(f"Can't convert {value} to number")
                    return value
            return inner

    
    def to_str(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                value = str(value)
            except ValueError:
                print(f"Can't convert {value} to string")
            return value
        return inner
    
    def to_bool(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                value = bool(value)
            except ValueError:
                print(f"Can't convert {value} to bool")    
            return value
        return inner
    
    def to_float(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                value = float(value)
            except ValueError:
                print(f"Can't convert {value} to float")    
            return value
        return inner
    
    
@TypeDecorators.to_int
def do_nothing(string):
    return string

@TypeDecorators.to_float
def do_nothing2(string):
    return string

@TypeDecorators.to_bool
def do_something(string):
    return string

@TypeDecorators.to_str
def do_something2(number):
    return number

print(do_nothing('25'))
print(do_nothing2('1'))
print(do_something('True'))
print(type(do_something2(53253)))