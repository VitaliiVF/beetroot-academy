n = input("Input your string: ")

if len(n) >= 2:
    print(n[0:2] + n[-2:])
else:
    print("Empty String")