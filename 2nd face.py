class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Value = 1
        
P = Person("Arafat", 15)
print(P.__dict__)
print(help(Person))