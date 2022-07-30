phone_number = input("Input your phone number: ")

if phone_number.isdigit() and len(phone_number) == 10:
    print("This is a valid phone number")
else:
    print("This is not a phone number.")