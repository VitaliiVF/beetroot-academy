from random import randint 

numbers_list_1 = []
numbers_list_2 = []
count = 1

while count <= 10:
    numbers_list_1.append(randint(1, 100))
    numbers_list_2.append(randint(1, 100))
    count += 1

print(f"First list of random numbers: {numbers_list_1}")
print(f"Second list of random numbers: {numbers_list_2}")

common_numbers = set(numbers_list_1) & (set(numbers_list_2))

if len(common_numbers) > 0:
    print(f"Common numbers: {list(common_numbers)}")
else:
    print("No common numbers")