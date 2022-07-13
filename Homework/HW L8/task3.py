def make_operation(operation: str, *args: int) -> int:
    if operation == "+":
        count = 0
        for i in args:     
            count += i
    elif operation == "-":
        count = args[0]
        for i in range(1, len(args)):
            count -= args[i]
    elif operation == "*":
        count = 1
        for i in args:
            count *= i
    else:
        return "Unknown operation, select only '+', '-' or '*'"
    return count

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
print(make_operation('/', 7, 6))