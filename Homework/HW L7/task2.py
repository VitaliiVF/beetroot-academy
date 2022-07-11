stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {fruit : int(stock[fruit] * prices[fruit]) for fruit in stock}

print("Total price of the stock fruits: ")

for key, value in total_price.items():
    print(f"{key}: {value} usd")