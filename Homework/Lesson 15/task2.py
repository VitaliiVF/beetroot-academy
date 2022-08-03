class Dog():
    def __init__(self, age, age_factor = 7):
        if age < 0:
            raise ValueError("Age can not be less than 0")
        
        self.age = age
        self.age_factor = age_factor
        
    def human_age(self):
        return self.age * self.age_factor
    

dog_patron = Dog(3)

print(f"The age of the Patron in the equivalent of human years is {dog_patron.human_age()} years")

