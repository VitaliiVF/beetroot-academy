class Person():
    
    def __init__(self, firstname, lastname, age):
        if age < 0:
            raise ValueError("Age can not be less than 0")
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")
        

vitalii = Person("Vitalii", "Fedun", 23)

vitalii.talk()