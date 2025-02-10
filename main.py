class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_Details(self):
        print(f"The name of student is {self.name} and the age of the student is {self.age} ")

p = Person("Arafat" , 25)
p.show_Details()
print(p.__dict__)
