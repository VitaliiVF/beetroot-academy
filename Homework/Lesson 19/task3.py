class Student:
    
    def __init__(self, size):
        self.student = [None] * size
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.student) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.student[self.index]
        
    def __getitem__(self, index):
        return self.student[index]
    
    def __setitem__(self, index, newvalue):
        self.student[index] = newvalue
        
c = Student(4)

c[0] = "Meghana"
c[1] = "Raju"
c[2] = "Hari"
c[3] = "Sreeja"

for i in c:
    print(i)
    
print()

print(c[0])
print(c[1])
print(c[2])
print(c[3])