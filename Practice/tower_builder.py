def tower_builder(n_floors):
    space = " "
    star = "*"
    result = []
    for i in range(1, n_floors + 1):
        floor = f"{space * (n_floors - i)}{star * (i * 2 - 1)}{space * (n_floors - i)}"
        result.append(floor)
    return result

print(tower_builder(5))