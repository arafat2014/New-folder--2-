class Employ:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"The employ name is {self.name} and his salary is {self.salary}")
        
a1 = Employ("Arafat", 12000)
a1.show()
    