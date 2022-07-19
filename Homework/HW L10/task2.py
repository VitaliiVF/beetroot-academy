def divided_square():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    return a**2 / b

try:
    print(divided_square())
except ValueError:
    print("Variables must be numbers")
except ZeroDivisionError:
    print("Can't divide by zero")