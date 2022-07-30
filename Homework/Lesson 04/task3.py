print("What is 50 plus 25 percent? Rounding to tenths")

answer = float(input())

while True:
    if answer == 62.5:
        print("You are right!")
        break
    else:
        print("You're wrong, try again.")
        answer = float(input())
