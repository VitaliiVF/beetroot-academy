def with_index(iterator, start = 0):
    count = start
    for elem in iterator:
        yield (count, elem)
        count += 1
        
        
n = ["one", "two", "three", "four", "five", "six", "seven"]

for i in with_index(n, 1):
    print(i)