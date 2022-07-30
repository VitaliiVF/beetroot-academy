count = 1
numbers_list = []
result_list = []

while count <= 100:
    numbers_list.append(count)
    if numbers_list[count - 1] % 7 == 0 and numbers_list[count - 1] % 5 != 0:
        result_list.append(count)
    count += 1

print(f"list of numbers that are divisible by 7 but not multiples of 5: {result_list}")