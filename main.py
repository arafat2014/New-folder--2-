class Employ:
    company = "Apple "
    def show(self):
        print(f"The employ name is {self.name} and the company name is {self.company}")
        
    def changCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employ()
e1.name = "Arafat"
e1.show()
e1.changCompany("tesla")
e1.show()