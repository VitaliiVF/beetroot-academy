days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

week_1 = {i + 1 : days[i] for i in range(len(days))}

print("The first version of the dictionary with the days of the week: ")

for key, value in week_1.items():
    print(f"{key}: {value}")

week_2 = {days[i] : i + 1  for i in range(len(days))}

print("The second version of the dictionary with the days of the week: ")

for key, value in week_2.items():
    print(f"{key}: {value}")
