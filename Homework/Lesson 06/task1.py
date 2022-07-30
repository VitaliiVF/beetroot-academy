import random

numbers_list = []
count = 1

while count <= 10:
    numbers_list.append(random.randint(1, 100))
    count += 1

print(f"List of random numbers: {numbers_list}")

print(f"The greatest number: {max(numbers_list)}")