import uuid

class Boss:

    def __init__(self, name: str, company: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.company = company
        self._workers = []
        
    @property
    def workers(self):
        return self._workers
    
    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __str__(self):
        return f"{self.name}."
    
    def __repr__(self):
        return f"<{self.name}.>"

class Worker:

    def __init__(self, name: str, company: str, boss: Boss):
        self.id = str(uuid.uuid4())
        self.name = name
        self.company = company
        if type(boss) == Boss:
            self._boss = boss
            boss.workers = self
        else:
            raise ValueError("Boss must be an instance of the Boss class")
    
    @property    
    def boss(self):
        return self._boss
    
    @boss.deleter
    def boss(self):
        self._boss.workers.remove(self)
    
    @boss.setter
    def boss(self, new_boss):
        if type(new_boss) == Boss:
            del self.boss
            self._boss = new_boss
            new_boss.workers = self
        else:
            raise ValueError("Boss must be an instance of the Boss class")
        
    def __str__(self):
        return f"{self.name}, {self.company}. Boss - {self.boss}"
    
    def __repr__(self):
        return f"<{self.name}, {self.company}. Boss - {self.boss}>"
        
   
john = Boss("John", "Google")
ihor = "Ihor"
ivan = Boss("Ivan", "Google")
jeck = Worker("Jeck", "Google", ivan)
vitalii = Worker("Vitalii", "Google", john)

jeck.boss = ivan
vitalii.boss = ivan

print(ivan.workers)
print(john.workers)

# vitalii.boss = ihor # ValueError, object "ihor" is not of class Boss
vitalii.boss = john

print(john.workers)
print(ivan.workers)
