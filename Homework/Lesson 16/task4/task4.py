class CustomException(Exception):
    
    def __init__(self, msg):
        with open("log.txt", "a+") as file:
            file.write(f"{msg}\n")
        

def triggerException(num):
    if num == 0:
        raise CustomException("Exception Triggered! Something went wrong.")
    else:
        print(num)

try:
    triggerException(0)
    print("Code has successfully been executed.")
except CustomException:
    print("Error: Number should not be 0.")