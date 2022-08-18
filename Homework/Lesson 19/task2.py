def in_range(*args):
    if len(args) == 1:
        stop = args[0]
        start = 0
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    else:
        start = args[0]
        stop = args[1]
        step = args[2]
    
    
    if step == 0:
        raise ValueError("Step can't be zero")
    if len(args) > 3:
        raise ValueError("in_range only takes 3 arguments")
    
    if stop >= 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


print(list(in_range(10)) == list(range(10)))
print(list(in_range(1, 11)) == list(range(1, 11)))
print(list(in_range(0, 30, 5)) == list(range(0, 30, 5)))
print(list(in_range(0, 10, 3)) == list(range(0, 10, 3)))
print(list(in_range(0, -10, -1)) == list(range(0, -10, -1)))
print(list(in_range(0)) == list(range(0)))
print(list(in_range(1, 0)) == list(range(1, 0)))