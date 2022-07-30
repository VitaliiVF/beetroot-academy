from random import randint

robor_number = randint(1, 10)

user_number = input("The robot wished for a number from 1 to 10, try to guess: ")

while user_number != "end":
    if not user_number.isdigit():
        print("Error, please enter a number or 'end'")
    elif int(user_number) == robor_number:
        print("""
        You guessed!
        But the robot has already wished for a new number, 
        try to guess again or write 'end' to finish
        """)
    else:
        print(f"""
        You did not guess right!
        The robot wished for the number {robor_number}
        But the robot has already wished for a new number, 
        try to guess again or write "end" to end the game
        """)
    robor_number = randint(1, 10)
    user_number = input("Number or 'end': ")
