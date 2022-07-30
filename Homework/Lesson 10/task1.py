# Обробка помилка IndexError

def oops():
    a_list = [0, 1, 2, 3]
    return a_list[4]
    
def test_oops():
    try:
        oops()
    except IndexError:
        print("Unknown index")
        
test_oops()

# Обробка помилка KeyError

def oops1():
    a_dict = {0: "zero", 1: "one", 2: "two", 3: "three"}
    return a_dict[4]
    
def test_oops1():
    try:
        oops1()
    except KeyError:
        print("Unknown key")

test_oops1()