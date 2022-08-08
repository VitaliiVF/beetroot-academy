class Animal:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        raise NotImplementedError("Must be implemented by a sub class")
    
class Cat(Animal):
    def talk(self):
        print("meow")

class Dog(Animal):
    def talk(self):
        print("woof woof")
        
def talk_animal(animal):
    animal.talk()
    
cat = Cat("Begemot")

dog = Dog("Patron")

talk_animal(cat)

talk_animal(dog)