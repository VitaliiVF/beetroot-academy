def test_func(list_numbers):
    count = 0
    for i in list_numbers:
        if i % 2 == 0:
            count += 1
    print(f"Local variables: {locals()}")
    return f"Number of even numbers: {count}"

print(test_func([2,2,3,3,4,4]))

print(f"Number of local variables: {test_func.__code__.co_nlocals}")
