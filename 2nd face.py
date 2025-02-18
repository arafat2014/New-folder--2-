class Employee:
    def __init__(self, name):
        self.name = name  
        
    def show(self):
        print(f"The name is {self.name}")      
class Dancer:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"The Dance is {self.name}")    
class DancerEmploy(Employee , Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance
        
o = DancerEmploy("Arafat", "Kathak")
print(o.name)
print(o.dance)
o.show()
print(DancerEmploy.mro())

    