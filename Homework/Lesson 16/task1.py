class Person():
    
    def __init__(self, firstname, lastname, age):
        if age < 0:
            raise ValueError("Age can't be less than 0")
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")

class Student(Person):
    
    def __init__(self, firstname, lastname, age, speciality, course):
        super().__init__(firstname, lastname, age)
        self.speciality = speciality
        self.course = course

    def study(self):
        print(f"""{self.firstname} {self.lastname} is a {self.course} year {self.speciality} studying.
{4 - self.course} year left until bachelor's degree""")

class Teacher(Person):
    
    def __init__(self, firstname, lastname, age, salary, academic_degree):
        super().__init__(firstname, lastname, age)
        self.salary = salary
        self.academic_degree = academic_degree
        
    def work(self):
        print(f"{self.firstname} {self.lastname} has a {self.academic_degree} and receives a salary of UAH {self.salary}")
        

ihor = Student("Ivan", "Ivanov", 23, "manager", 3)

stepan_petrovich = Teacher("Stepan", "Kovalev", 78, 30000, "doctorate in technical sciences")

stepan_petrovich.talk()
stepan_petrovich.work()

ihor.talk()
ihor.study()